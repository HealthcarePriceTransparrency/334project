# SQL Server Docker

Here are my notes on how to get the SQL Server Docker image up and running. I'm using the free tier from [Oracle Cloud](https://www.oracle.com/cloud/free/).

This sets up two services in Docker:

1. MySQL Server

    This is the database

1. NocoDB Web Interface
    
    This is a web interface for the database

## Setup

1. Export the data from Dolt

    1. Install Dolt

    1. Clone the data from Dolt

        `dolt clone dolthub/hospital-price-transparency`

    1. Export the data to a SQL file

        `dolt dump`

1. Get the SQL server running

    1. Install Docker

    1. Move into the 'docker' directory

        `cd docker`

    1. Copy the SQL file into the 'docker' directory

        `cp PATHTODOLTDUMP/doltdump.sql .`

    1. Run docker compose to setup the containers
    
        `docker compose up -d`
    
    1. Check that the containers are running
    
        `docker ps`
    
    1. Import the data exported from Dolt into the database
    
        1. Create the database on the server
        
            `docker exec -i mysql_container mysql -uroot -ppassword -e "create database hospital_price_transparency;"`

        1. Confirm the table exists

            `docker exec -i mysql_container mysql -uroot -ppassword -e "show databases;"`

        1. Import the data into the database

            Warning: This will take awhile.

            On unix:

            `docker exec -i mysql_container mysql -uroot -ppassword hospital_price_transparency < doltdump.sql`

            On windows:

            `cmd /c "docker exec -i mysql_container mysql -uroot -ppassword hospital_price_transparency < doltdump.sql"`

        1. Check that the data was imported

            `docker exec -i mysql_container mysql -u root -ppassword hospital_price_transparency -e "show tables;"`

            Note: Depending on system, this command may not show the tables you are looking for. This is likely because of strange import behavior from the Dolt dump where it creates a new database under the original database name.
            
            <details>
            <summary>If this is the case, you can follow these steps to confirm and fix the problem:</summary>

            1. Show the available databases

                `docker exec -i mysql_container mysql -u root -ppassword -e "show databases;"`

                The output of this command should look something like this:

                ```bash
                Database
                hospital-price-transparency
                hospital_price_transparency
                information_schema
                mysql
                noco_db
                performance_schema
                sys
                ubuntu
                ```

                If you see two databases with roughly the same name, proceed.

            1. Move the tables from the imported database to the proper database

                `docker exec -i mysql_container mysql -u root -ppassword hospital-price-transparency -e "RENAME TABLE cpt_hcpcs TO hospital_price_transparency.cpt_hcpcs;
                RENAME TABLE hospitals TO hospital_price_transparency.hospitals;
                RENAME TABLE prices TO hospital_price_transparency.prices;"`

            1. Confirm the tables were moved

                `docker exec -i mysql_container mysql -u root -ppassword hospital_price_transparency -e "show tables;"`

            1. Drop the now empty imported database

                `docker exec -i mysql_container mysql -u root -ppassword -e "DROP DATABASE \`hospital-price-transparency\`;"`

            1. Confirm the database was dropped

                `docker exec -i mysql_container mysql -u root -ppassword -e "show databases;"`

            </details>

    1. Create a read-only user for our db to prevent accidental writes when using the python scripts (pythonuser:longpasswordforpythonuser)

        `docker exec -i mysql_container mysql -uroot -ppassword -e "CREATE USER 'pythonuser'@'%' IDENTIFIED BY 'longpasswordforpythonuser'; GRANT SELECT ON hospital_price_transparency.* TO 'pythonuser'@'%'; FLUSH PRIVILEGES;"`

1. Create an unprivileged ssh user to allow access to the sql server

    1. Create the user: `useradd -s /sbin/nologin databaseTunnelUser`

    1. Give the user a password: `passwd databaseTunnelUser`

    <details>
    <summary>(Optional) If you want to use SSH instead of password login:</summary>

    1. Create the homedir for the user: `mkhomedir_helper databaseTunnelUser`

    1. Create an ssh key: `ssh-keygen -t rsa -b 4096 -C "databaseTunnelUser"`

    1. Copy the entire generated public key to a new line in the authorized users file on the server located at `/home/databaseTunnelUser/.ssh/authorized_keys`

    </details>

    <details>
    <summary>(Optional) If you want to further restrict the ssh user's privileges:</summary>

    Add the following to the `/etc/ssh/sshd_config` file:

    ```bash
    Match User databaseTunnelUser
        PermitOpen 127.0.0.1:9670
        X11Forwarding no
        AllowAgentForwarding no
        ForceCommand /bin/false
    ```

    </details>

1. Forward the Noco Web Interface

    This is going to depend on your setup. For an Oracle Cloud server I went about it like this:

    1. Install nginx

    1. Create a new nginx config file at `/etc/nginx/sites-available/nocoexample.conf`

        ```conf
        # Redirect http -> https
        server {
            server_name noco.example.com;
            listen 80;
            listen [::]:80;
            return 301 https://$host$request_uri;
        }

        # Handle https
        server {
            server_name nocodb.example.com;
            listen 443 ssl http2;
            listen [::]:443 ssl http2;

            #SSL configuration
            ssl_certificate /etc/letsencrypt/live/noco.example.com/fullchain.pem;
            ssl_certificate_key /etc/letsencrypt/live/noco.example.com/privkey.pem;
            ssl_session_cache shared:SSL:10m;
            ssl_protocols TLSv1.2 TLSv1.3;
            ssl_ciphers "TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384";
            ssl_prefer_server_ciphers on;
            
            add_header X-Content-Type-Options nosniff;
            add_header X-Frame-Options DENY;
            add_header X-XSS-Protection "1; mode=block";

            location / {
                proxy_pass http://localhost:9671;
                proxy_set_header X-Forwarded-Proto $scheme;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection 'upgrade';
                proxy_set_header Host $host;
            }
        }
        ```

    1. Symlink the config file to the enabled sites directory

        `ln -s /etc/nginx/sites-available/nocoexample.conf /etc/nginx/sites-enabled/nocoexample.conf`

    1. Restart nginx

        `systemctl restart nginx`

    1. Generate an SSL certificate with certbot

        1. Install certbot

        1. Run certbot to get a certificate

            Make not of where this command stores the outputted key files

            `certbot certonly --nginx -d noco.example.com`

        1. Auto renew SSL certs with a cronjob

            Open the cron editor:

            `crontab -e`

            Add the following line to the bottom:

            ```bash
            0 23 * * * certbot renew --quiet --deploy-hook "systemctl restart nginx"
            ```

### Usage

To access the database, you will need to create an ssh tunnel to the server. This is because the database is only accessible from the server itself.

#### In Python

See this stackoverflow post for a more in-depth explanation: https://stackoverflow.com/questions/31506958/sqlalchemy-through-paramiko-ssh

1. Use an ssh tunnel to connect to the hosted server

    Use the unprivileged ssh user credentials created at the end of the [setup section](#setup) to login to the server that is hosting the database.
    
    **For this project I've shared the credentials in our Google Drive folder.**

1. Connect to the database through the tunnel using the user created earlier:

    ```yaml
    uri: 127.0.0.1:9670
    user: pythonuser
    password: longpasswordforpythonuser
    ```

#### In NocoDB

See docs here: https://docs.nocodb.com/data-sources/connect-to-data-source/

#### Advanced Database Operations

For more advanced database operations, you can connect to the database using the root user and password:

```yaml
user: root
password: password
```
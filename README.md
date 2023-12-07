# 334 Project - Healthcare Price Transparency

I've attempted to make this a good resource for everything related to our project. I'll be moving things around as we go, so if you have any suggestions, please let me know.

## Resources

Important logins and links are shared in our project folder.

Google Drive Folder: https://drive.google.com/drive/folders/1ocedxrBb3HQyzmydgoHR4PNEdymWVgeO?usp=drive_link

## Pre-Processing

Notes on the pre-processing of the data.

### **Notable Changes**

*   Kept in 'city' feature, since with ordinal encoding, we would only have 3 features (npi_number, payer, and state )

*   Dropped rows where both city and state were null (about 600 rows out of +9,000 rows), since we would have to add in the city and state manually by looking up the hospital names

## Models

Some stats for our model work so far.

### KNN Regression
Created the model and chose a K of 6 based on the results of R2:
| K | Test R2 | Train R2 |
|---|----|---|
| 5 | 0.0008040154979879199 | 0.17977696608285532 |
| 6 | 0.1411911947661597 | 0.16643213159807746 |
| 7 | 0.12425772455590434 | 0.15282217668851883 |
| 8 | 0.1108127957041688 | 0.13256402729049965 |

## SQL Server Docker

*Not up yet*

Here are my notes on how to get the SQL Server Docker image up and running. I'm using the free tier from [Oracle Cloud](https://www.oracle.com/cloud/free/).

This sets up two services in Docker:

1. MySQL Server

    This is the database

1. NocoDB Web Interface
    
    This is a web interface for the database

### Setup

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
    
        `docker-compose up -d`
    
    1. Check that the containers are running
    
        `docker ps`
    
    1. Import the data exported from Dolt into the database
    
        1. Create the table in the db
        
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

    1. Create a read-only user for our db to prevent accidental writes when using the python scripts (pythonuser:longpasswordforpythonuser)

        `docker exec -i mysql_container mysql -uroot -ppassword -e "GRANT SELECT ON hospital_price_transparency.* TO 'pythonuser'@'%' IDENTIFIED BY 'longpasswordforpythonuser'; FLUSH PRIVILEGES;"`

1. Create an unprivileged ssh user to allow access to the sql server

    1. Create the user: `useradd -s /sbin/nologin databaseTunnelUser`

    1. Give the user a password: `passwd databaseTunnelUser`

1. Forward the Noco Web Interface

    This is going to depend on your setup. For an Oracle Cloud server I went about it like this:

    1. Install nginx

    1. Add a proxy_pass to the Noco service in the nginx config

        ```nginx
        ...
            location / {
                proxy_pass http://localhost:9671;
            }
        ...
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
    uri: localhost:9670
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

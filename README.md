# 334 Project - Healthcare Price Transparency



### **Notable Changes**

*   Kept in 'city' feature, since with ordinal encoding, we would only have 3 features (npi_number, payer, and state )
*   Dropped rows where both city and state were null (about 600 rows out of +9,000 rows), since we would have to add in the city and state manually by looking up the hospital names

## Models

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

### Usage

1. Get the SQL server running

    1. Install Docker
    1. Install Dolt
    1. In the 'docker/databases' directory, run `dolt clone dolthub/hospital-price-transparency`
    1. In the 'docker' directory, run `docker-compose up -d`
        * I think their docker image is broken? The databases it creates don't work...

1. Create an ssh user to allow access to the sql server

    1. Create the user: `useradd -s /sbin/nologin doltuser`
    1. Give the user a password: `passwd doltuser`

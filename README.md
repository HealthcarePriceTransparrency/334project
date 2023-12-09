# 334 Project - Healthcare Price Transparency

I've attempted to make this a good resource for everything related to our project. I'll be moving things around as we go, so if you have any suggestions, please let me know.

## Resources

Important logins, links, and secrets are shared in our project folder.

Google Drive Folder: https://drive.google.com/drive/folders/1ocedxrBb3HQyzmydgoHR4PNEdymWVgeO?usp=drive_link

### Usage

To access the database, you will need some extra resources not included in this repository such as authentication keys and passwords.

#### First Time Use

1. Clone this repository and cd into it

    ```bash
    git clone https://github.com/HealthcarePriceTransparrency/334project.git && cd 334project
    ```

1. Create a 'secrets' directory

    ```bash
    mkdir secrets
    ```

1. Copy the following files from the shared drive folder to the secrets folder:

    ```
    .env
    dbTunnel.key
    ```

#### Connecting to the Database

Examples for connecting to the database can be found in `dataFetchDemo.ipynb` file.

## Pre-Processing

Notes on the pre-processing of the data.

### Notable Changes

*   Kept in 'city' feature, since with ordinal encoding, we would only have 3 features (npi_number, payer, and state )

*   Dropped rows where both city and state were null (about 600 rows out of +9,000 rows), since we would have to add in the city and state manually by looking up the hospital names

## Models

Some stats for our model work so far.

### KNN Regression

Notes on the KNN model.

### Notable Changes

After updating the data pre-processing, I re-ran the KNN model:

* Training samples went from 7009 -> 7001.

#### R2 results for KNN with older data:
| K | Test R2 | Train R2 |
| --- | --- | --- |
| 5 | 0.0008040154979879199 | 0.17977696608285532 |
| 6 | 0.1411911947661597 | 0.16643213159807746 |
| 7 | 0.12425772455590434 | 0.15282217668851883 |
| 8 | 0.1108127957041688 | 0.13256402729049965 |

#### Results with cleaner data:
| K | Test R2 | Train R2 | 
| --- | --- | --- |
| 5 | 0.8644741640601704 | 0.6606602118046967 |
| 6 | 0.8713803040996428 | 0.6397757844687746 |
| 7 | 0.8692824717948242 | 0.6115449665102355 |
| 8 | 0.8687516010976353 | 0.589063313392763 |

| K | Test Mean AE | Train Mean AE | 
| --- | --- | --- |
| 5 | 0.1325378493805926 | 0.12301667814067577 |
| 6 | 0.13597014873452304 | 0.13214068256539496 |
| 7 | 0.14075470223374853 | 0.14068042164250563 |
| 8 | 0.14408334570586023 | 0.14723194803361775 |

| K | Test Mean SE | Train Mean SE | 
| --- | --- | --- |
| 5 | 0.07578135435519463 | 0.3767237798603035 |
| 6 | 0.07191967999673347 | 0.39990897853107743 |
| 7 | 0.07309271517609083 | 0.4312498964542299 |
| 8 | 0.07338955968652294 | 0.45620828222138304 |

| K | Test Median AE | Train Median AE | 
| --- | --- | --- |
| 5 | 0.0485564738721998 | 0.032741330733140256 |
| 6 | 0.05344826213077272 | 0.04039029712779443 |
| 7 | 0.05856244171786311 | 0.0462752752079002 |
| 8 | 0.06173719651683206 | 0.0483136723468999 |

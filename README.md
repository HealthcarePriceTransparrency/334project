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
Created the model and chose a K of 6 based on the results of R2:
| K | Test R2 | Train R2 |
|---|----|---|
| 5 | 0.0008040154979879199 | 0.17977696608285532 |
| 6 | 0.1411911947661597 | 0.16643213159807746 |
| 7 | 0.12425772455590434 | 0.15282217668851883 |
| 8 | 0.1108127957041688 | 0.13256402729049965 |




# 334 Project - Healthcare Price Transparency

I've attempted to make this a good resource for everything related to our project. I'll be moving things around as we go, so if you have any suggestions, please let me know.

## Resources

[Shared Google Drive Folder](https://drive.google.com/drive/folders/1ocedxrBb3HQyzmydgoHR4PNEdymWVgeO?usp=drive_link) (Researchers Only)

[[Placeholder] Project Proposal]()

[[PH] Project Presentation]()

[[PH] Research Writeup]()

### Repo Structure

- `data/` - Contains all of the data we have used in the models for our project
- `dataFetching/` - Contains notebooks related to fetching data from our hosted database
- `dataProcessing/` - Contains notebooks related to pre-processing data for use in our models
- `docker/` - Contains files related to hosting our database instance
- `models/` - Contains notebooks related to our models
- `secrets/` - (Only if accessing database) Contains files related to connecting to the db

## Usage

1. Clone this repository and cd into it

    ```bash
    git clone https://github.com/HealthcarePriceTransparrency/334project.git && cd 334project
    ```

1. Install Python packages

    (Optional) You can use a virtual environment if you want:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## (Optional; Researchers only) Connecting to the Database

While all of the necessary data is included in this repository for end users, those working on the project will need to connect to our hosted database to fetch new data. Doing so requires extra resources not included in this repository such as authentication keys and passwords.

1. If required, reach out to us and we can provide you with access to our shared folder on Google Drive

1. Create a 'secrets' directory in the root of this repository

    ```bash
    mkdir secrets
    ```

1. Copy the following files from the shared drive folder to the secrets folder:

    ```
    .env
    dbTunnel.key
    ```

# Data Fetching

This folder contains notebooks related to fetching specific data from our hosted database.

## Files

- `fetch_84206.ipynb`: Fetches data for the code "84206" from the hosted database.

- `fetchAll_842.ipynb`: Fetches all data beginning with the code "842*" from the hosted database.

## Why?

Ideally, this would be batched with our pre-processing to fetch the data and output the formatted files in one go. Instead, these notebooks output CSVs containing all of the fetched data which are transformed by the pre-processing notebooks. This was needed as we had to build out our data hosting solution alongside model development.

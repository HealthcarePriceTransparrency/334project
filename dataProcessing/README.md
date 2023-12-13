# Data Pre-Processing

This folder contains notebooks related to pre-processing the data in the `/data/` directory.

## Files

- `proc_84206.ipynb`: Processes the data for the code "84206" (84206.csv) and splits it into testing and training data stored at `/data/84206/*.csv`.

- `procAll_842.ipynb`: Processes the data for all codes beginning with "842" (842entries.csv) and splits it into testing and training data stored at `/data/84206/*.csv`.

## Notable Changes

*   Kept in 'city' feature, since with ordinal encoding, we would only have 3 features (npi_number, payer, and state )

*   Dropped rows where both city and state were null (about 600 rows out of +9,000 rows), since we would have to add in the city and state manually by looking up the hospital names

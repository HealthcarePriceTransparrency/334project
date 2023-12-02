# 334 Project - Healthcare Price Transparency
#### **Notable Changes**

*   Kept in 'city' feature, since with ordinal encoding, we would only have 3 features (npi_number, payer, and state )
*   Dropped rows where both city and state were null (about 600 rows out of +9,000 rows), since we would have to add in the city and state manually by looking up the hospital names

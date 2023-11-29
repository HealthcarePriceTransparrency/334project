# 334 Project - Healthcare Price Transparency

[Meeting Notes]https://docs.google.com/document/d/15t3UW49bSV2Z3Q1U-5dG3lzsEWozVwH9OO88m8xQMXE/edit?usp=sharing

1. Cleaning
   Standardaization - sklearn
   Feature trimming
     zip_code, street_address, url, publish_date, name
   Clean code (prices, cpt_hcps)
     Remove commas, dashes, and numbers after them
   One-hot encoding - sklearn
     (1/0) state, city, payer
   NPI & prices to integers and floats (respectively)
3. Modeling
   KNN - sklearn
   Decision Trees - sklearn
   

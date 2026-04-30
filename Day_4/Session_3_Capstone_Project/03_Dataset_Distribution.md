# Capstone Project: Dataset Distribution

## Overview
Once your team is formed and your problem statement is assigned, you will receive your project dataset. Unlike the clean, perfectly formatted data used in earlier labs, capstone datasets are designed to simulate messy, real-world data environments.

## What to Expect in the Data
- **Multiple Tables:** You will likely receive 3-5 related tables (e.g., Transactions, Customers, Products, Store Locations) requiring SQL joins or data modeling.
- **Missing Values:** Expect nulls and blanks. You will need to decide whether to impute, drop, or flag them.
- **Inconsistencies:** Look out for spelling errors, mismatched date formats, and duplicate records.
- **Large Volume:** The datasets will be larger than previous labs (100k+ rows), testing the efficiency of your code and dashboards.

## Receiving Your Data
1. **Access:** Datasets will be distributed via a secure link or a shared cloud folder by the instructor.
2. **Download & Secure:** Download the data to your local machine. Ensure every team member has a working copy. *Do not modify the original raw files.* Always create a copy for cleaning.
3. **Data Dictionary:** Along with the data files, you will receive a Data Dictionary. This is a crucial document that defines what every column in every table represents.

## First Steps with the Data (EDA)
Before jumping into building dashboards, you must perform Exploratory Data Analysis (EDA):
1. **Sanity Check:** Load the data into SQL or Python. Do the row counts match expectations?
2. **Examine the Dictionary:** Read the data dictionary thoroughly. If a column is unclear, ask the instructor (acting as the business stakeholder).
3. **Profile the Data:** Identify primary keys, foreign keys, and understand the cardinality of categorical variables. Check the distribution of numerical variables to spot extreme outliers.

## Data Security Note
Treat this data professionally. Do not upload the raw datasets to public repositories or share them outside the class environment.

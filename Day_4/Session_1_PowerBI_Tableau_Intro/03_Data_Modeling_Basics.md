# Introduction to Power BI & Tableau: Data Modeling Basics

## Overview
Data Modeling is the process of defining relationships between different data tables to create a logical structure that BI tools can query effectively. A good data model ensures accurate reporting, faster performance, and easier report creation.

## Why Data Modeling?
Real-world data rarely comes in a single, perfect, flat table. You usually have multiple tables (e.g., Customers, Products, Sales). Data modeling connects these tables so you can, for example, analyze Sales by Customer Region or Product Category.

## Key Concepts
### 1. Fact and Dimension Tables
- **Fact Tables:** Contain quantitative data or metrics (e.g., Sales transactions, website clicks). They hold the numbers you want to aggregate (sum, average, count) and foreign keys that link to dimension tables.
- **Dimension Tables:** Contain descriptive attributes related to the facts (e.g., Customer Name, Product Category, Store Location, Dates). You use these to filter, group, and slice the fact data.

### 2. Star Schema
The most common and recommended modeling approach for BI. It features a central Fact table surrounded by multiple Dimension tables, resembling a star. 
- Example: `Sales` Fact table linked to `Date`, `Product`, `Customer`, and `Store` Dimension tables.

### 3. Relationships & Cardinality
To connect tables, you define relationships using common columns (keys).
- **Primary Key:** A unique identifier in a dimension table (e.g., CustomerID).
- **Foreign Key:** The corresponding column in the fact table.
- **Cardinality:**
  - **One-to-Many (1:*):** The standard relationship. One product in the Product table can appear many times in the Sales table.
  - **One-to-One (1:1):** Rare, usually means tables could be combined.
  - **Many-to-Many (*:*):** Complex and should generally be resolved using a bridge/junction table.

## Data Modeling in Power BI
1. Go to the **Model View** (the relationship icon on the left).
2. Power BI often auto-detects relationships.
3. To manually create one, drag a field from one table onto the corresponding field in another table.
4. Double-click the relationship line to configure cardinality and cross-filter direction. (Single direction from Dimension to Fact is best practice).

## Data Modeling in Tableau
1. On the **Data Source** page, drag your primary table (usually the Fact table) onto the canvas.
2. Drag related tables (Dimensions) next to it to create relationships (often represented as "Noodles" in modern Tableau versions).
3. Tableau uses a semantic model that handles relationships dynamically without needing strict traditional joins, though physical joins can still be defined if needed.

## Best Practices
- **Aim for a Star Schema:** It is optimized for reading and filtering large datasets.
- **Hide key columns:** Hide ID columns in the report view to prevent confusion for end-users.
- **Use single-directional filtering:** Bi-directional filtering can cause ambiguity and performance issues; use it only when strictly necessary.

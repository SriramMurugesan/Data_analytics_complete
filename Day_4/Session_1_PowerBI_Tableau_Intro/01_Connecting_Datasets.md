# Introduction to Power BI & Tableau: Connecting Datasets

## Overview
Business Intelligence (BI) tools like Power BI and Tableau allow analysts to visualize data, share insights, and make data-driven decisions without deep programming knowledge. The first step in any BI workflow is connecting to your data.

## Supported Data Sources
Both tools support a wide variety of data sources:
- **Flat Files:** CSV, Excel, JSON, Text files
- **Relational Databases:** SQL Server, MySQL, PostgreSQL, Oracle
- **Cloud Data Warehouses:** Snowflake, Google BigQuery, Amazon Redshift
- **Cloud Services:** Salesforce, Google Analytics, SharePoint
- **Web Data:** Web scraping, OData feeds, REST APIs

## Connecting Data in Power BI
1. Open Power BI Desktop.
2. Click on **Get Data** in the Home ribbon.
3. Select the type of data source (e.g., "Text/CSV" or "SQL Server").
4. Browse to the file location or enter the server credentials.
5. Click **Load** to bring the data directly into the model, or **Transform Data** to open the Power Query Editor for data cleaning before loading.

## Connecting Data in Tableau
1. Open Tableau Desktop or Public.
2. Under the **Connect** pane on the left, choose your data source type (e.g., "Text file", "Microsoft Excel", or a server).
3. Navigate to your file or enter the database connection details.
4. Drag and drop the tables you want to analyze onto the canvas.
5. Choose between a **Live** connection (queries the database directly) or an **Extract** (creates a high-performance local copy of the data).

## Best Practices
- **Clean data first:** While BI tools have transformation capabilities (like Power Query in Power BI), it's often more efficient to clean data in SQL or Python beforehand if dealing with massive datasets.
- **Extract vs. Live:** Use Live connections for real-time dashboards where underlying data changes constantly. Use Extracts for faster performance on large, static datasets.
- **Security:** Never embed personal database credentials in shared dashboards. Use gateway connections or service accounts.

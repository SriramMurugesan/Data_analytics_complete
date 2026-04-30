# Interactive Dashboards: Filters & Slicers

## Overview
Interactivity is what separates a modern dashboard from a static report. Filters and Slicers are the primary tools used to allow users to interact with data, drill down into specific segments, and answer their own questions without needing a new report.

## Filters vs. Slicers
While they often achieve the same goal (restricting the data shown), they are presented differently:
- **Filters:** Usually reside in a dedicated "Filter Pane" (Power BI) or shelf (Tableau). They are often used by the report author to restrict data on the backend or are provided for advanced users.
- **Slicers:** Are visual elements placed directly on the report canvas. They act as interactive buttons, dropdowns, or sliders that the end-user can easily click to filter the entire page.

## Types of Slicers/Filters
1. **List/Dropdown:** Good for categorical data (e.g., selecting a specific Region or Product Category).
2. **Date Range (Slider):** Essential for time-series data. Allows users to select a start and end date to narrow down the view.
3. **Numeric Range:** Allows filtering by a range of values (e.g., Sales between $1000 and $5000).
4. **Hierarchy Slicers:** Allows filtering across multiple related levels (e.g., Year > Quarter > Month).

## Implementation in Power BI
1. To add a Slicer, click the **Slicer** icon in the Visualizations pane.
2. Drag the field you want to filter by (e.g., 'Year' or 'Region') into the Field bucket.
3. Format the slicer to be a dropdown, list, or slider using the Format pane.
4. **Edit Interactions:** By default, a slicer filters all visuals on the page. You can change this by selecting the slicer, going to the Format menu, and clicking "Edit Interactions" to stop it from affecting specific charts.

## Implementation in Tableau
1. To add a Filter, drag a field to the **Filters** shelf on a worksheet.
2. Choose the filtering criteria (e.g., select specific items from a list).
3. To make it interactive for the user on a dashboard, click the dropdown on the filter pill and select **Show Filter**.
4. To apply the filter across multiple sheets, click the filter dropdown again, select **Apply to Worksheets**, and choose "All Using This Data Source" or select specific sheets.

## Best Practices
- **Don't overwhelm:** Too many slicers clutter the dashboard. Only include the most critical ones.
- **Use Dropdowns for long lists:** If a category has more than 5-10 items, use a dropdown to save space.
- **Sync Slicers:** If you have multiple pages in a report, consider syncing slicers so a user's selection carries over as they navigate between pages.

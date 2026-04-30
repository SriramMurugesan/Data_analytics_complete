# Interactive Dashboards: KPI Cards

## Overview
Key Performance Indicators (KPIs) are the most critical metrics used to evaluate success or performance. KPI Cards are prominent, usually single-number visual elements placed at the top of a dashboard. They provide an immediate, at-a-glance summary of how things are going.

## Anatomy of a Great KPI Card
A standard number alone isn't enough. A good KPI card typically contains:
1. **The Core Metric:** The primary number (e.g., Total Revenue: $1.2M).
2. **Context / Target:** Something to compare the metric against (e.g., Target: $1.5M, or Last Year: $1.0M).
3. **Trend / Variance:** An indicator of performance (e.g., +20% YoY, or a red downward arrow).
4. **Sparkline (Optional):** A small, simple line chart in the background showing the recent trend.

## Implementing KPI Cards in Power BI
1. **Standard Card:** Click the **Card** visual icon. Drag a measure (e.g., Total Sales) into the field. It displays a simple number.
2. **KPI Visual:** Click the **KPI** visual icon. It requires three fields:
   - **Value:** The main metric (e.g., Sales this month).
   - **Trend Axis:** Usually a date field to establish context.
   - **Target:** The goal to compare against.
   Power BI automatically color-codes the visual (green for good, red for bad) based on the variance from the target.
3. **New Card Visual (Preview feature in newer versions):** Allows for multiple KPIs, images, and reference labels within a single visual container.

## Implementing KPI Cards in Tableau
Tableau doesn't have a specific "KPI Card" chart type, so you build them using text tables:
1. Create a new worksheet.
2. Drag your key Measure (e.g., Sales) to the **Text** mark.
3. Drag dimensions or calculated fields representing variance (e.g., YoY Growth) to the Text mark as well.
4. Click on the **Text** mark to format the layout, font size (make the main number large), and alignment.
5. **Add Shapes/Colors:** You can write a calculated field to determine if growth is positive or negative, drag that to the **Color** and **Shape** marks, and assign green up-arrows or red down-arrows accordingly.
6. Place this worksheet prominently on your dashboard.

## Best Practices
- **Placement:** Always put KPI cards at the top or top-left of the dashboard. This is where the user's eye naturally goes first.
- **Limit the Number:** Don't have 15 KPI cards. Stick to the 3-5 most important metrics for the specific audience of that dashboard.
- **Actionable:** A KPI should immediately tell the user if they need to take action. If a number is red, it should be obvious what that means and why.

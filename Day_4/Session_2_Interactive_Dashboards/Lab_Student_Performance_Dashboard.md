# Lab: Build a Student Performance Dashboard

## Objective
Apply the concepts of interactive dashboard building to create a comprehensive view of student performance. You will use BI tool concepts (Filters, Drill-downs, KPI Cards) to design a dashboard that helps educators identify trends and at-risk students.

## Dataset
Use the provided `students_data.csv` file located in the root directory.

### Data Dictionary Recap:
- `StudentID`: Unique identifier for each student.
- `Name`: Name of the student.
- `Age`: Age in years.
- `Gender`: Male / Female.
- `Attendance_Rate`: Percentage of classes attended.
- `Study_Hours_Per_Week`: Average hours studied.
- `Previous_Grades`: Past academic performance score.
- `Extracurricular_Activities`: Participation (Yes/No).
- `Final_Grade`: The target metric to analyze.

## Lab Instructions

Assume you are building this in your BI tool of choice (Power BI, Tableau, or even a Python dashboard using Dash/Streamlit). 

### Step 1: Connect and Prepare
1. Load `students_data.csv` into your tool.
2. Ensure data types are correct (e.g., Final_Grade, Attendance_Rate, and Study_Hours should be numerical).

### Step 2: Build KPI Cards (High-Level Summary)
Place these at the top of your dashboard:
1. **Average Final Grade:** The overall average score for all students.
2. **Average Attendance Rate:** The overall average attendance.
3. **Total Students:** Count of unique students.
4. *(Optional Challenge)* **At-Risk Students:** Create a metric counting students with a `Final_Grade` below 60 or `Attendance_Rate` below 75%.

### Step 3: Create Core Visualizations
1. **Grade Distribution:** Create a Histogram or Column Chart showing the distribution of `Final_Grade`. (X-axis: Grade Bins/Ranges, Y-axis: Count of Students).
2. **Attendance vs. Performance:** Create a Scatter Plot comparing `Attendance_Rate` (X-axis) and `Final_Grade` (Y-axis). Add a trendline to see the correlation.
3. **Study Hours Impact:** Create a Bar Chart showing Average `Final_Grade` broken down by `Study_Hours_Per_Week` (you may need to group study hours into bins like 0-5, 5-10, 10+).

### Step 4: Add Interactivity (Filters & Slicers)
Add slicers to the dashboard canvas to allow users to slice the data:
1. **Gender Slicer:** A dropdown or list to filter the entire dashboard by Male/Female.
2. **Extracurricular Activities Slicer:** A filter for Yes/No participation.

### Step 5: Implement Drill-Down
1. Create a hierarchy (or logical grouping) if possible. If using categorical bins for Age (e.g., Under 18, 18-20, Over 20), allow the user to click an Age group in a chart and drill down to see the individual students within that group.

### Step 6: Layout and Formatting
- Arrange the KPI cards at the top.
- Place slicers cleanly on the left pane or top right.
- Ensure colors are consistent (e.g., stick to a blue/grey theme).
- Make sure all axes and titles are clearly labeled.

## Deliverable
A functional, interactive dashboard (or a mockup/wireframe) that clearly communicates student performance and allows users to filter by demographics and activities.

# MINI PROJECT – DAY 2
# EXPLORATORY DATA ANALYSIS & VISUALIZATION

# Dataset:
# students_data.csv

# ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ## SECTION 1: STATISTICAL SUMMARY
df=pd.read_csv("students_data.csv")

# 1. Display summary statistics of the dataset
print(df.describe())
# 2. Find mean, median, and standard deviation of marks
print(df["marks"].mean())
print(df["marks"].median())
print(df["marks"].std())
# 3. Find average study hours and attendance
print(df["study_hours"].mean())
print(df["attendance"].mean())
# 4. Compare average marks across different cities
print(df.groupby("city")["marks"].mean())

# Question:
# What do you understand from the summary?

# ---

# ## SECTION 2: CORRELATION ANALYSIS

# 5. Calculate correlation between numerical columns
print(df.drop(columns=["student_id"]).corr(numeric_only=True))
# 6. Identify which variables are strongly related
print(df.drop(columns=["student_id"]).corr(numeric_only=True).unstack().sort_values(ascending=False))
# 7. Check relationship between:

#    * Study hours and marks
print(df.corr(numeric_only=True)["study_hours"]["marks"])
#    * Attendance and marks
print(df.corr(numeric_only=True)["attendance"]["marks"])
# Question:
# Which factor affects marks more?

# Important:
# Does correlation mean causation? Explain.

# ---

# ## SECTION 3: OUTLIER DETECTION

# 8. Identify outliers in marks
q1=df["marks"].quantile(0.25)
q3=df["marks"].quantile(0.75)
IQR=q3-q1
lower_bound=q1-1.5*IQR
upper_bound=q3+1.5*IQR
outliers=df[(df["marks"]<lower_bound) | (df["marks"]>upper_bound)]
print(outliers)
# 9. Identify outliers in study hours
q1=df["study_hours"].quantile(0.25)
q3=df["study_hours"].quantile(0.75)
IQR=q3-q1
lower_bound=q1-1.5*IQR
upper_bound=q3+1.5*IQR
outliers=df[(df["study_hours"]<lower_bound) | (df["study_hours"]>upper_bound)]
print(outliers)
# 10. Explain how outliers affect analysis

# Question:
# Should we remove outliers? Why or why not?

# ---

# ## SECTION 4: FEATURE ANALYSIS

# 11. Analyze how study hours affect marks
print(df.groupby("study_hours")["marks"].mean())
# 12. Analyze how attendance affects marks
print(df.groupby("attendance")["marks"].mean())
# 13. Compare performance based on gender
print(df.groupby("gender")["marks"].mean())
# 14. Compare performance across cities
print(df.groupby("city")["marks"].mean())

# Question:
# Which feature is most important for student performance?

# ---

# ## SECTION 5: BASIC VISUALIZATION

# 15. Create a bar chart:

#     * Average marks by city

# 16. Create a bar chart:

#     * Average marks by gender

# 17. Create a line chart:

#     * Marks trend (use student_id)

# 18. Create a histogram:

#     * Distribution of marks

# 19. Create a boxplot:

#     * Marks distribution

# Question:
# What do you observe from each chart?

# ---

# ## SECTION 6: ADVANCED VISUALIZATION

# 20. Create a scatter plot:

#     * Study hours vs marks

# 21. Create a heatmap:

#     * Correlation matrix

# 22. Create a distribution plot:

#     * Study hours

# 23. (Optional) Combine multiple variables in one visualization

# Question:
# Which visualization helped you understand data better?

# ---

# ## SECTION 7: VISUALIZATION ETHICS

# 24. Explain why choosing the right chart is important
# 25. What can go wrong with misleading charts?

# Example:
# Wrong scale, wrong chart type, etc.

# ---

# ## SECTION 8: MINI DASHBOARD (IMPORTANT)

# 26. Create a simple dashboard using multiple plots:

#     * Bar chart
#     * Scatter plot
#     * Histogram

# 27. Arrange them properly (single view)

# ---

# ## SECTION 9: INSIGHTS & CONCLUSION

# 28. Write at least 5 insights from your analysis

# Examples:

# * Students with higher study hours score more
# * Attendance impacts performance
# * Certain cities perform better

# 29. Suggest 2 improvements for students

# ---

# ## BONUS (OPTIONAL)

# * Predict student performance based on study habits
# * Suggest how college can improve results

# ---

# NOTE:
# Focus on understanding patterns and explaining insights clearly.
# Visualization should support your conclusions.

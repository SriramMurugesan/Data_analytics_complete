# MINI PROJECT: STUDENT PERFORMANCE ANALYSIS

# Objective:
# You are a Data Analyst. Your goal is to analyze student data and find insights about performance, study habits, and attendance.

# Dataset:
# students_data.csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# SECTION 1: DATA UNDERSTANDING
# --------------------------------------------------
# 1. Load the dataset into Python
df = pd.read_csv("students_data.csv")
# 2. Display the first 5 rows of the dataset
print(df.head())
# 3. Check the number of rows and columns
print(df.shape)
# 4. List all column names
print(df.columns)
# 5. Identify:
#    - Numerical columns
numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
print(f"\n[4] Numerical Columns  : {numerical_cols}")
#    - Categorical columns
categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()
print(f"    Categorical Columns: {categorical_cols}")
# 6. Check data types of each column
print(df.dtypes)
# 7. Generate summary statistics
print(df.describe())
print("#"*50)
# --------------------------------------------------
# SECTION 2: DATA CLEANING
# --------------------------------------------------
# 8. Check for missing values in each column
print(df.isnull().sum())
# 9. Identify columns with missing values
missing_cols = df.columns[df.isnull().any()].tolist()
print(f"\n[8] Columns with Missing Values: {missing_cols}")
# 10. Handle missing values (fill or remove)
#     - Mention what you chose and why
# fill missing values with mean
df["study_hours"] = df["study_hours"].fillna(df["study_hours"].mean())
df["attendance"] = df["attendance"].fillna(df["attendance"].mean())
# 11. Check for duplicate rows
print(df.duplicated().sum())
# 12. Remove duplicate records
df = df.drop_duplicates()
# 13. Verify that dataset is clean
print(df.isnull().sum())
print(df.duplicated().sum())

# Reflection:
# Why is data cleaning important before analysis?
print("Data cleaning is important before analysis because it ensures that the data is accurate, complete, and consistent. It also helps to identify and remove any errors or inconsistencies in the data that may affect the analysis results.")
print("#"*50)
# --------------------------------------------------
# SECTION 3: DATA EXPLORATION (EDA)
# --------------------------------------------------
# 14. Find the average marks of students
print(df["marks"].mean())
# 15. Find the minimum and maximum marks
print(df["marks"].min())
print(df["marks"].max())
# 16. Find the average attendance
print(df["attendance"].mean())
# 17. Identify the student with highest marks
print(df.loc[df["marks"].idxmax()])
# 18. Identify the student with lowest marks
print(df.loc[df["marks"].idxmin()])
print("#"*50)
# --------------------------------------------------
# SECTION 4: ANALYSIS & AGGREGATION
# --------------------------------------------------
# 19. Find average marks by city
print(df.groupby("city")["marks"].mean())
# 20. Find average marks by gender
print(df.groupby("gender")["marks"].mean())
# 21. Find average study hours by city
print(df.groupby("city")["study_hours"].mean())
# 22. Which city has the highest performing students?
print(df.groupby("city")["marks"].mean().idxmax())
# 23. Compare performance between male and female students
print(df.groupby("gender")["marks"].mean())
print("#"*50)

# Thinking Question:
# Which factor seems more important — study hours or attendance?
print("Study hours seems more important than attendance because it has a higher correlation with marks.")
print("#"*50)

# --------------------------------------------------
# SECTION 5: VISUALIZATION
# --------------------------------------------------
# 24. Create a bar chart for average marks by city
avg_marks_by_city = df.groupby("city")["marks"].mean()
plt.bar(avg_marks_by_city.index, avg_marks_by_city.values)
plt.xlabel("City")
plt.ylabel("Average Marks")
plt.title("Average Marks by City")
plt.show()
# 25. Create a bar chart for average marks by gender
avg_marks_by_gender = df.groupby("gender")["marks"].mean()
plt.bar(avg_marks_by_gender.index, avg_marks_by_gender.values)
plt.xlabel("Gender")
plt.ylabel("Average Marks")
plt.title("Average Marks by Gender")
plt.show()
# 26. Create a scatter plot for study hours vs marks
plt.scatter(df["study_hours"], df["marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()
# 27. (Optional) Create a chart for attendance vs marks
plt.scatter(df["attendance"], df["marks"])
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.title("Attendance vs Marks")
plt.show()

# Observation:
# What patterns do you observe from the graphs?
print("From the graphs, I observe that students with higher study hours and attendance tend to score higher marks.")
print("#"*50)

# --------------------------------------------------
# SECTION 6: CORRELATION ANALYSIS
# --------------------------------------------------
# 28. Calculate correlation between numerical columns
# Exclude 'student_id' as it is an identifier and not a relevant feature for correlation
corr_matrix = df.drop(columns=['student_id']).corr(numeric_only=True)
print(corr_matrix)
# 29. Identify strongly related variables
print(corr_matrix.unstack().sort_values(ascending=False).drop_duplicates())
# 30. Analyze relationship between:
#     - Study hours and marks
print(corr_matrix["study_hours"]["marks"])
#     - Attendance and marks
print(corr_matrix["attendance"]["marks"])

# Important:
# Does correlation mean causation? Explain.
print("Correlation does not mean causation. Just because two variables are correlated does not mean that one causes the other.")
print("#"*50)

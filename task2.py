# MINI PROJECT – DAY 2
# EXPLORATORY DATA ANALYSIS & VISUALIZATION

# Dataset:
# students_data.csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---

# ## SECTION 1: STATISTICAL SUMMARY
df = pd.read_csv("students_data.csv")

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
print("From the summary, I understand that the average marks of students are around 78.5, with a standard deviation of 10.2. The average study hours are around 5.5, with a standard deviation of 1.5. The average attendance is around 85, with a standard deviation of 5.2.")
print("#"*50)
# ---

# ## SECTION 2: CORRELATION ANALYSIS

# 5. Calculate correlation between numerical columns
print(df.drop(columns=["student_id"]).corr(numeric_only=True))
# 6. Identify which variables are strongly related
print(df.drop(columns=["student_id"]).corr(numeric_only=True).unstack().sort_values(ascending=False).drop_duplicates())
# 7. Check relationship between:

#    * Study hours and marks
print(df["study_hours"].corr(df["marks"]))
#    * Attendance and marks
print(df["attendance"].corr(df["marks"]))

# Question:
# Which factor affects marks more?
print("Attendance affects marks more than study hours.")
# Important:
# Does correlation mean causation? Explain.
print("Correlation does not mean causation. It only indicates a relationship between variables.")
print("#"*50)
# ---

# ## SECTION 3: OUTLIER DETECTION
# what is oulier ?
print("Outlier is a value that is significantly different from other values in the dataset.")
# what is IQR?
print("IQR is the interquartile range, which is the difference between the third quartile and the first quartile.")
# how do we find outliers?
print("We can find outliers using the IQR method. We calculate the first quartile (Q1) and the third quartile (Q3). Then we calculate the IQR by subtracting Q1 from Q3. Finally, we identify outliers as values that are less than Q1 - 1.5 * IQR or greater than Q3 + 1.5 * IQR.")
# 8. Identify outliers in marks
Q1_marks = df["marks"].quantile(0.25)
Q3_marks = df["marks"].quantile(0.75)
IQR_marks = Q3_marks - Q1_marks
outliers_marks = df[(df["marks"] < (Q1_marks - 1.5 * IQR_marks)) | (df["marks"] > (Q3_marks + 1.5 * IQR_marks))]
print("Outliers in marks:\n", outliers_marks)
# 9. Identify outliers in study hours
Q1_study = df["study_hours"].quantile(0.25)
Q3_study = df["study_hours"].quantile(0.75)
IQR_study = Q3_study - Q1_study
outliers_study = df[(df["study_hours"] < (Q1_study - 1.5 * IQR_study)) | (df["study_hours"] > (Q3_study + 1.5 * IQR_study))]
print("Outliers in study hours:\n", outliers_study)
# 10. Explain how outliers affect analysis
print("Outliers can significantly skew the mean and standard deviation, distorting the overall understanding of the general student population and leading to misleading correlations.")

# Question:
# Should we remove outliers? Why or why not?
print("It depends on the context. If outliers are data entry errors, they should be removed or corrected. If they represent genuine extreme cases (e.g., exceptional students), they might be valuable for specific analyses and should be kept or analyzed separately.")
print("#"*50)
# ---

# ## SECTION 4: FEATURE ANALYSIS

# 11. Analyze how study hours affect marks
print("Study hours affect marks positively.")
print(df.groupby("study_hours")["marks"].mean())
# 12. Analyze how attendance affects marks
print("Attendance affects marks positively.")
print(df.groupby("attendance")["marks"].mean())
# 13. Compare performance based on gender
print("Performance based on gender:", df.groupby("gender")["marks"].mean())
# 14. Compare performance across cities
print("Performance across cities:", df.groupby("city")["marks"].mean())

# Question:
# Which feature is most important for student performance?
print("Attendance affects marks more than study hours.")
print("#"*50)
# ---

# ## SECTION 5: BASIC VISUALIZATION

# 15. Create a bar chart:

#   *Average marks by city
plt.figure(figsize=(14,10))
plt.subplot(3,2,1)
df.groupby("city")["marks"].mean().plot(kind="bar")
# Seaborn alternative:
# sns.barplot(data=df.groupby("city")["marks"].mean().reset_index(), x="city", y="marks")
# 16. Create a bar chart:

#     * Average marks by gender
plt.subplot(3,2,2)
df.groupby("gender")["marks"].mean().plot(kind="bar")
# Seaborn alternative:
# sns.barplot(data=df.groupby("gender")["marks"].mean().reset_index(), x="gender", y="marks")
# 17. Create a line chart:

#     * Marks trend (use student_id)
plt.subplot(3,2,3)
plt.plot(df["student_id"], df["marks"], marker='o')
# Seaborn alternative:
# sns.lineplot(data=df, x="student_id", y="marks", marker='o')
# 18. Create a histogram:

#     * Distribution of marks
plt.subplot(3,2,4)
plt.hist(df["marks"], bins=10)
# Seaborn alternative:
# sns.histplot(data=df, x="marks", bins=10)
# 19. Create a boxplot:

#     * Marks distribution
plt.subplot(3,2,5)
sns.boxplot(y=df["marks"])
plt.tight_layout()
plt.show()

# Question:
# What do you observe from each chart?
print("I observe differences across groups and a normal distribution of marks with no severe outliers in the boxplot.")
print("#"*50)

# ---

# ## SECTION 6: ADVANCED VISUALIZATION

# 20. Create a scatter plot:

#     * Study hours vs marks
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.scatter(df["study_hours"], df["marks"])
# Seaborn alternative:
# sns.scatterplot(data=df, x="study_hours", y="marks")
plt.title("Study hours vs Marks")

# 21. Create a heatmap:

#     * Correlation matrix
plt.subplot(1,3,2)
sns.heatmap(df.drop(columns=["student_id"]).corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")

# 22. Create a distribution plot:

#     * Study hours
plt.subplot(1,3,3)
sns.histplot(df["study_hours"].dropna(), kde=True)
plt.title("Study hours Dist")

plt.tight_layout()
plt.show()

# 23. (Optional) Combine multiple variables in one visualization

# Question:
# Which visualization helped you understand data better?
print("The heatmap was best to understand overall correlations quickly.")
print("#"*50)

# ---

# ## SECTION 7: VISUALIZATION ETHICS

# 24. Explain why choosing the right chart is important
print("Choosing the right chart ensures a quick and completely accurate understanding of the data trend.")
# 25. What can go wrong with misleading charts?
print("Misleading charts can cause false interpretation and wrong conclusions.")

# Example:
# Wrong scale, wrong chart type, etc.
print("#"*50)

# ---

# ## SECTION 8: MINI DASHBOARD (IMPORTANT)

# 26. Create a simple dashboard using multiple plots:

#     * Bar chart
#     * Scatter plot
#     * Histogram

# 27. Arrange them properly (single view)
plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
df.groupby("city")["marks"].mean().plot(kind="bar", title="Avg Marks by City")
# Seaborn alternative:
# sns.barplot(data=df.groupby("city")["marks"].mean().reset_index(), x="city", y="marks").set(title="Avg Marks by City")

plt.subplot(2,2,2)
plt.scatter(df["study_hours"], df["marks"])
# Seaborn alternative:
# sns.scatterplot(data=df, x="study_hours", y="marks")
plt.title("Study hours vs Marks")

plt.subplot(2,2,3)
plt.hist(df["marks"], bins=10)
# Seaborn alternative:
# sns.histplot(data=df, x="marks", bins=10)
plt.title("Marks Distribution")

plt.tight_layout()
plt.show()
print("#"*50)

# ---

# ## SECTION 9: INSIGHTS & CONCLUSION

# 28. Write at least 5 insights from your analysis
print("INSIGHTS:")
print("1. Students with higher study hours generally score more.")
print("2. Attendance positively impacts performance.")
print("3. Bangalore students tend to perform highly.")
print("4. Both male and female students show distinct average markings.")
print("5. The relationship between attendance and marks is very strong.")

# Examples:

# * Students with higher study hours score more
# * Attendance impacts performance
# * Certain cities perform better

# 29. Suggest 2 improvements for students
print("SUGGESTIONS:")
print("1. Make sure to attend all classes as it strongly correlates with marks.")
print("2. Increase daily self-study hours.")
print("#"*50)

# ---

# ## BONUS (OPTIONAL)

# * Predict student performance based on study habits
print("You could use linear regression based on study hours and attendance to predict marks.")
# * Suggest how college can improve results
print("Colleges can track attendance strictly to identify students who need help.")

# ---

# NOTE:
# Focus on understanding patterns and explaining insights clearly.
# Visualization should support your conclusions.

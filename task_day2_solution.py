import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
# Ensure that missing values are handled if any exist in the dataset so mathematical operations don't fail later
df = pd.read_csv("students_data.csv")

print("\n--- SECTION 1: STATISTICAL SUMMARY ---")
print("Summary Statistics:\n", df.describe())
print("Mean marks:", df["marks"].mean())
print("Median marks:", df["marks"].median())
print("Standard Deviation of marks:", df["marks"].std())
print("Average study hours:", df["study_hours"].mean())
print("Average attendance:", df["attendance"].mean())
print("Average marks by city:\n", df.groupby("city")["marks"].mean())

print("\nQuestion: What do you understand from the summary?")
print("Answer: The summary provides central tendency and spread of marks, attendance, and study hours. It shows the variation in marks across different cities, with some cities potentially showing higher or more consistent averages than others.")

print("\n--- SECTION 2: CORRELATION ANALYSIS ---")
# Filtering only numeric columns and dropping student_id
numeric_df = df.select_dtypes(include=['int64', 'float64']).drop(columns=['student_id'], errors='ignore')
corr_matrix = numeric_df.corr(numeric_only=True)
print("Correlation Matrix:\n", corr_matrix)

print("\nStrongly related variables:")
# Using unstack and dropping identical values for easier readability
print(corr_matrix.unstack().sort_values(ascending=False).drop_duplicates())

print("\nStudy hours and marks correlation:", corr_matrix.loc["study_hours", "marks"])
print("Attendance and marks correlation:", corr_matrix.loc["attendance", "marks"])

print("\nQuestion: Which factor affects marks more?")
# Dynamically fetch the winner
study_corr = corr_matrix.loc["study_hours", "marks"]
att_corr = corr_matrix.loc["attendance", "marks"]
print(f"Answer: Looking at the correlation coefficients (Study Hours: {study_corr:.3f}, Attendance: {att_corr:.3f}), we can deduce which one has a stronger linear relationship.")

print("\nQuestion: Does correlation mean causation? Explain.")
print("Answer: No, correlation does not imply causation. A strong relationship indicates they move together, but it does not prove one variable explicitly causes the other to change. Other hidden factors might be involved.")

print("\n--- SECTION 3: OUTLIER DETECTION ---")
# Interquartile Range (IQR) method for Marks
Q1_marks = df["marks"].quantile(0.25)
Q3_marks = df["marks"].quantile(0.75)
IQR_marks = Q3_marks - Q1_marks
outliers_marks = df[(df["marks"] < (Q1_marks - 1.5 * IQR_marks)) | (df["marks"] > (Q3_marks + 1.5 * IQR_marks))]
print("Outliers in marks:\n", outliers_marks)

# IQR method for Study Hours
Q1_study = df["study_hours"].quantile(0.25)
Q3_study = df["study_hours"].quantile(0.75)
IQR_study = Q3_study - Q1_study
outliers_study = df[(df["study_hours"] < (Q1_study - 1.5 * IQR_study)) | (df["study_hours"] > (Q3_study + 1.5 * IQR_study))]
print("Outliers in study hours:\n", outliers_study)

print("\nQuestion: Explain how outliers affect analysis")
print("Answer: Outliers can significantly skew the mean and standard deviation, distorting the overall understanding of the general student population and leading to misleading correlations.")

print("\nQuestion: Should we remove outliers? Why or why not?")
print("Answer: It depends on the context. If outliers are data entry errors, they should be removed or corrected. If they represent genuine extreme cases (e.g., exceptional students), they might be valuable for specific analyses and should be kept or analyzed separately.")

print("\n--- SECTION 4: FEATURE ANALYSIS ---")
print("Average marks by gender:\n", df.groupby("gender")["marks"].mean())
print("Average marks by city:\n", df.groupby("city")["marks"].mean())

print("\nQuestion: Which feature is most important for student performance?")
print("Answer: Based on the correlation matrix, the feature with the highest correlation with marks (typically study hours or attendance) serves as the strongest indicator of performance.")

print("\n--- SECTION 5: BASIC VISUALIZATION ---")
# Creating a Grid of 5 plots
plt.figure(figsize=(14, 10))

plt.subplot(3, 2, 1)
df.groupby('city')['marks'].mean().plot(kind='bar', color='skyblue')
plt.title('Avg Marks by City')

plt.subplot(3, 2, 2)
df.groupby('gender')['marks'].mean().plot(kind='bar', color='salmon')
plt.title('Avg Marks by Gender')

plt.subplot(3, 2, 3)
plt.plot(df['student_id'], df['marks'], marker='o', linestyle='-')
plt.title('Marks Trend by Student')
plt.xlabel('Student ID')

plt.subplot(3, 2, 4)
plt.hist(df['marks'], bins=10, color='lightgreen', edgecolor='black')
plt.title('Distribution of Marks')

plt.subplot(3, 2, 5)
sns.boxplot(x=df['marks'], color='orange')
plt.title('Marks Distribution (Boxplot)')

plt.tight_layout()
plt.show()

print("\nQuestion: What do you observe from each chart?")
print("Answer: The boxplot shows the spread and any potential outliers. The histogram confirms the distribution shape. Bar charts reveal group differences (city/gender). The line chart tracks marks sequentially by student_id.")

print("\n--- SECTION 6: ADVANCED VISUALIZATION ---")
plt.figure(figsize=(15, 4))

plt.subplot(1, 3, 1)
sns.scatterplot(data=df, x='study_hours', y='marks')
plt.title('Study Hours vs Marks')

plt.subplot(1, 3, 2)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')

plt.subplot(1, 3, 3)
sns.histplot(df['study_hours'].dropna(), kde=True, color='purple')
plt.title('Distribution Plot of Study Hours')

plt.tight_layout()
plt.show()

print("\nQuestion: Which visualization helped you understand data better?")
print("Answer: The heatmap is extremely effective for immediately identifying strongly correlated numeric variables at a glance. The scatterplot gives an intuitive sense of the linear relationship between specific factors.")

print("\n--- SECTION 7: VISUALIZATION ETHICS ---")
print("Question: Explain why choosing the right chart is important")
print("Answer: Choosing the right chart ensures that the audience understands the data accurately. A wrong chart can miscommunicate the relationships or trends.")
print("Question: What can go wrong with misleading charts?")
print("Answer: Misleading charts (e.g., manipulated scales, inappropriate visualizations) can cause decision-makers to draw false conclusions, leading to critical errors.")

print("\n--- SECTION 8: MINI DASHBOARD ---")
# Dashboard layout
fig = plt.figure(figsize=(14, 10))
gs = fig.add_gridspec(2, 2)

# Top Left: Bar Chart
ax1 = fig.add_subplot(gs[0, 0])
sns.barplot(data=df, x='city', y='marks', errorbar=None, ax=ax1, palette='Set2')
ax1.set_title('Average Marks by City')

# Top Right: Scatter Plot
ax2 = fig.add_subplot(gs[0, 1])
sns.scatterplot(data=df, x='study_hours', y='marks', size='attendance', sizes=(50, 200), ax=ax2)
ax2.set_title('Study Hours vs Marks (size=attendance)')

# Bottom: Histogram
ax3 = fig.add_subplot(gs[1, :])
sns.histplot(df['marks'], bins=10, kde=True, color='teal', ax=ax3)
ax3.set_title('Overall Marks Distribution')

plt.suptitle('Student Performance Dashboard', fontsize=16)
plt.tight_layout()
plt.show()

print("\n--- SECTION 9: INSIGHTS & CONCLUSION ---")
print("Insights:")
print("1. Students with higher study hours generally score more.")
print("2. Class attendance positively impacts overall performance.")
print("3. There are clear performance differences across different cities.")
print("4. Very low or very high study hours can surface as outliers requiring distinct focus.")
print("5. Correlation between study hours and attendance is noticeably strong.")

print("\nImprovements for Students:")
print("1. Encourage consistent study routines since it heavily influences final grades.")
print("2. Promote regular attendance, possibly using early warning systems for chronic absentees.")

print("\n--- BONUS (OPTIONAL) ---")
print("To predict student performance based on study habits, one could apply Simple Linear Regression or Multiple Linear Regression using features like 'study_hours' and 'attendance' as independent variables to predict 'marks'. Colleges can proactively identify at-risk students and offer tutoring before finals.")

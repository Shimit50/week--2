import matplotlib.pyplot as plt
import seaborn as sns

# Bar chart - average scores per subject
subject_means = df[['math_score', 'science_score', 'english_score']].mean()
subject_means.plot(kind='bar')
plt.title('Average Scores per Subject')
plt.ylabel('Score')
plt.show()

# Pie chart - grade distribution
grades = pd.cut(df['average'], bins=[0, 60, 70, 80, 90, 100], 
                labels=['F', 'D', 'C', 'B', 'A'])
grade_counts = grades.value_counts()
grade_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Grade Distribution')
plt.show()

# Histogram - math scores distribution
df['math_score'].plot(kind='hist', bins=10)
plt.title('Math Scores Distribution')
plt.xlabel('Score')
plt.show()

# Line chart - performance trend by rank (if you have rank data)
# df.groupby('rank')['average'].mean().plot(kind='line')

# Scatter plot - Math vs Science
plt.scatter(df['math_score'], df['science_score'])
plt.title('Math vs Science Scores')
plt.xlabel('Math Score')
plt.ylabel('Science Score')
plt.show()

# Heatmap - correlation matrix
corr = df[['math_score', 'science_score', 'english_score']].corr()
sns.heatmap(corr, annot=True)
plt.title('Correlation Matrix')
plt.show()
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

df = pd.read_csv('labtasks/decision_trees/drug_consumption_clean.csv')

feature_columns = [
    "Age", "Gender", "Education", "Country", "Ethnicity",
    "Nscore (Neuroticism)", "Escore (Extraversion)", "Oscore (Openness to experience)",
    "Ascore (Agreeableness)", "Cscore (Conscientiousness)", "Impulsiveness", "SS (Sensation)"
]

# Example of multiple features selection
features = df[feature_columns]

# Select the label column
labels = df['Alcohol']

X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(random_state=42, max_depth= 3)
clf.fit(X_train, y_train)

plt.figure(figsize=(20, 10))
plot_tree(clf, filled=True, feature_names=feature_columns, class_names=clf.classes_)
plt.show()

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

conf_matrix = confusion_matrix(y_test, y_pred)
print(f'Confusion Matrix:\n{conf_matrix}')
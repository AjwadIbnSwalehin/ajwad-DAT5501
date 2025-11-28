import pandas as pd

file_path = "C:/Users/aibnswaleh001/Downloads/drug_consumption.data"
# above .data file is comma delimited
df = pd.read_csv(file_path, delimiter=",")

headings = ["ID", "Age", "Gender", "Education", "Country", "Ethnicity", "Nscore (Neuroticism)", "Escore (Extraversion)", "Oscore (Openness to experience)", "Ascore (Agreeableness)", "Cscore (Conscientiousness)", "Impulsiveness", "SS (Sensation)", "Alcohol", "Amphetamines", "Amyl Nitrate", "Benzodiazepine", "Caffeine", "Cannabis", "Chocolate", "Cocaine", "Crack", "Ecstasy", "Heroin", "Ketamine", "Legalh", "LSD", "Methamphetamine", "Mushrooms", "Nicotine", "Semer", "VSA (volatile substance abuse consumption)"]

df.columns = headings

drug_csv = df.to_csv("labtasks/decision_trees/drug_consumption_clean.csv")
import pandas as pd

df = pd.read_csv('bronze.csv')

# enlever les espaces de tout les colonnes 'object'

df[df.select_dtypes(['object']).columns] = df.select_dtypes(['object']).apply(lambda x: x.str.strip())


# Traitement des valeurs manquants 
# (choix :remplacer par la moyenne)

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

mean_TotalCharges = df['TotalCharges'].mean()


df['TotalCharges'] = df['TotalCharges'].fillna(mean_TotalCharges)


df['TotalCharges'] = df['TotalCharges'].astype(float)


# Remplacer les valeurs 'Yes' et 'No' par 1 et 0
df = df.replace({'Yes': 1, 'No': 0,'No internet service':2,'No phone service':3})

# Convertir les colonnes en entiers
df[['Partner', 'Dependents', 'PhoneService','Churn','MultipleLines','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies']] = df[['Partner', 'Dependents', 'PhoneService','Churn','MultipleLines','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies']].astype(int)

df.to_csv('bronze.csv',index=False)
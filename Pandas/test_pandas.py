import pandas as pd
import matplotlib.pyplot as plt

pandas_df = pd.read_excel('titanic3.xls')
print(pandas_df.shape)
print(pandas_df.columns)
print(pandas_df.head(5))

new_df = pandas_df.drop(['sibsp', 'parch', 'fare',
                'body', 'home.dest', 'boat', 
                'ticket', 'cabin', 'embarked'], 
                axis=1)

print(new_df.head(5))

#méthode describe() pour obtenir des statistiques descriptives sur les données
print(new_df.describe())

# pour les valeurs manquantes, on peut soit les supprimer, soit les remplacer par une valeur
#remplacer les valeurs manquantes par la moyenne
new_df.fillna(new_df['age'].mean())

#supprimer les valeurs manquantes
other_df = new_df.dropna(axis=0)
print(other_df.describe())

#on peut extraire des informations dircteùent
print(other_df['pclass'].value_counts())
other_df['pclass'].value_counts().plot(kind='bar')
plt.show()

#grouper les données
print(other_df[['pclass', 'survived', 'age', 'sex']].groupby(['sex']).mean())

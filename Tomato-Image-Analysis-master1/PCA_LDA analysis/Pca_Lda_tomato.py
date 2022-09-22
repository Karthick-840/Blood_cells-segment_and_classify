print(__doc__)

import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

# load dataset into Pandas DataFrame
tomato = pd.read_excel(r'Classification Run 17-8-2020.xls')

# print(tomato)
df = pd.DataFrame(tomato)


def applyFunc(s):
    return ''

df['Type'] = df['Picture Name'].apply(applyFunc)

df['Type'][df['Picture Name'].str.contains("Sa")] = "Standard"
df["Type"][df['Picture Name'].str.contains("Be")] = "Beef"
df["Type"][df['Picture Name'].str.contains("Ch")] = "Cherry"

# print(tomato['Type'])

# df = pd.read_csv(, names=['sepal length','sepal width','petal length','petal width','target'])

features = ['Area', 'Length', 'Width']

# Separating out the features
x = df.loc[:, features].values

# Separating out the target
y = df.loc[:, ['Type']].values

# Standardizing the features
x = StandardScaler().fit_transform(x)

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])
# X_r = pca.fit(X).transform(X)

lda = LinearDiscriminantAnalysis(n_components=2)
lineardiscriminants = lda.fit(x, y).transform(x)
linearDf = pd.DataFrame(data=lineardiscriminants, columns=['linear discriminant 1', 'linear discriminant 2'])

# Percentage of variance explained for each components
print('explained variance ratio (first two components): %s'
      % str(pca.explained_variance_ratio_))

lfinalDf = pd.concat([linearDf, df[['Type']]],axis=1)
pfinalDf = pd.concat([principalDf, df[['Type']]], axis=1)

fig1 = plt.figure(figsize=(8, 8))
ax = fig1.add_subplot(1, 1, 1)
ax.set_xlabel('PC 1', fontsize=15)
ax.set_ylabel('PC 2', fontsize=15)
ax.set_title('2 component PCA', fontsize=20)
targets = ['Standard', 'Beef', 'Cherry']
colors = ['r', 'g', 'b']
for target, color in zip(targets, colors):
    indicesToKeep = pfinalDf['Type'] == target
    ax.scatter(pfinalDf.loc[indicesToKeep, 'principal component 1'], pfinalDf.loc[indicesToKeep, 'principal component 2'],
               c=color, s=50)
ax.legend(targets)
ax.grid()

fig2 = plt.figure(figsize=(8, 8))
ax = fig2.add_subplot(1, 1, 1)
ax.set_xlabel('LD 1', fontsize=15)
ax.set_ylabel('LD 2', fontsize=15)
ax.set_title('2 component LDA', fontsize=20)
targets = ['Standard', 'Beef', 'Cherry']
colors = ['r', 'g', 'b']
for target, color in zip(targets, colors):
    indicesToKeep = lfinalDf['Type'] == target
    ax.scatter(lfinalDf.loc[indicesToKeep, 'linear discriminant 1'], lfinalDf.loc[indicesToKeep, 'linear discriminant 2'],
               c=color, s=50)
ax.legend(targets)
ax.grid()

plt.show()

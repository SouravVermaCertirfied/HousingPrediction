# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Linear Regression

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle


# %%
# get_ipython().magic('matplotlib inline')


# %%
USAHousing = pd.read_csv("4_1_USA_Housing.csv")


# %%
USAHousing.head()


# %%
USAHousing.columns


# %%
USAHousing.describe()


# %%
sns.pairplot(USAHousing)


# %%
USAHousing["Price"].plot.kde()


# %%
sns.displot(USAHousing["Price"])


# %%
sns.heatmap(USAHousing.corr())

# %% [markdown]
# # Train Test Split for Machine Learning

# %%
# make X as the independent variables - this should be dataFrame
# make y as the dependent variables   - this should be Series

# Not sure why this approch is not working
# independent_cols = ['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
#        'Avg. Area Number of Bedrooms', 'Area Population', 'Address']
# to_predict = 'Price'

# X = USAHousing[independent_cols]
# y = USAHousing[to_predict]
X = USAHousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
y = USAHousing['Price']

### TRAIN TEST SPLIT ###
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)


### Selecting a Machine Learning Mdoel and Fitting it ####
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, y_train)

### Predict ###



# %%
pickle.dump(lm, open('model.pkl','wb'))




# %%

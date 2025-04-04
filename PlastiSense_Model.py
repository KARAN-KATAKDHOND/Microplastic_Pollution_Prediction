import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
df= pd.read_csv("/content/microplastic_pollution_large_dataset.csv")
#df.head()

#df.info()

#df.describe()

#df.isnull().sum()

#df.head()

#df.drop(columns=["Temperature","pH_Level","Water_Flow_Rate"],inplace=True)

#df.head()

from sklearn.model_selection import train_test_split
x=df.drop(columns=["Microplastic_Concentration"])
y=df['Microplastic_Concentration']

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3, random_state=42)

# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# xtrain = scaler.fit_transform(xtrain)
# xtest = scaler.transform(xtest)

#CREATE A MODEL
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(xtrain, ytrain)   #TRAIN THE MODEL

ypred=model.predict(xtest)  #PREDICT THE TARGET VARIABLE

#SHOW RESULT
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
mae = mean_absolute_error(ytest, ypred)
mse = mean_squared_error(ytest, ypred)
r2 = r2_score(ytest, ypred)

# Print results
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R-squared Score:", r2)

#to download your ML

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)
print("Model saved successfully!")



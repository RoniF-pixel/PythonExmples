#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics


# In[6]:


calories=pd.read_csv('C:/Users/0&1/OneDrive/Documents/burnt/calories.csv')


# In[28]:


#print the first 5 rows of the calories dataframe
calories.head()


# In[29]:


exercise_data=pd.read_csv('C:/Users/0&1/Downloads/burnt/exercise.csv')


# In[30]:


exercise_data.head()


# In[31]:


#Combining the two Dataframes
data=pd.concat([exercise_data,calories['Calories']],axis=1)


# In[32]:


data.head()


# In[33]:


#Checking the number of rows and columns
data.shape


# In[34]:


#Getting some information about the data
data.info()


# In[35]:


#Checking for missing values
data.isnull().sum()


# In[36]:


#Descriptive Statistics 
data.describe()


# In[43]:


#Data Visualization
#plotting the Gender column in count plot
sns.set()
plt.figure(figsize=(6,6))
sns.countplot(x=data.Gender)
plt.show()


# In[50]:


#Finding the distribution of 'Age' column
plt.figure(figsize=(6,6))
sns.distplot(data.Age)
plt.show()


# In[51]:


#Finding the distribution of 'Height' column

sns.distplot(data.Height)
plt.show()


# In[52]:


#Finding the distribution of 'Weight' column
plt.figure(figsize=(6,6))
sns.distplot(data.Weight)
plt.show()


# In[53]:


#Finding the distribution of 'Duration' column
plt.figure(figsize=(6,6))
sns.distplot(data.Duration)
plt.show()


# In[54]:


#Finding the distribution of 'Heart_Rate' column
plt.figure(figsize=(6,6))
sns.distplot(data.Heart_Rate)
plt.show()


# In[55]:


#Finding the distribution of 'Body_Temp' column
plt.figure(figsize=(6,6))
sns.distplot(data.Body_Temp)
plt.show()


# In[58]:


correlation = data.corr()


# In[59]:


plt.figure(figsize=(10,10))
sns.heatmap(correlation,square=True,fmt='.1f',annot=True, cmap='Greens')


# In[60]:


#Converting the text data in 'Gender' column to numerical values
data.replace({"Gender":{'male':0,'female':1}},inplace=True)
data.head()


# In[64]:


#Seperating features and Target
X=data.drop(columns=['User_ID','Calories'],axis=1)
Y=data['Calories']


# In[65]:


X


# In[66]:


Y


# In[67]:


#Splitting the data into training data and Test data
X_train, X_test, Y_train , Y_test=train_test_split(X,Y,test_size=0.2,random_state=2)


# In[68]:


print(X.shape,X_train.shape,X_test.shape)


# In[69]:


#Model Training
#XGBoost Regressor
#loading the model 
model=XGBRegressor()


# In[70]:


#Training the model with X_train
model.fit(X_train,Y_train)


# In[71]:


#Evaluation
#Prediction on Test Data
test_data_prediction=model.predict(X_test)


# In[72]:


print(test_data_prediction)


# In[73]:


#Mean Absolute Error
#Using Linear Regression Model
#Importing Linear Regression Model
from sklearn.linear_model import LinearRegression


# In[74]:


#We have already converted the categorical gender column and selected the featueres along with target
#We also have splitted our data into training and testing data so we do model training using linear regression
#Performing Standardisation
#Standardizing
from sklearn.preprocessing import StandardScaler


# In[75]:


sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)


# In[76]:


#loading the linear regression model 
reg=LinearRegression()


# In[77]:


#Training our Linear Rigression Model to find the equation of our linear regression model
reg.fit(X_train,Y_train)


# In[78]:


#Model Evaluation
#prediction on testing data
Y_pred=reg.predict(X_test)


# In[79]:


#Comparing the Values predicted by our model by using r squared error
metrics.r2_score(Y_test,Y_pred)


# In[80]:


#Visualising the the actaul burnt calories and the Predicted burnt calories
plt.scatter(Y_test,Y_pred)
plt.xlabel("Actual Calories Burnt")
plt.ylabel("Predicted Calories Burnt")
plt.title("Actual Burnt Calories VS Predicted Burnt Calories")
plt.show()


# In[81]:


#Using Random Forest Regressor Model
#Importing random forest regressor model 
from sklearn.ensemble import RandomForestRegressor


# In[82]:


#Loading RandomForestRegressor to RandomForest variable.
RandomForest=RandomForestRegressor(n_estimators=100)


# In[83]:


#Training the Model
RandomForest.fit(X_train,Y_train)


# In[84]:


#Model Evaluation
Y_pred=RandomForest.predict(X_test)
Y_pred


# In[85]:


#Using R square metric for evaluation
error_score =metrics.r2_score(Y_test,Y_pred)
print("Rsquared Error Score = " , error_score)


# In[86]:


#Visualising the acual calories burnt and the predicted calories burnt
plt.scatter(Y_test,Y_pred)
plt.xlabel("Actual Calories Burnt")
plt.ylabel("Predicted Calories Burnt")
plt.title("Actual Burnt Calories VS Predicted Burnt Calories")
plt.show()


# In[87]:


#Visualising the same result in a plot
#preventing from error
Y_testlist=list(Y_test)


# In[88]:


#plotting the actual burnt calories (Y_testlist) in orange color and the predicted burnt calories (Y_pred) in grey color
plt.plot(Y_testlist, color="orange", label = 'Actual Burnt Calories')
plt.plot(Y_pred, color="grey", label = 'Predicted Burnt Calories')
plt.title("Actual Vs Predicted Burnt Clories")
plt.xlabel("Number of Values")
plt.ylabel("Calories Burnt")
plt.legend()
plt.show()


# In[89]:


#We  see that the actual Burnt Calories is slightly more than the predicted value which is not too much
#considering our 0.99 error obtained in our R squared score, so
#Random Forest Regressor Algorithm is best suited our current ML model predicting the calories burnt during exercise.


# In[ ]:





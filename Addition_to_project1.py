import pandas as pd
import numpy as np

file_name='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'
dff=pd.read_csv(file_name)
dff=dff.drop(["id"],axis=1)
dff=dff.drop(["Unnamed: 0"],axis=1)

from sklearn.model_selection import train_test_split
from sklearn import linear_model
X_train,X_test,y_train,y_test=train_test_split(dff,dff,test_size=.2,random_state=4);
reg = linear_model.LinearRegression()
train_x=np.asanyarray(X_train[['price']])
train_y=np.asanyarray(X_train[['yr_built']])
reg.fit(train_x,train_y)
test_x=np.asanyarray(X_test[['price']])
test_y=np.asanyarray(X_test[['yr_built']])
tes_y_=reg.predict(test_x)
mae= np.mean(np.absolute(test_y_ - test_y))
mae_=mae/21613
mse=np.mean((test_y_ - test_y) ** 2)
mse_=mse/21613
print("Mean absolute error: " , mae_)
print("Residual sum of squares (MSE): " ,mse_ )

'''from sklearn.model_selection import train_test_split
from sklearn import linear_model'''
X_train,X_test,y_train,y_test=train_test_split(dff,dff,test_size=0.2,random_state=4);
regg = linear_model.LinearRegression()
train_x=np.asanyarray(X_train[['grade']])
train_y=np.asanyarray(X_train[['sqft_living']])
regg.fit(train_x,train_y)
test_x=np.asanyarray(X_test[['grade']])
test_y=np.asanyarray(X_test[['sqft_living']])
tes_y_=regg.predict(test_x)
mae= np.mean(np.absolute(test_y_ - test_y))
mae_=mae/21613
mse=np.mean((test_y_ - test_y) ** 2)
mse_=mse/21613
print("Mean absolute error: " , mae_)
print("Residual sum of squares (MSE): " ,mse_ )

'''from sklearn.model_selection import train_test_split
from sklearn import linear_model'''
X_train,X_test,y_train,y_test=train_test_split(dff,dff,test_size=0.2,random_state=4);
regg = linear_model.LinearRegression()
train_x=np.asanyarray(X_train[['bedrooms']])
train_y=np.asanyarray(X_train[['yr_renovated']])
regg.fit(train_x,train_y)
test_x=np.asanyarray(X_test[['bedrooms']])
test_y=np.asanyarray(X_test[['yr_renovated']])
tes_y_=regg.predict(test_x)
mae= np.mean(np.absolute(test_y_ - test_y))
mae_=mae/21613
mse=np.mean((test_y_ - test_y) ** 2)
mse_=mse/21613
print("Mean absolute error: " , mae_)
print("Residual sum of squares (MSE): " ,mse_ )

'''from sklearn.model_selection import train_test_split
from sklearn import linear_model'''
X_train,X_test,y_train,y_test=train_test_split(dff,dff,test_size=0.2,random_state=4);
regg = linear_model.LinearRegression()
train_x=np.asanyarray(X_train[['bathrooms']])
train_y=np.asanyarray(X_train[['bedrooms']])
regg.fit(train_x,train_y)
test_x=np.asanyarray(X_test[['bathrooms']])
test_y=np.asanyarray(X_test[['bedrooms']])
tes_y_=regg.predict(test_x)
mae= np.mean(np.absolute(test_y_ - test_y))
mae_=mae/21613
mse=np.mean((test_y_ - test_y) ** 2)
mse_=mse/21613
print("Mean absolute error: " , mae_)
print("Residual sum of squares (MSE): " ,mse_ )


'''from sklearn.model_selection import train_test_split
from sklearn import linear_model'''
X_train,X_test,y_train,y_test=train_test_split(dff,dff,test_size=0.2,random_state=4);
regg = linear_model.LinearRegression()
train_x=np.asanyarray(X_train[['sqft_basement']])
train_y=np.asanyarray(X_train[['sqft_above']])
regg.fit(train_x,train_y)
test_x=np.asanyarray(X_test[['sqft_basement']])
test_y=np.asanyarray(X_test[['sqft_above']])
tes_y_=regg.predict(test_x)
mae= np.mean(np.absolute(test_y_ - test_y))
mae_=mae/21613
mse=np.mean((test_y_ - test_y) ** 2)
mse_=mse/21613
print("Mean absolute error: " , mae_)
print("Residual sum of squares (MSE): " ,mse_ )

'''from sklearn.model_selection import train_test_split
from sklearn import linear_model'''
X_train,X_test,y_train,y_test=train_test_split(dff,dff,test_size=0.2,random_state=4);
regg = linear_model.LinearRegression()
train_x=np.asanyarray(X_train[['sqft_above']])
train_y=np.asanyarray(X_train[['sqft_basement']])
regg.fit(train_x,train_y)
test_x=np.asanyarray(X_test[['sqft_above']])
test_y=np.asanyarray(X_test[['sqft_basement']])
tes_y_=regg.predict(test_x)
mae= np.mean(np.absolute(test_y_ - test_y))
mae_=mae/21613
mse=np.mean((test_y_ - test_y) ** 2)
mse_=mse/21613
print("Mean absolute error: " , mae_)
print("Residual sum of squares (MSE): " ,mse_ )



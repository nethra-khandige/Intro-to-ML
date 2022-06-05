import pandas as pd
import numpy as np

file_name='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'
dff=pd.read_csv(file_name)
dff=dff.drop(["id"],axis=1)
dff=dff.drop(["Unnamed: 0"],axis=1)
avg_bedrooms=dff["bedrooms"].astype("float").mean(axis=0)
dff["bedrooms"].replace(np.nan,avg_bedrooms,inplace=True)

avg_bathrooms=dff["bathrooms"].astype("float").mean(axis=0)
dff["bathrooms"].replace(np.nan,avg_bedrooms,inplace=True)

from sklearn.model_selection import train_test_split
from sklearn import linear_model
X_train,X_test,y_train,y_test=train_test_split(dff,dff,test_size=.2,random_state=4);
reg = linear_model.LinearRegression()
train_x=np.asanyarray(X_train[['yr_built']])
train_y=np.asanyarray(X_train[['price']])
reg.fit(train_x,train_y)
test_x=np.asanyarray(X_test[['yr_built']])
test_y=np.asanyarray(X_test[['price']])
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
train_y=np.asanyarray(X_train[['price']])
regg.fit(train_x,train_y)
test_x=np.asanyarray(X_test[['grade']])
test_y=np.asanyarray(X_test[['price']])
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
train_y=np.asanyarray(X_train[['price']])
regg.fit(train_x,train_y)
test_x=np.asanyarray(X_test[['bedrooms']])
test_y=np.asanyarray(X_test[['price']])
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
train_x=np.asanyarray(X_train[['floor']])
train_y=np.asanyarray(X_train[['price']])
regg.fit(train_x,train_y)
test_x=np.asanyarray(X_test[['floor']])
test_y=np.asanyarray(X_test[['price']])
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
train_y=np.asanyarray(X_train[['price']])
regg.fit(train_x,train_y)
test_x=np.asanyarray(X_test[['sqft_basement']])
test_y=np.asanyarray(X_test[['price']])
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
train_x=np.asanyarray(X_train[['zipcode']])
train_y=np.asanyarray(X_train[['price']])
regg.fit(train_x,train_y)
test_x=np.asanyarray(X_test[['zipcode']])
test_y=np.asanyarray(X_test[['price']])
tes_y_=regg.predict(test_x)
mae= np.mean(np.absolute(test_y_ - test_y))
mae_=mae/21613
mse=np.mean((test_y_ - test_y) ** 2)
mse_=mse/21613
print("Mean absolute error: " , mae_)
print("Residual sum of squares (MSE): " ,mse_ )



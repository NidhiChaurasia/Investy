import numpy as np   #array lists in python
import pandas as pd 
# import missingno as msno
# import plotly.express as px
# import seaborn as sns
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# %matplotlib inline
import csv
import warnings
warnings.filterwarnings("ignore")

# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.tree import DecisionTreeClassifier

# from MLM import 
invest_data=pd.read_csv('invest.csv')
print(invest_data)

# encoding sex column
invest_data.replace({'GENDER':{'Male':0,'Female':1}}, inplace=True)

3 # encoding 'smoker' column
invest_data.replace({'Do you invest in Investment Avenues?':{'Yes':0,'No':1}}, inplace=True)

# encoding 'region' column
invest_data.replace({'Do you invest in Stock Market?':{'Yes':0,'No':1}}, inplace=True)

invest_data.replace({'Your sources of information for investments is':{"Newspapers and Magazines": 0,"Internet": 1,"Financial Consultants": 2,"Television": 3,"Friends and Family": 4}}, inplace=True)

invest_data.replace({'Reasons for investing in Fixed Deposits':{
    "Risk Free": 0,
    "High Interest Rates": 1,
    "Fixed Returns": 2
}
}, inplace=True)

invest_data.replace({'Reasons for investing in Government Bonds':{
    "Safe Investment": 0,
    "Tax Incentives": 1 , 
    "Assured Returns":2
}
}, inplace=True)

invest_data.replace({'Reasons for investing in Mutual Funds':{
    "Better Returns": 0,
    "Tax Benefits": 1,
    "Fund Diversification": 2
}
}, inplace=True)

invest_data.replace({'Reasons for investing in Equity Market':{
    "Capital Appreciation": 0,
    "Dividend": 1,
    "Liquidity": 2
}
}, inplace=True)

invest_data.replace({'What are your savings objectives?':{
    "Retirement Plan": 0,
    "Health Care": 1,
    "Education": 2
}
}, inplace=True)

invest_data.replace({'Which investment avenue do you mostly invest in?':{
"Mutual Funds": 0,
"Equity Market": 1,
"Debentures": 2,
"Government Bonds": 3,
"Fixed Deposits": 4,
"Public Provident Fund": 5,
"Gold": 6 , 
"Real Estate": 7 ,
"Cryptocurrency": 8
}
}, inplace=True)

invest_data.replace({'How much return do you expect from any investment instrument?':{
"10%-20%": 0,
"20%-30%": 1,
"30%-40%": 2
}
}, inplace=True)

invest_data.replace({'How frequently do you monitor your investments?':{
"Daily": 0,
"Weekly": 1,
"Monthly": 2,
"Quarterly": 3,
"Yearly": 4
}
}, inplace=True)

invest_data.replace({'How long do you prefer to keep your money in any investment instrument?':{
"Less than 1 year": 0,
"1-3 years": 1,
"3-5 years": 2,
"More than 5 years": 3
}
}, inplace=True)

invest_data.replace({'What is your purpose behind investment?':{
"Wealth Creation": 0,
"Savings for Future": 1,
"Returns": 2
}
}, inplace=True)

invest_data.replace({'What are your investment objectives?':{
"Capital Appreciation": 0,
"Income": 1,
"Growth": 2
}
}, inplace=True)

invest_data.replace({'What are the factors considered by you while investing in any instrument?':{
"Returns": 0,
"Locking Period": 1,
"Risk": 2
}
}, inplace=True)

invest_data.replace({'Do you invest in Stock Market?':{'Yes':0,'No':1}
}, inplace=True)


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier


#splitting features
X = invest_data.drop('Which investment avenue do you mostly invest in?',axis=1)    #axis=1 when dropping column       
y = invest_data['Which investment avenue do you mostly invest in?']   
print(X)


X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=0.3,random_state=42)
print(X.shape , X_train.shape , X_test.shape)

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()
rf.fit(X_train , y_train)

import joblib

filename='trained_model.sav'
joblib.dump(rf,filename)



# input_data=(0,34,0,1,8,6,4,5,7,3,2,9,0,2,1,0,3,3,2,0,0,1,0,1,1)
# #change input data to numpy array
# input_data_as_numpy_array = np.asarray(input_data)

# #reshaping numpy array for predicting only one instance
# input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# prediction = rf.predict(input_data_reshaped)
# print(prediction)

# if(prediction[0]==0):
#     print ("Mutual Funds")
# elif(prediction[0]==1):
#     print('Equity Market')
# elif(prediction[0]==2):
#     print('Debentures')
# elif(prediction[0]==3):
#     print('Government Bonds')
# elif(prediction[0]==4):
#     print('Fixed Deposits')
# elif(prediction[0]==5):
#     print('Public Provident Fund')
# elif(prediction[0]==6):
#     print('Gold')
# elif(prediction[0]==7):
#     print('Real Estate')
# elif(prediction[0]==8):
#     print('Cryptocurrency')

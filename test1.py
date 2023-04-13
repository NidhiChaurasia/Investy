import joblib

cls=joblib.load('trained_model.sav')

input_data=(0,34,0,1,8,6,4,5,7,3,2,9,0,2,1,0,3,3,2,0,0,1,0,1,1)

data = cls.predict([input_data])

if(data[0]==0):
    print ("Mutual Funds")
elif(data[0]==1):
    print('Equity Market')
elif(data[0]==2):
    print('Debentures')
elif(data[0]==3):
    print('Government Bonds')
elif(data[0]==4):
    print('Fixed Deposits')
elif(data[0]==5):
    print('Public Provident Fund')
elif(data[0]==6):
    print('Gold')
elif(data[0]==7):
    print('Real Estate')
elif(data[0]==8):
    print('Cryptocurrency')
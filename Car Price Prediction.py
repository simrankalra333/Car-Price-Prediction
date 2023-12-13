from tkinter import *
import tkinter.ttk as ttk
import numpy as np
import pandas as pd
import joblib

model=joblib.load('regressor.joblib')
le=joblib.load('transmission.joblib')
lo=joblib.load('owner.joblib')
sc=joblib.load('scaler.joblib')
ct=joblib.load('onehot.joblib')


root=Tk()
root.title('Car Price Prediction System')
root.geometry('1000x1000')

def predict_price():
    
        temp=pd.DataFrame({'name':cbb1.get(),'year':e2.get(),'km_driven':e3.get(),
                       'fuel':cbb4.get(),'seller_type':cbb5.get(),'transmission':cbb6.get(),
                       'owner':cbb7.get(), 'mileage':e8.get(), 'engine':e9.get(),'max_power':e10.get(),
                       'seats':e11.get()}, index=[0])
        temp['transmission']=le.transform(temp['transmission'])
        temp['owner']=lo.transform(temp['owner'])
        temp=ct.transform(temp)
        temp=sc.transform(temp)
        predicted_price=float(model.predict(temp))
        predicted_price= round(predicted_price,2)
        l_price.config(text = predicted_price)

    
    
title=Label(root,text='Car Price Prediction',bg='white',fg='Red',font=('Ariel',30,'bold'))
title.place(x=300,y=10)

l1=Label(root,text='Car Company',bg='white',fg='blue',font=('Ariel',15,'bold'))
l1.place(x=30,y=100)
lst1=['Maruti','Hyundai','Mahindra','Tata','Honda','Toyota','Ford','Chevrolet','Renault',
      'Volkswagen','BMW','Skoda','Nissan','Jaguar','Volvo','Datsun','Mercedes-Benz','Fiat',
      'Audi','Lexus','Jeep','Others']
selected_company = StringVar()
cbb1=ttk.Combobox(root,font=3,values=lst1,width=15,textvariable=selected_company)
cbb1['state'] = 'readonly'
cbb1.place(x=240,y=100)
cbb1.set('Select')

l2=Label(root,text='Year of Mfg.',bg='white',fg='blue',font=('Ariel',15,'bold'))
l2.place(x=30,y=150)
e2=Entry(root,width=30)
e2.place(x=240,y=150,height=30)

l3=Label(root,text='Kilometres Driven',bg='white',fg='blue',font=('Ariel',15,'bold'))
l3.place(x=30,y=200)
e3=Entry(root,width=30)
e3.place(x=240,y=200,height=30)

l4=Label(root,text='Fuel Type',bg='white',fg='blue',font=('Ariel',15,'bold'))
l4.place(x=30,y=250)
lst4=['Diesel','Petrol','LPG','CNG']
selected_fuel = StringVar()
cbb4=ttk.Combobox(root,font=3,values=lst4,width=15,textvariable=selected_fuel)
cbb4['state'] = 'readonly'
cbb4.place(x=240,y=250)
cbb4.set('Select')

l5=Label(root,text='Seller Type',bg='white',fg='blue',font=('Ariel',15,'bold'))
l5.place(x=30,y=300)
lst5=['Individual','Dealer','Trustmark Dealer']
selected_seller = StringVar()
cbb5=ttk.Combobox(root,font=3,values=lst5,width=15,textvariable=selected_seller)
cbb5['state'] = 'readonly'
cbb5.place(x=240,y=300)
cbb5.set('Select')

l6=Label(root,text='Transmission',bg='white',fg='blue',font=('Ariel',15,'bold'))
l6.place(x=30,y=350)
lst6=['Manual','Automatic']
selected_trans = StringVar()
cbb6=ttk.Combobox(root,font=3,values=lst6,width=15,textvariable=selected_trans)
cbb6['state'] = 'readonly'
cbb6.place(x=240,y=350)
cbb6.set('Select')

l7=Label(root,text='Owner',bg='white',fg='blue',font=('Ariel',15,'bold'))
l7.place(x=500,y=100)
lst7=['First Owner','Second Owner','Third Owner','Fourth & Above Owner','Test Drive Car']
selected_owner = StringVar()
cbb7=ttk.Combobox(root,font=3,values=lst7,width=15,textvariable=selected_owner)
cbb7['state'] = 'readonly'
cbb7.place(x=710,y=100)
cbb7.set('Select')

l8=Label(root,text='Mileage\n(kmpl/kmpkg)',bg='white',fg='blue',font=('Ariel',15,'bold'))
l8.place(x=500,y=150)
e8=Entry(root,width=30)
e8.place(x=710,y=150,height=30)

l9=Label(root,text='Engine(CC)',bg='white',fg='blue',font=('Ariel',15,'bold'))
l9.place(x=500,y=250)
e9=Entry(root,width=30)
e9.place(x=710,y=250,height=30)

l10=Label(root,text='Max. Power(bhp)',bg='white',fg='blue',font=('Ariel',15,'bold'))
l10.place(x=500,y=300)
e10=Entry(root,width=30)
e10.place(x=710,y=300,height=30)

l11=Label(root,text='No. of Seats',bg='white',fg='blue',font=('Ariel',15,'bold'))
l11.place(x=500,y=350)
e11=Entry(root,width=30)
e11.place(x=710,y=350,height=30)

btn=Button(root,width=15,height=1,text='Predict Price',font=('Ariel',20,'bold'),bg='white',fg='red',command=predict_price)
btn.place(x=350,y=425)

l=Label(root,text='Price of car(in Rs):',bg='yellow',fg='black',font=('Ariel',20,'bold'))
l.place(x=250,y=550)

l_price=Label(root,bg='yellow',fg='black',font=('Ariel',20,'bold'))
l_price.place(x=505,y=550)

root.mainloop()
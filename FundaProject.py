import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import csv
from tkinter import *

Data = {'Temperature' : [],
            'Humidity' : [],
            'DayNight' : [],
            'Wind' : [],
            'Change Of Rain' : []}

with open('DataSet.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    print(type(reader))
    for columns in reader:
        Data['Temperature'].append(int(columns[0]))
        Data['Humidity'].append(int(columns[1]))
        Data['DayNight'].append(int(columns[2]))
        Data['Wind'].append(int(columns[3]))
        Data['Change Of Rain'].append(int(columns[4]))


df = pd.DataFrame(Data,columns=['Temperature','Humidity','DayNight','Wind','Change Of Rain'])

x = df[['Temperature','Humidity','DayNight','Wind']]
y = df['Change Of Rain']

model = LinearRegression()
results_formula = model.fit(x,y)
y_pred = model.predict(x)

print(df)
print('intercept: \n',model.intercept_)
print('codfficients: \n',model.coef_)
#-------------------------------------------------------------------------------------

def Predict():
    pre = model.intercept_ + (model.coef_[0]*tem.get()) + (model.coef_[1]*hum.get()) + (model.coef_[2]*don.get()) + (model.coef_[3]*wis.get())
    if pre < 0:
        pre = 0.00
    elif pre > 100:
        pre = 100.00
    chanceofrain.set(str(round(pre,2)) + " %")
#------------------------------------------------------------------------------------- 
root = Tk()
root.option_add("*Font","consolas 16")
root.title("Predict Weather")
Label(root,text="Predict Chance Of Rain",fg="white",bg="DeepSkyBlue2").grid(row=0,columnspan=2,ipadx=78)
Label(root,text="Please Input Your Data",fg="white",bg="DeepSkyBlue2",font=("Courier", 12)).grid(row=1,columnspan=2,ipadx=100)

tem = DoubleVar()
hum = DoubleVar()
don = DoubleVar()
wis = DoubleVar()
chanceofrain = StringVar()


Label(root,text="Temperature",font=("Courier", 12)).grid(row=2,column=0,sticky=W,pady=10,padx=3)
Entry(root ,textvariable = tem ,width=15).grid(row=2,column=1,sticky=W,padx=3)

Label(root,text="Humidity",font=("Courier", 12)).grid(row=3,column=0,sticky=W,pady=10,padx=3)
Entry(root ,textvariable = hum ,width=15).grid(row=3,column=1,sticky=W,padx=3)

Label(root,text="Day(1) or Night(0)",font=("Courier", 12)).grid(row=4,column=0,sticky=W,pady=10,padx=3)
Entry(root ,textvariable = don ,width=15).grid(row=4,column=1,sticky=W,padx=3)

Label(root,text="Wind speed",font=("Courier", 12)).grid(row=5,column=0,sticky=W,pady=10,padx=3)
Entry(root ,textvariable = wis ,width=15).grid(row=5,column=1,sticky=W,padx=3)

Button(root, text="Predict!",fg="white",bg="DeepSkyBlue2",bd=5,font=("consolas", 14),command = Predict ).grid(row=6,columnspan=2,pady=7)

Label(root,text="Chance Of Rain(%) = ",font=("Courier", 12)).grid(row=7,column=0,sticky=W,pady=5,padx=3)

Label(root,textvariable = chanceofrain ,font=("Courier", 12)).grid(row=7,column=1,sticky=W,pady=5,padx=3)

root.mainloop()

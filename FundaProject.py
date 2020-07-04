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

root = Tk()
root.option_add("*Font","consolas 16")
root.title("Predict Weather")
Label(root,text="Predict Chance Of Rain",fg="white",bg="DeepSkyBlue2").pack(fill=X,anchor=W)
Label(root,text="Please Input Your Data",fg="white",bg="DeepSkyBlue2",font=("Courier", 12)).pack(fill=X,anchor=W)
root.mainloop()

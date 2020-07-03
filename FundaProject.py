import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

acc_pred = {'Vehicle Population' : [8370,6922,6467,6584,8313
                                ,8488,9918,10996,8763,11087
                                ,11293,10715,10542,12175,11320
                                ,11668,12038,11214,12299,11506],
            'Human Population' : [132051,137966,157782,193198,234962
                                ,297475,340913,393255,458182,511063
                                ,567780,613153,643824,703372,767067
                                ,841314,922748,942000,1030000,1122700],
            'Accidents' : [14821000,15222000,15634000,16056000,16491000
                        ,16937000,17295000,17865000,18349000,18845000
                        ,19328000,19811000,20506000,21093000,21693000
                        ,22294000,22911000,23544000,24196000,24233000]}

df = pd.DataFrame(acc_pred,columns=['Vehicle Population','Human Population','Accidents'])

x = df[['Vehicle Population','Human Population']]
y = df['Accidents']

model = LinearRegression()
results_formula = model.fit(x,y)
y_pred = model.predict(x)

print(df)
print('intercept: \n',model.intercept_)
print('codfficients: \n',model.coef_)
print(type(acc_pred['Human Population']))

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)

data = pd.read_csv('C:\Himanshu\Superstore\Superstore.csv',encoding='ISO-8859-1')

print(type(data))

dataset = data.loc[:,['Order Date','Sales']]


dataset['Order Date'] = pd.to_datetime(dataset['Order Date'],infer_datetime_format=True)



indexDataSet = dataset.set_index(['Order Date'])


print(indexDataSet.head(5))

#cols = ['Row ID','Order ID','Ship Date','Ship Mode','Customer ID','Customer Name','Segment',
#        'Country','City','State','Postal Code','Region','Product ID','Category','Sub-Category','Product Name',
#        'Quantity','Discount','Profit']

#indexDataSet.drop(['Row ID'], inplace= True)

plt.xlabel('Order Date')
plt.ylabel('Sales')
plt.plot(indexDataSet)
plt.show()


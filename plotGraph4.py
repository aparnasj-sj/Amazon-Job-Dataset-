'''
Plot the scatter graph between year vs No. of jobs opening related to Java.
Print the year and number of Jobs opening in Java Profile.
Note: Use the Keyword 'Java' or 'java' in Basic Qualification
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("amazon_jobs_dataset.csv")
bq=df['BASIC QUALIFICATIONS']
bq=np.array(bq)
b=[]
# to sort out olnly Java 
for item in bq:
    item=str(item)
    
    if ('Java' in item) or ('java' in item):
        b.append(True)
        #pass
    else:
        b.append(False)
        #pass
df=df[b]
year=df['Posting_date'].str.split(', ',expand=True)[1] # extract year a
freq=year.value_counts() 
freq.sort_index(ascending=True,inplace=True)
x=freq.index
y=freq
plt.scatter(x,y)
plt.show()
s=x.shape[0]
for i in range(s):
    print(x[i],y[i])
    



'''
Plot the line graph between no. of Job postings with respect to year.
Print the year and the number of job posting as integer value.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("amazon_jobs_dataset.csv")

date=df.Posting_date
year=[]
for elm in date:
    year.append(elm.split(", ")[1])
year=np.array(year)
d={}
for elm in year:
    if elm in d:
        d[elm]+=1
    else:
        d[elm]=1
    
    
year=np.unique(year)


count=[]
for elm in year:
    
    count.append(d[elm])
count=np.array(count)

plt.plot(year,count)
plt.show()

s=year.shape[0]
#print(s)
for i in range(s):
    print(year[i],count[i])
    


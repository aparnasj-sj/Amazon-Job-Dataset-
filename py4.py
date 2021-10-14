'''
Find the month having most job openings in Year 2018 ?
Print the month (Month Name i.e January, February, March) and Number of job opening as Integer Value
'''

import csv
job={}
max_month=''
max_count=0
count=0
with open('amazon_jobs_dataset.csv') as fo:
    fdata=csv.DictReader(fo,skipinitialspace=True)
    flist=list(fdata)#list of orederedDict
    for row in flist:
        date=row['Posting_date']
        l=date.split(',')  #split mont/date , year
        if(int(l[1])==2018): # if 2018
            mon=l[0].split(' ')[0] #get month name alone 
            if mon in job:
                job[mon]+=1
            else:
                job[mon]=1
            if(job[mon]>max_count):
                max_month=mon
                max_count=job[mon]
print(max_month,max_count)
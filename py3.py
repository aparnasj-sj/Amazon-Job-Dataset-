'''
Find the country does Amazon need the most number of Java Developer?
Print the Country(Country Shortcut as given in Dataset) and number of job opening as integer value
Note :Here we will use the BASIC QUALIFICATIONS feature to find out whether Java is required for the job or not.Keyword is used is 'Java'.(Here case should not be changed).

'''

import csv
job={}
count=0
maxC=0
loc=''
with open('amazon_jobs_dataset.csv') as fo:
    fdata=csv.DictReader(fo,skipinitialspace=True)
    flist=list(fdata)#list of orederedDict
    for row in flist:
        q=row['BASIC QUALIFICATIONS']
        if('Java' in q):
            c_code=row['location'].split(',')[0] # list item number 1 is country code (split return list)
            if c_code in job:
                job[c_code]+=1
            else:
                job[c_code]=1
            if(job[c_code]>maxC):
                loc=c_code
                maxC=job[c_code]
print(c_code,maxC)
                
                
            
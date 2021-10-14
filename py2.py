'''
What are the total number of job openings related to Computer Vision ?
Note:For finding the job related to computer vision check the Job Title column.
'''


import csv
job={}
count=0
with open('amazon_jobs_dataset.csv') as fo:
    fdata=csv.DictReader(fo,skipinitialspace=True)
    flist=list(fdata)#list of orederedDict
    for row in flist:
        title=row['Title']
        if('Computer Vision' in title): #search if a word in a string 
            #if word in string 
            
            count+=1
print(count)
        
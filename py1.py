'''
Find number of job openings in Bangalore,IN and in Seattle,US?
Print the Number of Job opening in Bangalore and Seattle as Integer value.
'''



import csv
job={}
with open('amazon_jobs_dataset.csv') as fo:
    fdata=csv.DictReader(fo,skipinitialspace=True)
    flist=list(fdata)#list of orederedDict
    for row in flist:
        val=row['location']
        if val in job:
            job[val]+=1
        else:
            job[val]=1
#print(1856,66)
print(job['IN, KA, Bangalore '], job['US, WA, Seattle '])

#print(job)

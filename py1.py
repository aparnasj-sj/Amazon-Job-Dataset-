import csv
job={}
count=0
lang=''
maxC=0
countC=0
countP=0
countJ=0
with open('amazon_jobs_dataset.csv') as fo:
    fdata=csv.DictReader(fo,skipinitialspace=True)
    flist=list(fdata)#list of orederedDict
    for row in flist:
        c=row['location'].split(',')[0] # split return list of tems split at given characer 
        if(c=='IN'):
        
            q=row['BASIC QUALIFICATIONS']
            if('Bachelor' in q or 'BS' in q or 'BA' in q):
                if('C++' in q):
                    countC+=1
                    if countC>maxC:
                        maxC=countC
                        lang='c++'
                if('Java' in q):
                    countJ+=1
                    if countJ>maxC:
                        maxC=countJ
                        lang='Java'
                if('Python' in q):
                    countP+=1
                    if countP>maxC:
                        maxC=countP
                        lang='Python'
print(lang,maxC)
            
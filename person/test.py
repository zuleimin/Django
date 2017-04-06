import os,sys

s='Lesson'
filenew=open('nce3.txt','r+')
lines=filenew.readlines()
filenew.close()
filecount = 1
maxcount = 60
newfilename = repr(filecount) + '.txt'
i=j=0

for filecount in range(maxcount):
    newfilename = s + repr(filecount+1) + '.txt'
    newfile = open(newfilename,'w')
    for i in range(j,len(lines)):
        newfile.write(lines[j-1])
        j=j+1
        if s in lines[i]:
            filecount=filecount+1
            break
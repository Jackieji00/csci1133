# fileobj = open('somefile','w')
# for i in range(3):
#     record = ''
#     for j in range(1,4):
#         record += str(i*3+j)+','
#     record = record[:-1]
#     fileobj.write(record)
#     if i < 2:
#         fileobj.write('\n')
# fileobj.close()

#Generating Synthetic Test Data
# filename = input('filename: ')
# fileobj = open(filename,'w')
# import random
# for i in range(1001):
#     line = ''
#     line = str(i) + ' ' + str(random.randint(-1000,1000))
#     fileobj.write(line)
#     if i < 1000:
#         fileobj.write('\n')
# fileobj.close()

#strech
##letter frequencies
import urllib.request
url = 'http://textfiles.com/100/hack11a.txt'
uu = urllib.request.urlopen(url)
Letters=['A','B','C','D','E','F','G','H','I','J','K',\
  'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
contents = str(uu.readlines())
dic = {}
for i in contents:
    i = i.upper()
    if i in Letters:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
list1 = []
for (k,v) in dic.items():
    list1.append(k)
list1.sort()
uu.close()
for x in list1:
    print(x,dic[x])

#Workout
#Earthquake Data
infile = open('all_day.csv','r')
outfile = open('location_and_mag.csv','w')
lines = infile.readlines()
titles = lines[0].split(',')
# for i in range(0,22):
#     str0 = str(i) + ' '+ titles[i] +' '
#     str0 += '\n'
#     print(str0)
dic0 ={}
for j in lines[1:]:
    contents = j.split(',')
    dic0[contents[4]] = contents[14]
list0 = []
for k,v in dic0.items():
    list0.append(k)
list0.sort()
title = 'magnitude,location\n'
outfile.write(title)
for x in list0:
    str2 = dic0[x].strip('"')
    str1 = str(x) + ',' + str(str2) + '\n'
    outfile.write(str1)
infile.close()
outfile.close

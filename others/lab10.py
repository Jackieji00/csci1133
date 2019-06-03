# # fileobj = open('somefile','w')
# for i in range(3):
#  record = '' # start with a null string
#  for j in range(1,4):
#      record += str(i*3+j) + ',' # append each value and comma
#  record = record[:-1] # strip off the last comma
#  print(record)
#  # fileobj.write(record)
#  if i < 2:
#      print('\n')
# #      fileobj.write('\n') # no \n on last record!
# # fileobj.close()

# #Generating Synthetic Test Data
# fileobj = open('Testdata','w')
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
# import urllib.request
# url = 'http://textfiles.com/100/hack11a.txt'
# uu = urllib.request.urlopen(url)
# Letters=['A','B','C','D','E','F','G','H','I','J','K',\
#   'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# contents = str(uu.readlines())
# dic = {}
# for i in contents:
#     i = i.upper()
#     if i in Letters:
#         if i in dic:
#             dic[i] += 1
#         else:
#             dic[i] = 1
# list1 = []
# for (k,v) in dic.items():
#     list1.append(k)
# list1.sort()
# uu.close()
# for x in list1:
#     print(x,dic[x])

#Workout
##Earthquake Data, part one
file0 = open('/Users/max/Downloads/all_day.csv', 'r')
total0 = list(file0.readlines())
title0 = total0[0]
title0 = title0.split(",")
for x in range(0,len(total0)-1):
    total0[x]=total0[x].split(",")
result = open('sth','w')
for i in range(0,len(title0)-1):
    outcome0 = str(i)
    for x in range(0,len(total0)-1):
        outcome0 += ' ' +str(total0[x][i])
    result.write(outcome0)
    if i < len(title0)-1:
        result.write('\n')
file0.close()
result.close()

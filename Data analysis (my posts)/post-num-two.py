import numpy as np
from matplotlib import pyplot as plt
import csv
from collections import Counter
import pandas as pd
#plt.style.use('seaborn-v0_8-talk')

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]

dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]


js_dev_y_plot=plt.plot(ages_x,js_dev_y,color='r',linewidth=2,marker='.',label='js_dev')
dev_y_plot=plt.plot(ages_x,dev_y,color='k',linewidth=2,marker='.',label='dev')
#info for plot

plt.xlabel('ages') #for name of y label
plt.ylabel('salary') #for name of x label
plt.title('differences wages and salary') #for title name
plt.grid('true') #this is look for background
plt.legend() #This code is for the part that knows the meaning of the two lines,It is located above on the left.

#this code of print will print the available style you can use it like that

# -> plt.style.use('seaborn-v0_8-pastel')

print(plt.style.available)



plt.savefig(r".venv")
plt.show()

#------------------------------------------------------------------------------------------------
#second plot

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]
dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]
py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]
ages_x_number=np.arange(len(ages_x))
width=0.25

#plt.bar(ages_x_number-width,js_dev_y,width=width,color='y',label='js_dev')
#plt.bar(ages_x_number,dev_y,width=width,color='k',label='dev_y')
#plt.bar(ages_x_number+width,py_dev_y,width=width,color='r',label='py_dev')


#we can read this data by using pandas, it will be easier for that
#but i prefer this way to understand the concept

with open("data.csv","r")as csv_file:
    csv_reader=csv.DictReader(csv_file)
    language_counter=Counter()
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

#the data is very lager #so i will take the most common
#i will use 'Counter' library
#you can use numpy ,will take the same output

language=[]
uses=[]
for item in language_counter.most_common(15):
    language.append(item[0])
    uses.append(item[1])
language.reverse() # to get largest first
uses.reverse() # to get largest first
data=pd.read_csv("data.csv") # pandas module as pd ,to read data in format 'comma sprited Values'
print(data)# to see data
language=data['LanguagesWorkedWith']
IDS=data['Responder_id']
language_counter=Counter()
for item in language:
    language_counter.update(item.split(';')) #will counts the number of repetitions .
print(f"language counter :{language_counter}")#type dictionary
language_counter.most_common(15) # top 15
uses=list(language_counter.keys()) #get only language
language_final=list(language_counter.values()) #get number of repetitions
uses.sort()
language_final.sort()# to sort data

#some print to understand data

print(uses)
print(language_final)


#info for plot
plt.barh(uses,language_final)
plt.ylabel("language") #for name of y label
plt.xlabel("uses") #for name of x label
plt.title("language_uses") #for title name
plt.grid("Ture") #this is look of background
plt.show()


"""
In any graph, do these things:
1. Read the data
2. Verify the validity of the data
3. Remove false values ​​from the data and try to extract useful values ​​from them
4. Write the information on the graph to make it easier
5. Display the graph
"""
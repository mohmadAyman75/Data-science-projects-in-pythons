from matplotlib import pyplot as plt




ages=[25,26,27,28,29,30,31,32,33,34,35]
dev_y=[38496,42000,42515,45643,51356,57435,59213,61235,62135,63135,64515]
plt.plot(ages,dev_y)

#info for plot
plt.title("median salasy for devolper")
plt.xlabel("ages") #for name of x label
plt.ylabel("salary") #for name of y label

by_dev_y=[38496,52000,42515,45643,51356,57435,59213,61235,62135,63135,64515]
plt.plot(ages,by_dev_y)
plt.legend(["dev" ,"by_dev"]) #This code is for the part that knows the meaning of the two lines , It is located above on the left.

plt.show()


#seconde plot
income=[10000,15000,17000,18000,19000,20000,20500,21000,59123,60000,61000]
salary=[38496,42000,42515,45643,51356,57435,59213,61235,62135,63135,64515]
ages=[25,26,27,28,29,30,31,32,33,34,35]

#info for plot
plt.plot(ages,income,'k--',label='income') #for name of x label
plt.plot(ages,salary,'o--',label='salary') #for name of y label
plt.title("income and salary for developer") ##This code is for the part that knows the meaning of the two lines.
plt.legend()
plt.show()



import matplotlib.pyplot as plt
import numpy as np
import os
os.chdir(r"/media/santhosh/Education/Python/csv2plot") #change current work directory
file=open("eg.csv") #open csv file
year=[i for i in range(1990,2009)]
count=0
cont=[]
y990=[]
y991=[]
y992=[]
y993=[]
y994=[]
y995=[]
y996=[]
y997=[]
y998=[]
y999=[]
y000=[]
y001=[]
y002=[]
y003=[]
y004=[]
y005=[]
y006=[]
y007=[]
y008=[]
for line in file:
	country,y90,y91,y92,y93,y94,y95,y96,y97,y98,y99,y00,y01,y02,y03,y04,y05,y06,y07,y08=line.split(';') #to-split-the-values-seperated-by-";"
	cont.append(country)
	y990.append(float(y90.replace(',','')))
	y991.append(float(y91.replace(',','')))
	y992.append(float(y92.replace(',','')))
	y993.append(float(y93.replace(',','')))
	y994.append(float(y94.replace(',','')))
	y995.append(float(y95.replace(',','')))
	y996.append(float(y96.replace(',','')))
	y997.append(float(y97.replace(',','')))
	y998.append(float(y98.replace(',','')))
	y999.append(float(y99.replace(',','')))
	y000.append(float(y00.replace(',','')))
	y001.append(float(y01.replace(',','')))
	y002.append(float(y02.replace(',','')))
	y003.append(float(y03.replace(',','')))
	y004.append(float(y04.replace(',','')))
	y005.append(float(y05.replace(',','')))
	y006.append(float(y06.replace(',','')))
	y007.append(float(y07.replace(',','')))
	y008.append(float(y08.replace(',','')))
	count+=1
adata=np.array([y990,y991,y992,y993,y994,y995,y996,y997,y998,y999,y000,y001,y002,y003,y004,y005,y006,y007,y008]) #create an array using numpy
for i in range(1,count):
	plt.figure("electricity-production-by-"+cont[i]) #create a new figure with the title as name of the country
	plt.plot(year[:],adata[:,i],'r--')  #plot the graph 
	plt.plot(year[:],adata[:,i],'bs') #plot the points
	plt.xlabel('year')					#label the x-axis
	plt.ylabel('electricity production') #label the y-axis
	plt.title(cont[i])	#label the graph with the country name
	plt.savefig(cont[i],format='jpeg') #save the graphs
	#plt.show() #show the graphs

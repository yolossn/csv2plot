import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
os.chdir(r"/media/santhosh/Education/Python/csv2plot") #change current work directory
file=pd.read_csv("eg.csv",error_bad_lines=False,sep=";") #open csv file
print(file.country[1])
count=len(file.country)
year=[i for i in range(1990,2009)]
for y in range(0,count):
	for j in range(1,len(file.loc[1])):
		file.loc[y][j]=float(file.loc[y][j].replace(',',''))

#print(file)
os.chdir(r"/media/santhosh/Education/Python/csv2plot/graph")
for i in range(0,count):
	plt.figure("electricity-production-by-"+file.country[i]) #create a new figure with the title as name of the country
	plt.plot(year[:],file.loc[i][1:],'r--')  #plot the graph 
	plt.plot(year[:],file.loc[i][1:],'bs') #plot the points
	plt.xlabel('year')					#label the x-axis
	plt.ylabel('electricity production') #label the y-axis
	plt.title(file.country[i])	#label the graph with the country name
	plt.savefig(file.country[i],format='jpeg') #save the graphs
	#plt.show() #show the graphs'''

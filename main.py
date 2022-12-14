#If you would like to view the graph, once the programs runs, there should be a file named graph.png. if you click this, you can view the graph
#Also it may take a long time for the program to load for the first time
import numpy as np
import matplotlib.pyplot as plt

pennies = [22, 21, 30, 47, 4, 39, 7, 39, 3, 6, 36, 25, 21, 5, 43, 59, 5, 12, 22, 25, 10, 4, 38, 38, 42, 7, 14, 44, 53, 6, 19, 5, 31, 16, 5, 38, 20, 37, 5, 43, 59, 30, 24, 4, 8, 5, 5, 46, 50, 5, 50, 32, 27, 18, 3, 57, 41, 35, 3, 5, 3, 20, 28, 13, 6, 3, 4, 39, 32, 23, 6, 3, 4, 15, 4, 6, 8, 38, 4, 8, 16, 29, 28, 9, 9, 4, 26, 54, 20, 23, 5, 8, 45, 8, 9, 14, 4, 4, 4, 7, 23, 4, 14, 10, 5, 15, 8, 15, 4, 20, 15, 25, 45, 23, 10, 25, 42, 46, 31, 20, 45, 40, 41, 54, 46, 46, 40, 45, 7, 23, 46, 18, 29, 42, 43, 12, 16, 5, 21, 53, 37, 42, 34, 56, 13, 4, 5, 34, 33, 4, 25, 23, 4, 6, 30, 4, 4, 7, 4, 10, 4, 32, 4, 43, 38, 16, 4, 18, 18, 37, 4, 4, 21, 36, 17, 51, 5, 5, 30, 19, 18, 21, 26, 31, 4, 32, 10, 4, 5, 21, 12, 5, 10, 5, 25, 24, 46, 51, 4, 42, 44, 43, 15, 22, 20, 35, 39, 40, 48, 56, 31, 33, 7, 20, 20, 4, 46, 42, 31, 30, 7, 22, 46, 52, 8, 27, 13, 24, 12, 26, 35, 17, 6, 38, 50, 33, 29, 32, 36, 17, 26, 38, 8, 4, 55, 48, 56, 25, 21, 39, 39, 5, 42, 4, 21, 26, 23, 18, 16, 30, 13, 38, 47, 24, 19, 4, 38, 32, 17, 42, 6, 40, 25, 30, 55, 22, 6, 20, 40, 24, 51, 21, 46, 45, 5, 14, 37, 4, 46, 30, 19, 4, 12, 48, 25, 36, 37, 3, 1, 31, 49, 4, 24, 5, 23, 30, 43, 46, 18, 26, 31, 4, 24, 4, 5, 50, 47, 17, 28, 56, 3, 39, 5, 21, 20, 31, 39, 38, 16, 20, 22, 47, 6, 37, 37, 5, 38, 39, 38, 31, 5, 49, 30, 37, 38, 25, 33, 4, 4, 15, 24, 3, 27, 4, 4, 54, 5, 46, 24, 38, 50, 21, 31, 19, 25, 43, 29, 22, 4, 18, 7, 10, 37, 4, 26, 42, 23, 5, 4, 4, 5, 5, 15, 56, 4, 40, 20, 20, 4, 20, 16, 47, 15, 25, 36, 51, 47, 5, 4, 25, 9, 4, 4, 37, 14, 19, 4, 24, 60, 19, 7, 22, 6, 20, 41, 57, 5, 20, 32, 17, 38, 13, 27, 6, 4, 22, 29, 35, 28, 6, 29, 4, 43, 19, 35, 60, 21, 39, 39, 7, 24, 4, 6, 12, 4, 5, 3, 4, 29, 12, 6, 45, 23, 3, 5, 13, 31, 12, 30, 41, 10, 24, 22, 25, 4, 5, 5, 20, 38, 38, 8, 26, 7, 5, 45, 26, 5, 21, 3, 28, 41, 45, 6, 7, 29, 28, 46, 37, 15, 35, 4, 4, 24, 25, 47, 36, 41, 45, 31, 53, 4, 48, 4, 4, 3, 4, 4, 4, 23, 27, 6, 4, 5, 9, 3, 24, 5, 4, 34, 18, 14, 15, 36, 10, 33, 46, 4, 19, 31, 33, 32, 40, 35, 18, 3, 9, 34, 42, 18, 4, 5, 8, 28, 4, 48, 30, 14, 15, 5, 20, 29, 37, 19, 44, 46, 7, 5, 22, 21, 47, 29, 25, 10, 3, 3, 3, 34, 36, 12, 40, 50, 15, 22, 26, 5, 19, 39, 52, 4, 31, 5, 4, 52, 39, 48, 4, 4, 53, 4, 4, 16, 20, 6, 38, 33, 4, 48, 4, 5, 25, 30, 15, 28, 33, 4, 7, 16, 32, 5, 21, 49, 19, 10, 23, 34, 47, 25, 23, 27, 3, 19, 4, 28, 29, 22, 38, 35, 32, 4, 29, 38, 52, 29, 13, 24, 28, 3, 5, 27, 25, 6, 43, 26, 5, 38, 6, 5, 48, 4, 4, 19, 5, 4, 7, 35, 10, 4, 4, 4, 26, 33, 6, 15, 5, 8, 40, 23, 6, 3, 5, 6, 35, 21, 25, 13, 5, 25, 35, 30, 4, 3, 6, 5, 30, 18, 4, 45, 42, 20, 8, 42, 10, 18, 3, 4, 5, 43, 19, 38, 8, 57, 24, 31, 44, 4, 33, 5, 50, 4, 50, 4, 30, 60, 23, 5, 25, 4, 6, 4, 3, 4, 29, 12, 29, 5, 6, 6, 40, 51, 1, 27, 23, 26, 4, 5, 46, 25, 4, 16, 10, 32, 15, 4, 12, 37, 4, 29, 38, 4, 6, 21, 9, 31, 29, 6, 44, 4, 4, 38, 32, 42, 26, 26, 28, 30, 5, 51, 27, 44, 45, 16, 39, 21, 7, 4, 42, 8, 17, 14, 4, 3, 4, 4, 22, 18, 22, 44, 22, 5, 26, 6, 27, 6, 6, 32, 15, 3, 4, 19, 34, 46, 30, 20, 5, 20, 21, 49, 13, 47, 14, 18, 31, 50, 19, 4, 25, 31, 30, 6, 14, 8, 47, 31, 24, 30, 20, 34, 41, 44, 37, 35, 21, 43, 18, 29, 61, 31, 39, 39, 20, 21, 16, 35, 36, 44, 48, 28, 5, 23, 19, 21, 43, 13, 24, 19, 23, 24, 45, 5, 49, 52, 7, 4, 37, 46, 38, 26, 5, 5, 4, 5, 4, 4, 4, 4, 3, 5, 6, 4, 5, 46, 13, 39, 28, 35, 44, 22, 5, 26, 18, 4, 38, 14, 25, 5, 51, 10, 39, 32, 9, 37, 27, 42, 47, 25, 4, 49, 31, 4, 3, 3, 17, 24, 31, 18, 4, 18, 9, 7, 20, 47, 16, 46, 25, 28, 4, 3, 15, 60, 4, 51, 39, 34, 33, 4, 17, 4, 4, 13, 37, 8, 17, 19, 39, 27, 46, 33, 16, 41, 25, 14, 32, 19, 46, 15, 31, 7, 8, 7, 12, 40, 7, 5, 5, 16, 21, 42, 24, 4, 32, 38, 45, 3, 47, 37, 36, 54, 13, 38, 18, 46, 53, 35, 4, 4, 38, 23, 25, 26, 46, 18, 48, 29, 25, 44, 30, 44, 39, 30, 26, 42, 15, 27, 43, 5, 42, 3, 33, 4, 5, 19, 34, 20, 31, 52, 24, 4, 28, 4, 24, 27, 44, 61, 26, 44, 38, 39, 31, 19, 30, 29, 24, 41, 9, 8, 15, 37, 25, 4, 26, 35, 16, 37, 31, 19, 44, 11, 25, 17, 22, 45, 56, 50, 23, 45, 60, 4, 56, 45, 34, 27, 32, 19, 6, 5, 38, 4, 29, 6, 24, 37, 29, 27, 22, 39, 4, 38, 3, 4, 51, 22, 43, 24, 35, 5, 41, 41, 46, 32, 25, 56, 7, 36, 22, 42, 4, 36, 33, 19, 26, 53, 20, 31, 31, 5, 33, 43, 4, 4, 4, 4, 22, 4, 23, 20, 11, 5, 57, 56, 27, 47, 39, 5, 12, 42, 46, 13, 50, 6, 17, 32, 38, 42, 41, 5, 24, 3, 5, 5, 31, 19, 22, 33, 44, 43, 58, 5, 6, 26, 41, 38, 50, 14, 8, 27, 12, 19, 38, 24, 7, 12, 5, 12, 46, 51, 22, 17, 4, 21, 24, 31, 5, 29, 19, 33, 31, 38, 18, 24, 4, 3, 38, 27, 22, 15, 44, 5, 8, 4, 4, 4, 6, 5, 25, 5, 26, 61, 24, 4, 5, 42, 4, 4, 4, 21, 7, 15, 4, 24, 4, 20, 44, 22, 44, 61, 19, 14, 31, 7, 22, 23, 32, 4, 30, 28, 35, 34, 36, 16, 5, 38, 23, 30, 52, 56, 45, 22, 24, 4, 51, 29, 31, 22, 42, 52, 42, 4, 37, 5, 24, 57, 42, 39, 24, 6, 6, 34, 21, 4, 49, 42, 4, 4, 6, 14, 30, 14, 16, 45, 41, 26, 27, 35, 43, 5, 28, 24, 20, 42, 18, 27, 46, 24, 7, 44, 44, 44, 37, 46, 22, 26, 39, 23, 14, 6, 22, 37, 26, 35, 45, 14, 4, 40, 4, 30, 44, 45, 45, 3, 4 
]

n = int(input("How many coins would you like to sample? (Value of n)"))
trials = int(input("How many trials would you like to conduct?"))
flist = []
count= 0
tcount = 0
list= []
while tcount < trials:

    while count < n:
        rand_num = np.random.randint(1,1310)
        list.append(pennies[rand_num])
        count+=1
    value= np.sum(list)/n
    value= round(value)
    flist.append(value)
    count=0
    list = []
    tcount+=1
print(flist)
unique = np.unique(flist)
plt.hist(flist, bins=len(unique), range = (0,60))

plt.savefig('plot.png')
print("Go to plot.png for graph")
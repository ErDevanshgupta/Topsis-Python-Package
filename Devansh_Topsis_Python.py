# -*- coding: utf-8 -*-
"""
@author: Devansh Gupta
"""

# Importing the Library
import pandas as pd
import sys
import math


"""
Defining a function to normailze the data 
This function normalizes the data by divide each value by 
the square root of the sum of squares of the values in its column.
"""
def normalise(data):
    n,m=data.shape
    x=data.iloc[0:n,1:m]
    x=x.values.tolist()
    for j in range(0,len(x[0])):
        sumsq=0
        for i in range(0,n):
            sumsq+=x[i][j]*x[i][j]
        sumsq=math.sqrt(sumsq)
        for i in range(0,len(x)):
            x[i][j]/=sumsq
    return x


"""
This function multiplies each normalized
 value by its corresponding weight.
"""
def weighting(x,weight):
    for i in range(0,len(x)):
        for j in range(0,len(x[0])):
            x[i][j]*=weight[j]
    return x


"""
This function finds the ideal best (positive) and worst (negative)
 values for each criterion based on the requirement (req)
"""
def ideal(x,req):
    li=[]
    for j in range(0,len(x[0])):
        if(req[j]>0):
            can=-1e9
        else:
            can=1e9
        for i in range(0,len(x)):
            if(req[j]>0):
                can=max(can,x[i][j])
            else:
                can=min(can,x[i][j])
        li.append(can)
    return li


"""
This function computes the Euclidean distance of each
 alternative from the ideal best and worst solutions.
"""
def distance(x,req):
    li=[]
    for i in range(0,len(x)):
        dist=0
        for j in range(0,len(x[0])):
            dist+=(x[i][j]-req[j])*(x[i][j]-req[j])
        dist=math.sqrt(dist)
        li.append(dist)
    return li


"""
This function calculates the performance score
for each alternative and sorts them to determine the ranking.
"""
def performance(spos,sneg):
    li=[]
    for i in range(0,len(spos)):
        tot=(sneg[i]/(spos[i]+sneg[i]))
        li.append([i+1,tot])
    li=sorted(li, key = lambda x: x[1],reverse=True)
    for i in range(0,len(li)):
        li[i][1]=i+1
    return li

# Main Funcation 
def main():
    data=pd.read_csv(sys.argv[1])
    weight=[eval(x) for x in sys.argv[2].split(',')]
    reqstr=[sys.argv[3].split(',')]
    reqpos=[]
    reqneg=[]
    for i in reqstr[0]:
        if(i=='+'):
            reqpos.append(1)
            reqneg.append(-1)
        else:
            reqpos.append(-1)
            reqneg.append(1)
    x=normalise(data)
    x=weighting(x,weight)
    posideal=ideal(x,reqpos)
    negideal=ideal(x,reqneg)
    spos=distance(x,posideal)
    sneg=distance(x,negideal)
    li=performance(spos,sneg)

    for i in range(len(li)):
        print("Model "+str(li[i][0])+" ranks "+str(li[i][1]))

if __name__=="__main__":
    main()
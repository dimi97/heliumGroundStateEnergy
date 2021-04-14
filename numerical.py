import numpy as np
import math
from myCons import myCons as cons

class myFn:
    
    def makeVectorList(t,n):
      if t==1:
        vectorList=[]
        for i in range (0,n):
          vectorList.append([i])
      else:
        newVectorList=[]
        vectorList=myFn.makeVectorList(t-1,n)
        for i in vectorList:
          sum=np.sum(i)
          for j in range (0,n-sum):
            i.append(j)
            icopy=i.copy()
            newVectorList.append(icopy)    
            i.pop()     
        vectorList=newVectorList
      return vectorList
  
    def kSymmetry(vector):
        newVector=[]
        for i in vector:
            if i[1]%2==0:
                copy=i.copy()
                newVector.append(copy)
        return newVector    
     
    def func_n(J,K,M):        
        return 2*3.14**2*math.factorial(J+K+M+5)*(1/(M+2))*(1/(K+1)-1/(K+3)-1/(K+M+3)+1/(K+M+5))*(1/(2*cons.p))**(J+K+M+6)
    def func_c(J,K,M):
        return 8*3.14**2*math.factorial(J+K+M+4)*(1/(M+2))*(1/(K+1)-1/(K+M+3))*(1/(2*cons.p))**(J+K+M+5)
    def func_w(J,K,M):
        return myFn.func_n(J,K,M-1)
    
    def func_t1(J,K,M,j_1,k_1,m_1,j_2,k_2,m_2):
        return 2*(cons.p**2*myFn.func_n(J,K,M)-J*cons.p*myFn.func_n(J-1,K,M)+j_1*j_2*myFn.func_n(J-2,K,M)+k_1*k_2*myFn.func_n(J,K-2,M))
    def func_t2(J,K,M,j_1,k_1,m_1,j_2,k_2,m_2):
        return 2*m_1*m_2*myFn.func_n(J,K,M-2)+0.5*(-M*cons.p*(myFn.func_c(J,K,M)-myFn.func_c(J,K+2,M-2))+(m_1*j_2+m_2*j_1)*(myFn.func_c(J-1,K,M)-myFn.func_c(J-1,K+2,M-2))+(m_1*k_2+m_2*k_1)*(myFn.func_c(J+1,K,M-2)-myFn.func_c(J-1,K,M)))

    def matrix(cons,fn,vectorList):
        l=len(vectorList)
        matrix=np.zeros((l,l))
        
        for i in range (l):
            for j in range (l):
                  
                    j1=vectorList[i][0]
                    j2=vectorList[j][0]
                    
                    k1=vectorList[i][1]
                    k2=vectorList[j][1]
                    
                    m1=vectorList[i][2]
                    m2=vectorList[j][2]
                    
                    J=j1+j2
                    K=k1+k2
                    M=m1+m2
                          
                    matrix[i,j]=cons*fn(J,K,M)                 
        return matrix
                                 
    def tMatrix(cons,fn1,fn2,vectorList):
        l=len(vectorList)
        matrix=np.zeros((l,l))
        
        for i in range (l):
            for j in range (l):
                             
                    j1=vectorList[i][0]
                    j2=vectorList[j][0]
                    
                    k1=vectorList[i][1]
                    k2=vectorList[j][1]
                    
                    m1=vectorList[i][2]
                    m2=vectorList[j][2]
                    
                    J=j1+j2
                    K=k1+k2
                    M=m1+m2
                    
                    if M==0:
                          
                        matrix[i,j]=cons*fn1(J,K,M,j1,k1,m1,j2,k2,m2)
                    else:
                        matrix[i,j]=cons*fn1(J,K,M,j1,k1,m1,j2,k2,m2)+\
                            cons*fn2(J,K,M,j1,k1,m1,j2,k2,m2)                          
        return matrix
    
    
    def calcHamiltonian(T,C,W):
        H=T+C+W
        return H
        
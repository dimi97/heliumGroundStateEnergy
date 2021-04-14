import matplotlib
import matplotlib.pyplot as plt
from numerical import myFn
from myCons import myCons as cons
from scipy.linalg import eigh
from scipy import optimize
import numpy as np
import time


class main:
    def main():
        vectorList=myFn.makeVectorList(cons.t,cons.n)
        vectorList=myFn.kSymmetry(vectorList)
          
        N=myFn.matrix(1, myFn.func_n, vectorList)
        W=myFn.matrix(cons.e_2, myFn.func_w, vectorList)
        C=myFn.matrix(-cons.Z*cons.e_2, myFn.func_c, vectorList)
        
        T=myFn.tMatrix(0.5*cons.r_0*cons.e_2, myFn.func_t1,myFn.func_t2, vectorList)
             
        H=myFn.calcHamiltonian(T,C,W)
        
        eigvals, eigvecs = eigh(H, N, eigvals_only=False)

        energy=eigvals[0]
        
        # print("My Vector List \n",vectorList)
        # print("Vector List Lenght Length:",len(vectorList))
        # print ("Matrix N \n",N)
        # print ("Matrix W \n",W)
        # print ("Matrix C \n",C)
        # print ("Matrix T \n",T)
        # print("My Hamiltonian: \n",H)
        # print (energy)
        
        return energy

    def f(a):
        cons.setA(a+1e-6)
        
        energy=main.main()
        
        return energy
    
    
optA = optimize.brent(main.f)
    
print("min a:",optA)
print("energy:",main.f(optA))
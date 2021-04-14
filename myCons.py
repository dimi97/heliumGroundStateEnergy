class myCons:
    t=3
    n=3
    e_2=14.4
    a=0.1
    r_0=0.52917
    Z=2
    p=Z/(a*r_0)   
    
    def setA(x):    
        myCons.a=x
        myCons.p=myCons.Z/(myCons.a*myCons.r_0)  
        
        
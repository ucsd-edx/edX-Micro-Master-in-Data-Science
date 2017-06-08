import sys,os
import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt

from time import time
import math
import pandas as pd
from glob import glob
import pickle


def ex1(studentFunc):
    
    # General Checks for Tables
    answer = studentFunc()
    
    try: assert( type(answer)== type({}) )
    except AssertionError as e:
        print "Tables is not a dictionary."
        raise AssertionError('Your Answer is Incorrect') 
                
    try: assert( len(answer)== 476  ) 
    except AssertionError as e:
        print "Tables has the wrong length. Did you remove the correct stocks?"
        raise AssertionError('Your Answer is Incorrect') 
            
    
    # Checking IBM stock in tables
    IBM =pd.read_csv("Tester/IBM.csv", index_col=0)
    sIBM= answer["IBM"]
    
    try: assert( type(sIBM) == type(IBM) )   #<-- check type
    except AssertionError as e:
        print "Some values types in Tables are incorrect"
        print "Your value for type(Tables['IBM']) : "+str( type(sIBM) )
        print "Correct answer: "+str( type(IBM) )
        raise AssertionError('Your Answer is Incorrect') 
    
    
    try: assert( sIBM.shape == IBM.shape )  #<-- check shape
    except AssertionError as e:
        print "The shape of some of your values in Tables is incorrect"
        print "Your answer for Tables['IBM'].shape: "+str( sIBM.shape )
        print "Correct answer: "+str( IBM.shape )
        raise AssertionError('Your Answer is Incorrect') 
        
    IBM.head()
    
    try: assert( all(sIBM.columns == IBM.columns)  )  #<-- check column names
    except AssertionError as e:
        print "Some of your columns are named incorrectly. Are your columns in the same order as the IBM example?"
        print "Your answer for Tables['IBM'].columns: "+str( sIBM.columns )
        print "Correct answer: "+str( IBM.columns )
        raise AssertionError('Your Answer is Incorrect') 
    
    try: assert( (np.mean(IBM["Volume"])-np.mean(sIBM["Volume"]))<5   )  #<-- check mean of column
    except AssertionError as e:
        print "The mean of your Volume column is incorrect for Tables['IBM']. Are your values correct?"
        print "Your answer for np.mean(Tables['IBM']['Volume']) : "+str( np.mean(sIBM["Volume"]) ) 
        print "Correct answer: "+str( np.mean(IBM["Volume"]) )
        raise AssertionError('Your Answer is Incorrect') 
    
    print "great job!"
    return answer
    
    
    
    
    
    
    
    
    
    
def ex2(studentDiffs):
    
    # Load in student ad diff template
    sDiffs = studentDiffs
    Diffs  = pd.read_csv("Tester/Diffs.csv", index_col=0 )
    
    try: assert( type(sDiffs) == type(Diffs) )
    except AssertionError as e:
        print "Diffs is not the correct type"
        raise AssertionError('Your Answer is Incorrect') 
    
    try: assert( sDiffs.shape[1] == Diffs.shape[1] )
    except AssertionError as e:
        print "The number of columns of diffs is incorrect."
        print "Your answer for Diffs.shape[1]: "+str( sDiffs.shape[1] )
        print "Correct Answer: " +str( Diffs.shape[1] )
        raise AssertionError('Your Answer is Incorrect') 
                
    try: assert( "IBM_D" in sDiffs.columns and "IBM_P" in sDiffs.columns)
    except AssertionError as e:
        print "The columns IBM_D and IBM_P are not in Diffs."
        raise AssertionError('Your Answer is Incorrect') 
        
    try: assert( (np.nanmean(Diffs["IBM_D"].values)-np.nanmean(sDiffs["IBM_D"].values))*10000000 <1 )
    except AssertionError as e:
        print "You have the wrong value for np.nanmean(Diffs['IBM_D'].values) "
        print "Correct Answer : 2574.53874933423"
        print "Your Answer: "+str( np.nanmean(sDiffs["IBM_D"].values) )
        raise AssertionError('Your Answer is Incorrect') 
   
    print "great job!"
    return sDiffs
    
    
    
    
    
        

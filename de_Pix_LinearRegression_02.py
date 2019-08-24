#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import json
import urllib.request

from bs4 import BeautifulSoup
from pprint import pprint

#import csv
import unicodecsv as csv
from datetime import datetime
import codecs

import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  # To read data
from pandas import DataFrame

from sklearn.linear_model import LinearRegression
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

#-------------------------------------------------------------------------------
import pandas as pd  # To read data
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def Handle_Input_Min_Max():

    ##data = pd.read_csv ('data.csv') # загрузить набор данных
    #data = pd.read_csv ('pix_price1.csv') # загрузить набор данных
    #
    #X = data.iloc [:, 0] .values.reshape (-1, 1) # значения преобразует его в массив Numpy
    #Y = data.iloc [:, 1] .values.reshape (-1, 1) # -1 означает, что вычисляется размерность строк, но есть 1 столбец

    #----------------------------------------------------------------------

    df = pd.read_csv (r'c:\Git\ws01\de\tests\w1\pix_min_max_add.csv')
    print(df.head(3))

    X = pd.DataFrame(df['Pixel_Pitch']).values.reshape (-1, 1)
    Y = pd.DataFrame(df['dollar']).values.reshape (-1, 1)

    return X, Y    
#-------------------------------------------------------------------------------
def Handle_Input_ppi_detail():
    # ppi
    df2 = pd.read_csv (r'c:\Git\ws01\de\tests\w1\ppi_detail.csv')
    #print(data2)
    print(df2.head(3))
    #X2 = data2.iloc [:, 0] .values.reshape (-1, 1)   
    X2 = pd.DataFrame(df2['ppi']).values.reshape (-1, 1)
    
    return X2  

#-------------------------------------------------------------------------------
def Handle_coef_intercept(linear_regressor):
    
    print('linear_regressor=', linear_regressor)
    coef = linear_regressor.coef_
    intercept = linear_regressor.intercept_

    return coef, intercept 
#-------------------------------------------------------------------------------

# main module with import feature
#
def akaMain(argv):

    LinRegr_Pix_Dict = dict()

    X, Y = Handle_Input_Min_Max()
    X2   = Handle_Input_ppi_detail()
       
    linear_regressor = LinearRegression () # создать объект для класса

    linear_regressor.fit (X, Y) # выполнить линейную регрессию


    coef, intercept = Handle_coef_intercept(linear_regressor)

    print('coef=',coef)
    print ('intercept=',intercept)

    #-------------------------------------------------------------------------------
    LinRegr_Pix_Dict = dict()


    LinRegr_Pix_Dict['coef'] = list()
    LinRegr_Pix_Dict['intercept'] = list()


    LinRegr_Pix_Dict['coef'].append(str(round(coef[0][0],2))) 
    LinRegr_Pix_Dict['intercept'].append(str(round(intercept[0],2)))

    print ('LinRegr_Pix_Dict=',LinRegr_Pix_Dict)

    df_LinRegr_Pix = DataFrame(LinRegr_Pix_Dict, columns= ['coef', 'intercept'])

    print (df_LinRegr_Pix)

    export_csv = df_LinRegr_Pix.to_csv (r'c:\Git\ws01\de\tests\w1\LinRegr_Pix.csv', index = None, header=True)
    #-------------------------------------------------------------------------------


    print ('*********************************************')
    print ('*********************************************')
    print ('*********************************************')

#_______________________________________________________________________________
# main module stub to prevent auto execute
#

if __name__ == '__main__':


    if sys.version_info[0] >= 3:
        unicode = str

    #a = 'Москва'
    #b = Foo(a)
    #
    #print(str(b))
    #print(unicode(b))
    #print(repr(b))

    #print(translit(u"Реклама на светодиодных экранах в Москве.", 'ru', reversed=True))

    akaMain(sys.argv)
    sys.exit(0)

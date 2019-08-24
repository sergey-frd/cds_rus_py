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

from transliterate import translit, get_available_language_codes

import csv

#-------------------------------------------------------------------------------
#from c:/Git/ws01/de/tests/w1/bs_lib_1 import *
#from 'c:/Git/ws01/de/tests/w1/bs_lib_1' import *
from bs_lib_1        import *


#-------------------------------------------------------------------------------
def csv_reader_15(f_obj,
    Func_Parm_CSV,
    dct):

    N_line = 0

    reader = csv.DictReader(f_obj, delimiter=',')
    for line in reader:
        N_line     += 1  
        dct[Func_Parm_CSV][line['name']] = line 

        print  (N_line,\
            line['article'],\
            line['lvl2'],\
            line['main'],\
            line['up'],\
            line['location'],\
            line['href'],\
            line['meter_1'],\
            line['meter_2'],\
            line['pix_1'],\
            line['pix_2'],\
            line['name'],\
            line['in_rub'],\
            line['hronometraz'],\
            line['v_sutki'],\
            line['dney'],\
            line['anonce_code'],\
            line['anonce'])


        #    line['name'],\
        #    line['href'])

#-------------------------------------------------------------------------------

def Handle_product(
        Func_Parm_CSV,
        dct):

    try:
        f_Func_P_CSV = open(Func_Parm_CSV, 'r')

        dct = csv_reader_15(
            f_Func_P_CSV,
            Func_Parm_CSV,
            dct)

        f_Func_P_CSV.close()

    except IOError:
        print ("Error: cannot open file: " + Func_Parm_CSV + "\n")
        sys.exit(2)


#-------------------------------------------------------------------------------
# main module with import feature
#
def akaMain(argv):


    dct = dict() 
    dct['product.csv']    = dict() 

    ### dct = dict() 
    ### dct['plotn.csv']    = dict() 
    ### dct['location.csv'] = dict() 
    ### dct['mosk_ao.csv']  = dict() 
    ### 
    ### dct = Handle_csv_2_dict('plotn.csv'   ,dct)
    ### dct = Handle_csv_2_dict('location.csv',dct)
    ### dct = Handle_csv_2_dict('mosk_ao.csv' ,dct)
    ### 
    ### # print ("src_obl=",src_obl)
    ### # print ("src_loc=",src_loc)
    ### # print ("src_pl_mo=",src_pl_mo)
    ### #----------------------------------------------------------
    ### ## pprint(dct)
    ### 
    ### #Handle_mosk_ao(dct)
    ### Handle_plotn(dct)
    
    Handle_product(
        'product.csv',
        dct)

    print ('*********************************************')
    print ('*********************************************')
    print ('*********************************************')

    sys.exit(0)




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

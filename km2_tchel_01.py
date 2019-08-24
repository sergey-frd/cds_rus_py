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
#import StringIO
#
from unidecode import unidecode
#-------------------------------------------------------------------------------
def remove_non_ascii(text):
    return unidecode(unicode(text, encoding = "utf-8"))

#-------------------------------------------------------------------------------
#from c:/Git/ws01/de/tests/w1/bs_lib_1 import *
#from 'c:/Git/ws01/de/tests/w1/bs_lib_1' import *
from bs_lib_1        import *

##-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def Handle_km2_tchel_2(\
    dct):

    out_file = 'plotn_town.csv'
    of = codecs.open(out_file, 'w','utf-8')

    line = \
        'subiekt'+','+\
        'plotn'+','+\
        'tchel'+','+\
        'km2'+','+\
        'fo'+','+\
        'nn'+','+\
        'region'+'\n'

    of.write(line)

    Func_Parm_CSV ='location'
    N_line = 0
    for kk in dct['km2_town.csv']:
        N_line     += 1           
        #print ("kk=",kk)



        if kk in dct['tchel_town.csv']:
            pltn = str(round(float(dct['tchel_town.csv'][kk]['tchel'])/float(dct['km2_town.csv'][kk]['km2']),2))
            #print (N_line,"=>",kk,"=>",dct['km2_town.csv'][kk]['km2'],dct['tchel_town.csv'][kk]['tchel'],pltn)

            line = dct['tchel_town.csv'][kk]

            #decoded_str = line['region'].decode("utf-8",errors='ignore')
            #region = decoded_str.encode('ascii', 'ignore')

            #region = remove_non_ascii(line['region'])

            print  ("+++" , N_line, \
                line['subiekt'],\
                pltn,\
                line['tchel'],\
                line['km2'],\
                line['fo'],\
                line['nn'],\
                line['region'])

            pltn = str(round(float(dct['tchel_town.csv'][kk]['tchel'])/float(dct['km2_town.csv'][kk]['km2']),2))
            line2 = \
                line['subiekt']+','+\
                pltn+','+\
                line['tchel']+','+\
                dct['km2_town.csv'][kk]['km2']+','+\
                line['fo']+','+\
                line['nn']+','+\
                line['region']

            of.write(line2+'\n')

        else:

            line = dct['km2_town.csv'][kk]
            print  ("---" ,N_line, \
                line['subiekt'],\
                line['plotn'],\
                line['tchel'],\
                line['km2'],\
                line['fo'],\
                line['nn'])
                #line['region'])

            line2 = \
                line['subiekt']+','+\
                line['plotn']+','+\
                line['tchel']+','+\
                line['km2']+','+\
                line['fo']+','+\
                line['nn']+','+\
                ''

            of.write(line2+'\n')



            #dct[Func_Parm_CSV][kk] = pltn 
        #else:
        #    print (N_line,"***********",kk,dct['km2_town.csv'][kk])

    of.close()

    return dct

#-------------------------------------------------------------------------------
def csv_reader_14(
    f_obj,
    Func_Parm_CSV,
    dct):

    N_line = 0
    print ("*********************************************")
    reader = csv.DictReader(f_obj, delimiter=',')

    if 'location.csv' == Func_Parm_CSV :
        for line in reader:
            N_line     += 1  
            dct[Func_Parm_CSV][line['name']] = line 

            #print  (N_line,\
            #    line['name'],\
            #    line['href'])


    elif   'tchel_town.csv' == Func_Parm_CSV :
        for line in reader:
            N_line     += 1  
            dct[Func_Parm_CSV][line['subiekt']] = line 


            ## line = \
            ##     'subiekt'+','+\
            ##     'plotn'+','+\
            ##     'tchel'+','+\
            ##     'km2'+','+\
            ##     'fo'+','+\
            ##     'nn'+','+\
            ##     'region'+'\n'




    elif   'km2_town.csv' == Func_Parm_CSV :
        for line in reader:
            N_line     += 1  
            dct[Func_Parm_CSV][line['subiekt']] = line 

            ## line = \
            ##     'subiekt'+','+\
            ##     'plotn'+','+\
            ##     'tchel'+','+\
            ##     'km2'+','+\
            ##     'fo'+','+\
            ##     'nn' + '\n'



    elif   'product.csv' == Func_Parm_CSV :

        for line in reader:
            N_line     += 1  
            dct[Func_Parm_CSV][line['article']] = line 

            #print  (N_line,\
            #    line['article'],\
            #    line['lvl2'],\
            #    line['main'],\
            #    line['up'],\
            #    line['location'],\
            #    line['href'],\
            #    line['meter_1'],\
            #    line['meter_2'],\
            #    line['pix_1'],\
            #    line['pix_2'],\
            #    line['name'],\
            #    line['in_rub'],\
            #    line['hronometraz'],\
            #    line['v_sutki'],\
            #    line['dney'],\
            #    line['anonce_code'],\
            #    line['anonce'])

    elif   'plotn.csv' == Func_Parm_CSV:

        for line in reader:
            N_line     += 1  
            dct[Func_Parm_CSV][line['subiekt']] = line 

            #print  (N_line,\
            #    line['subiekt'],\
            #    line['plotn'],\
            #    line['tchel'],\
            #    line['km2'],\
            #    line['fo'],\
            #    line['nn'])

    elif 'mosk_ao.csv'  == Func_Parm_CSV:

        
        for line in reader:
            N_line     += 1  
            dct[Func_Parm_CSV][line['subiekt']] = line 

            #print  (N_line,\
            #    line['subiekt'],\
            #    line['okrug'],\
            #    line['km2'],\
            #    line['perc_plsh'],\
            #    line['mesto_plsh'],\
            #    line['tchel'],\
            #    line['perc_tchel'],\
            #    line['mesto_tchel'],\
            #    line['plotn'],\
            #    line['mesto_plotn'])

    return dct

#-------------------------------------------------------------------------------
def Handle_csv_2_dict(\
    Func_Parm_CSV,dct):

    try:
        f_Func_P_CSV = open(Func_Parm_CSV, 'r')

        dct = csv_reader_14(f_Func_P_CSV,
                 Func_Parm_CSV,dct)

        #src = f_Func_P_CSV.read()
        f_Func_P_CSV.close()

    except IOError:
        print ("Error: cannot open file: " + Func_Parm_CSV + "\n")
        sys.exit(2)

    return dct
#-------------------------------------------------------------------------------
def Handle_write_all_csv(\
    flag_tramsl,
    dict_plotn):

    Handle_write_csv(\
        flag_tramsl,
        'mosk_ao.csv',
        dict_plotn)


#-------------------------------------------------------------------------------
def Handle_write_csv(\
    flag_tramsl,
    out_file,
    dct):

    #print ("out_file=",out_file)
    line = ''
    if out_file == 'mosk_ao.csv':
        line = \
            'subiekt'+','+\
            'okrug'+','+\
            'km2'+','+\
            'perc_plsh'+','+\
            'mesto_plsh'+','+\
            'tchel'+','+\
            'perc_tchel'+','+\
            'mesto_tchel'+','+\
            'plotn'+','+\
            'mesto_plotn' + '\n'


    if flag_tramsl == 0:
        out_file = out_file.replace('.csv','_ru.csv')

    of = codecs.open(out_file, 'w','utf-8')

    #if out_file == 'product.csv':
    of.write(line)

    sort_keys=sorted(dct.keys())
    for kk in sort_keys:

        val = dct[kk]

        line = \
            kk  + ','+\
            val + '\n'

        if flag_tramsl == 1:
            line = translit(line, 'ru', reversed=True)

        of.write(line)

    of.close()

#-------------------------------------------------------------------------------
# main module with import feature
#
def akaMain(argv):

    dct = dict() 

    dct['tchel_town.csv'] = dict() 
    dct['km2_town.csv']   = dict() 

    dct = Handle_csv_2_dict('tchel_town.csv'   ,dct)
    dct = Handle_csv_2_dict('km2_town.csv'   ,dct)

    dct = Handle_km2_tchel_2(dct)


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

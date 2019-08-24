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

##-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
def csv_reader_15(f_obj,
    Func_Parm_CSV,
    dct):

    N_line = 0

    reader = csv.DictReader(f_obj, delimiter=',')
    for line in reader:
        N_line     += 1  
        dct[Func_Parm_CSV][line['name']] = line 

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

        if not line['location'].lstrip() in dct['location'] :


            if not line['up'].lstrip() in dct['local_pltn.csv'] :

                print  (N_line,'---',\
                    '['+line['up']+']',\
                    line['article'],\
                    line['anonce'])

            else:
                print  (N_line,'+++',\
                    line['up'],\
                    dct['local_pltn.csv'][line['up'].lstrip()],\
                    line['article'],\
                    line['anonce'])


        else:
            print  (N_line,'***',\
                line['location'],\
                dct['location'][line['location'].lstrip()],\
                line['article'],\
                line['anonce'])





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

def Handle_mosk_ao(\
    dct):

    N_line = 0
    for kk in dct['location.csv']:
        N_line     += 1           
        #print ("kk=",kk)
        if 'AO' in kk:
            #print ("kk=",kk)
            kk_list = kk.split(' ')
            if kk_list[0] in dct['mosk_ao.csv']:
                print (N_line,"=>",kk,"=>",dct['mosk_ao.csv'][kk_list[0]]['plotn'])
            else:
                print (N_line,"***********",kk,)


#-------------------------------------------------------------------------------

def Handle_km2_tchel(\
    dct):

    Func_Parm_CSV ='location'
    N_line = 0
    for kk in dct['km2_town.csv']:
        N_line     += 1           
        #print ("kk=",kk)


        if kk in dct['tchel_town.csv']:
            pltn = str(round(float(dct['tchel_town.csv'][kk]['tchel'])/float(dct['km2_town.csv'][kk]['km2']),2))
            print (N_line,"=>",kk,"=>",dct['km2_town.csv'][kk]['km2'],dct['tchel_town.csv'][kk]['tchel'],pltn)
            dct[Func_Parm_CSV][kk] = pltn 
        #else:
        #    print (N_line,"***********",kk,dct['km2_town.csv'][kk])


    return dct
#-------------------------------------------------------------------------------

def Handle_plotn(\
    dct):

    Func_Parm_CSV ='local_pltn.csv'

    dct[Func_Parm_CSV]    = dict() 
    of = codecs.open('local_pltn.csv', 'w','utf-8')

    line = \
        'up'+','+\
        'plotn'+ '\n'
    of.write(line)

    N_line = 0
    for kk in dct['location.csv']:
        N_line     += 1           
        #print ("kk=",kk)


        if 'oblast' in kk or 'kraj' in kk or 'stan' in kk :
            #print ("kk=",kk)
            #kk_list = kk.split(' ')
            if kk in dct['plotn.csv']:
                print (N_line,"=>",kk,"=>",dct['plotn.csv'][kk]['plotn'])

                line = \
                    kk+','+\
                    dct['plotn.csv'][kk]['plotn']+ '\n'
                of.write(line)
                dct[Func_Parm_CSV][kk] = line 


            else:
                print (N_line,"***********",kk,)


    N_line = 0
    for kk in dct['location.csv']:
        N_line     += 1           
        #print ("kk=",kk)
        if 'AO' in kk:
            #print ("kk=",kk)
            kk_list = kk.split(' ')
            if kk_list[0] in dct['mosk_ao.csv']:
                print (N_line,"=>",kk,"=>",dct['mosk_ao.csv'][kk_list[0]]['plotn'])

                line = \
                    kk+','+\
                    dct['mosk_ao.csv'][kk_list[0]]['plotn']+ '\n'
                of.write(line)
                dct[Func_Parm_CSV][kk] = line 

            else:
                print (N_line,"***********",kk,)

    print ("=>",'Moskva',"=>",dct['mosk_ao.csv']['Vsja Moskva']['plotn'])
    line = \
        'Moskva'+','+\
        dct['mosk_ao.csv']['Vsja Moskva']['plotn']+ '\n'
    of.write(line)
    dct[Func_Parm_CSV]['Moskva'] = dct['mosk_ao.csv']['Vsja Moskva']['plotn'] 

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

    elif   'km2_town.csv' == Func_Parm_CSV :
        for line in reader:
            N_line     += 1  
            dct[Func_Parm_CSV][line['subiekt']] = line 

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
#
def to_digit(input_str):

    result =''  
    for p in input_str:
        if '[' == p:
            break

        elif '.' == p:
            result += p
            continue
        else:
            if p.isdigit():
                result += p

    return result
#-------------------------------------------------------------------------------
# main module with import feature
#
def akaMain(argv):

    dct = dict() 



    dct['tchel_town.csv'] = dict() 
    dct['km2_town.csv']   = dict() 
    dct['location']       = dict() 

    dct = Handle_csv_2_dict('tchel_town.csv'   ,dct)
    dct = Handle_csv_2_dict('km2_town.csv'   ,dct)

    dct['plotn.csv']    = dict() 
    dct['location.csv'] = dict() 
    dct['mosk_ao.csv']  = dict() 
    dct['product.csv']  = dict() 

    dct = Handle_csv_2_dict('plotn.csv'   ,dct)
    dct = Handle_csv_2_dict('location.csv',dct)
    dct = Handle_csv_2_dict('mosk_ao.csv' ,dct)
    dct = Handle_csv_2_dict('product.csv' ,dct)



    # print ("src_obl=",src_obl)
    # print ("src_loc=",src_loc)
    # print ("src_pl_mo=",src_pl_mo)
    #----------------------------------------------------------
    ## pprint(dct)

    #Handle_mosk_ao(dct)
    dct = Handle_plotn(dct)

    dct = Handle_km2_tchel(dct)

    #pprint(dct)
    pprint(dct['local_pltn.csv'])
    
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

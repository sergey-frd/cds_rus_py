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

def Handle_money_day(line,dct):

	
    sek_v_sut = float(line['hronometraz']) * \
                     float(line['v_sutki'])

    sek_v_sutki = str(round(sek_v_sut,2))
    #print('sek_v_sutki=',sek_v_sutki)


    m_r_d = float(line['in_rub']) / \
            float(line['dney'])

    rub_usd=dct['usd_rub.csv']['rub_usd']
    #print('rub_usd=',rub_usd)
    m_d_d = m_r_d * float(rub_usd )
    #rub_usd = dct['usd_rub.csv']['usd_rub']

    #print('rub_usd2=',dct['usd_rub.csv']['rub_usd2'])
    #print('usd_rub=',dct['usd_rub.csv']['usd_rub'])

    sec_r = m_r_d / sek_v_sut
    sec_d = m_d_d / sek_v_sut


    sec_rub = str(round(sec_r,3))
    sec_dol = str(round(sec_d,3))

    money_dol_day = str(round(m_d_d,2))
    #money_dol_day = ''

    money_rub_day = str(round(m_r_d,2))

    print('money_rub_day=',money_rub_day)
    print('money_dol_day=',money_dol_day)

    print('sec_rub=',sec_rub)
    print('sec_dol=',sec_dol)

    #return money_rub_day,money_dol_day,sek_v_sutki
    return money_rub_day,money_dol_day,sec_rub,sec_dol


#-------------------------------------------------------------------------------
# Pixel Density
def Handle_pixels_m2(pixels,area):

    Pixel_Density = str(round(float(pixels)/ \
                          float(area),2))
    print('Pixel_Density=',Pixel_Density)
    return Pixel_Density

#-------------------------------------------------------------------------------

def Handle_pixels(line):


    pixels = str(round(float(line['pix_1']) * \
                       float(line['pix_2']),0))
    print('pixels=',pixels)
    return pixels

#-------------------------------------------------------------------------------

def Handle_area(line):


    area = str(round(float(line['meter_1']) * \
                     float(line['meter_2']),2))
    print('area=',area)
    return area

#-------------------------------------------------------------------------------

def Handle_diagonal_pixels(line,diag_in ):

    m1 = float(line['pix_1'])**2
    m2 = float(line['pix_2'])**2
    d  = (m1 + m2)**0.5

    p = d/float(diag_in)

    diagonal_pixels = str(round(d, 2))
    ppi = str(round(p, 2))


    print('diagonal_pixels =',diagonal_pixels)
    print('ppi =',ppi)
    return diagonal_pixels,ppi
#-------------------------------------------------------------------------------

def Handle_diagonal(line):

    m1 = float(line['meter_1'])**2
    m2 = float(line['meter_2'])**2
    d  = (m1 + m2)**0.5
    d_in  = d*100/2.54
    diagonal = str(round(d, 2))
    diag_in = str(round(d_in, 2))

    print('diagonal m=',diagonal,'diagonal in=',diag_in)
    return diagonal,diag_in
##-------------------------------------------------------------------------------

def Handle_product_d(
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
def csv_reader_14(
    f_obj,
    Func_Parm_CSV,
    dct):

    out_file = 'detail.csv'
    of = codecs.open(out_file, 'w','utf-8')

    line = \
        'article'+','+\
        'lvl2'+','+\
        'main'+','+\
        'up'+','+\
        'location'+','+\
        'href'+','+\
        'meter_1'+','+\
        'meter_2'+','+\
        'pix_1'+','+\
        'pix_2'+','+\
        'name'+','+\
        'in_rub'+','+\
        'hronometraz'+','+\
        'v_sutki' +','+\
        'dney'  +','+\
        'anonce_code'+','+\
        'anonce'+','+\
        'money_rub_day'+','+\
        'money_dol_day'+','+\
        'sec_rub'+','+\
        'sec_dol'+','+\
        'area'+','+\
        'diagonal'+','+\
        'diag_in'+','+\
        'pixels'+','+\
        'diagonal_pixels'+','+\
        'ppi'+','+\
        'Pixel_Density'
    of.write(line+ '\n')

    N_line = 0
    print ("*********************************************")
    reader = csv.DictReader(f_obj, delimiter=',')

    if   'usd_rub.csv' == Func_Parm_CSV :

        for line in reader:
            N_line     += 1  
            print  ('usd_rub.csv',N_line,line)
            dct[Func_Parm_CSV][line['usd_rub']] = str(line['value']) 

    elif   'product.csv' == Func_Parm_CSV :

        for line in reader:
            N_line     += 1  
            dct[Func_Parm_CSV][line['article']] = line 

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

            money_rub_day  ,\
            money_dol_day  ,\
            sec_rub        ,\
            sec_dol        = Handle_money_day(line,dct)

            area           = Handle_area(line)

            diagonal        ,\
            diag_in        = Handle_diagonal(line)

            pixels         = Handle_pixels(line)

            diagonal_pixels,\
            ppi            = Handle_diagonal_pixels(line,diag_in )

            Pixel_Density  = Handle_pixels_m2(pixels,area) # Pixel Density

            line2 =\
                line['article']+','+\
                line['lvl2']+','+\
                line['main']+','+\
                line['up']+','+\
                line['location']+','+\
                line['href']+','+\
                line['meter_1']+','+\
                line['meter_2']+','+\
                line['pix_1']+','+\
                line['pix_2']+','+\
                line['name']+','+\
                line['in_rub']+','+\
                line['hronometraz']+','+\
                line['v_sutki']+','+\
                line['dney']+','+\
                line['anonce_code']+','+\
                line['anonce']+','+\
                money_rub_day  +','+\
                money_dol_day  +','+\
                sec_rub        +','+\
                sec_dol        +','+\
                area           +','+\
                diagonal       +','+\
                diag_in        +','+\
                pixels         +','+\
                diagonal_pixels+','+\
                ppi+','+\
                Pixel_Density            

            of.write(line2+ '\n')
            #sys.exit(0)

    of.close()
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
#-------------------------------------------------------------------------------


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




    dct['product.csv']  = dict() 
    dct['usd_rub.csv']  = dict() 


    dct = Handle_csv_2_dict('usd_rub.csv' ,dct)
    pprint(dct['usd_rub.csv'])

    dct = Handle_csv_2_dict('product.csv' ,dct)



    # print ("src_obl=",src_obl)
    # print ("src_loc=",src_loc)
    # print ("src_pl_mo=",src_pl_mo)
    #----------------------------------------------------------
    ## pprint(dct)

    ##Handle_mosk_ao(dct)
    #dct = Handle_plotn(dct)
    #
    #dct = Handle_km2_tchel(dct)

    #pprint(dct)
    #pprint(dct['local_pltn.csv'])
    
    #Handle_product_d(
    #    'product.csv',
    #    dct)

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

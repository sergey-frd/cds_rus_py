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

def Handle_Ppi_Detail(pix_list):

    Plotn_Town = '0' 

    out_file = 'ppi_detail.csv'
    of = codecs.open(out_file, 'w','utf-8')


    line = \
      'ppi'


    of.write(line+ '\n')
    for ll in pix_list:

        line =\
            ll            

        of.write(line+ '\n')

    of.close()
#-------------------------------------------------------------------------------

def Handle_Dollars(line,dct):

    Plotn_Town = '0' 
#-------------------------------------------------------------------------------

def Handle_Plotn_Town(line,dct):

    Plotn_Town = '0' 
    tchel_Town = '0'  	
    km2_Town   = '0'

    if line['main'] == 'Moskva' and 'AO' in line['up']:
        kk = line['up'].replace('AO','').strip().lstrip()


        print ("============= mosk_ao kk=",line['up'],line['article'],kk)

        if kk in dct['mosk_ao.csv'] :
            line2 = dct['mosk_ao.csv'][kk] 

            Plotn_Town = line2['plotn'] 
            tchel_Town = line2['tchel']  	
            km2_Town   = line2['km2']  
        else:
            print ("*************** mosk_ao kk=",kk)
    else:
        if line['location'] in dct['plotn_town.csv'] :
            line2 = dct['plotn_town.csv'][line['location']] 

            Plotn_Town = line2['plotn'] 
            tchel_Town = line2['tchel']  	
            km2_Town   = line2['km2']  



    print (line['location'], '=>',"Plotn_Town=",Plotn_Town,tchel_Town,km2_Town)
    return Plotn_Town,tchel_Town,km2_Town
#-------------------------------------------------------------------------------
#from c:/Git/ws01/de/tests/w1/bs_lib_1 import *
#from 'c:/Git/ws01/de/tests/w1/bs_lib_1' import *
from bs_lib_1        import *

#-------------------------------------------------------------------------------
def csv_reader_14(
    f_obj,
    Func_Parm_CSV,
    dct):

    print ("csv_reader_14 Func_Parm_CSV=",Func_Parm_CSV)
    print ("csv_reader_14 f_obj=",f_obj)

    N_line = 0
    print ("*********************************************")
    reader = csv.DictReader(f_obj, delimiter=',')

    print ("reader=",reader)
    pprint (reader)


    if 'pix_price.csv' == Func_Parm_CSV :
        for line in reader:
            N_line     += 1  
            dct[Func_Parm_CSV][line['Pixel_Pitch_avr']] = line 

    elif 'location.csv' == Func_Parm_CSV :
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

    elif 'plotn_town.csv'  == Func_Parm_CSV:

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
    Func_Parm_CSV,
    dct):

    print ("Handle_csv_2_dict Func_Parm_CSV=",Func_Parm_CSV)
    try:
        f_Func_P_CSV = open(Func_Parm_CSV, 'r')

        print ("Handle_csv_2_dict f_Func_P_CSV=",f_Func_P_CSV)
        dct = csv_reader_14(f_Func_P_CSV,
                 Func_Parm_CSV,dct)

        #src = f_Func_P_CSV.read()
        f_Func_P_CSV.close()

    except IOError:
        print ("Error: cannot open file: " + Func_Parm_CSV + "\n")
        sys.exit(2)

    return dct
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

def Handle_diagonal_pixels(line,
                           diag_in,
                           area ):

    m1 = float(line['pix_1'])**2
    m2 = float(line['pix_2'])**2
    d  = (m1 + m2)**0.5

    p = d/float(diag_in)

    s_dol = float(area) * p * 218.94 + 2744.03

    scr_dol = str(round(s_dol, 2))

    diagonal_pixels = str(round(d, 2))
    ppi = str(round(p, 2))


    print('diagonal_pixels =',diagonal_pixels)
    print('ppi =',ppi)
    print('scr_dol =',scr_dol)

    return diagonal_pixels,ppi,scr_dol
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
def csv_reader_14_dtl(
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
        'Pixel_Density'+','+\
        'Plotn_Town'+','+\
        'tchel_Town'+','+\
        'km2_Town'+','+\
        'scr_dol'


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
            ppi,\
            scr_dol         = Handle_diagonal_pixels(line,diag_in,area )

            if not ppi in     dct['pix_list.csv']:
                dct['pix_list.csv'].append(ppi)

            Pixel_Density  = Handle_pixels_m2(pixels,area) # Pixel Density


            Plotn_Town,tchel_Town,km2_Town = Handle_Plotn_Town(line,dct)


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
                Pixel_Density+','+\
                Plotn_Town+','+\
                tchel_Town+','+\
                km2_Town+','+\
                scr_dol            

            of.write(line2+ '\n')
            #sys.exit(0)

    of.close()
    return dct

#-------------------------------------------------------------------------------
def Handle_csv_2_dict_dtl(\
    Func_Parm_CSV,dct):

    try:
        f_Func_P_CSV = open(Func_Parm_CSV, 'r')

        dct = csv_reader_14_dtl(f_Func_P_CSV,
                 Func_Parm_CSV,dct)

        #src = f_Func_P_CSV.read()
        f_Func_P_CSV.close()

    except IOError:
        print ("Error: cannot open file: " + Func_Parm_CSV + "\n")
        sys.exit(2)

    return dct

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




    dct['pix_list.csv']   = list() 

    dct['pix_price.csv']  = dict() 
    dct['product.csv']    = dict() 
    dct['usd_rub.csv']    = dict() 

    #dct['tchel_town.csv'] = dict() 
    #dct['km2_town.csv']   = dict() 

    dct['location']       = dict() 
    dct['plotn.csv']      = dict() 
    dct['location.csv']   = dict() 
    dct['mosk_ao.csv']    = dict() 


    dct['plotn_town.csv']    = dict() 

    dct = Handle_csv_2_dict('pix_price.csv' ,dct)
    dct = Handle_csv_2_dict('plotn_town.csv' ,dct)
 

    #dct = Handle_csv_2_dict('tchel_town.csv'   ,dct)
    #dct = Handle_csv_2_dict('km2_town.csv'   ,dct)

    dct = Handle_csv_2_dict('plotn.csv'   ,dct)
    dct = Handle_csv_2_dict('location.csv',dct)
    dct = Handle_csv_2_dict('mosk_ao.csv' ,dct)




    dct = Handle_csv_2_dict_dtl('usd_rub.csv' ,dct)
    #pprint(dct['usd_rub.csv'])

    dct = Handle_csv_2_dict_dtl('product.csv' ,dct)



    print ('*********************************************')
    pix_list = sorted(dct['pix_list.csv'])
    #pprint(pix_list)
    Handle_Ppi_Detail(pix_list)

    # linear_regressor.coef_= [[-218.94773184]]



#linear_regressor= LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
#         normalize=False)
#linear_regressor.coef_= [[-218.94773184]]
#linear_regressor.intercept_= [2744.03311907]
#
#2.5    ,1073.25 
#[[ 4.81]    [[ 575.88]   [[1690.89452893] 4.81   , 575.88       
# [ 3.  ]     [1250.  ]    [2087.18992356] 3      ,1250          
# [ 8.  ]     [ 441.5 ]    [ 992.45126437] 8      , 441.5        
# [ 2.6 ]     [1600.  ]    [2174.76901629] 2.6    ,1600          
# [ 3.91]     [ 757.25]    [1887.94748759] 3.91   , 757.25       
# [16.  ]     [ 476.5 ]    [-759.13059034] 16     , 476.5        
# [ 1.25]     [6500.  ]    [2470.34845428] 1.25   ,6500          
# [10.  ]     [ 475.  ]    [ 554.55580069] 10     , 475          
# [ 5.95]]    [ 464.19]]   [1441.29411464]]5.95   , 464.19       
            









           
            
            
            
            
            
            
            











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

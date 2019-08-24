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

#-------------------------------------------------------------------------------
#from c:/Git/ws01/de/tests/w1/bs_lib_1 import *
#from 'c:/Git/ws01/de/tests/w1/bs_lib_1' import *
from bs_lib_1        import *

##-------------------------------------------------------------------------------
#
#
#-------------------------------------------------------------------------------
def Handle_write_all_csv(\
    flag_tramsl,
    dict_usd_rub):

    Handle_write_csv(\
        flag_tramsl,
        'usd_rub.csv',
        dict_usd_rub)


#-------------------------------------------------------------------------------
def Handle_write_csv(\
    flag_tramsl,
    out_file,
    dct):

    #print ("out_file=",out_file)
    line = ''
    if out_file == 'usd_rub.csv':
        line = \
            'usd_rub'+','+\
            'value' + '\n'


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



    dict_usd_rub = dict() 
    base_link = 'https://freecurrencyrates.com/ru/convert-RUB-USD'


    response = urllib.request.urlopen(base_link)
    html_doc = response.read()

    #sys.exit(0)

    soup = BeautifulSoup(html_doc, 'html.parser')


    #    <div id="to_iso-module"  class="input-field">
    #        <span class="sign prefix cp-sign-text" title="$">$</span>
    #        <input  type="text"
    #                id="value_to"
    #                class="thin cp-input"
    #                value="0.015"
    #            >
    #

    rub_usd2 = 0.015
    rub_usd  = 0.0153
    usd_rub  = 65.2198

    for input_item in soup.find_all('div', attrs = {'class': 'input-field'}): 
        for b_item in input_item.find_all('input', attrs = {'class': 'thin cp-input','id': 'value_to'}): 
            #print ('b_item=',b_item)
            rub_usd2 = b_item.get('value')
            print ('rub_usd2=',rub_usd2)



    for p_item in soup.find_all('p'):
        if 'RUB/USD' in p_item.text:
            #print ('p_item=',p_item.text)
            p_list = p_item.text.split(' ')
            #print ('p_list=',p_list)

            i = 0
            for pp in p_list:
                #print (i,'pp=',pp)
                if pp == 'получите':
                    rub_usd = p_list[i+1]
                    print ('*** rub_usd=',rub_usd)


                if pp == 'или':
                    usd_rub = p_list[i+1]
                    print ('*** usd_rub=',usd_rub)
                    break
                i += 1

         
    dict_usd_rub['rub_usd2'] =  rub_usd2
    dict_usd_rub['rub_usd'] =  rub_usd 
    dict_usd_rub['usd_rub'] =  usd_rub 

    print ("===========================================")
    #print ("dict_plotn=")
    #pprint(dict_plotn)
    
    Handle_write_all_csv(\
        0,
        dict_usd_rub)
    
    Handle_write_all_csv(\
        1,
        dict_usd_rub)


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

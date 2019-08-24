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



    dict_plotn = dict() 
    #base_link = 'https://www.calc.ru/kurs-USD-RUB.html'
    base_link = 'https://www.calc.ru'


    response = urllib.request.urlopen(base_link)
    html_doc = response.read()

    sys.exit(0)

    soup = BeautifulSoup(html_doc, 'html.parser')


    #<div class="main_block">
    #    <div class="content">
    #                <div itemprop="articleBody">
    #        <table cellpadding="0" cellspacing="0" width="100%">
    #                    <tr>
    #            	<td align="left" valign="top" colspan="3"> 
    #               <h2>Доллар США в рублях на сегодня:</h2><br><center>
    #    <div class="t18">
    #    <b>1 доллар США (USD)</b> равняется 
    #    <b>64.73 российский рубль (RUB)</b><br>
    #    <b>1 российский рубль (RUB)</b> равняется 
    #    <b>0.015448 доллар США (USD)</b>
    #    <br><div></center> 



    for main_block_item in soup.find_all('div', attrs = {'class': 'main_block'}): 
        for content_item in content.find_all('div', attrs = {'class': 'content'}): 
            for articleBody_item in content_item.find_all('div', attrs = {'class': 'articleBody'}): 
                for table_item in articleBody_item.find_all('table'): 
                    for tr_item in table_item.find_all('tr'): 
                        for td_item in tr_item.find_all('td'): 
                            for b_item in td_item.find_all('b'): 
                                if None != b_item:
                                    a_txt = b_item.text.strip()
                                    title_txt = ''
                                    print ('b_txt=',translit(a_txt,'ru', reversed=True))


    ##print (soup)table class="standard sortable
    #for sortable_item in soup.find_all('table', attrs = {'class': "standard sortable"}): 
    #
    #
    #    #print ('sortable_item',sortable_item)
    #    for tr_item in sortable_item.find_all('tr'): 
    #        #print ('tr_item',translit(tr_item,'ru', reversed=True))
    #        #print ('tr_item',tr_item)
    #
    #        b_item = tr_item.find('b')
    #        if None != b_item:
    #            a_txt = b_item.text.strip()
    #            title_txt = ''
    #            #print ('b_txt=',translit(a_txt,'ru', reversed=True))
    #        else:
    #            a_item = tr_item.find('a')
    #            title_txt = a_item.get('title')
    #            #if None != title_txt:
    #            #    #print ('title_txt',title_txt)
    #            #    #print ('title_txt',translit(title_txt,'ru', reversed=True))
    #
    #            ##print ('a_item',a_item['title'])
    #            a_txt = a_item.text.strip()
    #            #print ('a_txt',translit(a_txt,'ru', reversed=True))
    #            #
    #
    #
    #
    #
    #
    #        #print ('---------------------------------------------')
    #        i  = 0
    #        line = ''
    #        for td_item in tr_item.find_all('td'): 
    #            i  += 1
    #
    #            txt = td_item.text.strip().replace(',','.')
    #
    #            dig = to_digit(txt)
    #            #print (i,'td_item',dig,translit(txt,'ru', reversed=True))
    #            #print (i,'td_item',dig)
    #
    #
    #            if i == 8:
    #                line += dig + ','
    #                #line = nn 
    #                dict_plotn[a_txt] = title_txt + ',' + line 
    #                print (translit(a_txt,'ru', reversed=True),':',\
    #                       translit(dict_plotn[a_txt],'ru', reversed=True))
    #                continue
    #            
    #            line += dig + ','
    #            
    #
    #print ("===========================================")
    ##print ("dict_plotn=")
    ##pprint(dict_plotn)
    #
    #Handle_write_all_csv(\
    #    0,
    #    dict_plotn)
    #
    #Handle_write_all_csv(\
    #    1,
    #    dict_plotn)


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

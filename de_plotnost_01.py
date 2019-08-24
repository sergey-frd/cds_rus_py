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
        'plotn.csv',
        dict_plotn)


#-------------------------------------------------------------------------------
def Handle_write_csv(\
    flag_tramsl,
    out_file,
    dct):

    #print ("out_file=",out_file)
    line = ''
    if out_file == 'plotn.csv':
        line = \
            'subiekt'+','+\
            'plotn'+','+\
            'tchel'+','+\
            'km2'+','+\
            'fo'+','+\
            'nn' + '\n'


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



    dict_plotn = dict() 

    base_link = 'https://ru.wikipedia.org/wiki/%D0%9F%D0%BB%D0%BE%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C_%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F_%D1%81%D1%83%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B9_%D0%A4%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8'
    response = urllib.request.urlopen(base_link)
    html_doc = response.read()


    soup = BeautifulSoup(html_doc, 'html.parser')

    #print (soup)
    for sortable_item in soup.find_all('table', attrs = {'class': "standard sortable"}): 


        #print ('sortable_item',sortable_item)
        for tr_item in sortable_item.find_all('tr'): 
            #print ('tr_item',translit(tr_item,'ru', reversed=True))
            #print ('tr_item',tr_item)


            #print ('---------------------------------------------')
            i  = 0
            line = ''
            for td_item in tr_item.find_all('td'): 
                i  += 1
                #print ('td_item',td_item.text.strip())
                #print ('th_item',translit(th_item,'ru', reversed=True))
                #itle = ''
                #if 'title' in td_item:
                #   title = td_item[title]
                txt = td_item.text.strip().replace(',','.')
                #print (i,'td_item',translit(txt,'ru', reversed=True))
                if i == 1:
                    nn = txt
                    continue

                elif i == 2:
                    key = txt
                    #dict_plotn[key] = line 
                    continue

                elif i == 6:
                    line += txt + ','
                    line += nn 
                    dict_plotn[key] = line 
                    print (translit(key,'ru', reversed=True),\
                           translit(dict_plotn[key],'ru', reversed=True))
                    continue

                line += txt + ','
                
 
    print ("===========================================")
    #print ("dict_plotn=")
    #pprint(dict_plotn)
                
                #for a_item in td_item.find_all('a'): 
                #    #print ('a_item',a_item.text.strip())
                #    print ('a_item',translit(a_item.text.strip(),'ru', reversed=True))


            #for th_item in sortable_item.find_all('th'): 
            #    print ('th_item',th_item)
            #    #print ('th_item',translit(th_item,'ru', reversed=True))

    Handle_write_all_csv(\
        0,
        dict_plotn)

    Handle_write_all_csv(\
        1,
        dict_plotn)


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

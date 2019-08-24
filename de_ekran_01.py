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

###from bs_lib_1        import *


#-------------------------------------------------------------------------------
def Handle_product_in_item(\
    id_ekran,
    soup2):





    for a_item in soup2.find_all('div', attrs = {'class': 'sr-proMainInfo-baseInfo-name'}): 
        for a_item in soup2.find_all('h1', attrs = {'class': 'sr-proMainInfo-baseInfoH1 J-baseInfo-name'}): 
            a_item_txt = a_item.text.strip().lstrip()
            print (id_ekran, 'a_item_txt =',a_item_txt)
            print ('---------------------------------------------')







    k = 0

    for a_item in soup2.find_all('div', attrs = {'class': 'sr-proMainInfo-baseInfo-propertyPrice'}): 
        k  += 1
        #print ("a_item=",a_item)
        for sortable_item in a_item.find_all('table'): 
            j  = 0
            #print ("sortable_item=",sortable_item)
            for tr_item in sortable_item.find_all('tr'): 
                j  += 1

            print ('---------------------------------------------')
            #print (k,j,"tr_item=",tr_item)
            i  = 0
            line   = ''
            region = ''
            okrug  = ''

            for th_item in sortable_item.find_all('th'): 
                i  += 1
                #print (k,j,i,'td_item',td_item)
                th_item_txt = th_item.text.strip().lstrip()
                print (k,j,i,'th_item_txt =',th_item_txt)

            for td_item in sortable_item.find_all('td'): 
                i  += 1
                #print (k,j,i,'td_item',td_item)
                td_item_txt = td_item.text.strip().lstrip()
                print (k,j,i,'td_item_txt =',td_item_txt)


            print ('---------------------------------------------')




    for a_item in soup2.find_all('div', attrs = {'class': 'sr-proMainInfo-baseInfo-propertyAttr'}): 
        k  += 1
        #print ("a_item=",a_item)
        for sortable_item in a_item.find_all('table'): 
            j  = 0
            #print ("sortable_item=",sortable_item)
            for tr_item in sortable_item.find_all('tr'): 
                j  += 1

                print ('---------------------------------------------')
                #print (k,j,"tr_item=",tr_item)
                i  = 0
                line   = ''
                region = ''
                okrug  = ''

                for th_item in tr_item.find_all('th'): 
                    i  += 1
                    #print (k,j,i,'td_item',td_item)
                    th_item_txt = th_item.text.strip().lstrip()
                    print (k,j,i,'th_item_txt =',th_item_txt)

                for td_item in tr_item.find_all('td'): 
                    i  += 1
                    #print (k,j,i,'td_item',td_item)
                    td_item_txt = td_item.text.strip().lstrip()
                    print (k,j,i,'td_item_txt =',td_item_txt)


                print ('---------------------------------------------')

  
    k = 0
    for a in soup2.find_all('div', attrs = {'class': 'sr-layout-subblock detail-tab-item J-tab-cnt'}): 
        for b in a.find_all('div', attrs = {'class': 'sr-layout-content detail-desc'}): 
            for c_item in b.find_all('div', attrs = {'class': 'rich-text cf'}): 
                for item in c_item.find_all('span', attrs = {'style': 'font-size:20px;'}): 
                    k  += 1
                    key_item = item.text.strip().lstrip()
                    print (k,"key_item=",key_item)
                    #sys.exit(0)


            #print ("Handle_product_in_item soup2=",soup2)
            #for div_item in soup2.find_all('div', attrs = {'class': 'rich-text cf'}): 

            #print ("div_item=",div_item)
            #for sortable_item in div_item.find_all('table'): 
            for sortable_item in c_item.find_all('table'): 

                j  = 0
                for tr_item in sortable_item.find_all('tr'): 
                    j  += 1

                    print ('---------------------------------------------')
                    i  = 0
                    line   = ''
                    region = ''
                    okrug  = ''

                    for th_item in tr_item.find_all('th'): 
                        i  += 1
                        #print (k,j,i,'td_item',td_item)
                        th_item_txt = th_item.text.strip().lstrip()
                        print (k,j,i,'th_item_txt =',th_item_txt)

                    for td_item in tr_item.find_all('td'): 
                        i  += 1
                        #print (i,'td_item',td_item)
                        td_item_txt = td_item.text.strip().lstrip()
                        print (k,j,i,'td_item_txt =',td_item_txt)
                        #sys.exit(0)
                        
                        #print ('td_item',td_item.text.strip())
                        

                        ### #print ('th_item',translit(th_item,'ru', reversed=True))
                        ### #itle = ''
                        ### #if 'title' in td_item:
                        ### #   title = td_item[title]
                        ### txt = td_item.text.strip().replace(',','.')
                        ### print (i,'td_item',translit(txt,'ru', reversed=True))


                    #print ('sortable_item',sortable_item)
                    #sys.exit(0)

#-------------------------------------------------------------------------------
def Handle_product(\
    soup):

    i  = 0
    for shop_item_product_in_item in soup.find_all('div', attrs = {'class': 'prod-info'}): 

        #print ("shop_item_product_in_item=",shop_item_product_in_item)


        #for list_item in soup.find_all('div', attrs = {'class': 'prod-list'}): 
        #    for info_item in soup.find_all('div', attrs = {'class': 'prod-info'}): 
        for product_name_item in shop_item_product_in_item.find_all('h2', attrs = {'class': 'product-name'}): 
            for link in product_name_item.find_all('a'):
                #print ("link=",link)
                i  += 1
                print (i, '---------------------------------------------')
                product_href = 'https:' + link.get('href')
                print ("product_href=",product_href)

                response2 = urllib.request.urlopen(product_href)
                html_doc2 = response2.read()

                soup2 = BeautifulSoup(html_doc2, 'html.parser')


                #print ("soup2=============================================")
                #print ("soup2=",soup2)
                #sys.exit(0)


                Handle_product_in_item(\
                    i,
                    soup2)
                #print (i, '---------------------------------------------')

                print ("=============================================")
                #sys.exit(0)


        #if i >0:
        #    break

        #3# for product_name_item in shop_item_product_in_item.find_all('div', attrs = {'class': 'product-property'}): 
        #3# 
        #3#     print ("product-property=",product_name_item)
        #3#     sys.exit(0)

#-------------------------------------------------------------------------------
# main module with import feature
#
def akaMain(argv):



    ## argc = len(argv)
    ## 
    ## i=1
    ## 
    ## CONF_DOXY4UG        =sys.argv[i]; i=i+1
    ## #CONF_DOXY4UG  ='c:\\Git\\w01\cpss\\tools\\DoxyGen\\conf_doxy4ug.ini'
    ## 
    ## CONF_DOXY4UG   =os.path.normpath(CONF_DOXY4UG)
    ## 
    ## print ("CONF_DOXY4UG         : ",CONF_DOXY4UG)  

    #-----------------------------------   


    ##base_link = 'http://xn--80aaaaaz9adflmd2aj2f6f.xn--p1ai/'
    base_link = 'https://www.made-in-china.com/products-search/hot-china-products/LED_Display_Panel.html'

    response = urllib.request.urlopen(base_link)
    html_doc = response.read()


    soup = BeautifulSoup(html_doc, 'html.parser')

    Handle_product(\
        soup)

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

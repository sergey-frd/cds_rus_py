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

#-------------------------------------------------------------------------------
#
#def gt_001(input_str):
#
#    if all_digit(input_str) == 1:
#
#    flag = 0 
#    for p in input_str:
#
#        if p.isdigit() or p = '.':
#            flag = 1 
#            break
#
#    return flag

#-------------------------------------------------------------------------------
#
def all_digit(input_str):

    if input_str == '':
        return 0

    flag = 0 
    result = ''  
    for p in input_str:

        if p.isdigit() or p == '.':
            result += p
            continue
        else:
            flag = 1 
            break

    if flag == 0:
        if float(result) < 0.0001:
            #return 0
            flag = 1 

    return flag


#-------------------------------------------------------------------------------
#
def to_digit(input_str):

    if input_str == '':
        return '0','0'

    result_1 = ''  
    result_2 = '' 
    flag = 0 

    for p in input_str:

        if p.isdigit() or p == '.':
            if flag == 0:
                result_1 += p
            else:
                result_2 += p
        else:
            if flag == 0:
                flag = 1 
            else:
                break

    return result_1,result_2

#-------------------------------------------------------------------------------
def Handle_write_all_csv(\
    flag_tramsl,
    dict_location,
    dict_inv_loc,
    dict_folder_id,
    dict_type_screen,
    dict_inv_type_scr, 
    dict_period_razmesenia,
    dict_product):

    Handle_write_csv(\
        flag_tramsl,
        'location.csv',
        dict_location)
    
    Handle_write_csv(\
        flag_tramsl,
        'inv_loc.csv',
        dict_inv_loc)
    
    Handle_write_csv(\
        flag_tramsl,
        'folder.csv',
        dict_folder_id)
    
    Handle_write_csv(\
        flag_tramsl,
        'type_screen.csv',
        dict_type_screen)
    
    Handle_write_csv(\
        flag_tramsl,
        'inv_type_scr.csv',
        dict_inv_type_scr)
    
    Handle_write_csv(\
        flag_tramsl,
        'period_razmesenia.csv',
        dict_period_razmesenia)

    Handle_write_csv(\
        flag_tramsl,
        'product.csv',
        dict_product)

#-------------------------------------------------------------------------------
def Handle_write_csv(\
    flag_tramsl,
    out_file,
    dct):

    #print ("out_file=",out_file)
    line = ''
    if out_file == 'product.csv':
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
            'anonce'+ '\n'


    elif out_file == 'location.csv':
        line = \
            'name'+','+\
            'href' + '\n'
    elif out_file == 'inv_loc.csv':
        line = \
            'href'+','+\
            'name' + '\n'
    elif out_file == 'folder.csv':
        line = \
            'option_code'+','+\
            'name'+','+\
            'base_local'+','+\
            'n_level'+','+\
            'level' + '\n'
    elif out_file == 'type_screen.csv':
        line = \
            'code'+','+\
            'name' + '\n'
    elif out_file == 'period_razmesenia.csv':
        line = \
            'code'+','+\
            'value' + '\n'




            #'data_kinds'+','+\
            #'data_value' + '\n'

#        'data_name'+','+\


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
def Handle_product_in_item(ii,base,dict_product,\
    link_lvl2,
    dict_inv_loc,
    dict_folder_id,
    dict_inv_type_scr,
    data,
    soup):

    product_anonce_txt  = ""
    anonce_code         = ""
    product_anonce_meter= ""
    product_anonce_pix  = ""
    product_name        = ""
    price_in_rub        = ""


    #for product_in_item in soup.find_all('div', attrs = {'class': 'shop2-item-product-in'}): 
        #for product_top_wr_item in product_in_item.find_all('div', attrs = {'class': 'product-top-wr'}): 
        #
        #    i  = 0
        #    for product_info_wr_item in product_top_wr_item.find_all('div', attrs = {'class': 'product-info-wr'}): 
        #
        #        i  += 1
        #
        #        #if i > 3:
        #        #    break
        #
        #        for product_article_item in product_info_wr_item.find_all('div', attrs = {'class': 'product-article'}): 
        #            print ("000 product_article_item=",product_article_item)

    i  = 0
    for shop2_item_product_in_item in soup.find_all('div', attrs = {'class': 'shop2-item-product-in'}): 

        i  += 1
        #print (i, '---------------------------------------------')
        #print ("shop2_item_product_in_item=",shop2_item_product_in_item)
        #print (i, '---------------------------------------------')

        for product_price_current_box in shop2_item_product_in_item.find_all('div', attrs = {'class': 'price-current'}): 
            price_current = product_price_current_box.text.strip().replace('руб.','').lstrip()

            price_in_rub =''  
            for p in price_current:
                if p.isdigit():
                    price_in_rub += p

        for product_top_wr_item in shop2_item_product_in_item.find_all('div', attrs = {'class': 'product-top-wr'}): 


            for product_info_wr_item in product_top_wr_item.find_all('div', attrs = {'class': 'product-info-wr'}): 

                for product_name_item in product_info_wr_item.find_all('div', attrs = {'class': 'product-name'}): 
                    product_name = product_name_item.text.strip()
                    product_name = product_name.replace(',',';')
                    ## print ("product_name=",product_name)

                    for link in product_name_item.find_all('a'):
                        product_href = link.get('href')

                        ## print("link_lvl2=",link_lvl2)
                        ## print("product_href=",product_href)

                for product_article_item in product_info_wr_item.find_all('div', attrs = {'class': 'product-article'}): 
                    product_article_list = product_article_item.text.strip().split(' ')
                    product_article = product_article_list[1]


        product_anonce_list_0_0 = ''
        product_anonce_list_0_1 = ''
        product_anonce_pix      = ''

        for product_anonce_item in shop2_item_product_in_item.find_all('div', attrs = {'class': 'product-anonce'}): 
            product_anonce_list = product_anonce_item.text.strip().split('\n')
            if len(product_anonce_list) > 1:
                product_anonce_list_0 = product_anonce_list[0].split(' ')

                if len(product_anonce_list_0) > 2:

                    product_anonce_list_0_0 = product_anonce_list_0[0]
                    product_anonce_list_0_1 = product_anonce_list_0[1]

                    product_anonce_txt = product_anonce_list_0_0 + ' '+ product_anonce_list_0_1
                    product_anonce_meter = product_anonce_list_0[2]
                else:
                    product_anonce_txt = product_anonce_list_0_0
                    product_anonce_meter = product_anonce_list_0[1]

                if ' ' in product_anonce_list[1]:
                    product_anonce_list_1 = product_anonce_list[1].split(' ')
                    if len(product_anonce_list_1) > 1:
                        product_anonce_pix = product_anonce_list_1[1]

                ## print ("product_anonce_list_0=",product_anonce_list_0)
                ## print ("product_anonce_list_1=",product_anonce_list_1)
    
        #product_options_box_list = shop2_item_product_in_item.find_all ('ul', attrs = {'class': 'product-options'}) 
        for product_options_box in  shop2_item_product_in_item.find_all ('ul', attrs = {'class': 'product-options'}): 
        #for product_options_box in product_options_box_list :
    
            dict_options = dict() 
            dict_options["opt_dney"]            = ''
            dict_options["hronometraz_rolika"]  = ''
            dict_options["option_data_kinds"]   = ''
            dict_options["option_data_value"]   = ''
            dict_options["option_data_name"]    = ''
            #dict_options["li_option_body"]     = ''
            dict_options["transl_v_sutki"]      = ''

            dict_options = Handle_product_options_box_item(\
                    "odd",
                    dict_options,
                    data,
                    product_options_box)

            dict_options = Handle_product_options_box_item(\
                    "even",
                    dict_options,
                    data,
                    product_options_box)

            #print (i, '---------------------------------------------')
            #print("link_lvl2=",link_lvl2)
            #print("product_href=",product_href)
            #
            #print ("product_article=",product_article)
            #print ("product_anonce_txt=",product_anonce_txt)
            #print ("product_anonce_meter=",product_anonce_meter)
            #print ("product_anonce_pix=",product_anonce_pix)
            #
            #print ("product_name=",product_name)
            #print ("price_in_rub =",price_in_rub)  
            #
            #print ("dict_options=")
            #pprint(dict_options)
            #print ("dict_options2=")
            #pprint(dict_options2)

            #print (i, '---------------------------------------------')
            #if ',' in price_in_rub:
            #    p_rub = int(price_in_rub.split(',')[0])
            #else:
            #    p_rub = int(price_in_rub)
            #
            #if ',' in dict_options["hronometraz_rolika"]:
            #    h_rolika = int(dict_options["hronometraz_rolika"].split(',')[0])
            #else:
            #    h_rolika = int(dict_options["hronometraz_rolika"])
            #
            #if ',' in dict_options["transl_v_sutki"]:
            #    v_sutki = int(dict_options["transl_v_sutki"].split(',')[0])
            #else:
            #    v_sutki = int(dict_options["transl_v_sutki"])
            #
            #if 'Месяц' == dict_options["opt_dney"]:
            #    dney = 30 
            #else:
            #    if all_digit(dict_options["opt_dney"]) == 1: print ("??? opt_dney = ", dict_options["opt_dney"]); continue  
            #    dney = int(dict_options["opt_dney"]) 

            #price_sec1 = p_rub/(h_rolika*v_sutki*dney)
            #price_sec2 = round(price_sec1,2)
            #price_sec  = str(price_sec2)


            link_lv  = ''
            href_list = os.path.split(product_href)
            path_list = os.path.split(link_lvl2)

            if 'moskva' in path_list[0] or 'moskva' in path_list[1]:
                if  not link_lvl2 in dict_inv_loc:
                    print ("!!!! CONTINUE link_lvl2 =",link_lvl2)  
                    #sys.exit(0)
                    continue

                loc_text = dict_inv_loc[link_lvl2]
                folder_val = dict_folder_id[loc_text].split(',')
                if 'moskva' in path_list[0] :
                    folder_up = 'Москва,'+folder_val[2].lstrip()
                else:
                    folder_up = 'Россия,Москва'

            else:
                #link_lv  = os.path.join(link_lvl2, href_list[1])
                #link_lv  = link_lvl2 +'/'+ href_list[0]
                link_lv  = href_list[0]

                if not link_lv in dict_inv_loc:
                    print ("!!!! CONTINUE link_lv =",link_lv)  
                    #sys.exit(0)
                    continue

                loc_text = dict_inv_loc[link_lv]
                folder_val = dict_folder_id[loc_text].split(',')
                #folder_up = folder_val[2]


                if  'oblast'     in path_list[0] or\
                    'respublika' in path_list[0] or\
                    'chuvashiya' in path_list[0] or\
                    'region'     in path_list[0] or\
                    'stan'       in path_list[0] or\
                    'kray'       in path_list[0]:
                    #folder_up = 'Россия,'+folder_val[2]
                    if not path_list[0] in dict_inv_loc:
                        print ("!!!! CONTINUE link_lv =",path_list[0])  
                        #sys.exit(0)
                        continue
                    folder_txt = dict_inv_loc[path_list[0]]
                else:                    
                    if not link_lvl2 in dict_inv_loc:
                        print ("!!!! CONTINUE link_lvl2 =",link_lvl2)  
                        #sys.exit(0)
                        continue
                    folder_txt = dict_inv_loc[link_lvl2]
                folder_up = 'Россия,'+ folder_txt


            if 'Медиафасад' in product_anonce_txt:
                anonce_lst = product_anonce_txt.split(' ')
                if len(anonce_lst) > 1:
                    product_anonce_txt = anonce_lst[0]
                    metr               = anonce_lst[1]

            if link_lvl2          == '': print ("!!! link_lvl2          =", translit(link_lvl2,'ru', reversed=True)); continue  
            if folder_up          == '': print ("!!! folder_up          =", translit(folder_up,'ru', reversed=True)); continue  
            if loc_text           == '': print ("!!! loc_text           =", translit(loc_text,'ru', reversed=True)); continue  
            if product_href       == '': print ("!!! product_href       =", translit(product_href,'ru', reversed=True)); continue  
            if product_anonce_txt == '': print ("!!! product_anonce_txt =", translit(product_anonce_txt,'ru', reversed=True)); continue  
            if product_name       == '': print ("!!! product_name       =", translit(product_name,'ru', reversed=True)); continue  
            if dict_options["opt_dney"]       == '': print ("!!! opt_dney       =", translit(dict_options["opt_dney"],'ru', reversed=True)); continue  
            if dict_options["hronometraz_rolika"]       == '': print ("!!! hronometraz_rolika       =", translit(dict_options["hronometraz_rolika"],'ru', reversed=True)); continue  
            if dict_options["transl_v_sutki"]       == '': print ("!!! transl_v_sutki       =", translit(dict_options["transl_v_sutki"],'ru', reversed=True)); continue  

            metr = product_anonce_meter.lstrip().replace(',','.')
            pix  = product_anonce_pix.lstrip().replace(',','.')

            metr_1,metr_2 = to_digit(metr)
            pix_1,pix_2   = to_digit(pix)


            if metr_1 ==   '': print ("???* metr_1 = ", metr_1); continue  
            if metr_2 ==   '': print ("???* metr_2 = ", metr_2); continue  
            if pix_1  ==   '': print ("???* pix_1  = ", pix_1) ; continue  
            if pix_2  ==   '': print ("???* pix_2  = ", pix_2) ; continue  

            if all_digit(metr_1) == 1: print ("??? metr_1 = ", metr_1); continue  
            if all_digit(metr_2) == 1: print ("??? metr_2 = ", metr_2); continue  
            if all_digit(pix_1)  == 1: print ("??? pix_1  = ", pix_1) ; continue  
            if all_digit(pix_2)  == 1: print ("??? pix_2  = ", pix_2) ; continue  

            if all_digit(price_in_rub)                         == 1: print ("??? price_in_rub = ", price_in_rub); continue  
            #if all_digit(price_sec)                            == 1: print ("??? price_sec = ", price_sec); continue  
            if all_digit(dict_options["hronometraz_rolika"].replace(',','.'))   == 1: print ("??? dict_options[hronometraz_rolika] = ", dict_options["hronometraz_rolika"].replace(',','.')); continue  
            if all_digit(dict_options["transl_v_sutki"].replace(',','.'))       == 1: print ("??? dict_options[transl_v_sutki] = ", dict_options["transl_v_sutki"].replace(',','.')); continue  
            #if all_digit(dict_options["opt_dney"])             == 1: print ("??? dict_options[opt_dney] = ", dict_options["opt_dney"]); continue  

            if not product_anonce_txt in dict_inv_type_scr:
                print ("??? product_anonce_txt =",product_anonce_txt)  
                #sys.exit(0)
                #continue 
                anonce_code = ''
            else:
                anonce_code = dict_inv_type_scr[product_anonce_txt]


            if dict_options["opt_dney"] == 'Месяц':
                dict_options["opt_dney"] = '30'

            line = \
                link_lvl2.replace(',',';')  + ','+\
                folder_up.lstrip()  + ','+\
                loc_text.replace(',',';')  + ','+\
                product_href.replace(',',';')  + ','+\
                metr_1  + ','+\
                metr_2  + ','+\
                pix_1  + ','+\
                pix_2  + ','+\
                product_name  + ','+\
                price_in_rub  + ','+\
                dict_options["hronometraz_rolika"].replace(',','.')  + ','+\
                dict_options["transl_v_sutki"].replace(',','.')  + ','+\
                dict_options["opt_dney"].replace(',','.')  + ','+\
                anonce_code  + ','+\
                product_anonce_txt.replace(',',';')

            #str(metr_kv)  + ','+\
            #product_anonce_meter.replace('х','*') .replace('м','')  + ','+\
            #product_anonce_pix.replace('х','*')  + ','+\

            print (i,translit(product_article,'ru', reversed=True) ,translit(line, 'ru', reversed=True))  

                #+ ','+\
                #dict_options["option_data_kinds"].replace(',',';')  + ','+\
                #dict_options["option_data_value"].replace(',',';') 

               ### dict_options["option_data_name"]  + ','+\
               ### dict_options["li_option_body"]  + ','+\

            dict_product[product_article] = line

    return dict_product

#-------------------------------------------------------------------------------
def Handle_product_options_box_item(\
        product_opt,
        dict_options,
        data,
        product_options_box):




    ulTag_List = product_options_box.find_all("li", {product_opt + " type-select"})

    p = 0
    for ulTag in ulTag_List :
        p += 1
        #print (p, "+++ ulTag                   =",ulTag) 

        #liTag = ulTag.find("div", {"class":"option-title"})
        liTag_List = ulTag.find_all("div", {"class":"option-title"})
        for liTag in liTag_List :
            #print ("liTag =",liTag)  
            option_title = liTag.text.strip()

            #if option_title != 'Период размещения':

            ## print (p, product_opt + " option_title =",option_title)  


            #li_option_body_box = ulTag.find("div", {"class":"option-body"})
            li_option_body_list = ulTag.find_all("div", {"class":"option-body"})
            for li_option_body_box in li_option_body_list :

                li_option_body = li_option_body_box.text.strip()

                #print (p, product_opt ,li_option_body) 
                #dict_options["li_option_body"] = li_option_body


                #<div class="option-title">Период размещения</div>
                #<div class="option-title">Хронометраж ролика</div>
                #<div class="option-title">Трансляций в сутки</div>

                #if option_title == "Хронометраж ролика":

                for li_opt_body in li_option_body_box :

                    li_shop2_cf = li_option_body_box.find("select", {"class":"shop2-cf"})
                    #print (p, product_opt + " li_shop2_cf =",li_shop2_cf)  
                    if li_shop2_cf == None:

                        if option_title == "Хронометраж ролика":
                            hronometraz_rolika = li_opt_body
                            #print (p, product_opt + " option_title =",option_title)  
                            dict_options["hronometraz_rolika"] = hronometraz_rolika
                            #print (p,product_opt + " hronometraz_rolika1  =",dict_options["hronometraz_rolika"])

                        elif option_title == "Период размещения":
                            opt_time_list = li_opt_body.strip().split(' ')
                            ## print (p, u, product_opt + " opt_time =",opt_time)  
                            #dict_options["opt_time"] = opt_time
                            dict_options["opt_dney"] = opt_time_list[0]

                        elif option_title == "Трансляций в сутки":
                            transl_v_sutki = li_opt_body
                            #print (p, product_opt + " option_title =",option_title)  
                            dict_options["transl_v_sutki"] = transl_v_sutki
                            #print (p,product_opt + " transl_v_sutki  =",dict_options["transl_v_sutki"])
        
                    else:

                        u = 0
                        option_data_kinds = ''
                        for option_lst in li_shop2_cf.find_all('option') :
                            u += 1                 
                            #print ("odd  option_lst =",option_lst)

                            #if option_lst.has_attr("selected") or option_title == "Хронометраж ролика":
                            if option_lst.has_attr("selected"):
                                option_selected   = option_lst["selected"].strip()
                                #print (p, u, product_opt + " option_selected   =",option_selected)


                                #transl_v_sutki = option_lst["cf_kolicestvo_translacij_sutki_"].strip()
                                #print (p, product_opt + " cf_kolicestvo_translacij_sutki_ =",transl_v_sutki)  
                                #dict_options["transl_v_sutki"] = transl_v_sutki


                                #print (p, product_opt + " option_title =",option_title)  
                                #print (p, product_opt + " option_lst =",option_lst)  

                                ### dict_options["option_title"] = option_title

                                option_data_name  = option_lst["data-name"].strip()

                                option_data_kinds = option_lst["data-kinds"]
                                #option_data_kinds_list = option_lst["data-kinds"]
                                #if len(option_data_kinds_list) > 1:
                                #    option_data_kinds = ''
                                #    for option_data_k in option_data_kinds_list :
                                #        option_data_kinds += option_data_k + ';'
                                #else:
                                #    option_data_kinds = option_data_kinds_list

                                option_data_value = option_lst["data-value"].strip()

                                #print (p, u, product_opt + " option_data_name  =",option_data_name)
                                dict_options["option_data_name"] = option_data_name

                                if option_data_name == "hronometraz_rolika":
                                    hronometraz_rolika = option_lst.text
                                    #print (p,product_opt + " hronometraz_rolika2  =",hronometraz_rolika ) 	
                                    dict_options["hronometraz_rolika"] = hronometraz_rolika


                                elif option_data_name == "period_razmesenia":
                                    opt_time_list = option_lst.text.strip().split(' ')
                                    #print (p, u, product_opt + " cf_period_razmesenia opt_time_list =",opt_time_list)  
                                    #dict_options["opt_time"] = opt_time
                                    dict_options["opt_dney"] = opt_time_list[0]

                                elif option_data_name == "kolicestvo_translacij_sutki_":
                                    transl_v_sutki = option_lst.text.strip()
                                    #print (p, product_opt + " option_title =",option_title)  
                                    dict_options["transl_v_sutki"] = transl_v_sutki
                                    #print (p,product_opt + " transl_v_sutki  =",dict_options["transl_v_sutki"])

                                ## print (p, u, product_opt + " option_data_kinds =",option_data_kinds)
                                ## print (p, u, product_opt + " option_data_value =",option_data_value)

                                option_value = option_lst["value"]
                                ## print (p, u, product_opt + " option_value   =",option_value)

                                dict_options["option_data_kinds"] = option_data_kinds
                                dict_options["option_data_value"] = option_data_value
                                ### dict_options["option_value"] = option_value
    return dict_options

#-------------------------------------------------------------------------------

def Handle_vrema_raboty(\
        data,
        block_body_item):

    dict_vrema_raboty = dict()

    for vrema_raboty_item in block_body_item.find_all('select', attrs = {'name': "s[vrema_raboty]" }): 

        for option_item in vrema_raboty_item.find_all('option'):
            #print ("000 option_item=",option_item)
            if option_item['value'].strip() != '':
                dict_vrema_raboty[option_item['value'].strip()] = \
                                 option_item.text.strip()


    return dict_vrema_raboty

#-------------------------------------------------------------------------------

def Handle_period_razmesenia(\
        data,
        block_body_item):

    dict_period_razmesenia = dict()

    for period_razmesenia_item in block_body_item.find_all('select', attrs = {'name': "s[period_razmesenia]" }): 

        for option_item in period_razmesenia_item.find_all('option'):
            #print ("000 option_item=",option_item)
            if option_item['value'].strip() != '':
                dict_period_razmesenia[option_item['value'].strip()] = \
                                 option_item.text.strip()


    return dict_period_razmesenia

#-------------------------------------------------------------------------------

def Handle_type_screen(\
        data,
        block_body_item):

    #print ("Handle_type_screen : ","started")  
    dict_type_screen  = dict()
    dict_inv_type_scr = dict()

    for typescreen_item in block_body_item.find_all('select', attrs = {'name': "s[typescreen]" }): 

        for option_item in typescreen_item.find_all('option'):
            #print ("000 option_item=",option_item)
            if option_item['value'].strip() != '':

                dict_type_screen[option_item['value'].strip()] = \
                                 option_item.text.strip()

                dict_inv_type_scr[option_item.text.strip()] = \
                                 option_item['value'].strip()

    return dict_type_screen, dict_inv_type_scr

#-------------------------------------------------------------------------------

def Handle_block_body(\
        data,
        soup):

    dict_folder_id = dict()
    list_folder_id = list()

    #print ("Handle_block_body : ","started")  
    for search_online_store_item in soup.find_all('div', attrs = {'class': 'search-online-store'}): 
        #print ("000 search_online_store_item=",search_online_store_item)
        for block_body_item in search_online_store_item.find_all('div', attrs = {'class': 'block-body'}): 
            #rint ("000 block_body_item=",block_body_item)

            for folder_id_item in block_body_item.find_all('select', attrs = {'name': "s[folder_id]" }): 
                base_local = ''
                for option_item in folder_id_item.find_all('option'):

                    option_code = option_item['value'].strip()
                    option_txt = option_item.text.strip()
                    option_list = option_txt.split(' ')
                    len_option_list = len(option_list)

                    #if '»»' in option_txt:
                    #else:
                    if len_option_list == 1:
                        name  = option_list[0]
                        name_s = name.lstrip()
                        n_level = 1
                        level = ''
                        base_local = name
                    else:
                        name = option_txt.replace('»','')
                        name_s = name.lstrip()
                        if '»»' in option_txt:
                            n_level = 3
                            level = '»»'
                        else:
                            n_level = 2
                            level = '»'
                            base_local = name

                    list_folder_id.append(name)
                    #if level != 3:
                    #if str(option_list[0][0]) != ' ':
                    #    base_local = name

                    #print ("000 option_item=",base_local, option_list)
                    #print ("000 option_item=",option_code,option_txt,len_option_list,name,level, option_list)
                    #print ("000 option_item=",option_code,name,name_s,n_level,level)

                    line = \
                        option_code + ','+\
                        name        + ','+\
                        base_local  + ','+\
                        str(n_level)+ ','+\
                        level       + '\n'

                    dict_folder_id[name_s] = line

           #for older_field_item in block_body_item.find_all('div', attrs = {'class': 'field select folder-field'}): 
           #   print ("000 folder_field_item=",folder_field_item)
                #for option_item in folder_field_item.find_all('option'): 
                    #for _item in _item.find_all('div', attrs = {'class': ''}): 
                    #    for _item in _item.find_all('div', attrs = {'class': ''}): 
                    #print ("000 option_item=",option_item)


    return list_folder_id,block_body_item,dict_folder_id

#-------------------------------------------------------------------------------

def Handle_fixed_panel_wr(\
        data,
        soup):

    #with open('index.csv', 'w','utf-8') as csv_file:
    #    writer = csv.writer(csv_file)
    #writer.writerow([a_href,a_txt, datetime.now()])

    dict_location = dict()
    dict_inv_loc  = dict()

    for fixed_panel_wr_item in soup.find_all('div', attrs = {'class': 'fixed-panel-wr'}): 
        for fixed_panel_in_item in fixed_panel_wr_item.find_all('div', attrs = {'class': 'fixed-panel-in'}): 
            for folders_block_wr_item in fixed_panel_in_item.find_all('div', attrs = {'class': 'folders-block-wr'}): 
                for folders_ul_item in folders_block_wr_item.find_all('ul', attrs = {'class': 'folders-ul'}): 
                    #for folders_block_in_item in folders_block_wr_item.find_all('div', attrs = {'class': 'folders-block-in'}): 


                    #if i > 3:
                    #    break


                    #product_item = product_item.text.strip() 
                    #print ("000 folders_ul_item=",folders_ul_item)

                    li_hasClass_List = folders_ul_item.find_all("li", {'class': "hasClass"})

                    i  = 0
                    for li_hasClass in li_hasClass_List :
                        i += 1
                        #print (i, '*********************************************')

                        #print ("-- li_hasClass=",li_hasClass)


                        li_hasClass_a_list = li_hasClass.find_all('a')
                        for hasClass_a in li_hasClass_a_list :

                            a_href = hasClass_a.get('href')
                            a_txt = hasClass_a.text.strip()

                            #print ("---- a_href=",a_href,a_txt)
                            #print ("---- a_txt=",a_txt)
                            #print ("---- hasClass_a=",a_href,a_txt)

                            dict_location[a_txt] = a_href
                            dict_inv_loc[a_href] = a_txt

    return dict_location,dict_inv_loc

#_______________________________________________________________________________

class Foo(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'str: %s' % self.name

    def __unicode__(self):
        return 'uni: %s' % self.name.decode('utf-8')

    def __repr__(self):
        return 'repr: %s' % self.name

#-------------------------------------------------------------------------------

def make_unicode(input):
    if type(input) != unicode:
        input =  input.decode('utf-8')
        return input
    else:
        return input

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


    base_link = 'http://xn--80aaaaaz9adflmd2aj2f6f.xn--p1ai/'
    response = urllib.request.urlopen(base_link)
    html_doc = response.read()


    soup = BeautifulSoup(html_doc, 'html.parser')

    dict_location,dict_inv_loc = Handle_fixed_panel_wr(\
            data,
            soup)

    #print ("===========================================")
    #print ("dict_location=")
    #pprint(dict_location)

    list_folder_id,block_body_item, dict_folder_id = Handle_block_body(\
            data,
            soup)
    #print ("===========================================")
    #print ("dict_folder_id=")
    #pprint(dict_folder_id)
    #pprint(list_folder_id)

    dict_type_screen, dict_inv_type_scr = Handle_type_screen(\
            data,
            block_body_item)

    #print ("===========================================")
    #print ("dict_type_screen=")
    #pprint(dict_type_screen)


    dict_period_razmesenia = Handle_period_razmesenia(\
            data,
            block_body_item)

    #print ("===========================================")
    #print ("dict_period_razmesenia=")
    #pprint(dict_period_razmesenia)


    dict_vrema_raboty = Handle_vrema_raboty(\
            data,
            block_body_item)

    #print ("===========================================")
    #print ("dict_vrema_raboty=")
    #pprint(dict_vrema_raboty)


    #Handle_product_in_item(\
    #        data,
    #        soup)


    print ("===========================================")
    sort_keys=sorted(dict_location.keys())
    i  = 0

    dict_product = dict() 

    for kk in sort_keys:

        val  = dict_location[kk]
        val2 = dict_folder_id[kk]
        val2_list  = val2.split(',')
        #print ("key=",kk,val,val2)
        #print ("val2_list=",val2_list)

        #base = ''
        #if val2_list[1][0] != ' ':
        #    base = val2_list[1][0]
        #    continue
        #else:
        #    base = val2_list[1]
        base = val2_list[2]

        link_lvl2 = base_link + val[1:]

        if 'shop/folder' in link_lvl2 or\
           'shop/product' in link_lvl2:
            continue

        #if link_lvl2 != 'http://xn--80aaaaaz9adflmd2aj2f6f.xn--p1ai/moskva':
        #    continue
       
      
        #if link_lvl2 != 'http://xn--80aaaaaz9adflmd2aj2f6f.xn--p1ai/bashkortostan':
        #    continue

        response_lvl2 = urllib.request.urlopen(link_lvl2)
        html_doc_lvl2 = response_lvl2.read()
        #print ("html_doc_lvl2=",html_doc_lvl2)


        soup_lvl2 = BeautifulSoup(html_doc_lvl2, 'html.parser')
        #print ("soup_lvl2=",soup_lvl2)
        #sys.exit(0)


        i  += 1
        #print ("===========================================")
        print ('*********',i,link_lvl2)
        #print (i,base, val2_list[1], '==============================================')
        #print ("===========================================")
        dict_product = Handle_product_in_item(i,base,dict_product,\
            val,
            dict_inv_loc,
            dict_folder_id,
            dict_inv_type_scr,
            data,
            soup_lvl2)

        #if i > 0:        
        #    break

        #sys.exit(0)


    Handle_write_all_csv(\
        0,
        dict_location,
        dict_inv_loc,
        dict_folder_id,
        dict_type_screen,
        dict_inv_type_scr, 
        dict_period_razmesenia,
        dict_product)

    Handle_write_all_csv(\
        1,
        dict_location,
        dict_inv_loc,
        dict_folder_id,
        dict_type_screen,
        dict_inv_type_scr, 
        dict_period_razmesenia,
        dict_product)

    sys.exit(0)


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

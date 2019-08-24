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
def Handle_pix_add(\
        interv_key_dict,of2,of_price ):


    Func_Parm_CSV = 'ppi_detail.csv'
    
    sort_keys=sorted(interv_key_dict.keys())

    try:

        ff = open(Func_Parm_CSV)
        src = ff.read()
        ff.close()
        src_list = src.split("\n")

        len_src_list = len(src_list)
        for indx in range(0,len_src_list-1):
            line =   src_list[indx]


            nn_line = indx+1
            if indx == 0:
                continue

            f_kk = float(line) + 100000

            #print(nn_line,f_kk) 
            for akk in sort_keys:

                lst = akk.split(',')
                f_min = float(lst[0])
                f_max = float(lst[1])

                if f_kk >= f_min and f_kk <= f_max:

                    f_sum = interv_key_dict[akk]
                    ff_kk = round(f_kk-100000,2)
                    r_kk = str(ff_kk)

                    #print(nn_line,r_kk,'=>',akk,str(f_sum))
                     
                    line2 =\
                        r_kk+','+\
                        str(f_sum)
                    print (r_kk,"f_sum=",f_sum)
                    of2.write(line2+'\n')
                     
                    line3 =\
                        r_kk+','+\
                        str(f_sum)+',,'
                    #print (r_kk,"f_sum=",f_sum)
                    of_price.write(line3+'\n')

                    
                    break
            


        #f_Func_P_CSV = open(Func_Parm_CSV, 'r')
        #
        #
        #N_line = 0
        #print ("*********************************************")
        #reader = csv.DictReader(f_Func_P_CSV, delimiter=',')
        #
        #print ("reader=",reader)
        ##pprint (reader)
        #
        #
        #for line in reader:
        #    N_line     += 1  
        #    print(N_line,line) 
        #
        #
        ##print ("Handle_csv_2_dict f_Func_P_CSV=",f_Func_P_CSV)
        ##dct = csv_reader_14(f_Func_P_CSV,
        ##         Func_Parm_CSV,dct)
        #
        ##src = f_Func_P_CSV.read()
        #f_Func_P_CSV.close()
    
    except IOError:
        print ("Error: cannot open file: " + Func_Parm_CSV + "\n")
        sys.exit(2)


        of2.close()
        of_price.close()

#-------------------------------------------------------------------------------
def Handle_dict_pix_interv(\
        key_dict):


    interv_key_dict = dict()


    sort_keys=sorted(key_dict.keys())
    
    len_key_dict = len(sort_keys) 

    sum = 0
    nn = 0
    i = 0

    for akk in sort_keys:

        nn += 1
        kk = akk - 100000
        f_sum = key_dict[akk]

        if nn == 1:
            interv_key_dict['100000,'+str(akk)] = f_sum
        nn += 1

        if i == 0:
            i = 1
            sum = f_sum
            s_akk = str(akk)

        else:
            interv_key_dict[str(s_akk) +','+str(akk)] = (sum + f_sum) / 2
            i = 0
            sum = 0


    if i == 1:
        interv_key_dict[str(s_akk) +','+ '999999.0'] = f_sum
    else:
        interv_key_dict[str(akk)   +','+ '999999.0'] = f_sum


    return interv_key_dict

    ##----------------------------------------------------
    #out_file2 = 'pix_add.csv'
    #of2 = codecs.open(out_file2, 'w','utf-8')
    #
    #line2 = \
    #    'Pixel_Pitch'+','+\
    #    'dollar'
    #
    #of2.write(line2+'\n')
    #sort_keys=sorted(pix_min_max.keys())
    #
    #sum = 0
    #for kk in pix_min_max:
    #
    #    lst = pix_min_max[kk]
    #    for ll in lst:
    #
    #        line2 =\
    #            kk+','+\
    #            ll
    #
    #        print (kk,"line2=",line2)
    #        of2.write(line2+'\n')
    #
    #of2.close()
    #
    #Func_Parm_CSV == 'ppi_detail.csv'
    #
    #try:
    #    f_Func_P_CSV = open(Func_Parm_CSV, 'r')
    #
    #    #print ("Handle_csv_2_dict f_Func_P_CSV=",f_Func_P_CSV)
    #    #dct = csv_reader_14(f_Func_P_CSV,
    #    #         Func_Parm_CSV,dct)
    #
    #    #src = f_Func_P_CSV.read()
    #    f_Func_P_CSV.close()
    #
    #except IOError:
    #    print ("Error: cannot open file: " + Func_Parm_CSV + "\n")
    #    sys.exit(2)


#-------------------------------------------------------------------------------
def Handle_pix_min_max(\
        pix_min_max):

    out_file2 = 'pix_min_max_add.csv'
    of2 = codecs.open(out_file2, 'w','utf-8')

    line2 = \
        'Pixel_Pitch'+','+\
        'dollar'

    of2.write(line2+'\n')
    sort_keys=sorted(pix_min_max.keys())

    sum = 0
    for kk in pix_min_max:

        lst = pix_min_max[kk]
        for ll in lst:

            line2 =\
                kk+','+\
                ll

            print (kk,"line2=",line2)
            of2.write(line2+'\n')

    return of2
    #of2.close()

#-------------------------------------------------------------------------------
def Handle_dict_pix(\
        dict_pix):

    out_file2 = 'pix_price_add.csv'
    of2 = codecs.open(out_file2, 'w','utf-8')

    line2 = \
        'Pixel_Pitch_avr'+','+\
        'dollar_avr'+','+\
        'dollar_min'+','+\
        'dollar_max'

    of2.write(line2+'\n')

    key_dict = dict()

    sort_keys=sorted(dict_pix.keys())

    sum = 0
    for kk in sort_keys:

        akk = round(float(kk),2) + 100000

        lst = dict_pix[kk]
        i = 0
        sum = 0
        for ll in lst:
            f_ll = float(ll)
            sum += f_ll

            if i == 0:
                dollar_min = f_ll
                dollar_max = f_ll
            else:
                if dollar_min  > f_ll:
                    dollar_min = f_ll
                                       
                if dollar_max  < f_ll:
                    dollar_max = f_ll
            i += 1

        f_i = float(i)
        f_sum = sum/f_i
        dollar_avr = str(round(f_sum,2))

        key_dict[akk] = f_sum

        line2 =\
            kk+','+\
            dollar_avr+','+\
            str(dollar_min)+','+\
            str(dollar_max)

        print (kk,"line2=",line2)
        of2.write(line2+'\n')

    #of2.close()

    return key_dict,of2

#-------------------------------------------------------------------------------
def Handle_out_csv(\
    dict_info,list_info):

    dict_pix = dict()
    pix_min_max = dict()

    out_file = 'screen.csv'
    of = codecs.open(out_file, 'w','utf-8')

    out_file2 = 'pix_price_all.csv'
    of2 = codecs.open(out_file2, 'w','utf-8')

    line = \
        'id'+','+\
        'name'+','+\
        'unit'+','+\
        'quantity'+','+\
        'FOB_Price'+','+\
        'dollar_avr'+','+\
        'dollar_min'+','+\
        'dollar_max'+','

    for ll in list_info:
        #print(ll)
        line += ll +','

    line += '\n'

    of.write(line)



    line2 = \
        'Pixel_Pitch'+','+\
        'dollar_avr'+','+\
        'dollar_min'+','+\
        'dollar_max'+','+\
        'id'+','+\
        '\n'
    of.write(line2)




    for kk in dict_info:

        #print(kk,dict_info[kk])


        if not 'unit'        in dict_info[kk]: continue 
        if not 'Pixel_Pitch' in dict_info[kk]: continue 

        # average
        dollar_avr = str(round(\
            (float(dict_info[kk]['dollar_min'])+\
             float(dict_info[kk]['dollar_max']))/2,\
            2))

        line = \
            str(kk)+','+\
            dict_info[kk]['name']+','+\
            dict_info[kk]['unit']+','+\
            dict_info[kk]['quantity']+','+\
            dict_info[kk]['FOB_Price']+','+\
            dollar_avr+','+\
            dict_info[kk]['dollar_min']+','+\
            dict_info[kk]['dollar_max']+','

        for ll in list_info:
            #print(ll)


            #if not dict_info[kk][ll] in dict_info[kk]:
            if not ll in dict_info[kk]:
                line += '' +','
            else:


                if ll == 'Pixel_Pitch': 
                    Pix_Pitch,p_2   = to_digit(dict_info[kk][ll] )
                    Pix_Pitch_str = Pix_Pitch.strip().lstrip()

                    line += Pix_Pitch_str +','

                    if dict_info[kk]['unit'] == 'Square_Meter': 

                        line2 = \
                            Pix_Pitch_str+','+\
                            dollar_avr+','+\
                            dict_info[kk]['dollar_min']+','+\
                            dict_info[kk]['dollar_max']+','+\
                            str(kk)

                        print (kk,"line2=",line2)
                        of2.write(line2+'\n')


                        if not Pix_Pitch_str in dict_pix:
                            dict_pix[Pix_Pitch_str] = list() 

                        dict_pix[Pix_Pitch_str].append(dollar_avr) 



                        if not Pix_Pitch_str in pix_min_max:
                            pix_min_max[Pix_Pitch_str] = list() 

                        pix_min_max[Pix_Pitch_str].append(dict_info[kk]['dollar_min']) 
                        pix_min_max[Pix_Pitch_str].append(dict_info[kk]['dollar_max']) 


                elif ll == 'Pixel_Density':
                    Pix_Density,p_2   = to_digit(dict_info[kk][ll].replace(';','') )
                    line += Pix_Density.strip().lstrip()  +','

                else:
                    line += dict_info[kk][ll]  +','

        #print (kk,"line=",line)
        of.write(line+'\n')

        #break
    of.close()
    of2.close()\

    return dict_pix, pix_min_max

#-------------------------------------------------------------------------------
def Handle_product_base(\
    soup):

    dict_info = dict()
    list_info = list()

    i  = 0
    for shop_item_product_in_item in soup.find_all('div', attrs = {'class': 'prod-info'}): 
        for product_name_item in shop_item_product_in_item.find_all('h2', attrs = {'class': 'product-name'}): 
            for link in product_name_item.find_all('a'):
                #print ("link=",link)

                i  += 1
                dict_info[i] = dict()

                print (i, '---------------------------------------------')
                #product_href = 'https:' + link.get('href')
                #print ("product_href=",product_href)

                link_txt = link.text.strip().lstrip().replace(',',';')
                print (i,"link_txt=",link_txt)


                dict_info[i]['name'] = link_txt

                #<div class="product-property">
                #FOB Price: <span class="info"><strong class="price">US $ 158-218</strong> / Piece</span><br>
                #Min. Order: <span class="info"><strong>1 Piece</strong></span> <br>
                #</div>

        for property_item in shop_item_product_in_item.find_all('div', attrs = {'class': 'product-property'}): 

            property_item_txt = property_item.text.strip().lstrip()
            #print ("property_item_txt=",property_item_txt)

            if '/' in property_item_txt:

                property_list = property_item_txt.split('/')
                price_interval = property_list[0].strip().lstrip()
                #print ("price_interval=",price_interval)

                FOB_Price = 'FOB Price: US $'
                Min_Order = 'Min. Order:'
                dict_info[i]['FOB_Price'] = FOB_Price.replace('FOB Price:','').strip().lstrip()
                #dict_info[i]['Min_Order'] = Min_Order


                if FOB_Price in price_interval:
                    dollar_interval = price_interval.replace(FOB_Price,'').strip().lstrip().split('-')
                    print ("dollar_interval=",dollar_interval)
                    dollar_min = dollar_interval[0].strip().lstrip()
                    if len(dollar_interval) >1:
                        dollar_max = dollar_interval[1].strip().lstrip()
                    else:
                        dollar_max = dollar_min

                    print ("dollar_min=",dollar_min)
                    print ("dollar_max=",dollar_max)

                    dict_info[i]['dollar_min'] = dollar_min
                    dict_info[i]['dollar_max'] = dollar_max

                #print (1,property_list[1].strip().lstrip())


                prop_list2 = property_list[1].strip().lstrip().split('\n')
                unit = prop_list2[0].strip().lstrip()
                print ("unit=",prop_list2[0].strip().lstrip())
                dict_info[i]['unit'] = unit.replace(' ','_')

                #print ("prop_list2[1]=",prop_list2[1].strip().lstrip())
                if Min_Order in prop_list2[1]:
                    quantity = prop_list2[1].replace(Min_Order,'').strip().lstrip().replace(unit,'')
                    print ("quantity=",quantity)
                    dict_info[i]['quantity'] = quantity


        for extra_property_item in shop_item_product_in_item.find_all('div', attrs = {'class': 'extra-property cf'}):

            for ul_property_item in extra_property_item.find_all('ul', attrs = {'class': 'property-list'}): 
                #print ("ul_property_item=",ul_property_item)
                for li_item in ul_property_item.find_all('li', attrs = {'class': 'J-faketitle ellipsis'}): 
                    #print ("li_item=",li_item)
                    li_item_txt = li_item.text.strip().lstrip()
                    #print ("li_item_txt=",li_item_txt)

                    for property_val_item in li_item.find_all('span', attrs = {'class': 'property-val'}): 

                        property_val_item_txt = property_val_item.text.strip().lstrip()
                        #print ("property_val_item_txt=",property_val_item_txt)

                        name = li_item_txt.replace(property_val_item_txt,'').strip().lstrip()
                        if name[-1] == ':':
                            name = name[:-1]

                        name = name.replace(',',';')
                        name = name.replace(' ','_')
                        name = name.replace(':','')

                        print (name,"=>",property_val_item_txt.replace(',',';'))
                        dict_info[i][name] = property_val_item_txt.replace(',',';')

                        if not name in list_info:
                            list_info.append(name)

                #sys.exit(0)

        #return dict_info,list_info
    return dict_info,list_info


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


    dict_info,list_info = Handle_product_base(\
        soup)

    print ('* dict_info ********************************************')
    #pprint (dict_info)
    #print ('*********************************************')
    #print ("list_info=",list_info)

    #sys.exit(0)

    dict_pix, pix_min_max = Handle_out_csv(\
        dict_info,list_info)

    print ("=============================================")
    key_dict,of_price = Handle_dict_pix(\
        dict_pix)

    print ('* key_dict ********************************************')
    pprint (key_dict)


    print ("=============================================")
    of2 = Handle_pix_min_max(\
        pix_min_max)


    print ("=============================================")
    interv_key_dict = Handle_dict_pix_interv(\
        key_dict)

    print ('* interv_key_dict ********************************************')
    pprint (interv_key_dict)


    print ("=============================================")
    Handle_pix_add(\
        interv_key_dict,of2,of_price )



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

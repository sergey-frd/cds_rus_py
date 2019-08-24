#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pprint import pprint
import json
from bs4 import BeautifulSoup

with open('c:/Git/ws01/de/tests/w1/de_0.json', 'r') as f:
    data = json.load(f)

## #print (data)
## pprint(data)
## 
## 
## print ("data[Base] = ")
## pprint (data['Base'])

## print ("data[Base]HTML_PARSER = ",data['Base']['HTML_PARSER'])



#-------------------------------------------------------------------------------
#
def bs_lib_cases(\
        data,
        soup):

    #-----------------------------------   
    if data['Base']['CASE_HTML_PARSER'] == 'Y':

        print ('*******************************')
        print ("CASE_HTML_PARSER")

        print(soup.prettify())

    #-----------------------------------   
    if data['Base']['CASE_TITLE'] == 'Y':

        print ('*******************************')
        print ("CASE_TITLE")

        print(soup.title)
        # <title>The Dormouse's story</title>           
    #-----------------------------------   
    if data['Base']['CASE_TITLE_NAME'] == 'Y':

        print ('*******************************')
        print ("CASE_TITLE_NAME")


        print(soup.title.name)
        # u'title'


    #-----------------------------------   
    if data['Base']['CASE_TITLE_STRING'] == 'Y':

        print ('*******************************')
        print ("CASE_TITLE_STRING")   


        print(soup.title.string)
        # u'The Dormouse's story'

    #-----------------------------------   
    if data['Base']['CASE_TITLE_PARENT_NAME'] == 'Y':

        print ('*******************************')
        print ("CASE_TITLE_PARENT_NAME")   

        print(soup.title.parent.name)
        # u'head'


    #-----------------------------------   
    if data['Base']['CASE_P'] == 'Y':

        print ('*******************************')
        print ("CASE_P")   

        print(soup.p)
        # <p class="title"><b>The Dormouse's story</b></p>

    #-----------------------------------   
    if data['Base']['CASE_P_CLASS'] == 'Y':

        print ('*******************************')
        print ("CASE_P_CLASS")   
        print(soup.p['class'])
        # u'title'
    #-----------------------------------   
    if data['Base']['CASE_A'] == 'Y':

        print ('*******************************')
        print ("CASE_A")   

        print(soup.a)
        # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

    #-----------------------------------   
    if data['Base']['CASE_FIND_ALL_A'] == 'Y':

        print ('*******************************')
        print ("CASE_FIND_ALL_A")   


        print(soup.find_all('a'))
          # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
          #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
          #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


    #-----------------------------------   
    if data['Base']['CASE_LINK_FIND_ALL_A'] == 'Y':

        print ('*******************************')
        print ("CASE_LINK_FIND_ALL_A")   

        for link in soup.find_all('a'):
            print(link.get('href'))
        # http://example.com/elsie
        # http://example.com/lacie
        # http://example.com/tillie

    #-----------------------------------   
    if data['Base']['CASE_GET_TEXT'] == 'Y':

        print ('*******************************')
        print ("CASE_GET_TEXT")   

        print(soup.get_text())

    #-----------------------------------   
    if data['Base']['CASE_FIND_ID'] == 'Y':

        print ('*******************************')
        print ("CASE_FIND_ID")   
        print(soup.find(id="link3"))
        # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>



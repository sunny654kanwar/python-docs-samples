# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from django.shortcuts import render
#-------------------------------------------------
import requests
from requests.auth import HTTPBasicAuth
#-------------------------------------------------

# Create your views here.
@api_view(['POST'])
def sapcall(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
       # json_data = json.loads(body_unicode)
#        response = req(json_data['from_curr'], json_data['to_curr'], json_data['amount'])
        #-----------------------------------------
        #response = requests.get("""https://hved.xss.accenture.com/sap/opu/odata/sap/ZBLKC_CREATE_SALES_ORDER_SRV/SalesOrderSet('CM-1')""")
        s = requests.session()
        #Starting a GET request to the SAP system to fetch the CSRF token
        url = """https://hved.xss.accenture.com/sap/opu/odata/sap/ZBLKC_CREATE_SALES_ORDER_SRV/SalesOrderSet('CM-1')"""
        headers = {'X-CSRF-Token': 'Fetch'}
        response = s.get(url, headers=headers,auth=HTTPBasicAuth('TEST_SERVICE', 'test123'))
        token = response.headers.get('x-csrf-token')

        url_p = """https://hved.xss.accenture.com/sap/opu/odata/sap/ZBLKC_CREATE_SALES_ORDER_SRV/SalesOrderSet"""
        headers_p = {'X-CSRF-Token': token, 'Content-Type': 'application/atom+xml;type=entry; charset=utf-8'}
        xml = """<?xml version="1.0" encoding="utf-8"?>
                    <entry xml:base="http://hved.xss.accenture.com/sap/opu/odata/sap/ZBLKC_CREATE_SALES_ORDER_SRV/" xmlns="http://www.w3.org/2005/Atom" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata" xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices">
                        <id>http://hved.xss.accenture.com/sap/opu/odata/sap/ZBLKC_CREATE_SALES_ORDER_SRV/SalesOrderSet('CM-1')</id>
                        <title type="text">SalesOrderSet('CM-1')</title>
                        <updated>2017-11-22T15:44:10Z</updated>
                        <category term="ZBLKC_CREATE_SALES_ORDER_SRV.SalesOrder" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme"/>
                        <link href="SalesOrderSet('CM-1')" rel="self" title="SalesOrder"/>
                        <content type="application/xml">
                            <m:properties>
                                <d:Transactiontype/>
                                <d:Transactionnumber>0000000000</d:Transactionnumber>
                                <d:Transactionhash/>
                                <d:TermsPayment/>
                                <d:SoldToParty>200024</d:SoldToParty>
                                <d:Sellerid/>
                                <d:ScheduleLineNumber>0002</d:ScheduleLineNumber>
                                <d:SalesOffice>Z001</d:SalesOffice>
                                <d:SalesDocumentType>OR</d:SalesDocumentType>
                                <d:SalesDocument>14</d:SalesDocument>
                                <d:PriceUnit>1</d:PriceUnit>
                                <d:Prevtransactionhash/>
                                <d:RefDoc/>
                                <d:RefDocType/>
                                <d:PoNumber>477566</d:PoNumber>
                                <d:Pdoctype/>
                                <d:PaymentIn>EUR</d:PaymentIn>
                                <d:OrderUnit>EA</d:OrderUnit>
                                <d:OrderQuantity>100.000</d:OrderQuantity>
                                <d:OrderPriceUnit>EA</d:OrderPriceUnit>
                                <d:NetOrderValue>200000.000</d:NetOrderValue>
                                <d:NetOrderPrice>2000.000</d:NetOrderPrice>
                                <d:Item>00010</d:Item>
                                <d:ConfirmedQuantity>100.000</d:ConfirmedQuantity>
                                <d:Buyerid/>
                            </m:properties>
                        </content>
                    </entry>"""
        response_p = s.post(url_p, data=xml, headers=headers_p, auth=HTTPBasicAuth('TEST_SERVICE', 'test123'))
        #print response.status_code
        # -----------------------------------------
        #response = 'Success!'
        return Response(response_p)
    else:
        return HttpResponse(Http404)
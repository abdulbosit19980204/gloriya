from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# for check unexpect
import zeep
from zeep import settings
from zeep.plugins import HistoryPlugin
from zeep import Client, Settings
from zeep.transports import Transport
from lxml import etree
from datetime import datetime as dt


# Create your views here.
@api_view(['GET'])
def dashboard_view(request):
    # return render(request, 'dashboard.html')

    settings = Settings(strict=False, xml_huge_tree=True)
    history = HistoryPlugin()
    transport = Transport(timeout=10)
    reasionsReturn = 'http://192.168.1.241:5443/EVYAP_UT/EVYAP_UT.1cws?wsdl'
    client = Client(wsdl=reasionsReturn, transport=transport, plugins=[history], settings=settings)
    user = client.service.GetUserByTelegramID(5814532358)
    print(user)
    orders = client.service.GetOrderList(user['Code'])
    # for i in orders:
    #     orders_details = client.service.GetOrderDetails(i['NumOrder'], i['DateOrder'], '2024.05.05')
    #     print(orders_details)
    # cilients = client.service.GetCilients(user['Code'])
    price_list = client.service.GetPriceList(user['Code'])
    user_business = client.service.GetBusinessRegions(user['Code'])
    print(user_business)
    kpi = client.service.GetKPI(user['Code'])
    print(kpi)
    income = client.service.GetIncomesList()
    print(income)
    user_by_data = client.service.GetUser("Sam-5", "Sam-5")
    print(user_by_data)
    dillers = client.service.GetDilers()
    # print(dillers)
    try:
        warehouses = client.service.GetWarehouses()
        # product_blance = client.service.GetProductBlance()
        # print(warehouses)
    except:
        user = None

    return Response(
        status=status.HTTP_200_OK,
        data={
            "cilent": user
        }
    )


def login_view(request):
    return render(request, '../templates/Admin/dist/index.html')


def logout_view(request):
    return render(request, '')


def tables_view(request):
    settings = Settings(strict=False, xml_huge_tree=True)
    history = HistoryPlugin()
    transport = Transport(timeout=10)
    reasionsReturn = 'http://192.168.1.241:5443/EVYAP_UT/EVYAP_UT.1cws?wsdl'
    client = Client(wsdl=reasionsReturn, transport=transport, plugins=[history], settings=settings)
    user = client.service.GetUserByTelegramID(5814532358)
    clients = client.service.GetClients(user['Code'])
    d = {
        "user": user,
        "clients": clients,
    }
    return render(request, '../templates/Admin/dist/tables-responsive.html', context=d)

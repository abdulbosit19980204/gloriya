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

settings = Settings(strict=False, xml_huge_tree=True)
history = HistoryPlugin()
transport = Transport(timeout=10)
reasionsReturn = 'http://192.168.1.241:5443/EVYAP_UT/EVYAP_UT.1cws?wsdl'
client = Client(wsdl=reasionsReturn, transport=transport, plugins=[history], settings=settings)


# Create your views here.
# @api_view(['GET'])
def dashboard_view(request):
    # return render(request, 'dashboard.html')

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

    # return Response(
    #     status=status.HTTP_200_OK,
    #     data={
    #         "cilent": user
    #     }
    # )
    return render(request, '../templates/Admin/dist/index.html',)


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


def getWarehouses_view():
    warehouses = client.service.GetWarehouses()
    return warehouses


def getProductBlance_view(CodeProject, CodeSklad):
    productBlance = client.service.GetProductBalance(CodeProject, CodeSklad)
    return productBlance


def getClients_view(UserCode):
    clients = client.service.GetClients(UserCode)
    return clients


def getPriceTypes_view(UserCode):
    priceList = client.service.GetPriceTypes(UserCode)
    return priceList


def getUser_view(request):
    print(request.GET.get('user'))
    user = request.GET.get('user')
    password = request.GET.get('password')
    user_data = client.service.GetUser(user, password)
    wharehouses = getWarehouses_view()
    # print(wharehouses)
    products = getProductBlance_view(user_data['CodeProject'], user_data['CodeSklad'])
    clients = getClients_view(user_data['Code'])
    priceList = getPriceList_view(user_data['Code'])
    print(user_data),
    print(priceList)
    d = {
        "user": user_data,
        "clients": clients,
        "wharehouses": wharehouses,
        "products": products
    }

    return render(request, '../templates/Admin/dist/tables-responsive.html', context=d)


def getRateOfCurrency_view(Code, Data):
    currency_rate_now = client.service.GetRateOfCurrency(Code, Data)


def getClientBlance(ClientCode, Data):
    pass


def getPriceList_view(UserCode):
    priceList = client.service.GetPriceList(UserCode)
    return priceList


def checkProductBlance_view(UserCode):
    pass


def getOrderList(CodeAgent):
    pass


def getOrderDetail_view(NumberOrder, OrderDate1, OrderDate2):
    pass


def getShippingList_view(UserCode):
    pass


def getBusinessRegions_view(UserCode):
    pass


def getDiscountList_view(UserCode):
    pass


def getReasonOfReturn_view(UserCode):
    pass


def getCashmansList_view(UserCode):
    pass


def getKPI(CodeUser):
    pass


def getDilers():
    pass


def getOrganizations():
    pass


def getWarehousesUser(CodeUser):
    pass


def getContracts(CodeUser, CodeClient):
    pass


def getClientsThroughINN(INN):
    pass


def getBankName(MFO):
    pass

import urllib3
import requests

def handleList():
    orderList = [
    100039643,
    100039573,
    100039571,
    100039569,
    100039567,
    100039565,
    100039561
    ]
    for item in orderList:
        print(item)
        testGet(item)

def testGet(orderId):
    params = {'orderId':orderId}
    url = "http://qacbz-clearing.soa.yeshj.com/api/v1/payment"
    r = requests.get(url,params = params)
    print(r.url) #print(r.text)#print(r.encoding) #print(r.json())
    # r1 = requests.post("http://qacbz-clearing.soa.yeshj.com/api/v1/forward_biz_recon", data=payload) //表单形式
    r1 = requests.post("http://qacbz-clearing.soa.yeshj.com/api/v1/forward_biz_recon", json=params)
    print(r1.url) #print(r1.text)

if __name__ == '__main__':
    handleList()


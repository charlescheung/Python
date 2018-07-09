import time
class testNotifyClearing(object):
    def forwardBizRecon(self,statusExp = 0, httpStatusExp = 200, messageExp = "OK"):
        '''
        结算子合同明细查询
        '''
        print("/v1/forward_biz_recon...")
        url = "http://qacbz-clearing.soa.yeshj.com/api/v1/forward_biz_recon"
        orderId = "94790552"
        postData = {"orderId": orderId,}
        respAct = self.sendRequest(url, "POST", data=postData, statusExp=statusExp,
                                   httpStatusExp=httpStatusExp,messageExp=messageExp)
        print("正向对账通知end：" + orderId)
        return respAct

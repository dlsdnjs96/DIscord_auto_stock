import win32com.client



def connect_cpcybos():
    objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
    bConnect = objCpCybos.IsConnect
    if (bConnect == 0):
        print("PLUS가 정상적으로 연결되지 않음. ")
        return None
    return objCpCybos


def getStockInfo_by_code(stock_code):
    objStockMst = win32com.client.Dispatch("DsCbo1.StockMst")
    objStockMst.SetInputValue(0, stock_code)   #종목 코드 - 삼성전자
    objStockMst.BlockRequest()

    rqStatus = objStockMst.GetDibStatus()
    rqRet = objStockMst.GetDibMsg1()
    if rqStatus != 0:
        print("연결에 실패하였습니다. \r\nError{} : {}".format(rqStatus, rqRet))
        return None
    
    data_form = [['code', 0],  #종목코드
                ['name', 1],  # 종목명
                ['time', 4],  # 시간
                ['cprice', 11], # 종가
                ['diff', 12],  # 대비
                ['open', 13],  # 시가
                ['high', 14],  # 고가
                ['low', 15],   # 저가
                ['offer', 16],  #매도호가
                ['bid', 17],   #매수호가
                ['vol', 18],   #거래량
                ['vol_value', 19],  #거래대금
                ['exFlag', 58], #예상체결가 구분 플래그
                ['exPrice', 55], #예상체결가
                ['exDiff', 56], #예상체결가 전일대비
                ['exVol', 57], #예상체결수량
                ]
                

    stock_info = {}
    for i in data_form:
        stock_info[i[0]] = objStockMst.GetHeaderValue(i[1])
    
    return stock_info
    

if __name__ == '__main__':
    sInfo = getStockInfo_by_code('A005930')
    
    print(sInfo)

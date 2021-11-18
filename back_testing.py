import pandas as pd

def getDate(dd):
    ask = ''
    ask += str(dd)[:4]+'-'
    ask += str(dd)[4:6]+'-'
    ask += str(dd)[6:]

    return ask

data = pd.read_csv('C:\\Users\\dlsdn\\source\\repos\\Auto_Stocks_Trading\\stock_data_1d.csv', encoding='euc-kr')
#data['날짜'] = pd.to_datetime(data['날짜'])
data.sort_values(['날짜'], axis=0, ascending=False)
#data['날짜'] = pd.to_numeric(data['날짜'])

start_date = '20150101'
end_date = data['날짜'].max()

kinds = data['종목코드'].unique()
print(kinds)

gb = data.groupby('종목코드')
for k in kinds:
    data_ = gb.get_group(k)
    len_ = len(data_)
    start_cash = 1000000

    print(len_)


    for i in range(1, 3):
        start_cash = 1000000
        K = i*0.1
        print('K = {}'.format(K))
        #print('종목코드 : '.format(k))
        for idx in range(len_-5400+365, 0, -1):
            today_data = data_.iloc[idx, :]
            yesterday_data = data.iloc[idx+1, :]

            if yesterday_data['저가'] < yesterday_data['시가'] and yesterday_data['시가'] < yesterday_data['종가'] and yesterday_data['종가'] < yesterday_data['고가']:
                gap = round((K *(yesterday_data['고가'] - yesterday_data['저가'])) + yesterday_data['저가'])
                if today_data['고가'] >= gap:
                    stock_cnt = round(start_cash/gap)
                    tmp = start_cash
                    start_cash -= stock_cnt*gap
                    start_cash += stock_cnt*today_data['종가']

                    print('날짜 {}\t| 차익 : {:,}  \t| {:,} -> {:,}'.format(getDate(today_data['날짜']), start_cash-tmp, gap, today_data['종가']))

        print('최종금액 : {:,}'.format(start_cash))




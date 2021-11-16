from pywinauto import application
import time, os
import userInfo
import Auto_Stocks_Trading


def start_creon_plus():
    os.system('taskkill /IM coStarter* /F /T')
    os.system('taskkill /IM CpStart* /F /T')
    os.system('taskkill /IM DibServer* /F /T')
    os.system('wmic process where "name like \'%coStarter%\'" call terminate')
    os.system('wmic process where "name like \'%CpStart%\'" call terminate')
    os.system('wmic process where "name like \'%DibServer%\'" call terminate')
    time.sleep(5)       

    
    app = application.Application()
    app.start('C:\CREON\STARTER\coStarter.exe /prj:cp /id:{} /pwd:{} /pwdcert:{} /autostart'.format(userInfo.getId(), userInfo.getPw(), userInfo.getPwcert()))

    limited_time = 0
    while(Auto_Stocks_Trading.check_creon_system() == False):
        time.sleep(3)
        limited_time += 1
        if limited_time >= 20:
            print('대기시간 초과')
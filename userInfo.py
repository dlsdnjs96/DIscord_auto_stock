import os
from dotenv import load_dotenv


load_dotenv('creon.env')

TOKEN = os.getenv('TOKEN')
ID = os.getenv('ID')
PW = os.getenv('PW')
PWcert = os.getenv('PWcert')

def getToken():
    return TOKEN

def getId():
    return ID

def getPw():
    return PW

def getPwcert():
    return PWcert
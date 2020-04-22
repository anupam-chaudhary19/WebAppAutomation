from random import Random
import TestUtility.XLUtils
from TestUtility import XLUtils

path="C:/Users/Anupam/PycharmProjects/WebAppAutomation/TestUtility/login.xlsx"
rows= XLUtils.getRowCount(path, 'Sheet1')
class Config():
    URL ="http://newtours.demoaut.com/mercurysignon.php"
   # username = "automationscript"
   # password = "Zxcv@1234"
    usernameC= XLUtils.readData(path,"Sheet1",2,1)
    passwordC= XLUtils.readData(path,"Sheet1",2,2)



for r in range(2,rows+1):
    username= XLUtils.readData(path,"Sheet1",r,1)
    password = XLUtils.readData(path,"Sheet1",r,2)
    writedataVerified= XLUtils.writeData(path,"Sheet1",r,3,"Test passed")
    writedataFailed = XLUtils.writeData(path, "Sheet1", r, 3, "Test failed")
    # Registeration Page Data



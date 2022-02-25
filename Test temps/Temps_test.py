#coding= utf-8
#Programme utiliser pour faire des test sur le temps sur python

import time
import datetime
import os
if __name__=="__main__" :
    debut=time.time()
    time.sleep(2)
    fin = time.time()
    print(fin - debut)
    temps=time.localtime()
    print(temps.tm_year)
    print("Il est {}:{}:{} ".format(temps.tm_hour,temps.tm_min,temps.tm_sec))
    print(temps)
    print(time.localtime(debut))
    print(time.strftime("%A %d %B %Y %H:%M:%S"))
    print(datetime.datetime.now())
    print(datetime.date.today())








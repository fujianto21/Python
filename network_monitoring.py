import time
import psutil
import os
from os import system
from datetime import datetime
os.system('CLS')
system('mode con: cols=85 lines=3')

# Menu
print("Interface Mode:")
print("1. LAN")
print("2. Wi-Fi")
interfaceModeSelect = int(input("Pilih Interface: "))

interfaceMode = "Ethernet"  # Default
if interfaceModeSelect == 2:
    interfaceMode = "Wi-Fi"

def net_usage(inf, type):
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
    net_in_1 = net_stat.bytes_recv # DOWNLOAD
    net_out_1 = net_stat.bytes_sent # UPLOAD
    time.sleep(1)
    net_stat = psutil.net_io_counters(pernic=True, nowrap=True)[inf]
    net_in_2 = net_stat.bytes_recv
    net_out_2 = net_stat.bytes_sent

    net_in = round((net_in_2 - net_in_1) / 1024 / 1024, 2)
    net_out = round((net_out_2 - net_out_1) / 1024 / 1024, 2)

    if type == "PRINT":
        return 'IN : '+str(net_in)+ ' MB/s | OUT : '+str(net_out)+' MB/s'
    elif type == "COUNTER":
        return net_in + net_out

cnt = 1
total = 0
os.system('CLS')
while(True):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    total += net_usage(interfaceMode, 'COUNTER')
    if cnt == 1:
        print('Time : ' +current_time+ ' => '+net_usage(interfaceMode, 'PRINT')+' | CNT : '+str(round(total,2))+' MB        ')
    else:
        print('Time : ' +current_time+ ' => '+net_usage(interfaceMode, 'PRINT')+' | CNT : '+str(round(total,2))+' MB        ', end = "\r")
    cnt +=1
from datetime import date
import time
import serial
import datetime
import os
#
from mplot_class import mplot
import tstamp
import nowtime
from read2m5_class import read2m5
from fwrite_class import filewrite

fl=open("2log_log.txt",'a',encoding="utf-8")
s1=tstamp.timestamp()+": read2log.py started\n"
fl.write(s1)
#
path = './go_2log.txt' # flag file
#
fn='2L_'+nowtime.nowtime()+".csv"
f=open(fn,'w',encoding="utf-8")
# plot class
splot=mplot(20)
# initial time
start = time.time()
#
read2log=read2m5()
#
fwrite=filewrite()
read2log=read2m5()
while True:
  is_file = os.path.isfile(path) # check flag file
  if is_file: # file was found
    array=read2log.reads()
    fwrite.write(array)
# plot
    splot.plot(array)
  else: # flag not found
    s1=tstamp.timestamp()+": read2log.py stopped\n"
    fl.write(s1)
    fl.close()
    fwrite.close()
    exit()
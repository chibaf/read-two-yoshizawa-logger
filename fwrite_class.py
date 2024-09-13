class filewrite():

  def __init__(self):
    from datetime import date
    import time
    import datetime
    today = date.today()
    t=time.localtime()
    self.start = time.time()
    current_time=time.strftime("_H%H_M%M_S%S",t)
    fname= "2L_"+str(today)+current_time+".csv"
    self.f=open(fname,'w',encoding="utf-8")

  def write(self,array):
    import tstamp
    import time
    leng=len(array)
    temps=""
    for i in range(0,leng-1):
      temps=temps+str(array[i])+","
    temps=temps+str(array[leng-1])
    ttime=time.time()-self.start
    if ttime<0.001:
      ttime=0.0
    ttime=round(ttime,5)
    self.f.write(tstamp.timestamp()+","+str(ttime)+","+str(temps)+'\n')
  
  def close(self):
    self.f.close() 
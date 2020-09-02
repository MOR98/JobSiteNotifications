import requests
from bs4 import BeautifulSoup
import time
import datetime
from win10toast import ToastNotifier

#initial toast to show the script is online, this disappears after 6 seconds
toaster = ToastNotifier()
toaster.show_toast("Job Alert", "online", threaded=True,
                   icon_path=None, duration=6)  

urlA = "fill"
urlB = "fill"
historyP = "history.txt"
#this function takes in a url and returns the number of times our desired keywords are found 
#print is used to display or not the count
def countJobs(Print,url):
  res = requests.get(url)
  html_page = res.content
  soup = BeautifulSoup(html_page, 'html.parser')
  text = soup.find_all(text=True)
  text = str(text)
  keywords = {'graduate','Graduate','Technology','technology',
              'Associate','associate','Linux','linux','python',
              'Python','Systems','systems',' ai','AI',
              'Artifical Intelligence','Artifical intelligence',
              'artificial intelligence'}
  count = 0
  for i in keywords:
    c = text.count(str(i))
    count = count + c
    if(Print):print(i," :",c)
  if(Print):print("Total Count = ",count)
  return count

#Needs inital value to compare, using history file we can remember even if the script has not been running
history = open(str(historyP),'r')
lines = history.readlines()
CurrentCountS = int(lines[1])
CurrentCountI = int(lines[2])
history.close()


#While true, reassign new previous number, then check if this has changed, toast if needed then save to file
while(True):
  runtime = datetime.datetime.now()
  print(runtime)

  #Company A 
  PrevCountS = CurrentCountS
  CurrentCountS = countJobs(0,urlA)
 

  if(PrevCountS != CurrentCountS):
    print("NewJob!")
    #this notification remains in the windows notification center
    toaster.show_toast("Job Alert", "Jobs Updated by Company A", threaded=True,
                   icon_path=None, duration=None)  

  #Company B
  PrevCountI = CurrentCountI
  CurrentCountI = countJobs(0,urlB)

  if(PrevCountI != CurrentCountI):
    print("NewJob!")
    #this notification remains in the windows notification center
    toaster.show_toast("Job Alert", "Jobs Updated by Company B", threaded=True,
                   icon_path=None, duration=None)


  print('Company A keywords : '  ,CurrentCountS)
  print('Company B keywords : '  ,CurrentCountI)
  #open file for write and update
  history = open(str(historyP),'w')
  history.write(str(runtime)+ "\n")
  history.write(str(CurrentCountS)+ "\n")
  history.write(str(CurrentCountI))
  history.close()
  time.sleep(3600)

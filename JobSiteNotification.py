import requests
from bs4 import BeautifulSoup
import time
import datetime
from win10toast import ToastNotifier

#initial toast to show the script is online, this disappears after 6 seconds
toaster = ToastNotifier()
toaster.show_toast("Job Alert", "online", threaded=True,
                   icon_path=None, duration=6)  

urlA = "fillme"
urlB = "fillme"
historyPath = "fillme"
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
history = open('history txt file path','r')
lines = history.readlines()
CurrentCountS = int(lines[0])
CurrentCountI = int(lines[1])
history.close()


#While true, reassign new previous number, then check if this has changed, toast if needed then save to file
while(True):
  print('Company A keywords found last run: '  ,CurrentCountS)
  print('Company B keywords found last run: '  ,CurrentCountI)
  print(datetime.datetime.now())

  #open file to check previous value
  history = open(historyPath,'r')
  lines = history.readlines()
  #Company A 
  PrevCountS = CurrentCountS
  CurrentCountS = countJobs(0,urlA)
  lines[0] = str(CurrentCountS)

  if(PrevCountS != CurrentCountS):
    print("NewJob!")
    #this notification remains in the windows notification center
    toaster.show_toast("Job Alert", "Jobs Updated by Company A", threaded=True,
                   icon_path=None, duration=None)  

  #Intel Leixlip
  PrevCountI = CurrentCountI
  CurrentCountI = countJobs(0,urlB)
  lines[1] = str(CurrentCountI)

  if(PrevCountI != CurrentCountI):
    print("NewJob!")
    #this notification remains in the windows notification center
    toaster.show_toast("Job Alert", "Jobs Updated by Company B", threaded=True,
                   icon_path=None, duration=None)

  history.close()
  #open file for write and update
  history = open(historyPath,'w')
  history.write(str(CurrentCountS)+ "\n")
  history.write(str(CurrentCountI))
  history.close()
  time.sleep(60)

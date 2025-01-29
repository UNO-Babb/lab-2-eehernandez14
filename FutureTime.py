#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  hours = input("Enter hours: ")
  hours = int(hours)

  minutes = input("Enter Minutes: ")
  minutes = int(minutes)
  
  futureMinute = currentMinute + minutes
  extraHour = futureMinute // 60 
  futureHour = currentHour + hours + extraHour
  futureHour = futureHour % 24 
  futureMinute = futureMinute % 60
  print(futureHour)
  print(futureMinute)
  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  strHour = str(futureHour)
  strMinute = str(futureMinute)
  if futureMinute < 10:
    strMinute = str(futureMinute)
  print(strHour + ":" + strMinute)

if __name__ == '__main__':
  main()

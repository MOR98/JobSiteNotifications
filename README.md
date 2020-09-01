# JobSiteNotifications

This script is intended to check job sites for updates in various keywords, however it can be used for any similar purpose.
The script will provide a windows notification toast and remain in the notification centre when an update is detected.
You will need to update the urls for sites you wish to use, and edit the path to your history.txt file.

Running this task in the background would be best, as opposed to just running it constant with a delay.
To do this simply remove the loop, cut the delay and create a batch file and run that with windows scheduler (once a day then once an hour per day). 
This will mean I no longer need to even remember to run this task as windows will :)

You will need requests, bs4, time, datetime, win10toast libraries.

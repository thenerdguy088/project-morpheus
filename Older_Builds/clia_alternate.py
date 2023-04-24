import webbrowser as wb
import random
import datetime
import time
import sys
import math
def open_yt(link_00):
	wb.open_new("https://www.youtube.com/"+str(link_00))
def open_reddit(link_01):
	wb.open_new("https://www.reddit.com/r/"+str(link_01))
def sub(p,q):
	print(">>>",p-q,"is the difference between",p,"and",q)
def multiply(x,y):
	print(">>>",x*y,"is the product of",x,"and",y)
def div (m,n):
		if m > n:
			print(">>>",m/n,"is the quotient of",m,"and",n,)
		elif m < n:
			print(">>>",n/m,"is the quotient of",n,"and",m) 
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1	
def stopwatch(result):
	second = 0    
	minute = 0    
	hours = 0
	for h in range(0,result+1,1):
	   	print('>>> %d : %d : %d '%(hours,minute,second))
	   	time.sleep(1)
	   	second+=1
	   	if(second == 60):
	   	  	 	second = 0
	   	  	 	minute+=1
	   	if(minute == 60):
	   	  	 	minute = 0
	   	  	 	hour+=1
x="="*122
y="-"*122
h=0
td=["Truth","Dare"]
task_list=[]
add_num=[]
ytchannels=["YouTube Channels:",">>> Jeff Geerling - @JeffGeerling",">>> Mrwhosetheboss - @mrwhosetheboss",">>> LGR - @LGR"]
logindetails={"123":"1234"}
avcommands=["Commands Accepted By CL1A:","-"*122,"1. About CL1A:",">>> /checkpyver - Checks Python Version",">>> /showytchannels - Displays Youtube Channels",">>> /closeterminal - Closes The Program",">>> /commands - Display Commands supported by CL1A","-"*122,"2. CL1A Arithmetic Suite:",">>> /addnos - Adding Numbers",">>> /subnos - Subtracting 2 Numbers",">>> /multinos - Multiplying 2 Numbers",">>> /divnos - Dividing 2 Numbers",">>> /sqrt - Takes Square Root","-"*122,"3. CL1A Productivity Suite:",">>> /addtasks - Tasks which you would like to do",">>> /displaytasks - Displays the tasks that were added",">>> /deletetasks - Deletes the tasks that were added",">>> /stopwatch - Sets A Stopwatch",">>> /randomnopick - Picks A Random Number",">>> /settimer - Sets a timer","-"*122,"4. Miscellanous Features:",">>> /openytchannel - Opening a Youtube Channel",">>> /opensubreddit - Opening A Subreddit","-"*122,"5. CL1A Mini - Games:",">>> /coinflip - Flips A Coin",">>> /truthordare - Randomly Outputs Truth (Or) Dare for a certain number of players",">>> /diceroll - Simulates the roll of a dice for a certain number of players"]
print("\t\t   CL1A  -  The Ultimate Assistant")
print(">>> Say hello! to CL1A -  The Ultimate Assistant, a Python program that appears like a linux terminal and yet processes more like a personal assistant. CL1A stands for Command-Line Assistant.","\n"+str(x))
opt=True
while opt==True:
	command=input("<<< $ ")
   if(command=="/commands"):
   	for w in avcommands:
   		print(w)
    print(x)

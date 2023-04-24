import webbrowser as wb
import random
import datetime
import time
import sys
import wikipedia as wiki
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
avcommands=["Commands Accepted By CL1A:","-"*67,"1. About CL1A:",">>> /gethelp - Know What CL1A is",">>> /checkpyver - Checks Python Version",">>> /showytchannels - Displays Youtube Channels",">>> /closeterminal - Closes The Program",">>> /commands - Display Commands supported by CL1A","-"*67,"2. CL1A Arithmetic Suite:",">>> /addnos - Adding Numbers",">>> /subnos - Subtracting 2 Numbers",">>> /multinos - Multiplying 2 Numbers",">>> /divnos - Dividing 2 Numbers",">>> /sqrt - Takes Square Root","-"*67,"3. CL1A Productivity Suite:",">>> /addtasks - Tasks which you would like to do",">>> /displaytasks - Displays the tasks that were added",">>> /deletetasks - Deletes the tasks that were added",">>> /stopwatch - Sets A Stopwatch",">>> /randomnopick - Picks A Random Number",">>> /settimer - Sets a timer","-"*67,"4. Miscellanous Features:",">>> /openytchannel - Opening a Youtube Channel",">>> /opensubreddit - Opening A Subreddit","-"*67,"5. CL1A Wiki Suite:",">>> /searchwiki - Search Wikipedia and scrapes information for search results in wikipedia",">>> /showwiki - Scrapes Info from Wikipedia","-"*67,"6. CL1A Mini - Games:",">>> /coinflip - Flips A Coin",">>> /truthordare - Randomly Outputs Truth (Or) Dare for a certain number of players",">>> /diceroll - Simulates the roll of a dice for a certain number of players"]
h=0
td=["Truth","Dare"]
x="="*67
task_list=[]
add_num=[]
ytchannels=["YouTube Channels:",">>> Jeff Geerling - @JeffGeerling",">>> Mrwhosetheboss - @mrwhosetheboss",">>> LGR - @LGR"]
print("\t\t   CL1A  -  The Ultimate Assistant")
print(x)
opt="yes"
while opt=="yes":
	command=input("<<< $ ")
	if (command=="/gethelp"):
		print(">>> Say hello! to CL1A -  The Ultimate Assistant, a Python program that appears like a linux terminal and yet processes more like a personal assistant. CL1A stands for Command-Line Assistant.","\n"+str(x))
	elif(command=="/commands"):
		for w in avcommands:
			print(w)
		print(x)
	elif(command=="/showytchannels"):
		for k in ytchannels:
			print(k)
		print(x)
	elif (command=="/openytchannel"):
		yt_channel=input("<<< Enter Channel:")
		open_yt(yt_channel)
		print(">>> Opening Youtube - "+yt_channel.title())
		print(x)
	elif (command=="/addnos"):
		n=int(input("<<< Enter No. Of Elements:"))
		for u in range(n):
			element=int(input("<<< Enter Number:"))
			add_num.append(element)
		print(">>>",sum(add_num),"is the sum.")
		print(x)
	elif (command=="/subnos"):
		num1=int(input("<<< Enter Number 1:"))
		num2=int(input("<<< Enter Number 2:"))
		sub(num1,num2)
		print(x)
	elif (command=="/multinos"):
		num1=int(input("<<< Enter Number 1:"))
		num2=int(input("<<< Enter Number 2:"))
		multiply(num1,num2)
		print(x)
	elif (command=="/divnos"):
		num1=int(input("<<< Enter Number for Divisor:"))
		num2=int(input("<<< Enter Number For Dividend:"))
		div(num1,num2)
		print(x)
	elif (command=="/sqrt"):
		num=int(input("<<< Enter Number:"))
		print(">>>",math.sqrt(num),"is the square root for",num)
		print(x)
	elif (command=="/coinflip"):
		list1=["Head","Tail"]
		print(">>>",random.choice(list1))
		print(x)
	elif (command=="/truthordare"):
		n=int(input("Enter No.Of Players:"))
		for q in range(1,n+1):
				print("Player",q,":",random.choice(td))
		print(x)
	elif (command=="/diceroll"):
		n=int(input("Enter No.Of Players:"))
		for g in range(1,n+1):
				print("Player",g,":",random.randrange(1,7))
		print(x)
	elif (command=="/stopwatch"):
		m= int(input("<<< Enter MInutes:"))	
		s= int(input("<<< Enter Seconds:"))
		result=m*60+s    
		stopwatch(result)  
		print(x)   
	elif (command=="/addtasks"):
		n=int(input("<<< Enter Number Of Tasks:"))
		for f in range(n):
			task=input("<<< Enter Task:")
			task_list.append(task)
		print(x)
	elif (command=="/deletetasks"):
		task_1=input("<<< Enter Task:")
		task_list.remove(task_1)
		print(">>>",task_1,"has been removed successfully and has only",len(task_list),"tasks.")
		print(x)
	elif (command=="/displaytasks"):
		for t in task_list:
					h+=1
					print(">>>","Task",h,":",t)
		print(x)
	elif (command=="/searchwiki"):
		wiki_page=input("<<< Enter Article:")
		results=input("<<< Enter No.Of Results:")
		print(wiki.search(wiki_page,results))
		print(x)
	elif (command=="/showwiki"):
		wiki_page=input("<<< Enter Article:")
		sents=input("<<< Enter No.Of Sentences:")
		lang=input("<<< Enter Language (en/hi/ta):")
		wiki.set_lang(lang)
		print(wiki.summary(wiki_page,sents))
		print(x)
	elif(command=="/checkpyver"):
	    print(">>>","Python",sys.version)
	    print(x)
	elif (command=="/opensubreddit"):
		subreddit=input("<<< Enter Subreddit:")
		open_reddit(subreddit)
		print(">>> Opening r/"+str(subreddit),"Subreddit")
		print(x)
	elif (command=="/randomnopick"):
		n1=int(input("<<< Enter Start Value:"))
		n2=int(input("<<< Enter End Value:"))
		print(">>>",random.randrange(n1,n2),"is the random number generated from",n1,"to",n2)
		print(x)
	elif (command=="/settimer"):
		m= int(input("<<< Enter MInutes:"))
		s= int(input("<<< Enter Seconds:"))
		result=m*60+s
		countdown(result)
		print(x)
	elif (command=="/closeterminal"):
		print(">>> Sending CL1A Process to KILL Signal"+str("."*10),"\n>>> CL1A has been terminated"+str("."*10))
		print(x)
		exit()	
	else:
		print("This is not a valid command.","\nType /commands to know what CL1A can do.")
		print(x)
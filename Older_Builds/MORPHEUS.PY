import webbrowser as wb
import sys
import math
import random
import datetime 
import wikipedia as wiki
import pyttsx3
from random_word import RandomWords
h=0
point=0
opt_00='Y'
x='='*109
D='\t'*6
task_list=[]
ht=random.choice(['Head','Tail']) 
add_num=[]
avcommands=['Commands Accepted By MORPHEUS:','-'*100,'1. About MORPHEUS:','>>> /gethelp - Know What MORPHEUS is','>>> /checkpyver - Checks Python Version','>>> /showytchannels - Displays Youtube Channels','>>> /closeterminal - Closes The Program','>>> /commands - Display Commands supported by MORPHEUS','-'*100,'2. MORPHEUS Arithmetic Suite:','>>> /addnos - Adding Numbers','>>> /subnos - Subtracting 2 Numbers','>>> /multinos - Multiplying 2 Numbers','>>> /divnos - Dividing 2 Numbers','>>> /sqrt - Takes Square Root','-'*100,'3. MORPHEUS Productivity Suite:','>>> /addtasks - Tasks which you would like to do','>>> /displaytasks - Displays the tasks that were added','>>> /deletetasks - Deletes the tasks that were added','>>> /randomnopick - Picks A Random Number','-'*100,'4. Miscellanous Features:','>>> /openytchannel - Opening a Youtube Channel','>>> /translate - Translates the text typed,from one language to another','/showytchannels - Displays Youtube Channels','-'*100,'5. MORPHEUS Wiki Suite:','>>> /searchwiki - Search Wikipedia and scrapes information for search results in wikipedia','>>> /showwiki - Scrapes Info from Wikipedia','-'*100,'6. MORPHEUS Mini - Games:','>>> /coinflip - Flips A Coin','>>> /truthordare - Randomly Outputs Truth (Or) Dare for a certain number of players','>>> /diceroll - Simulates the roll of a dice for a certain number of players','>>> /scramble - Scrambling Words']
avcommands_1=['Commands Accepted By MORPHEUS','Number 1 About MORPHEUS:','/gethelp is used for knowing What MORPHEUS is','/checkpyver is used for Checking Python Version','/closeterminal is used for Closing The Program','/commands is used for displaying commands supported by MORPHEUS','Number 2 MORPHEUS Arithmetic Suite','/addnos is used for Adding Numbers','/subnos is used for Subtracting 2 Numbers','/multinos is used for Multiplying 2 Numbers','/divnos is used for Dividing 2 Numbers','/sqrt is used for Takes Square Root','Number 3 MORPHEUS Productivity Suite','/addtasks is used for adding tasks which you would like to do','/displaytasks is used for displaying the tasks that were added','/deletetasks is used for Deleting the tasks that were added','/randomnopick is used for Picking A Random Number','Number 4 Miscellanous Features','>>> /translate is used for Translating the text typed,from one language to another','Number 5 MORPHEUS Wiki Suite','/searchwiki is used for Searching Wikipedia and scrapes information for search results in wikipedia','/showwiki is used for scraping Info from Wikipedia','Number 6 MORPHEUS Mini Games','/coinflip is used for Flips A Coin','/truthordare is used for Randomly Outputting Truth (Or) Dare for a certain number of players','/diceroll is used for Simulating the roll of a dice for a certain number of players','scramble is used for Scrambling Words']
def speakaloud(str):
	engine = pyttsx3.init()
	engine.setProperty('rate',150)
	engine.say(str)
	engine.runAndWait()
def translate(fl,sl,str1):
	wb.open_new('https://translate.google.co.in/?+sl='+str(fl)+'&tl='+str(sl)+'&text='+str(str1)+'&op=translate')
	speakaloud('Opening Google Translate')
	print('>>> Opening Google Translate...')
def sub(p,q):
	subprod=p-q
	speakaloud(str((subprod))+'is the difference between'+str(p)+'and'+str(q))
	print('>>>',subprod,'is the difference between',p,'and',q)
def multiply(x,y):
	multiprod=x*y
	speakaloud(str(multiprod)+'is the product of'+str(x)+'and'+str(y))
	print('>>>',x*y,'is the product of',x,'and',y)
def div (m,n):
	if m > n:
		divprod1=int(m/n)
		speakaloud(str(divprod1)+'is the quotient of'+str(m)+'and'+str(n))
		print('>>>',m/n,'is the quotient of',m,'and',n)
	else:
		speakaloud(n/m,'is the quotient of',n,'and',m)
		print('>>>',n/m,'is the quotient of',n,'and',m) 
print(str(D)+'MORPHEUS')
print(x)
opt=True
while opt==True:
	command=input('>>> $ ')
	if (command=='/gethelp'):
		speakaloud(">>> MORPHEUS, a program developed with In The Matrix's 7th Cycle, has arrived to take you down the rabbit hole of programming to see how far it goes.")
		print(">>> MORPHEUS, a program developed with In The Matrix's 7th Cycle, has arrived to take you down the rabbit hole of programming to see how far it goes",'\n'+str(x))
	elif(command=='/commands'):
		for w in avcommands:
			print('>>>',w)
		speakaloud(avcommands_1)
		print(x)
	elif (command=='/addnos'):
		speakaloud('Enter Number Of Elements')
		n=int(input('>>> Enter Number Of Elements: '))
		for u in range(n):
			speakaloud('Enter Number')
			element=int(input('>>> Enter Number: '))
			add_num.append(element)
		speakaloud(str(sum(add_num))+'is the sum.')
		print('>>>',sum(add_num),'is the sum.')
		print(x)
	elif (command=='/subnos'):
		speakaloud('Enter Number 1')
		num1=int(input('>>> Enter Number 1: '))
		speakaloud('Enter Number 2')
		num2=int(input('>>> Enter Number 2: '))
		sub(num1,num2)
		print(x)
	elif (command=='/multinos'):
		speakaloud('Enter Number 1')
		num1=int(input('>>> Enter Number 1: '))
		speakaloud('Enter Number 2')
		num2=int(input('>>> Enter Number 2: '))
		multiply(num1,num2)
		print(x)
	elif (command=='/divnos'):
		speakaloud('Enter Number 1')
		num1=int(input('>>> Enter Number 1: '))
		speakaloud('Enter Number 2')
		num2=int(input('>>> Enter Number 2: '))
		div(num1,num2)
		print(x)
	elif (command=='/sqrt'):
		speakaloud('Enter Number')
		num=int(input('>>> Enter Number: '))
		sqrt=math.sqrt(num)
		print('>>>',sqrt,'is the square root for',num)
		speakaloud(str(sqrt)+'is the square root for'+str(num))
		print(x)	
	elif (command=='/coinflip'):
		speakaloud(ht)
		print(ht)
		print('>>> You Either Die A Hero, Or You Live Long Enough To See Yourself Become The Villain — Harvey Dent in The Dark Knight (2008)')
		speakaloud('You Either Die A Hero, Or You Live Long Enough To See Yourself Become The Villain — Harvey Dent in The Dark Knight (2008)')
		print(x)
	elif (command=='/truthordare'):
		speakaloud('Enter Number Of Players')
		n=int(input('>>> Enter Number Of Players: '))
		for q in range(1,n+1):
			f=random.choice(['Truth','Dare'])
			speakaloud('Player'+str(q)+':'++str(f))
			print('Player',q,':',f)
		print(x)
	elif (command=='/diceroll'):
		speakaloud('Enter Number Of Players')
		n=int(input('>>> Enter Number Of Players: '))
		for g in range(1,n+1):
			z=random.randrange(1,7)
			print('Player',g,':',z)
			speakaloud('Player'++str(g)+':'+str(z))
		print(x)  
		print(x)   
	elif (command=='/addtasks'):
		speakaloud('Enter Number Of Tasks')
		n=int(input('>>> Enter Number Of Tasks: '))
		for f in range(n):
			speakaloud('Enter Task')
			task=input('>>> Enter Task: ')
			task_list.append(task)
		print('>>>',n,'tasks has been successfullly added to the list.')
		speakaloud(str(n)+'tasks has been successfullly added to the list')
		print(x)
	elif (command=='/deletetasks'):
		speakaloud('Enter Task')
		task_1=input('>>> Enter Task: ')
		if task_1 not in task_list:
			speakaloud(str(task_1)+'does not exists in the list.')
			print('>>>',task_1,'does not exists in the list.')
		else:
			task_list.remove(task_1)
			speakaloud(str(task_1)+'has been removed successfully and has only'+str(len(task_list))+'tasks.')
			print('>>>',task_1,'has been removed successfully and has only',len(task_list),'tasks.')
			print(x)
	elif (command=='/displaytasks'):
		for t in task_list:
			h+=1
			print('>>>','Task',h,':',t)
		speakaloud('Task'+str(h)+'is'+str(t))
		print(x)
	elif (command=='/searchwiki'):
		speakaloud('Enter Article')
		wiki_page=input('>>> Enter Article: ')
		speakaloud('Enter Number Of Results')
		results=input('>>> Enter Number Of Results: ')
		SEARCHWIKI=wiki.search(wiki_page,results)
		for wiki_0 in SEARCHWIKI:
			print('>>>',wiki_0)
		speakaloud(wiki.search(wiki_page,results))
		print(x)
	elif (command=='/showwiki'):
		speakaloud('Enter Article')
		wiki_page=input('>>> Enter Article: ')
		speakaloud('Enter Number Of Sentences')
		sents=input('>>> Enter Number Of Sentences: ')
		print(wiki.summary(wiki_page,sents))
		speakaloud(wiki.summary(wiki_page,sents))
		print(x)
	elif (command=='/translate'):
		speakaloud('Enter Text For Translation')
		txt=input('>>> Enter Text For Translation: ')
		speakaloud('Enter First Language')
		L_1=input('>>> Enter First Language: ')
		speakaloud('Enter Second Language')
		L_2=input('>>> Enter Second Language: ')
		translate(L_1,L_2,txt)
		print(x)
	elif (command=='/scramble'):
		speakaloud('If you get your answers correct, your points will be incremented')
		print('>>> If you get your answers correct, your points will be incremented.')
		speakaloud('If you get your answers wrong, your points will be decremented')
		print('>>> If you get your answers wrong, your points will be decremented.')
		speakaloud('Enter Number Of Words For Unscrambling')
		n=int(input('>>> Enter Number Of Words (For Unscrambling): '))
		for f in range(n):
			R=RandomWords()
			scramble=R.get_random_word()
			scramble1=scramble.upper()[::-1]
			speakaloud(scramble1)
			print('>>>',scramble1)
			wrd=input('>>> Enter Unscrambled Word:')
			if wrd==scramble:
				point+=1
				print('>>> Points:',point)
				print('>>> You WON! :)')
			else:
				point-=1
				print('>>> Points:',point)
				print('>>> You LOST! :(')
		print(x)
	elif(command=='/checkpyver'):
		print('>>>','Morpheus Runs On',' Python',sys.version)
		speakaloud('Morpheus Runs On'+' Python'+str(sys.version))
		print(x)
	elif (command=='/randomnopick'):
		speakaloud('Enter Start Value')
		n1=int(input('>>> Enter Start Value: '))
		speakaloud('Enter End Value')
		n2=int(input('>>> Enter End Value: '))
		randrange_00=random.randrange(n1,n2)
		speakaloud(str(randrange_00)+'is the random number generated from'+str(n1)+'to'+str(n2))
		print('>>>',randrange_00,'is the random number generated from',n1,'to',n2)
		print(x)
	elif (command=='/closeterminal'):
		speakaloud('You have escaped from the real world'+"Be Beware The Analyst is looking out for you as you've awakened yourself from The Matrix"+"Good Luck Out There")
		print('>>> You have escaped from the real world.',"\n>>> Be Beware The Analyst is looking out for you as you've awakened yourself from The Matrix.","\n>>> Good Luck Out There!")
		print(x)
		exit()
	else:
		print('This is not a valid command.','\nType /commands to know what MORPHEUS can help you with.')
		speakaloud('This is not a valid command'+'Type /commands to know what MORPHEUS can help you with')
		print(x)

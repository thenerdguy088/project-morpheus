#importing modules 
from webbrowser import open_new - #opens web browser w/ link as parameter
from sys import version - #used to check python  
from math import sqrt 
from random import choice,randrange - #generates random outcomes 
import wikipedia as wiki - #scraping wikipedia articles
import pyttsx3 - #speaks when text passed as argument
from random_word import RandomWords - #generates random words
from googlesearch import search - #scrapes links

#assigning_variables
h=0 - #tasks iternation no.
point=0 - #scramble points iternation no.
x='='*100 - #seperation repetition
D='\t'*6 - tab sapce repetition
task_list=[]
ht=choice(['Head','Tail']) - #generates random outcomes for heads and tails
add_num=[] - #adds element to list for addition of numbers
search_results=[] - #appends scraped links 
opt=True - #while condition initialization
#defining_functions
def speak(str):
	engine = pyttsx3.init()
	engine.setProperty('rate',150)
	engine.say(str)
	engine.runAndWait()

def translate(fl,sl,str1):
	open_new('https://translate.google.co.in/?+sl='+str(fl)+'&tl='+str(sl)+'&text='+str(str1)+'&op=translate')
	speak('Opening Google Translate')
	print('>>> Opening Google Translate...')

def sub(p,q):
	subprod=p-q
	speak(str((subprod))+'is the difference between'+str(p)+'and'+str(q))
	print('>>>',subprod,'is the difference between',p,'and',q)

def multiply(x,y):
	multiprod=x*y
	speak(str(multiprod)+'is the product of'+str(x)+'and'+str(y))
	print('>>>',x*y,'is the product of',x,'and',y)

def div (m,n):
	if m > n:
		divprod1=int(m/n)
		speak(str(divprod1)+'is the quotient of'+str(m)+'and'+str(n))
		print('>>>',m/n,'is the quotient of',m,'and',n)
	else:
		speak(n/m,'is the quotient of',n,'and',m)
		print('>>>',n/m,'is the quotient of',n,'and',m)

#main_program 
print(str(D)+'MORPHEUS')
print(x)
while opt==True:
	command=input('>>> $ ')

 if ('who are you' in command):
		speak("MORPHEUS, a program developed with In The Matrix's 7th Cycle by Neo, has arrived to take you down the rabbit hole of programming to see how far it goes.")
		print(">>> MORPHEUS, a program developed with In The Matrix's 7th Cycle, has arrived to take you down the rabbit hole of programming to see how far it goes",'\n'+str(x))
	elif (command=='add numbers'):
		speak('Enter Number Of Elements')
		n=int(input('<<< Enter Number Of Elements: '))
		for u in range(n):
			speak('Enter Number')
			element=int(input('<<< Enter Number: '))
			add_num.append(element)
		speak(str(sum(add_num))+'is the sum.')
		print('>>>',sum(add_num),'is the sum.')
		print(x)

	elif ('subract 2 numbers'in command):
		speak('Enter Number 1')
		num1=int(input('<<< Enter Number 1: '))
		speak('Enter Number 2')
		num2=int(input('<<< Enter Number 2: '))
		sub(num1,num2)
		print(x)

	elif ('multiply 2 numbers'in command):
		speak('Enter Number 1')
		num1=int(input('<<< Enter Number 1: '))
		speak('Enter Number 2')
		num2=int(input('<<< Enter Number 2: '))
		multiply(num1,num2)
		print(x)

	elif ('divide 2 numbers'in command):
		speak('Enter Number 1')
		num1=int(input('<<< Enter Number 1: '))
		speak('Enter Number 2')
		num2=int(input('<<< Enter Number 2: '))
		div(num1,num2)
		print(x)

	elif ('take square root'in command):
		speak('Enter Number')
		num=int(input('<<< Enter Number: '))
		sqrt_00=sqrt(num)
		print('>>>',sqrt_00,'is the square root for',num)
		speak(str(sqrt)+'is the square root for'+str(num))
		print(x)

	elif ('flip a coin'in command):
		speak(ht)
		print(ht)
		print('>>> You Either Die A Hero, Or You Live Long Enough To See Yourself Become The Villain — Harvey Dent in The Dark Knight (2008)')
		speak('You Either Die A Hero, Or You Live Long Enough To See Yourself Become The Villain — Harvey Dent in The Dark Knight (2008)')
		print(x)

	elif ('play truth or dare'in command):
		speak('Enter Number Of Players')
		n=int(input('<<< Enter Number Of Players: '))
		for q in range(1,n+1):
			f=choice(['Truth','Dare'])
			speak('Player'+str(q)+':'+str(f))
			print('Player',q,':',f)
		print(x)

	elif ('roll a dice'in command):
		speak('Enter Number Of Players')
		n=int(input('<<< Enter Number Of Players: '))
		for g in range(1,n+1):
			z=randrange(1,7)
			print('Player',g,':',z)
			speak('Player'++str(g)+':'+str(z))
		print(x)

	elif ('add tasks'in command):
		speak('Enter Number Of Tasks')
		n=int(input('<<< Enter Number Of Tasks: '))
		for f in range(n):
			speak('Enter Task')
			task=input('<<< Enter Task: ')
			task_list.append(task)
		print('>>>',n,'tasks has been successfullly added to the list.')
		speak(str(n)+'tasks has been successfullly added to the list')
		print(x)

	elif ('delete tasks'in command):
		speak('Enter Task')
		task_1=input('<<< Enter Task: ')
		if task_1 not in task_list:
			speak(str(task_1)+'does not exists in the list.')
			print('>>>',task_1,'does not exists in the list.')
		else:
			task_list.remove(task_1)
			speak(str(task_1)+'has been removed successfully and has only'+str(len(task_list))+'tasks.')
			print('>>>',task_1,'has been removed successfully and has only',len(task_list),'tasks.')
			print(x)

	elif ('show tasks'in command):
		for t in task_list:
			h+=1
			print('>>>','Task',h,':',t)
		speak('Task'+str(h)+'is'+str(t))
		print(x)

	elif ('search for wikipedia articles'in command):
		speak('Enter Article')
		wiki_page=input('<<< Enter Article: ')
		speak('Enter Number Of Results')
		results=input('<<< Enter Number Of Results: ')
		SEARCHWIKI=wiki.search(wiki_page,results)
		for wiki_0 in SEARCHWIKI:
			print('>>>',wiki_0)
		speak(wiki_0)
		print(x)

	elif ('show wikipedia article'in command):
		speak('Enter Article')
		wiki_page=input('<<< Enter Article: ')
		speak('Enter Number Of Sentences')
		sents=input('<<< Enter Number Of Sentences: ')
		print(wiki.summary(wiki_page,sents))
		speak(wiki.summary(wiki_page,sents))
		print(x)

	elif ('search web' in command):
		speak('Enter Search String')
		search_00=input('<<< Enter Search String: ')
		speak('Enter Number Of Results')
		numresults=int(input('<<< Enter Number Of Results: '))
		for A in search(search_00,num_results=numresults):
			search_results.append(A)
		print('>>> Opening',len(search_results)-1,'Tabs for',search_00)
		speak('Opening'+str(len(search_results)-1)+'Tabs for'+str(search_00))
		for B in search_results:
			open_new(B)
		search_results.clear()
		print(x)

	elif 'write notes' in command:
		f=open('morpheusnotes.txt','a')
		speak('Enter Notes')
		notes=input('<<< Enter Notes:')
		f.write(notes)

	elif 'open notes' in command:
		f = open('morpheusnotes.txt',"r")
		speak(f.read())
		print(f.read())

	elif ('translate text' in command):
		speak('Enter Text For Translation')
		txt=input('<<< Enter Text For Translation: ')
		speak('Enter First Language')
		L_1=input('<<< Enter First Language: ')
		speak('Enter Second Language')
		L_2=input('<<< Enter Second Language: ')
		translate(L_1,L_2,txt)
		print(x)

	elif ('open scramble game' in command):
		speak('If you get your answers correct, your points will be incremented')
		print('>>> If you get your answers correct, your points will be incremented.')
		speak('If you get your answers wrong, your points will be decremented')
		print('>>> If you get your answers wrong, your points will be decremented.')
		speak('Enter Number Of Words For Unscrambling')
		n=int(input('>>> Enter Number Of Words (For Unscrambling): '))
		for f in range(n):
			R=RandomWords()
			scramble=R.get_random_word()
			scramble1=scramble.upper()[::-1]
			speak(scramble1)
			print('>>>',scramble1)
			speak('Enter Unscrambled Word')
			wrd=input('<<< Enter Unscrambled Word:')
			if wrd==scramble:
				point+=1
				speak('Points'+str(point))
				print('>>> Points:',point)
				speak('You WON')
				print('>>> You WON! :)')
			else:
				point-=1
				speak('Points'+str(point))
				print('>>> Points:',point)
				speak('You LOST')
				print('>>> You LOST! :(')
		print(x)

	elif('check python version' in command):
		print('>>>','Morpheus Runs On '+'Python',version)
		speak('Morpheus Runs On'+' Python'+str(version))
		print(x)

	elif('pick a random number') in command:
		speak('Enter Start Value')
		n1=int(input('<<< Enter Start Value: '))
		speak('Enter End Value')
		n2=int(input('<<< Enter End Value: '))
		randrange_00=randrange(n1,n2)
		speak(str(randrange_00)+'is the random number generated from'+str(n1)+'to'+str(n2))
		print('>>>',randrange_00,'is the random number generated from',n1,'to',n2)
		print(x)

	elif ('close the program' in command):
		speak('You have escaped from the real world'+"Be Beware The Analyst is looking out for you as you've awakened yourself from The Matrix"+"Good Luck Out There")
		print('>>> You have escaped from the real world.',"\n>>> Be Beware The Analyst is looking out for you as you've awakened yourself from The Matrix.","\n>>> Good Luck Out There!")
		print(x)
		exit()

	else:
		print('This is not a valid command.','\nType /commands to know what MORPHEUS can help you with.')
		speak('This is not a valid command'+'Type /commands to know what MORPHEUS can help you with')
		print(x)

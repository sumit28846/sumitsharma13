import os
import pyttsx3
print("Hi I am Leo")
while True:
	print("Chat with me with your requirements: " , end='')
	p = input()
	if (("run" in p) or ("execute" in p) or ("open" in p) or ("want" in p) or ("get" in p)) and (("notepad" in p) or ("editor" in p)):
		os.system("notepad")
	elif (("run" in p) or ("open")) and ("youtube" in p):
		os.system("start chrome www.youtube.com")
	elif (("run" in p) or ("open")) and ("camera" in p):
		os.system("start microsoft.windows.camera:")
	elif (("run" in p) or ("open")) and ("cmd" in p):
		os.system("start cmd")
	elif (("run" in p) or ("open")) and ("fb" in p):
		os.system("start chrome www.facebook.com")
	elif (("run" in p) or ("open")) and ("twitter" in p):
		os.system("start chrome www.twitter.com")
	elif (("run" in p) or ("open")) and ("pmi" in p):
		os.system("start chrome pmi.org.in")
	elif (("run" in p) or ("open")) and ("linkedin" in p):
		os.system("start chrome www.linkedin.com")
	elif (("run" in p) or ("open")) and ("gmail" in p):
		os.system("start chrome www.gmail.com")
	elif (("run" in p) or ("open")) and ("quora" in p):
		os.system("start chrome www.quora.com")
	elif (("run" in p) or ("open")) and ("darsa" in p):
		os.system("start chrome www.darsa.ai")
	elif (("run" in p) or ("execute" in p) or ("open" in p) or ("want" in p) or ("get" in p)) and ("chrome" in p):
		os.system("chrome")
	elif (("run" in p) or ("execute" in p) or ("open" in p) or ("want" in p) or ("get" in p))  and ("media player" in p):
		os.system("wmplayer")
	elif (("run" in p) or ("execute" in p) or ("open" in p) or ("want" in p) or ("get" in p))  and ("winrar" in p):
		os.system("WinRaR")
	elif (("run" in p) or ("execute" in p) or ("open" in p) or ("want" in p) or ("get" in p))  and (("excel" in p) or ("sheet" in p)):
		os.system("Excel")
	elif (("run" in p) or ("execute" in p) or ("open" in p) or ("want" in p) or ("get" in p))  and ("anydesk" in p):
		os.system("Anydesk")
	elif (("run" in p) or ("execute" in p) or ("open" in p) or ("want" in p) or ("get" in p))  and ("access" in p):
		os.system("MSACCESS")
	elif (("run" in p) or ("execute" in p) or ("open" in p) or ("want" in p) or ("get" in p))  and ("note" in p):
		os.system("ONENOTE")
	elif (("run" in p) or ("execute" in p) or ("open" in p) or ("want" in p) or ("get" in p))  and (("powerpoint" in p) or ("ppt" in p)):
		os.system("POWERPNT")
	elif (("run" in p) or ("execute" in p) or ("open" in p) or ("want" in p) or ("get" in p))  and ("word" in p):
		os.system("WINWORD")
	elif ("hi" in p) or ("hello" in p):
		print("Hello")
	elif ("good morning" in p) or ("morning" in p):
		print("Very Good Morning")
	elif ("good afternoon" in p):
		print("Good Afternoon")
	elif ("good evening" in p):
		print("Good evening")
	elif ("how are you" in p):
		print("I am doing well")
	elif ("time" in p):
		os.system("time")
	elif ("date" in p):
		os.system("date")
	elif ("exit" in p) or ("quite" in p) or ("bye" in p):
		break
	if ("dont" in p) or ("no" in p) or ("never" in p) or ("dont" in p):
		print("Okay")
	else:
		print("Sorry the command is not executable")
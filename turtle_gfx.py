# coding=utf-8

import sys
import turtle
import speech_recognition as sr
import file_reader as fr
import executor

bob = turtle.Turtle()
executor = executor.Executor(bob, 100, 90)
r = sr.Recognizer()	
lang = 'en-us'
reader = fr.FileReader()
phrases = reader.load(lang)
phrase = ""

while not executor.is_terminated():
	with sr.Microphone() as source:   
		print "adjusting"
		r.adjust_for_ambient_noise(source)
		print "listening..."
		audio = r.listen(source)
		print "recognizing..."
	try:
		said = r.recognize_google(audio, language = lang, show_all=False).lower()
		print("You said:" + said)
		for (phrase, cmd) in phrases.iteritems():
			print "comparing " + said + " == " + phrase
			if(said == phrase):
				print "match: ", cmd
				executor.execute(cmd, 1)
				break
				
	except LookupError:               
		print("Could not understand audio")
	except sr.UnknownValueError:
		print("Recognition failed")
	except:
		print("Unexpected error:", sys.exc_info()[0])
		raise

print "finished"
turtle.done()

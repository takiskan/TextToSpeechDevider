from gtts import gTTS #Needed to generate text to speach file
from playsound import playsound #Needed to play the sound
language = 'en'#Here can change the language output
cost = 3000#Here you can change the cost


def main():
	Money = input("Enter money: ")
	print (Money)
	Purchasable = str(int(int(Money)/cost))
	print ("You can buy " + Purchasable)
	#return main()
	file = "sound" + str(Money) + ".mp3"#Creating the sound files title
	tts = gTTS(str(Purchasable),language)#Caching up the sound file
	try :
		tts.save(file)
	except:
		playsound(file)
	finally:
		playsound(file)
	return main()
main()
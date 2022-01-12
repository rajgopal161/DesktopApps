import pyttsx3

converter = pyttsx3.init()

# voices = converter.getProperty('voices')
  
# for voice in voices:
#     # to get the info. about various voices in our PC 
#     print("Voice:")
#     print("ID: %s" %voice.id)
#     print("Name: %s" %voice.name)
#     print("Age: %s" %voice.age)
#     print("Gender: %s" %voice.gender)
#     print("Languages Known: %s" %voice.languages)
    

converter.setProperty('rate', 150)
# Set volume 0-1
converter.setProperty('volume', 0.7)

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
  
# Use female voice
converter.setProperty('voice', voice_id)


  
# Queue the entered text 
# There will be a pause between
# each one like a pause in 
# a sentence
filee = open('test.txt', 'r').read()

#converter.say(filee)

converter.save_to_file(filee  , 'speech.mp3')

  
# Empties the say() queue
# Program will not continue
# until all speech is done talking
converter.runAndWait()





  


import speech_recognition as sr
r = sr.Recognizer()
print('Start')
with sr.Microphone() as source:
    while True:
        print('Listening')
        audio = r.listen(source)
        try:
            print('You said : '+r.recognize_google(audio, None,'th'))
        except:
            print('Error!')
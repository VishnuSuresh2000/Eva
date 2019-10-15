import speech_recognition as sr

microphone = sr.Microphone()
recognizer = sr.Recognizer()


with microphone as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    print("Say Something")
    # listens for the user's input
    audio = recognizer .listen(source)
    print(audio)

    try:
        text = recognizer.recognize_google(audio)
        print("you said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
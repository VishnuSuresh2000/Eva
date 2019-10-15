import speech_recognition as sr
import nltk
la=[]

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
        tok = nltk.word_tokenize(text=text)
        print(tok)
        print(nltk.pos_tag(tokens=tok))
        try:
            from googlesearch import search
        except ImportError:
            print("error")

        for j in search(text, tld='co.in', num=10, stop=10):
            la.append(j)
        print(la)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
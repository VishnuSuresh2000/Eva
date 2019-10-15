import speech_recognition as sr
r=sr.Recognizer()
mic_list=sr.Microphone.list_microphone_names()

for j,microphone_name in enumerate(mic_list):
    print(microphone_name)
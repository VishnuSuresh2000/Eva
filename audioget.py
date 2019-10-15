import speech_recognition as sr
r=sr.Recognizer()
mic_list=sr.Microphone.list_microphone_names()

mic_name="Microphone (2- Realtek High Definition Audio)"

for j,microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = j
with sr.Microphone(device_index = device_id,sample_rate=48000,chunk_size=1024) as source:
    r.adjust_for_ambient_noise(source)
    print("Say Something")
    # listens for the user's input
    audio = r.listen(source)
    print(audio)

    try:
        text = r.recognize_google(audio)
        print("you said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
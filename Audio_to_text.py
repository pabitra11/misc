import speech_recognition as sr

r = sr.Recognizer()


#for i, microphone_name in enumerate(mic_list):
#    if microphone_name == mic_name:
 #       device_id = i
#    print(device_id )

with sr.Microphone() as source:
    # wait for a second to let the recognizer adjust the
    # energy threshold based on the surrounding noise level
    r.adjust_for_ambient_noise(source)
    print("Say Something")
    # listens for the user's input
    audio = r.listen(source)
    print("listen Something")
    try:
        print("intry")
        text = r.recognize_google(audio)
        print("you said: " .format(text))

        # error occurs when google could not understand what was said

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")



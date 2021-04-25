import speech_recognition as sr
import pyttsx3
import genes
import time


engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
r = sr.Recognizer()

responses =[]
mutation = ''

def get_voice():
    # obtain audio from the microphone
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        output = r.recognize_sphinx(audio)
        responses.append(output)
        print("output is: " + output)
        print(responses[-1])

def say(input):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
    engine.say(input)
    engine.runAndWait()
    time.sleep(2)



def main():
    # obtain audio from the microphone
    say("Have you ever had known genes mapped for known mutations")

    say("what ethnicity do you identify as?")

    say("how many generations back have you traced your families gene history?")

    say("has either parent been diagnosed with cancer?")

    say("has any grandparent been diagnosed with cancer?")

    say("What was the diagnosis and at what age?")

    time.sleep(1)

    say('generating recommendation. please wait')

    say('I have determined your disposition to be not strong. Have a nice day')





    say("say")
    if(responses[-1] == 'yes'):
        say("what known gene mutation?")
        get_voice()
        mutation = responses[-1]
        mutation = genes.classify(mutation)
        print(mutation)

    else:
        mutation = None



    try:
        print("Tim thinks you said " + responses[-1])
        say("Tim thinks you said " + responses[-1])

    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))










if __name__ == '__main__':
    main()
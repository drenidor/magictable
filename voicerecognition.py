import time
import speech_recognition as sr
import constants as c
import tablecontrol as tc
import led


def recognize_speech_from_mic(recognizer, microphone):
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        print ("~ Lade Welt - Bitte warten ~")
        recognizer.adjust_for_ambient_noise(source)
        print ("<<< Bitte jetzt sprechen >>>")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='de-DE')
    except sr.RequestError:
        # API was unreachable or unresponsive
        text = ("API nicht erreichbar")
    except sr.UnknownValueError:
        # speech was unintelligible
        text = ("Spracheingabe nicht verstanden")
    return text


if __name__ == "__main__":
	# create recognizer and mic isinstance
    # setup gpio pins and calibrate table
    print ("~ Initialisiere ... ~")
    tc.gpio_setup()
    tc.table_calibrate()
    while True:
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        text = recognize_speech_from_mic(recognizer, microphone)
        text = text.lower()
        if (text) == c.MERLIN[0]:
            print ("~~~ " + text + " ~~~ Merlin / sitzen")
            tc.table_sitposition(c.MERLIN[1])
        elif (text) == c.MERLIN[2]:
            print ("~~~ " + text + " ~~~ Merlin / stehen")
            tc.table_standposition(c.MERLIN[3])
        elif (text) == c.JAN[0]:
            print ("~~~ " + text + " ~~~ Jan / sitzen")
            tc.table_sitposition(c.JAN[1])
        elif (text) == c.JAN[2]:
            print ("~~~ " + text + " ~~~ Jan / stehen")
            tc.table_standposition(c.JAN[3])
        elif (text) == c.CELINA[0]:
            print ("~~~ " + text + " ~~~ Celina / sitzen")
            tc.table_sitposition(c.CELINA[1])
        elif (text) == c.CELINA[2]:
            print ("~~~ " + text + " ~~~ Celina / stehen")
            tc.table_standposition(c.CELINA[3])
        elif (text) == c.OLLI[0]:
            print ("~~~ " + text + " ~~~ Olli / sitzen")
            tc.table_sitposition(c.OLLI[1])
        elif (text) == c.OLLI[2]:
            print ("~~~ " + text + " ~~~ Olli / stehen")
            tc.table_standposition(c.OLLI[3])
        elif text == c.PROGRAM_EXIT:
            print ("~~~ " + text + " ~~~ Programm beendet")
            tc.gpio_cleanup()
            break
        else:
            print ("~ " + text + " - Bitte Eingabe wiederholen ~")

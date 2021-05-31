import pyglet
import speech_recognition as sr


def start_listening():
    print("Start listening...")
    file = pyglet.resource.media("audio/wet.mp3")
    file.play()


def end_listening():
    print("End listening.")
    file = pyglet.resource.media("audio/suppressed.mp3")
    file.play()


def init_speech():
    r = sr.Recognizer()
    start_listening()

    with sr.Microphone() as source:
        print("Say something")
        command_audio = r.listen(source)

    end_listening()

    command_string = ""

    try:
        command_string = r.recognize_google(command_audio)
    except LookupError:
        print("Couldn't understand you, bro.")

    print("Your command:")
    print(command_string)


init_speech()

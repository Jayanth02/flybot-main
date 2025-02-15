
import speech_recognition as sr
from threading import Event


def secondary_listen_for_stop(stop_event):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for 'stop' command...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        while not stop_event.is_set():
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)
                response = recognizer.recognize_google(audio).lower()
                print(f"Heard: {response}")
                if "stop" in response:
                    print("Stop command detected!")
                    stop_event.set()
                    break
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Error with speech recognition: {e}")
                break
            except sr.WaitTimeoutError:
                pass

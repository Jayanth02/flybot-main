
import speech_recognition as sr

def listen_for_response(timeout=5, phrase_time_limit=10):
	recognizer = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		try:
			recognizer.adjust_for_ambient_noise(source, duration=0.5)
			audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
			print("Processing...")
			response = recognizer.recognize_google(audio)
			print(f"You said: {response}")
			return response.lower()
		except sr.UnknownValueError:
			print("Sorry, I didn't catch that.")
		except sr.RequestError as e:
			print(f"Recognition service error: {e}")
		except sr.WaitTimeoutError:
			print("Listening timed out.")
	return None
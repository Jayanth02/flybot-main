from auth.login import send_login_data
from audio.tts import send_text_to_speech
from audio.playback import play_audio_in_memory
from chat.conversation import conversation_loop
from threading import Event
import io
import os
import pygame
from utility.suppress_logs import suppress_pygame_logs, suppress_stdout_stderr



# Set environment variable to suppress Pygame output
os.environ["SDL_VIDEODRIVER"] = "dummy"

# Initialize pygame mixer with suppress_stdout_stderr
with suppress_stdout_stderr():
    pygame.mixer.init()


def main():
    email = "strikin123@gmail.com"
    password = "Superchat@1"

    auth_token = send_login_data(email, password)
    if auth_token:
        greeting_message = f"Hello, I'm ready to chat with you. Say 'stop' whenever you want to end."
        print(greeting_message)

        audio_data = send_text_to_speech(auth_token, greeting_message)
        if audio_data:
            stop_event = Event()
            play_audio_in_memory(audio_data, stop_event)

        conversation_loop(email, auth_token)
    else:
        print("Login failed. Exiting...")

if __name__ == "__main__":
    main()

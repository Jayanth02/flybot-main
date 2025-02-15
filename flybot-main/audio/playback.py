import io
import pygame
import time
import keyboard
from threading import Event

def play_audio_in_memory(audio_data, stop_event):
    if not audio_data:
        print("No audio data to play.")
        return

    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        pygame.mixer.music.load(io.BytesIO(audio_data))
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            if stop_event.is_set():
                pygame.mixer.music.stop()
                break
            time.sleep(0.1)
    except Exception as e:
        print(f"Error playing audio: {e}")
        pygame.mixer.quit()
        pygame.mixer.init()

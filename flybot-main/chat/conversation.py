from audio.tts import send_text_to_speech
from audio.playback import play_audio_in_memory
from chat.bot import send_chat_message
from speech.recognition import listen_for_response
from speech.stop_listening import secondary_listen_for_stop
from threading import Thread, Event


def conversation_loop(email, auth_token):
    print("Starting conversation...")

    stop_event = Event()
    while True:
        user_response = listen_for_response()  # Listen for user input after starting conversation

        if user_response == "hey stop":
            print("Stopping the conversation.")
            stop_message = "Bot successfully stopped."
            audio_data = send_text_to_speech(auth_token, stop_message)
            if audio_data:
                stop_event = Event()
                play_audio_in_memory(audio_data, stop_event)
            break

        if user_response:
            print(f"Processing user input: {user_response}")
            # Call /chat endpoint for bot's response
            bot_response = send_chat_message(auth_token, user_response)

            if bot_response:
                print(f"Bot: {bot_response}")  # Print text response

                # Call /voice endpoint for audio response
                audio_data = send_text_to_speech(auth_token, bot_response)

                if audio_data:
                    # Play audio response
                    stop_event = Event()
                    audio_thread = Thread(target=play_audio_in_memory, args=(audio_data, stop_event))
                    listen_thread = Thread(target=secondary_listen_for_stop, args=(stop_event,))
                    audio_thread.start()
                    listen_thread.start()
                    audio_thread.join()
                    stop_event.set()
                else:
                    print("Failed to generate audio response.")
            else:
                print("Failed to get a response from the bot.")
        else:
            print("No valid input detected. Listening again.")
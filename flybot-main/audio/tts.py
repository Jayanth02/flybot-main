from utility.session import create_session
from requests.exceptions import RequestException
from config.settings import VOICE_ENDPOINT, DEFAULT_TIMEOUT

def send_text_to_speech(auth_token, text):
    session = create_session()
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    data = {"user_input": text, "target_lang": "en"}

    try:
        response = session.post(VOICE_ENDPOINT, headers=headers, json=data, timeout=DEFAULT_TIMEOUT)
        if response.status_code == 200:
            return response.content
    except RequestException as e:
        print(f"TTS Error: {e}")
    return None

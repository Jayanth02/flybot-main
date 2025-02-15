
from requests.exceptions import RequestException
from utility.session import create_session
from config.settings import CHAT_ENDPOINT, DEFAULT_TIMEOUT

def send_chat_message(auth_token, message):
    session = create_session()
    headers = {"Authorization": f"Bearer {auth_token}"}
    data = {"user_input": message,"response_length":"short", "target_lang": "en"}

    try:
        response = session.post(CHAT_ENDPOINT, headers=headers, json=data, timeout=20)
        if response.status_code == 200:
            return response.json().get("response", "")
    except RequestException as e:
        print(f"Chat Error: {e}")
    return None

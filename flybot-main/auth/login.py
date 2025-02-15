from requests.exceptions import RequestException
from utility.session import create_session
from config.settings import LOGIN_ENDPOINT, DEFAULT_TIMEOUT


def send_login_data(email, password):
    session = create_session()
    
    data = {
        "email": email,
        "password": password
    }
    try:
        response = session.post(LOGIN_ENDPOINT, json=data, timeout=15)
        if response.status_code == 200:
            auth_token = response.json().get("token")
            if auth_token:
                print(f"Login Success! Welcome {email}")
                return auth_token
            else:
                print("Login Failed: Token not found in the response")
        else:
            print(f"Login Failed: Server returned status code {response.status_code}")
    except RequestException as e:
        print(f"Login Error: {e}")
    return None
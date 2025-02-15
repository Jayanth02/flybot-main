# Base URL for the API
BASE_URL = "https://suitable-jolly-falcon.ngrok-free.app"

# API Endpoints
LOGIN_ENDPOINT = f"{BASE_URL}/login"      # Login endpoint
VOICE_ENDPOINT = f"{BASE_URL}/voice"     # Text-to-speech endpoint
CHAT_ENDPOINT = f"{BASE_URL}/chat"       # Chatbot interaction endpoint

# Request Configuration
DEFAULT_TIMEOUT = 15                     # Default timeout for API requests in seconds
RETRY_COUNT = 3                          # Number of retries for failed requests
BACKOFF_FACTOR = 0.5                     # Backoff factor for retries
STATUS_FORCELIST = [500, 502, 503, 504]  # HTTP status codes to trigger retry

# Audio Configuration (if applicable)
AUDIO_FORMATS = ["mp3", "ogg", "wav"]    # Supported audio formats for playback

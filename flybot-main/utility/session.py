from requests.adapters import HTTPAdapter
import requests
from urllib3.util.retry import Retry
from config.settings import RETRY_COUNT, BACKOFF_FACTOR, STATUS_FORCELIST



def create_session():
    session = requests.Session()
    retry_strategy = Retry(
        total=RETRY_COUNT,
        backoff_factor=BACKOFF_FACTOR,
        status_forcelist=STATUS_FORCELIST
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session
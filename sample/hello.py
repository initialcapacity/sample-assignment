import requests


def message(message_url:str) -> str | None:
    response = requests.get(message_url)
    if response.status_code != 200:
        return None

    return f"Goodbye {response.text}"

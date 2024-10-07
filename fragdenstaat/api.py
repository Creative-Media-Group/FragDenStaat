import requests


class API:
    def __init__(self) -> None:
        r = requests.get(url="https://fragdenstaat.de/api/v1/")
        print(r.text)


if __name__ == "__main__":
    API()

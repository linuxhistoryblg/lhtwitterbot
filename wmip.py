# Get external IP address from:
# https://www.ipify.org/
# Dan 2021.01.09
from requests import get
from sys import exit as exit


def get_ip():
    # URL = https://www.ipify.org/
    url = 'https://api.ipify.org/'

    # Fetch HTML
    try:
        page = get(url)
    except Exception as err:
        return f'Unable to Reach {url} | {err}'

    if page.status_code == 200:
        return page.content.decode()
    else:
        return f'Unable to Reach {url}'


if __name__ == "__main__":
    print(get_ip())

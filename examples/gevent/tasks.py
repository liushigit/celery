import requests

from celery import task


@task(ignore_result=True)
def urlopen(url):
    print('Opening: {0}'.format(url))
    try:
        _response = requests.get(url)
    except Exception as exc:
        print('Exception for {0}: {1!r}'.format(url, exc))
        return url, 0
    print('Done with: {0}'.format(url))
    return url, 1

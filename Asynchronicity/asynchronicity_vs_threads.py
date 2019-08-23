# 1. Reading data from an API
# 2. Using one thread for each request
# 3. Repeating same things with asynchronicity
# 4. Repeating same things without threads
# 5. Comparing execution times

from threading import Thread
import urllib.request
import urllib.parse
from urllib.error import HTTPError, URLError
import json
import time
import asyncio

api_endpoint_url = 'https://restcountries.eu/rest/v2/name/'


async def get_info(country):
    url = api_endpoint_url + str(country)

    try:
        data = urllib.request.urlopen(url)
    except HTTPError:
        print(f'Sorry! Could not retrieve anything on {country}')
        return None
    except URLError as e:
        print('Failed to reach server!')
        print(f'Reason: {e.reason}')
        return None
    else:
        data = data.read().decode()
        # print(f'Retrieved data on {country}')
        return data


def display_info(country):
    info = get_info(country)
    if info != None:
        x = json.loads(info)
        y = x[0]
        for key, value in y.items():
            print(f'{key}: {value}')


# Request example
#
# >>> display_info('USA')
# name: United States of America
# topLevelDomain: ['.us']
# alpha2Code: US
# ...
#
# >>> display_info('dfgg')
# Sorry! Could not retrieve anything on dfgg

# get_info retrieves JSON file


def without_threads_200_times(country='USA'):
    count = 0
    for repeat in range(200):
        get_info(country)
        count += 1
    print(f'Requested information {count} times.')


def with_threads_200_times(country='USA'):
    count = 0
    # thread_list = []
    for thread in range(200):
        thread = Thread(target=get_info, args=('USA',))
        thread.start()
        count += 1
    print(f'Requested information {count} times.')

async def with_async_200_times(country='USA'):
    count = 0
    for repeat in range(200):
        await get_info(country)
        count += 1
    print(f'Requested information {count} times.')


start = time.time()
without_threads_200_times()
print('Execution time without threads: ', round(time.time()-start, 3), 'seconds.')

start = time.time()
with_threads_200_times()
print('Execution time with threads: ', round(time.time()-start, 3), 'seconds.')

start = time.time()
asyncio.run(with_async_200_times())
print('Execution time with async: ', round(time.time()-start, 3), 'seconds.')

# Traditional way
# Requested information 200 times.
# Execution time without threads:  83.332 seconds.
# 
# Threads
# Requested information 200 times.
# Execution time with threads:  1.46 seconds.
# 
# Asynchronicity
# Requested information 200 times.
# Execution time with async:  74.972 seconds.
# 
# Asynchronicity + multithreading (fastest)
# * def get_info    ---->   async def get_info 
# Requested information 200 times.
# Execution time with threads:  0.049 seconds.
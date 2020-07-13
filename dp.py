#!/usr/bin/python
import sys
import requests
import json
from jsonpath_rw import jsonpath, parse
import jsonpath_rw_ext as jp


def result_all(data):
    title = jp.match('data.children[*].data.title', data)
    url = jp.match('data.children[*].data.url', data)
    selftext = jp.match('data.children[*].data.selftext', data)
    for titles, urls, selftexts in zip(title, url, selftext):
        print(titles)
        print(urls)
        print(selftexts.encode('utf-8'))


def result_some(data):
    title = jp.match('data.children[*].data.title[?(@.Challenge)]', data)
    url = jp.match('data.children[*].data.url', data)
    selftext = jp.match('data.children[*].data.selftext', data)
    for titles, urls, selftexts in zip(title, url, selftext):
        print(titles)
        print(urls)
        print(selftexts.encode('utf-8'))


arguments = len(sys.argv)
print(sys.argv)
payload = ''
if arguments >= 4:
    print('usage: dp [challenge_number/difficulty/all] [difficulty]')
elif arguments == 0:
    print('usage: dp [challenge_number/difficulty/all] [difficulty]')
else:
    arggs = sys.argv
    link = 'https://www.reddit.com/r/dailyprogrammer/search.json'
    if arggs[1] == 'all':
        payload = {'q': 'Challenge', 'restrict_sr': 'true', 'sort': 'new'}
        bring = 'all'
    elif arggs[1].isdigit():
        if arguments == 2:
            payload = {'q': 'Challenge #' + arggs[1], 'restrict_sr': 'true'}
        elif arggs[2].lower() == 'easy' or arggs[2].lower() == 'intermediate' or arggs[2].lower() == 'hard' and arguments == 3:
            payload = {'q': 'Challenge #' + arggs[1] + '[' + arggs[1] + ']', 'restrict_sr': 'true'}
        else:
            print('usage: dp [challenge_number/difficulty/all] [difficulty]')
            exit()
    elif arggs[1].lower() == 'easy' or arggs[1].lower() == 'intermediate' or arggs[1].lower() == 'hard' and arguments == 2:
        payload = {'q': '[' + arggs[1] + ']', 'restrict_sr': 'true'}
    else:
        print('usage: dp [challenge_number/difficulty/all] [difficulty]')
        exit()
reddit = requests.get(link, params=payload,  headers={'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'})
response = json.loads(reddit.text)

if bring == 'all':
    result_all(response)




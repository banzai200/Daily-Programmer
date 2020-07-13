#!/usr/bin/python
import sys
import requests
import json
import jsonpath_rw_ext as jp


def result_all(data):
        title = jp.match('data.children[*].data.title', data)
        url = jp.match('data.children[*].data.url', data)
        selftext = jp.match('data.children[*].data.selftext', data)
        for titles, urls, selftexts in zip(title, url, selftext):
            print(titles + '\n')
            print(selftexts.encode('utf-8') + '\n')
            print(urls)


def main():
    arguments = len(sys.argv)
    payload = ''
    if arguments >= 4:
        print('usage: dailyprogrammer [challenge_number/difficulty/all] [difficulty]')
        exit()
    elif arguments == 1:
        print('usage: dailyprogrammer [challenge_number/difficulty/all] [difficulty]')
        exit()
    else:
        arggs = sys.argv
        link = 'https://www.reddit.com/r/dailyprogrammer/search.json'
        if arggs[1] == 'all':
            payload = {'q': 'Challenge', 'restrict_sr': 'true', 'sort': 'new', 'limit': '100'}
        elif arggs[1].isdigit():
            if arguments == 2:
                payload = {'q': 'title:#' + arggs[1], 'restrict_sr': 'true', }
            elif arggs[2].lower() == 'easy' or arggs[2].lower() == 'intermediate' or arggs[2].lower() == 'hard' and arguments == 3:
                payload = {'q': 'title:#' + arggs[1] + '+[' + arggs[2] + ']', 'restrict_sr': 'true'}
            else:
                print('usage: dailyprogrammer [challenge_number/difficulty/all] [difficulty]')
                exit()
        elif arggs[1].lower() == 'easy' or arggs[1].lower() == 'intermediate' or arggs[1].lower() == 'hard' and arguments == 2:
            payload = {'q': 'title:' + arggs[1] + '', 'restrict_sr': 'true', 'sort': 'new', 'limit': '100'}
        else:
            print('usage: dailyprogrammer [challenge_number/difficulty/all] [difficulty]')
            exit()
    reddit = requests.get(link, params=payload,  headers={'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'})
    print(reddit.request.url)
    response = json.loads(reddit.text)
    result_all(response)




# !/usr/bin/env python3
import sys
import json
import datetime
import time

def formatJson(str):
    str = str.replace('][', ',')
    str = str.replace('}{', '},{')
    str = str.replace(']{', '],[{')
    str = str.replace('}[', '}],{')
    return str
    
def separateJson(str):
    str = str.replace('][', ']\n[')
    str = str.replace('}{', '}\n{')
    str = str.replace(']{', ']\n[{')
    str = str.replace('}[', '}\n[{')
    return str

for line in sys.stdin:
    newLine = separateJson(line)
    for line in newLine.splitlines():
        # remove leading and trailing whitespace
        line = line.strip()
        # parse the input we got from mapper.py
        file = json.loads(formatJson(line))
        # check if item is only one item or list of items
        if type(file) is dict:
            file = [file]
        for item in file:
            specific_resource_type = None
            if 'crawler_target' in item:
                specific_resource_type = item['crawler_target']['specific_resource_type']
            if 'object' in item:
                object = item['object']
                if 'social_media' in object:
                    social_media = object['social_media']
                    if social_media == 'instagram':
                        specific_resource_type = 'instagram'
            if specific_resource_type == 'youtube':
                snippet = item['snippet']
                # check if comment is a reply
                if 'topLevelComment' in snippet:
                    snippet = snippet['topLevelComment']['snippet']
                # get date from snippet.publishedAt
                date = snippet['publishedAt'][0:10]
                print(f'{specific_resource_type}\t{date}')
            elif specific_resource_type == 'twitter':
                date = item['created_at']
                # format date
                date = datetime.datetime.strptime(date, '%a %b %d %H:%M:%S %z %Y').strftime('%Y-%m-%d')
                print(f'{specific_resource_type}\t{date}')
            elif specific_resource_type == 'instagram':
                date = item['created_time']
                # format date from timestamp
                date = datetime.datetime.fromtimestamp(int(date)).strftime('%Y-%m-%d')
                print(f'{specific_resource_type}\t{date}')
            elif specific_resource_type == 'facebook':
                postDate = item['created_time'][0:10]
                comments = item['comments']['data']
                print(f'{specific_resource_type}\t{postDate}')
                for comment in comments:
                    date = comment['created_time'][0:10]
                    print(f'{specific_resource_type}\t{date}')
            elif 'GraphImages' in item:
                graphImages = item['GraphImages']
                for image in graphImages:
                    date = image['taken_at_timestamp']
                    # format date from timestamp
                    date = datetime.datetime.fromtimestamp(int(date)).strftime('%Y-%m-%d')
                    print(f'instagram\t{date}')
                    comments = image['comments']['data']
                    for comment in comments:
                        date = comment['created_at']
                        # format date
                        date = datetime.datetime.fromtimestamp(int(date)).strftime('%Y-%m-%d')
                        print(f'instagram\t{date}')



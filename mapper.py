# /usr/bin/env python3
import sys
import json
import datetime
import time

with open('../raw_json/facebook_post_1641972260556_y83jramqg4.json', 'r', encoding='utf8') as f:
    file = json.load(f)

# for line in sys.stdin:
print(json.dumps(file, indent=4, sort_keys=True))
for item in file:
    specific_resource_type = item['crawler_target']['specific_resource_type']
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


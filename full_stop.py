from urllib.request import urlopen
import json
import time

"""
This file will download json files provided by pushshift api calls
"""
after = 1
before = 0

for day in range(0, 25555):	
    # Example 'thot' query
	#query_url = "https://api.pushshift.io/reddit/search/comment/?q=%thot&after=" + \
    #                str(after) + "d&before=" + str(before) + "d&sort=asc&size=100000"
	#query_url = "https://api.pushshift.io/reddit/search/comment/?q=%22full%20stop%22&after=1d&before=0d&sort=asc&size=100000"
	
    query_url = "https://api.pushshift.io/reddit/search/comment/?q=%22full%20stop%22&after=" + \
                str(after) + "d&before=" + str(before) + "d&sort=asc&size=100000"
    r = urlopen(query_url)
    raw_json = json.load(r)

    mem_file_name = "day_of_record_" + str(day) +".json"
    print(mem_file_name)
    with open( mem_file_name,'w') as storage_file:
        json.dump(raw_json, storage_file)
    storage_file.close()

    after += 1
    before += 1

print('DONE')

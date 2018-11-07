from urllib.request import urlopen
import json
import time

# November 1, 0:0:0 = 1541055600
# October 31, 2018 0:0:0 = 1540969200
# One day = 86400
# One week = 604800
#query_url = "https://api.pushshift.io/reddit/search/comment/?q=%22full%20stop%22&after=1d&before=0d&sort=asc&size=100000"


f = open("thot_count_record.txt", "w")

after = 1
before = 0

for x in range(0, 1459):
    #query_url = "https://api.pushshift.io/reddit/search/comment/?q=%22full%20stop%22&after=" + \
    #            str(after) + "d&before=" + str(before) + "d&sort=asc&size=100000"
    query_url = "https://api.pushshift.io/reddit/search/comment/?q=%thot&after=" + \
                    str(after) + "d&before=" + str(before) + "d&sort=asc&size=100000"
    r = urlopen(query_url)

    raw_json = json.load(r)
    f.write( str( len(raw_json['data']) )+ '\n' )

    after += 1
    before += 1



f.close()
print('DONE')








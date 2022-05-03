import requests
import json
import time

import pandas as pd
from args import args
from myerror import MyError

def datatracker():
    with requests.Session() as session:

        resp = session.post(args['url_login'], data=args['site_cred'])
        if resp.status_code != 200:
            raise MyError(resp, "POST fail on login")

        # this query picks up all data from the tle_latest class, change query in args.py when necessary
        resp = session.get(args['query'])
        if resp.status_code != 200:
            print(resp)
            raise MyError(resp, "GET fail on request for Starlink satellites")

        # use the json package to break the json formatted response text into a Python structure (a list of dictionaries)
        apidata = json.loads(resp.text)
        print(f"Total of {len(apidata)} objects...")
        objtlist = []

        maxs = 1
        for item in apidata:
            print(f"Scanning Object = {item['NORAD_CAT_ID']}-{item['OBJECT_NAME']}...")
            # save each object in a list
            objtlist.append(item)

            """
            #In case the amount of data is too large, due to the rate limit reasons
            maxs += 1
            if maxs > 200:
                print("Snoozing for 60 secs for rate limit reasons (max 20/min and 200/hr)...")
                time.sleep(60)
                maxs = 1
            """

        # output
        df_data = pd.DataFrame(objtlist)
        #print(df_data)
        df_data.to_csv(args['output_csv'])

        print("Completed session")
        session.close()


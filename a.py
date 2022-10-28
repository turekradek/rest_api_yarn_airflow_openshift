import time
import json
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth

ts = int(time.time()) * 1000
URL_TS = ts - (60 * 60 * 1000)
    
url = 'https://mapr-web.advantagedp.org:20202/ws/v1/cluster/apps?user=ingest_pipeline-s&finalStatus=SUCCEEDED&startedTimeBegin=1568491200000'
url2 = 'https://mapr-web.advantagedp.org:20202/ws/v1/cluster/apps?user=session_checker-s&finalStatus=SUCCEEDED&finishedTimeBegin=1568491200000'
auth = HTTPBasicAuth('ingest_pipeline-s', '1Rt.d5WssojT.2')
auth2 = HTTPBasicAuth('session_checker-s', 'ohydn6-20DfJq_ZW')
proxies = {'http': 'socks5h://192.168.67.2:1081', 'https': 'socks5h://192.168.67.2:1081'}
requests.urllib3.disable_warnings()
response = requests.get(url, auth=auth, proxies=proxies, verify=False)
response_json = response.json()
response2 = requests.get(url2, auth=auth2, proxies=proxies, verify=False)
response2_json = response2.json()
# response_json
# response2_json ## wyswietla zmienne 
# names, ids, trackingUrls, diagnostics, queues = zip(
#      *(
#          (
#             item["name"],
#             item["id"],
#             item["trackingUrl"],
#             item["diagnostics"],
#             item["queue"],
#         )
#         for item in response_json["apps"]["app"]
#     )
# )
# df = pd.DataFrame(
#     {
#         "Names": names,
#         "Ids": ids,
#         "TrackingUrls": trackingUrls,
#         "Diagnostics": diagnostics,
#         "Queues": queues,
#     }
# )
# df
url3 = 'https://api.devops.advantagedp.org:6443/version'
auth3 = HTTPBasicAuth('devops_apps_pol-s', 'k1.oandvaL3Q7ydJ')
response3 = requests.get(url3, auth=auth3, proxies=proxies, verify=False)
response3_json = response3.json()
import configuracja
endpoint_op = 'https://api.devops.advantagedp.org:6443/api/v1/namespaces/data-pipeline-monitoring-prod/pods'
auth4 = HTTPBasicAuth(configuracja.user, configuracja.password)
import subprocess
import os 
import sys
# token_ = subprocess.Popen("TOKEN=$(oc whoami -t)", stdout=subprocess.PIPE, shell=True )
# t = token_.communicate()
# print( os.environ['TOKEN'])
token_ = configuracja.token #sys.argv[1]
endp= subprocess.Popen('ENDPOINT=$(oc config current-context | cut -d/ -f2 | tr - .)', stdout=subprocess.PIPE, shell=True )
# NAMESPACE=$(oc config current-context | cut -d/ -f1)
polecenie = subprocess.Popen(f"""curl -k \
    -H 'Authorization: Bearer {token_}' \
    -H 'Accept: application/json' \
    'https://api.devops.advantagedp.org:6443/api/v1/namespaces/boson-team/pods' | jq .""", stdout=subprocess.PIPE, shell=True )
a = polecenie.communicate()
# print( token_ )
print( a )
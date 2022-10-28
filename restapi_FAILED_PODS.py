# import time
# import json
# import pandas as pd
# import requests
# from requests.auth import HTTPBasicAuth

# ts = int(time.time()) * 1000
# URL_TS = ts - (60 * 60 * 1000)
    
# url = 'https://mapr-web.advantagedp.org:20202/ws/v1/cluster/apps?user=ingest_pipeline-s&finalStatus=SUCCEEDED&startedTimeBegin=1568491200000'
# url2 = 'https://mapr-web.advantagedp.org:20202/ws/v1/cluster/apps?user=session_checker-s&finalStatus=SUCCEEDED&finishedTimeBegin=1568491200000'
# auth = HTTPBasicAuth('ingest_pipeline-s', '1Rt.d5WssojT.2')
# auth2 = HTTPBasicAuth('session_checker-s', 'ohydn6-20DfJq_ZW')
# proxies = {'http': 'socks5h://192.168.67.2:1081', 'https': 'socks5h://192.168.67.2:1081'}
# requests.urllib3.disable_warnings()
# response = requests.get(url, auth=auth, proxies=proxies, verify=False)
# response_json = response.json()
# response2 = requests.get(url2, auth=auth2, proxies=proxies, verify=False)
# response2_json = response2.json()
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
# url3 = 'https://api.devops.advantagedp.org:6443/version'
# auth3 = HTTPBasicAuth('devops_apps_pol-s', 'k1.oandvaL3Q7ydJ')
# response3 = requests.get(url3, auth=auth3, proxies=proxies, verify=False)
# response3_json = response3.json()
# response3_json
# import configuracja
# endpoint_op = 'https://api.devops.advantagedp.org:6443/api/v1/namespaces/data-pipeline-monitoring-prod/pods'
# auth4 = HTTPBasicAuth(configuracja.user, configuracja.password)
# res4 = requests.get(endpoint_op, auth=auth4 , proxies=proxies, verify=False)
# res4_json = res4.json()
# import subprocess
# import os 
# import sys
# token_ = subprocess.Popen("TOKEN=$(oc whoami -t)", stdout=subprocess.PIPE, shell=True )
# t = token_.communicate()
# print( os.environ['TOKEN'])
# token_ = configuracja.TOKEN #sys.argv[1]
# token_ = 'sha256~5SD3AoYhafphTB1L5hl4ii4JnjHFkkT9HTJDRJiv_3g'
# TOKEN = 'sha256~5SD3AoYhafphTB1L5hl4ii4JnjHFkkT9HTJDRJiv_3g'
# endp= subprocess.Popen('ENDPOINT=$(oc config current-context | cut -d/ -f2 | tr - .)', stdout=subprocess.PIPE, shell=True )
# # NAMESPACE=$(oc config current-context | cut -d/ -f1)
# polecenie = subprocess.Popen(f"""curl -k \
#     -H 'Authorization: Bearer {token_}' \
#     -H 'Accept: application/json' \
#     'https://api.devops.advantagedp.org:6443/api/v1/namespaces/boson-team/pods' | jq .""", stdout=subprocess.PIPE, shell=True )
# a = polecenie.communicate()
# res4 = requests.get(endpoint_op, auth=auth4 , proxies=proxies, verify=False)
# res4_json = res4.json()
# res4_json
# TOKEN=$(oc whoami -t)
# ENDPOINT=$(oc config current-context | cut -d/ -f2 | tr - .)
# NAMESPACE=$(oc config current-context | cut -d/ -f1)


######################################
from sqlite3 import connect

# from datetime import datetime
import json
from webbrowser import get

from requests.auth import HTTPBasicAuth
import configuration_class
import subprocess
import os 
import sys
import logging
from io import StringIO

import datetime as dt
import time

import pandas as pd
import requests
from requests.auth import HTTPBasicAuth

# import airflow
# from airflow.models import DAG
# from airflow.operators.dummy_operator import DummyOperator
# from airflow.operators.email_operator import EmailOperator
# from airflow.operators.python_operator import BranchPythonOperator, PythonOperator
# from airflow.utils.email import send_email
# from airflow_dags_devops_apps_pol.config import devops_airflow_common_conf
# from airflow_dags_devops_apps_pol.devops_monitoring_utilities import msteams_on_task_failure_callback
# from airflow.hooks.base_hook import BaseHook
# from airflow.operators.dagrun_operator import TriggerDagRunOperator
# from airflow_dags_devops_apps_pol.devops_teams_utilities import trigger_teams

# proxies = {'http': 'socks5h://192.168.67.2:1081', 'https': 'socks5h://192.168.67.2:1081'}
# TOKEN = 'sha256~v5Q-2D07QAoYfxDsqwCKqJcJI8vJ6XZNLZoBH_wGCd4'
# ENDPOINT = r'https://api.devops.advantagedp.org:6443'
# API_PART = 'api/v1'
# NAMESPACES = 'namespaces'
# NAMESPACE = 'data-pipeline-monitoring-prod'
# datapipeline = 'data-pipeline-monitoring-prod'
# PODS = 'pods'
# boson = 'boson-team'
# datapipeline = 'data-pipeline-monitoring-prod'
# url6 = '/'.join([ENDPOINT,API_PART,NAMESPACES,NAMESPACE,PODS])
# print( url6)
# headers = {'Accept': 'application/json',"Authorization": "Bearer "+ TOKEN}
# res = requests.get(url6, headers=headers, proxies=proxies , verify=False)
# res_j = res.json()
# KURWA TOKEN WYSTARCZY GLABIE :)
# boson = 'boson-team'
# res_j
# def check_login():
#     try:
        
#         os.system('oc whoami')
#         # os.system('oc login https://api.devops.advantagedp.org:6443 -u devops_apps_pol-s -p k1.oandvaL3Q7ydJ')
        
#     except Exception:
#         logging.exception('BlaD LOGOWANIA')
#         # logging.exception('WIADOMOSC JAK BLAD ')


# proxies = {'http': 'socks5h://192.168.67.2:1081', 'https': 'socks5h://192.168.67.2:1081'}
# # LOGOWNAIE I TOKEN 
# # os.system('oc login https://api.devops.advantagedp.org:6443 -u devops_apps_pol-s -p k1.oandvaL3Q7ydJ')
# TOKEN = os.system('oc whoami -t')
# print( TOKEN )
# TOKEN = 'sha256~B30xUNWj8jbfLg01Ug77Xm5N4YgY6cLvoa5XbYYO5gs'
# headers = {'Accept': 'application/json',"Authorization": "Bearer "+ TOKEN}
# ENDPOINT = r'https://api.devops.advantagedp.org:6443'
# API_PART = 'api/v1'
# NAMESPACES = 'namespaces'
# NAMESPACE = 'data-pipeline-monitoring-prod'
# import configuration_class 

monitoring_failde_pods = configuration_class.OpenShiftPodsMonitoring()
monitoring_failed_pods_data_pipeline = monitoring_failde_pods.MONITORING_FAILED_PODS_DATA_PIPELINE_MONITORING_PROD_DICT
print( ' ------------------------ ', monitoring_failed_pods_data_pipeline )
def make_endpoint(NAMESPACE, ENDPOINT=r'https://api.devops.advantagedp.org:6443', API_PART='api/v1', NAMESPACES='namespaces', PODS='pods'):
    return '/'.join([ENDPOINT,API_PART,NAMESPACES,NAMESPACE,PODS])

def login_dict():
    # TOKEN = 'sha256~wfTI7SW-TKVccd4f_ZEMz2GIWmx2T3l0mOcGjx3CNR0'
    print( ' JESTEM Z  login_dict :) ')
    os.system('oc login https://api.devops.advantagedp.org:6443 -u devops_apps_pol-s -p k1.oandvaL3Q7ydJ')
    # print( 'po logowaniu ')
    TOKEN = subprocess.run(['oc', 'whoami', '-t'], stdout=subprocess.PIPE, stderr=subprocess.PIPE) #stdout=subprocess.PIPE) 
    
    # print( " \t \t  os.system('TOKEN=$(oc whoami -t)')   ")
    print( '   Ma byc token    ',TOKEN , '      TOKEN__stdout___', TOKEN.stdout.decode())
    # print( TOKEN , '      TOKEN__stderr____', TOKEN.stderr.decode())
    
    TOKEN = TOKEN.stdout.decode().strip()

    # TOKEN = 'sha256~xC8bk65186mHixEUXGfYbjvs7rr3kmW10jh_ErKK_BI'

    
    dictionary = {
        "proxies" : {'http': 'socks5h://192.168.67.2:1081', 'https': 'socks5h://192.168.67.2:1081'},
        "namespace" : monitoring_failed_pods_data_pipeline[0]['name'],  #'data-pipeline-monitoring-prod',
        "token" : TOKEN,
        'url' :  monitoring_failed_pods_data_pipeline[0]['url'],  #make_endpoint('data-pipeline-monitoring-prod'),
        "headers" : {'Accept': 'application/json',"Authorization": "Bearer "+ TOKEN}
    }
    return dictionary

slownik= login_dict() 
# print( slownik )
def check_if_login():
    try: 
        # os.system('oc whoami')
        r = requests.get(url='https://api.devops.advantagedp.org:6443', headers={'Accept': 'application/json',"Authorization": "Bearer "+ 'sha256~B30xUNWj8jbfLg01Ug77Xm5N4YgY6cLvoa5XbYYO5gs'}, proxies={'http': 'socks5h://192.168.67.2:1081', 'https': 'socks5h://192.168.67.2:1081'}, verify=False)
    except requests.exceptions.HTTPError as err:
        print( ' no connection ', r.status_code )
        raise err 
    
# check_if_login()
# r = requests.get(url='https://api.devops.advantagedp.org:6443', headers={'Accept': 'application/json',"Authorization": "Bearer "+ 'sha256~B30xUNWj8jbfLg01Ug77Xm5N4YgY6cLvoa5XbYYO5gs'}, proxies={'http': 'socks5h://192.168.67.2:1081', 'https': 'socks5h://192.168.67.2:1081'}, verify=False)
# print( r.status_code)


def get_failed_pods(**kwargs):
    # os.system('oc login https://api.devops.advantagedp.org:6443 -u devops_apps_pol-s -p k1.oandvaL3Q7ydJ')
    # proxies = {'http': 'socks5h://192.168.67.2:1081', 'https': 'socks5h://192.168.67.2:1081'}
    # TOKEN = 'sha256~wfTI7SW-TKVccd4f_ZEMz2GIWmx2T3l0mOcGjx3CNR0'
    # headers = {'Accept': 'application/json',"Authorization": "Bearer "+ TOKEN}
    # url7 = make_endpoint('data-pipeline-monitoring-prod')
    # print( url7)
    res7 = requests.get(kwargs['url'], headers=kwargs['headers'], proxies=kwargs['proxies'], verify=False)
    # res7 = requests.get(url7, headers=headers, proxies=proxies, verify=False)
    res_j = res7.json()
    df = pd.DataFrame.from_dict(res_j, orient='index')
    # res_j
    kind,apiVersion, metadata, items = zip(
        *(
            (
                res_j["kind"],
                res_j["apiVersion"],
                res_j["metadata"],
                res_j["items"],
            )
            for item in res_j
        )
    )
    df = pd.DataFrame(
        {
            "Kind": kind,
            "ApiVersion": apiVersion,
            "Metadata": metadata,
            "Items": items,
        }
    )
    print(f'df \n {df.head(2)}' )

    # print( len(res_j['items']))
    # print( type(res_j['items'][0]))
    df2 = pd.DataFrame(res_j['items'])
    print(f'\n df2 \n {df2.head(2)}' )
    now = dt.datetime.now()
    # czas = time.strftime()
    beauty_time = now.strftime("%Y-%m-%d  %H:%M:%S")
    

    name,namespace, creationTimestamp, manageFields_time, status_phase,status_starttime = zip(
        *(
            (
                df2.iloc[idx]['metadata']['name'],       
                df2.iloc[idx]['metadata']['namespace'],           
                dt.datetime.fromisoformat(df2.iloc[idx]['metadata']['creationTimestamp'][:-1] + '+00:00').strftime("%Y-%m-%d  %H:%M:%S"),            
                df2.iloc[idx]['metadata']['managedFields'][0]['time'],# to samo             
                df2.iloc[idx]['status']['phase'],            
                df2.iloc[idx]['status']['startTime']
                
                # PONIZEJ BLAD PONIEWAZ df2.iloc[idx]['status']['containerStatuses'][0]['state'] BEDZIE # 3 {'running': {'startedAt': '2022-09-05T07:09:03Z'}}
                # 2 {'terminated': {'exitCode': 0, 'reason': 'Completed', 'startedAt': '2022-09-05T07:06:03Z', 'finishedAt': '2022-09-05T07:07:06Z', 'containerID': 'cri-o://c0cc76ca287fe25d23b02d8660c9092b328ee1baa07f1c6b7201f2ad144ee2fc'}}
                # df2.iloc[idx]['status']['containerStatuses'][0]['state']['terminated']['reason'],            
                # df2.iloc[idx]['status']['containerStatuses'][0]['state']['terminated']['startedAt'],
                # df2.iloc[idx]['status']['containerStatuses'][0]['state']['terminated']['finishedAt']
                
            )
            for idx in df2.index
        )
    )
    now = dt.datetime.now()
    # czas = time.strftime()
    beauty_time = now.strftime("%Y-%m-%d  %H:%M:%S")
    print(f'now  {now}' )
    print(f'beauty_time {beauty_time}' )
    
    df3 = pd.DataFrame(
        {
            "Name": name,
            "Namespace": namespace,
            "CreationTimestamp": creationTimestamp,
            "ManageFields_time": manageFields_time,
            "Status_phase": status_phase,
            # "Status_startTime":status_starttime,
            "Time_now": dt.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
            # "Status_starttime": status_starttime,
            # "Status_containerStatuses_0_state_terminated_reason": status_containerStatuses_0_state_terminated_reason,
            # "Status_containerStatuses_0_state_terminated_startedAt": status_containerStatuses_0_state_terminated_startedAt,
            # "Status_containerStatuses_0_state_terminated_finishedAt": status_containerStatuses_0_state_terminated_finishedAt,
        }
    )
    print( type(beauty_time))
    print(f'\n df3 \n {df3}' )
    error = 'Failed'
    errory = df3.loc[df3["Status_phase"]  ==  error ]

    print( f'\n \n Pods with status Failed  \n {errory}     ')
    errory_html = errory.to_html

    running = 'Running'
    runningi = df3.loc[df3["Status_phase"]  ==  running ]
    runnigni_html = runningi.to_html

    errory_html = errory.to_html
    
    # print( errory_html)
    # print( runnigni_html )
    return errory_html

get_failed_pods(**slownik)
# get_failed_pods( **slownik)

# a = '2022-09-02T21:20:01Z'
# b = datetime.fromisoformat('2020-01-06T00:00:00.000Z'[:-1] + '+00:00')
# print (b.strftime("%Y-%m-%d  %H:%M:%S") )

# b = datetime.fromisoformat(a[:-1] + '+00:00')
# print (b.strftime("%Y-%m-%d  %H:%M:%S") )

# print( f' \n \n LONG RUNNING PODS \n \n ')
def get_long_running_pods( long_time_running=6 , **kwargs):
    
    # url7 = make_endpoint(NAMESPACE)
    # res7 = requests.get(url7, headers=headers, proxies=proxies , verify=False)
    res7 = requests.get(kwargs['url'], headers=kwargs['headers'], proxies=kwargs['proxies'], verify=False)
    res_j = res7.json()
    df = pd.DataFrame.from_dict(res_j, orient='index')
    kind,apiVersion, metadata, items = zip(
        
        *(
            (
                res_j["kind"],
                res_j["apiVersion"],
                res_j["metadata"],
                res_j["items"],
            )
            for item in res_j
        )
    )
    df = pd.DataFrame(
        {
            "Kind": kind,
            "ApiVersion": apiVersion,
            "Metadata": metadata,
            "Items": items,
        }
    )
    print(f' \t df \n {df.head()}' )
    print( ' * ' * 20 )
    df2 = pd.DataFrame(res_j['items'])
    print(f'\n df2 \n {df2.head(15)}' )
    now = dt.datetime.now()
    # czas = time.strftime()
    beauty_time = now.strftime("%Y-%m-%d  %H:%M:%S")
    
    name,namespace, creationTimestamp, manageFields_time, status_phase,status_starttime = zip(
        *(
            (
                df2.iloc[idx]['metadata']['name'],       
                df2.iloc[idx]['metadata']['namespace'],           
                df2.iloc[idx]['metadata']['creationTimestamp'],
                df2.iloc[idx]['metadata']['managedFields'][0]['time'],# to samo             
                df2.iloc[idx]['status']['phase'],            
                df2.iloc[idx]['status']['startTime']
                # datetime.fromisoformat(df2.iloc[idx]['metadata']['creationTimestamp'][:-1] + '+00:00').strftime("%Y-%m-%d  %H:%M:%S"),            
                # PONIZEJ BLAD PONIEWAZ df2.iloc[idx]['status']['containerStatuses'][0]['state'] BEDZIE # 3 {'running': {'startedAt': '2022-09-05T07:09:03Z'}}
                # 2 {'terminated': {'exitCode': 0, 'reason': 'Completed', 'startedAt': '2022-09-05T07:06:03Z', 'finishedAt': '2022-09-05T07:07:06Z', 'containerID': 'cri-o://c0cc76ca287fe25d23b02d8660c9092b328ee1baa07f1c6b7201f2ad144ee2fc'}}
                # df2.iloc[idx]['status']['containerStatuses'][0]['state']['terminated']['reason'],            
                # df2.iloc[idx]['status']['containerStatuses'][0]['state']['terminated']['startedAt'],
                # df2.iloc[idx]['status']['containerStatuses'][0]['state']['terminated']['finishedAt']
                
            )
            for idx in df2.index
        )
    )
    now = dt.datetime.now()
    # czas = time.strftime()
    beauty_time = now.strftime("%Y-%m-%d  %H:%M:%S")
    # print(f'now  {now}' )
    # print(f'beauty_time {beauty_time}' )
    
    df3 = pd.DataFrame(
        {
            "Name": name,
            "Namespace": namespace,
            "CreationTimestamp": creationTimestamp,
            "ManageFields_time": manageFields_time,
            "Status_phase": status_phase,
            "Time_now": dt.datetime.now().strftime("%Y-%m-%d  %H:%M:%S"),
            # "Status_starttime": status_starttime,
            # "Status_containerStatuses_0_state_terminated_reason": status_containerStatuses_0_state_terminated_reason,
            # "Status_containerStatuses_0_state_terminated_startedAt": status_containerStatuses_0_state_terminated_startedAt,
            # "Status_containerStatuses_0_state_terminated_finishedAt": status_containerStatuses_0_state_terminated_finishedAt,
        }
    )
    
    def difference_dates_hours(date1):
        now = dt.datetime.now()
        beauty_time = now.strftime("%Y-%m-%d  %H:%M:%S")
        beauty_time = dt.datetime.strptime(beauty_time,"%Y-%m-%d  %H:%M:%S")
        delta = (beauty_time - date1).total_seconds()
        min = delta / 60
        hours = delta / (60 * 60) 
        # print( f''' JESTEM W differences_dates_hours now = {type(beauty_time) } - {beauty_time}  DATE1 = {type(date1)} , {date1} 
        #       \n delta = {type(delta)}   {delta}  min = {min}   hours = {hours}''')
        
        return hours
   
    def difference_dates_minutes(date1 ):
        now = dt.datetime.now()
        beauty_time = now.strftime("%Y-%m-%d  %H:%M:%S")
        beauty_time = dt.datetime.strptime(beauty_time,"%Y-%m-%d  %H:%M:%S")
        delta = (beauty_time - date1).total_seconds()
        min = delta / 60
        # hours = delta / (60 * 60) 
        # print( f''' JESTEM W differences_dates_hours now = {type(beauty_time) } - {beauty_time}  DATE1 = {type(date1)} , {date1} 
        #       \n delta = {type(delta)}   {delta}  min = {min}   hours = {hours}''')
        
        return min
    
    def difference_dates_seconds(date1):
        now = dt.now()
        beauty_time = now.strftime("%Y-%m-%d  %H:%M:%S")
        beauty_time = dt.datetime.strptime(beauty_time,"%Y-%m-%d  %H:%M:%S")
        delta = (beauty_time - date1).total_seconds()
        # min = delta / 60
        # hours = delta / (60 * 60) 
        # print( f''' JESTEM W differences_dates_hours now = {type(beauty_time) } - {beauty_time}  DATE1 = {type(date1)} , {date1} 
        #       \n delta = {type(delta)}   {delta}  min = {min}   hours = {hours}''')
        
        return delta
    
    def change_creationtimestamp(date):
        date = dt.datetime.fromisoformat(date[:-1] + '+00:00').strftime("%Y-%m-%d  %H:%M:%S")
        return dt.datetime.strptime(date,"%Y-%m-%d  %H:%M:%S")
    
    
    df3['Zmiana_timestamp'] = df3['CreationTimestamp'].apply(change_creationtimestamp)
    df3['Date_diff_hours'] = df3['Zmiana_timestamp'].apply(difference_dates_hours)
    print( type(beauty_time))
    print(f'\n  \t df3 \n {df3.head(3)}' )
    error = 'Failed'
    errory = df3.loc[df3["Status_phase"]  ==  error ]

    errory_html = errory.to_html

    running = 'Running'
    runningi = df3.loc[df3["Status_phase"]  ==  running ]
    runnigni_html = runningi.to_html

    errory_html = errory.to_html
    
    # print( errory_html)
    print( runnigni_html )
    return runnigni_html


# get_long_running_pods(**slownik)


def logout():
    os.system('oc logout')
    
    
# logout()
# get_long_running_pods(**slownik)
# os.system('oc login https://api.devops.advantagedp.org:6443 -u devops_apps_pol-s -p k1.oandvaL3Q7ydJ')
# a = os.system('oc whoami')
# print( f' {type(a)} - {a} ')
# check_login()
# a = '2022-09-05  08:17:28'

# b = datetime.now()
# b = b.strftime("%Y-%m-%d  %H:%M:%S")
# print( a )
# print( type(b ) , b  )
# aa = datetime.strptime(a,"%Y-%m-%d  %H:%M:%S")
# bb = datetime.strptime(b,"%Y-%m-%d  %H:%M:%S")
# print( type(aa ))
# print( type(bb ))
# roznica= bb - aa 
# print( roznica.days)
# print( '--  ',roznica.total_seconds())
# print( type(roznica.total_seconds))
# start_time = datetime.strptime("2:13:57", "%H:%M:%S")
# end_time = datetime.strptime("11:46:38", "%H:%M:%S")
# delta = end_time - start_time

# sec = delta.total_seconds()
# print('difference in seconds:', sec)
# min = sec / 60
# print('difference in minutes:', min)

# # get difference in hours
# hours = sec / (60 * 60)
# print('difference in hours:', hours)

# c = '2022-09-04T12:40:00Z'
# def change_creationtimestamp(date):
#         date = datetime.fromisoformat(date[:-1] + '+00:00').strftime("%Y-%m-%d  %H:%M:%S")
#         return datetime.strptime(date,"%Y-%m-%d  %H:%M:%S")
    
# d = change_creationtimestamp(c)
# print( f'd ZMIENIONY 2022-09-06T12:40:00Z  {d}')
# print( f' co to jest d {type(d)}   {d}')
# def difference_dates_hours(date1):
#         now = datetime.now()
#         beauty_time = now.strftime("%Y-%m-%d  %H:%M:%S")
#         # beauty_time = datetime.fromisoformat(now[:-1] + '+00:00').strftime("%Y-%m-%d  %H:%M:%S")
#         beauty_time = datetime.strptime(beauty_time,"%Y-%m-%d  %H:%M:%S")
#         delta = (beauty_time - date1).total_seconds()
#         min = delta / 60
#         hours = delta / (60 * 60) 
#         print( f''' JESTEM W differences_dates_hours now = {type(beauty_time) } - {beauty_time}  DATE1 = {type(date1)} , {date1} 
#               \n delta = {type(delta)}   {delta}  min = {min}   hours = {hours}''')
        
#         return hours 
    
# e = '2022-09-06  08:29:47'
# print( f' e to data do porownania {type(e)}   {e }')

# zmiana_e = datetime.strptime(e,"%Y-%m-%d  %H:%M:%S" )
# print(f' e to data do porownania { type(zmiana_e)} , {zmiana_e}' )
# g = difference_dates_hours(zmiana_e)
# print( f' now jaki to typ  {type(g)}    ,  {g}  ')



# print( f' difference_dates {difference_dates_hours(d)}')
# print( 'wez sobie token')
# a = os.system('oc whoami -t') 
# print( a )

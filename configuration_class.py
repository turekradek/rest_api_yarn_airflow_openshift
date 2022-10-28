
"""
    Configuration parameters for openshift pods monitoring
    
"""

import os
import time

class BaseConfig:
    """
    Base configuration parameters for all devops monitoring DAGs.
    """
    DEVOPS_EMAILS = "{{ devops_airflow_emails }}"
    MAPR_TICKETFILE_LOCATION = "/opt/mapr/tickets/{{ mapr_ticket_name }}"
    YARN_API_GET_CRED = {"user": os.environ.get("IP_USER"), "userp":os.environ.get("IP_PASS")}
    MONITORING_SCRIPTS_PATH = "{{ devops_monitoring_deploy_path }}"
    YARN_API = "{{ yarn_api_endpoint }}"
    DIRLL_API = "{{ drill_api }}"
    
    
    
class OpenShiftPodsMonitoring(BaseConfig):
    """
    Configuration parameters for namespaces and pods of openshift monitorin
    """
    DAG_ID = "openshift_pods_monitoring"
    
    MONITORING_FAILED_PODS_BOSON_TEAM_DICT = [ 
        {
            "name": "boson-team",
            "app_name":"airflow-kpi",
            "url":   "https://api.devops.advantagedp.org:6443/api/v1/namespaces/boson-team/pods"                                      
        },
        # {
        #     "name": "boson-team",
        #     "app_name":"bosonwiki",
        #     "url":   "https://api.devops.advantagedp.org:6443/api/v1/namespaces/boson-team/pods"                                      
        # },
        #  {
        #     "name": "boson-team",
        #     "app_name":"car-logger",
        #     "url":   "https://api.devops.advantagedp.org:6443/api/v1/namespaces/boson-team/pods"                                      
        # },
        # {
        #     "name": "boson-team",
        #     "app_name":"cronjob-release",
        #     "url":   "https://api.devops.advantagedp.org:6443/api/v1/namespaces/boson-team/pods"                                      
        # },
                       
                                              
    ]
    
    MONITORING_FAILED_PODS_DATA_PIPELINE_MONITORING_PROD_DICT = [
        
        {
            "name": "data-pipeline-monitoring-prod",
            "app_name":"dpm-cron-aggragate",
            "url":  "https://api.devops.advantagedp.org:6443/api/v1/namespaces/data-pipeline-monitoring-prod/pods"                                      
        },
        
        {
            "name": "data-pipeline-monitoring-prod",
            "app_name":"dpm-cron-car-owner-alerting",
            "url":  "https://api.devops.advantagedp.org:6443/api/v1/namespaces/data-pipeline-monitoring-prod/pods"                                      
        },
        
        {
            "name": "data-pipeline-monitoring-prod",
            "app_name":"dpm-cron-join",
            "url":  "https://api.devops.advantagedp.org:6443/api/v1/namespaces/data-pipeline-monitoring-prod/pods"                                      
        },
        
        {
            "name": "data-pipeline-monitoring-prod",
            "app_name":"dpm-cron-whitelisting-monitoring",
            "url":  "https://api.devops.advantagedp.org:6443/api/v1/namespaces/data-pipeline-monitoring-prod/pods"                                      
        },
            
        
        
    ]
    
    
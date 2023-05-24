import os
from datetime import date, timedelta
import json
import requests

TOKEN_TOPVISOR = os.environ['TOKEN_TOPVISOR']
USER_ID_TOPVISOR = os.environ['USER_ID_TOPVISOR']


class TopVisor:
    headers = {
        "User-Id": str(USER_ID_TOPVISOR),
        "Authorization": 'bearer ' + TOKEN_TOPVISOR,
        "Content-Type": "application/json",
    }
    projects_url = 'https://api.topvisor.com/v2/json/get/projects_2/projects'
    summary_url = 'https://api.topvisor.com/v2/json/get/positions_2/summary'

    @staticmethod
    def get_data():
        json_data = {
            "fields": ["url"],
            "dates": [str(date.today() - timedelta(days=7)), str(date.today())],
            "limit": 200,
            "show_searchers_and_regions": True,
            "include_positions_summary_params": {
                "show_tops": 1
            }
        }
        response_top = requests.get(url=TopVisor.projects_url, json=json_data, headers=TopVisor.headers)
        return json.loads(response_top.text) if response_top.status_code == 200 else None

    @staticmethod
    def get_detail_data(project_id, region_index):
        json_data = {
            "project_id": str(project_id),
            "region_index": str(region_index),
            "dates": [str(date.today() - timedelta(days=7)), str(date.today())],
            "limit": 200,
            "show_tops": 1,
            "show_visibility": 1,
            "show_avg": 1,
            "show_dynamics": 1,

        }
        response_top = requests.get(url=TopVisor.summary_url, json=json_data, headers=TopVisor.headers)
        return json.loads(response_top.text) if response_top.status_code == 200 else None

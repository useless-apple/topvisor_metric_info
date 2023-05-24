import os
from datetime import date, timedelta

import requests
import json

TOKEN_METRIC = os.environ['TOKEN_METRIC']


class Yandex:
    url = 'https://api-metrika.yandex.ru/stat/v1/data'
    headers = {
        "Host": "api-metrika.yandex.net",
        "Authorization": 'OAuth ' + TOKEN_METRIC,
        "Content-Type": "application/x-yametrika+json",
    }

    @staticmethod
    def get_data(metric_id, metrics):
        payload_data = {
            'ids': int(metric_id),
            'attribution': 'first',
            'metrics': ','.join(str(x) for x in metrics),
            'dimensions': 'ym:s:TrafficSource',
            'date1': date.today() - timedelta(days=31),
            'date2': date.today() - timedelta(days=1),
            'limit': 100000,
            'accuracy': 'full',
            'filters': "ym:s:lastSignTrafficSource=='organic' AND ym:s:isRobot=='No'"
        }
        response_yan = requests.get(url=Yandex.url, params=payload_data, headers=Yandex.headers)
        response = []
        if response_yan.status_code == 200:
            result = json.loads(response_yan.text)['totals']
            for metric in metrics:
                if 'visits' in metric:
                    response.append(result[metrics.index(metric)])
                else:
                    response.append(round(result[metrics.index(metric)], 2))
            return response
        else:
            return None

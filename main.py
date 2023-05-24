import math
import time
from datetime import date

from topvisor import TopVisor
from xls_parser import XLS
from yandex import Yandex

input_path = 'domains.xlsx'
output_path = 'result_{}.xlsx'.format(date.today())

print('--Начал обработку--')
xls = XLS(input_path, output_path)
sites = xls.xls_to_dict()

response_site = []
response_top_visor = TopVisor.get_data()


class Tops:
    def __init__(self):
        self.top_1_10_current = ''
        self.top_1_10_dynamics = ''
        self.top_11_30_current = ''
        self.top_11_30_dynamics = ''
        self.top_31_50_current = ''
        self.top_31_50_dynamics = ''
        self.top_51_100_current = ''
        self.top_51_100_dynamics = ''
        self.top_101_10000_current = ''
        self.top_101_10000_dynamics = ''


class SiteTopVisor:
    def __init__(self):
        self.visibilities_current = ''
        self.visibilities_dynamics = ''

        self.dynamics_up = ''
        self.dynamics_down = ''

        self.tops = Tops()


class SiteMetric:
    def __init__(self):
        self.metric = ''
        self.visits = ''
        self.bounceRate = ''
        self.pageDepth = ''


class Site:
    def __init__(self):
        self.domain = ''
        self.project_id = ''
        self.region_index = ''
        self.metric = SiteMetric()
        self.top_visor = SiteTopVisor()


print('Сайтов в обработке ' + str(len(sites)))
for item in sites:
    if item['domain'] == '' or item['domain'] is None:
        print('Домен не указан')
        continue
    elif item['metric'] == '' or item['metric'] is None or math.isnan(item['metric']):
        print(item['domain'] + ' Метрика не указана')
        continue

    print('Обрабатываю ' + item['domain'])

    if response_top_visor and 'result' in response_top_visor:
        for i in response_top_visor['result']:
            if i['url'] == item['domain']:
                for search in i['searchers']:
                    if search['name'] == 'Yandex':
                        for reg in search['regions']:
                            cur_site = Site()
                            cur_site.domain = '{}({})'.format(item['domain'], reg['areaName'])
                            cur_site.project_id = i['id']
                            cur_site.region_index = reg['index']
                            cur_site.metric.metric = item['metric']

                            detail_data = TopVisor.get_detail_data(cur_site.project_id, cur_site.region_index)

                            cur_site.top_visor.visibilities_current = detail_data['result']['visibilities'][-1]
                            cur_site.top_visor.visibilities_dynamics = detail_data['result']['visibility_dynamic']

                            cur_site.top_visor.dynamics_up = detail_data['result']['dynamics']['up']
                            cur_site.top_visor.dynamics_down = detail_data['result']['dynamics']['down']

                            cur_site.top_visor.tops.top_1_10_current = detail_data['result']['tops'][-1]['1_10']
                            cur_site.top_visor.tops.top_1_10_dynamics = detail_data['result']['tops_dynamics']['1_10']

                            cur_site.top_visor.tops.top_11_30_current = detail_data['result']['tops'][-1]['11_30']
                            cur_site.top_visor.tops.top_11_30_dynamics = detail_data['result']['tops_dynamics'][
                                '11_30']

                            cur_site.top_visor.tops.top_31_50_current = detail_data['result']['tops'][-1]['31_50']
                            cur_site.top_visor.tops.top_31_50_dynamics = detail_data['result']['tops_dynamics'][
                                '31_50']

                            cur_site.top_visor.tops.top_51_100_current = detail_data['result']['tops'][-1]['51_100']
                            cur_site.top_visor.tops.top_51_100_dynamics = detail_data['result']['tops_dynamics'][
                                '51_100']

                            cur_site.top_visor.tops.top_101_10000_current = detail_data['result']['tops'][-1][
                                '101_10000']
                            cur_site.top_visor.tops.top_101_10000_dynamics = detail_data['result']['tops_dynamics'][
                                '101_10000']
                            metrics = ['ym:s:visits', 'ym:s:bounceRate', 'ym:s:pageDepth']
                            data_metric = Yandex.get_data(item['metric'], metrics)
                            cur_site.metric.visits = data_metric[0]
                            cur_site.metric.bounceRate = data_metric[1]
                            cur_site.metric.pageDepth = data_metric[2]
                            response_site.append(cur_site)
                    else:
                        continue

xls.dict_to_xls(xls.data_to_format(response_site))

print('--Закончил обработку--')
time.sleep(3)

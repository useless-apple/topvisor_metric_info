import pandas as pd


class XLS:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def xls_to_dict(self):
        xls = pd.ExcelFile(r"{}".format(self.input_path)).parse()
        return xls.to_dict('records')

    def dict_to_xls(self, po):
        df = pd.DataFrame(po)
        df.columns = ['Домен', 'Метрика', 'Посещения', 'Отказы', 'Глубина просмотров',
                      'Видимость сайта', 'Топ_1_10', 'Топ_11_30', 'Топ_31_50', 'Топ_51_100', 'Топ_101_10000',
                      'Позиций улучшилось', 'Позиций ухудшилось']
        df.to_excel(self.output_path)

    @staticmethod
    def data_to_format(sites):
        data_to_xls = []
        for site in sites:
            top_1_10 = '{} ({})'.format(site.top_visor.tops.top_1_10_current, site.top_visor.tops.top_1_10_dynamics)
            top_11_30 = '{} ({})'.format(site.top_visor.tops.top_11_30_current, site.top_visor.tops.top_11_30_dynamics)
            top_31_50 = '{} ({})'.format(site.top_visor.tops.top_31_50_current, site.top_visor.tops.top_31_50_dynamics)
            top_51_100 = '{} ({})'.format(site.top_visor.tops.top_51_100_current,
                                          site.top_visor.tops.top_51_100_dynamics)
            top_101_10000 = '{} ({})'.format(site.top_visor.tops.top_101_10000_current,
                                             site.top_visor.tops.top_101_10000_dynamics)
            visibilities = '{} ({})'.format(site.top_visor.visibilities_current, site.top_visor.visibilities_dynamics)
            data_to_xls.append((site.domain,
                                site.metric.metric,
                                site.metric.visits,
                                site.metric.bounceRate,
                                site.metric.pageDepth,
                                visibilities,
                                top_1_10,
                                top_11_30,
                                top_31_50,
                                top_51_100,
                                top_101_10000,
                                site.top_visor.dynamics_up,
                                site.top_visor.dynamics_down,
                                ))
        return data_to_xls

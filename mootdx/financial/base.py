from .. import config
from ..config import settings


# def reporthook(downloaded, total_size):
#     print('Downloaded {}, Total is {}'.format(downloaded, total_size))


class BaseFinancial:
    def __init__(self, mode='content'):
        self.mode = mode

        try:
            default = settings.get('SERVER').get('GP')[0][1:]
            self.bestip = config.get('BESTIP').get('GP', default)
        except ValueError:
            self.bestip = ('106.14.95.149', 7727)

    def fetch_and_parse(self, report_hook=None, downdir=None, chunk_size=51200, *args, **kwargs):
        """
        function to get data , 参考 https://docs.python.org/3/library/urllib.request.html#module-urllib.request

        :param report_hook 使用urllib.request 的report_hook 来汇报下载进度
        :param downdir 数据文件下载的地址，如果没有提供，则下载到临时文件中，并在解析之后删除
        :param chunk_size chunk_size
        :return: 解析之后的数据结果
        """

        file = self.content(report_hook=report_hook, downdir=downdir, chunk_size=chunk_size, *args, **kwargs)
        return self.parse(file, *args, **kwargs)

    def content(self, report_hook=None, downdir=None, proxies=None, chunk_size=1024 * 50, *args, **kwargs):
        raise NotImplementedError('will impl in subclass')

    def parse(self, download_file, *args, **kwargs):
        raise NotImplementedError('will impl in subclass')

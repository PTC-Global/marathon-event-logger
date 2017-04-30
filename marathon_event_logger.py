#!/usr/bin/env python

import os
from marathon import MarathonClient

MARATHON_SERVERS = os.environ.get('MARATHON_SERVERS', 'http://master.mesos:8080')
AUTH_TOKEN = os.environ.get('MARATHON_AUTH_TOKEN', None)
USERNAME = os.environ.get('MARATHON_USERNAME', None)
PASSWORD = os.environ.get('MARATHON_PASSWORD', None)

c = MarathonClient(
        MARATHON_SERVERS.split(','),
        username=USERNAME,
        password=PASSWORD,
        auth_token=AUTH_TOKEN)

for event in c.event_stream(raw=True):
    print event.strip()

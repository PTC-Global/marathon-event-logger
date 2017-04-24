# How to run

```
docker run --rm -it -e MARATHON_SERVERS=http://172.17.0.2:8080 bergerx/marathon-event-logger
```

# Example output
```
bekir@ubuntu:~$ docker run --rm -it -e MARATHON_SERVERS=http://172.17.0.2:8080 bergerx/marathon-event-logger
{"eventType": "event_stream_attached", "remoteAddress": "172.17.0.5", "timestamp": "2017-04-24T07:21:07.516Z"}
{"condition": "Created", "eventType": "instance_changed_event", "host": "172.17.0.3", "instanceId": "test.marathon-97550c22-28be-11e7-901c-3ad18a53e083", "runSpecId": "/test", "runSpecVersion": "2017-04-24T01:13:38.470Z", "timestamp": "2017-04-24T07:21:10.596Z"}
{"appId": "/test", "eventType": "status_update_event", "host": "172.17.0.3", "ports": [17972], "slaveId": "2aaf163a-e9a0-4bdd-acdc-d41d6c16c537-S0", "taskId": "test.97550c22-28be-11e7-901c-3ad18a53e083", "taskStatus": "TASK_RUNNING", "timestamp": "2017-04-24T07:21:11.417Z", "version": "2017-04-24T01:13:38.470Z"}
{"condition": "Running", "eventType": "instance_changed_event", "host": "172.17.0.3", "instanceId": "test.marathon-97550c22-28be-11e7-901c-3ad18a53e083", "runSpecId": "/test", "runSpecVersion": "2017-04-24T01:13:38.470Z", "timestamp": "2017-04-24T07:21:11.419Z"}
{"appId": "/test", "eventType": "status_update_event", "host": "172.17.0.3", "message": "Container exited with status 0", "ports": [17972], "slaveId": "2aaf163a-e9a0-4bdd-acdc-d41d6c16c537-S0", "taskId": "test.97550c22-28be-11e7-901c-3ad18a53e083", "taskStatus": "TASK_FINISHED", "timestamp": "2017-04-24T07:21:11.473Z", "version": "2017-04-24T01:13:38.470Z"}
{"condition": "Finished", "eventType": "instance_changed_event", "host": "172.17.0.3", "instanceId": "test.marathon-97550c22-28be-11e7-901c-3ad18a53e083", "runSpecId": "/test", "runSpecVersion": "2017-04-24T01:13:38.470Z", "timestamp": "2017-04-24T07:21:11.475Z"}
{"eventType": "event_stream_detached", "remoteAddress": "172.17.0.5", "timestamp": "2017-04-24T07:21:11.667Z"}
{"condition": "Created", "eventType": "instance_changed_event", "host": "172.17.0.3", "instanceId": "test.marathon-9a5309e3-28be-11e7-901c-3ad18a53e083", "runSpecId": "/test", "runSpecVersion": "2017-04-24T01:13:38.470Z", "timestamp": "2017-04-24T07:21:15.616Z"}
{"appId": "/test", "eventType": "status_update_event", "host": "172.17.0.3", "ports": [29269], "slaveId": "2aaf163a-e9a0-4bdd-acdc-d41d6c16c537-S0", "taskId": "test.9a5309e3-28be-11e7-901c-3ad18a53e083", "taskStatus": "TASK_RUNNING", "timestamp": "2017-04-24T07:21:16.440Z", "version": "2017-04-24T01:13:38.470Z"}
...
```

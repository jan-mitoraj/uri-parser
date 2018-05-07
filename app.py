#!/usr/bin/env python
import sys
from urlparse import urlparse

schemes = {
        'remmina' : { 'cmd': "xfreerdp /v:{hostname}:{port} /u:{username} /p:{password} /cert-ignore", 'default_port': 3389},
        'ssh' : { 'cmd': "ssh {username}@{hostname} -p {port}", 'default_port': 22}
        }


if len(sys.argv) == 1:
    print "Error: No URI"
    sys.exit(-1)

uri = urlparse(sys.argv[1])

if uri.scheme in schemes:
    print schemes[uri.scheme]['cmd'].format(
            hostname = uri.hostname,
            port = uri.port if uri.port else schemes[uri.scheme]['default_port'],
            username = uri.username,
            password = uri.password or ""
            )

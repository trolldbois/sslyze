#!/usr/bin/env python

from time import time
import sys

from plugins import PluginsFinder


def main():
    
    sslyze_plugins = PluginsFinder()
    available_plugins = sslyze_plugins.get_plugins()
    available_commands = sslyze_plugins.get_commands()

    from plugins.PluginCertInfo import PluginCertInfo

    worker = PluginCertInfo()
    worker._shared_settings = dict()
    worker._shared_settings['nb_retries'] = 1
    worker._shared_settings['timeout'] = 10
    worker._shared_settings['starttls'] = False
    # serverconnectivitytester
    worker._shared_settings['https_tunnel_host'] = host
    worker._shared_settings['https_tunnel_port'] = port
    worker._shared_settings['https_tunnel_user'] = user
    worker._shared_settings['https_tunnel_password'] = password
    worker._shared_settings['http_get'] = None
    worker._shared_settings['cert'] = None
    worker._shared_settings['sni'] = None
    
    ip = sys.argv[1]
    target = (ip,ip,443,3)

    storePath = ''
    x = worker._get_cert(target, storePath)[0].as_dict()

    name = x['subject']['commonName']
    print name
    try:
        alts = x['extensions']['X509v3 Subject Alternative Name']['DNS']
        for n in alts:
            if n == name:
                continue
            print n
    except KeyError:
        pass



if __name__ == "__main__":
    main()

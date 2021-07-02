import os

from mitmproxy.options import Options
from mitmproxy.proxy.config import ProxyConfig
from mitmproxy.proxy.server import ProxyServer
from mitmproxy.tools.dump import DumpMaster
from mitmproxy.http import HTTPFlow
import json


class Handler:
    def __init__(self, config):
        self.config = config
        print('Ready on ' + config["host"] + ":" + config["port"])

    def request(self, flow: HTTPFlow):
        for redirect in list(self.config["redirect"]):
            before = redirect["before"]
            after = redirect["after"]
            if flow.request.url.__contains__(before):
                mae = flow.request.url
                flow.request.url = flow.request.url.replace(before, after)
                print("Replace " + mae + " to " + flow.request.url)


if __name__ == "__main__":
    config = {
        "host": "0.0.0.0",
        "port": "14514",
        "redirect": [
            {
                "before": "https://repo1.maven.org/maven2",
                "after": "https://maven.aliyun.com/nexus/content/groups/public"
            },
            {
                "before": "https://repo.maven.apache.org/maven2",
                "after": "https://maven.aliyun.com/nexus/content/groups/public"
            },
            {
                "before": "https://jcenter.bintray.com",
                "after": "https://maven.aliyun.com/nexus/content/groups/public"
            }
        ]
    }
    if os.path.exists("./config.json"):
        config = json.load(open("./config.json"))
    else:
        f = open("./config.json", "w")
        f.write(json.dumps(config))
        f.close()

    options = Options(listen_host=config["host"], listen_port=int(config["port"]), http2=False, ssl_insecure=True)
    server = DumpMaster(options, with_termlog=False, with_dumper=False)
    server.server = ProxyServer(ProxyConfig(options))
    master = server
    master.addons.add(Handler(config))
    master.run()

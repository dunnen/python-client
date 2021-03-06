from ark.api.resource import Resource


class Peer(Resource):
    # TO FIX - PEER FUNCTION NOT WORKING
    def peer(self, ip, port):
        return self.request_get('api/peers/get', {'ip': ip, 'port': port})

    def peers(self, parameters=None):
        return self.request_get('api/peers', parameters)

    def version(self):
        return self.request_get('api/peers/version')

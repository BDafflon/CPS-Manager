from flask import Flask, Response, jsonify, request


class EndpointAction(object):

    def __init__(self, action):
        self.action = action
        self.response = Response(status=200, headers={})

    def __call__(self, *args):
        print(args)
        rep = self.action()

        return jsonify(rep)


class CPSManagerAPI(object):
    app = None

    def __init__(self, name):
        self.app = Flask(name)
        self.cpsList=[{"type":"CPS","name":"CPS1","IP":'127.0.0.1','port':5001,"status":"running"}]

    def run(self):
        self.app.run()

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name, EndpointAction(handler))


    def help(self):
        rep={"add":"/add","remove":"/remove","list CPS":"/list"}
        return rep


    def add(self):

        cps={}
        cps["type"] = request.args.get('type')
        cps["name"] =request.args.get('name')
        cps["ip"] = request.args.get('ip')
        cps["port"] = request.args.get('port')
        cps["status"] = request.args.get('status')

        self.cpsList.append(cps)
        return None

    def remove(self):
        return None

    def listing(self):
        # Execute anything
        return self.cpsList

class CPSManager:
    def __init__(self):
        self.manager = CPSManagerAPI('manager')
        self.manager.add_endpoint(endpoint='/', endpoint_name='/', handler=self.manager.help)
        self.manager.add_endpoint(endpoint='/add', endpoint_name='add', handler=self.manager.add)
        self.manager.add_endpoint(endpoint='/remove', endpoint_name='remove', handler=self.manager.remove)
        self.manager.add_endpoint(endpoint='/list', endpoint_name='list', handler=self.manager.listing)
        self.manager.run()
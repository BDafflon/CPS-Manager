from flask import Flask, Response, jsonify, request


class CPSManagerAPI(object):
    app = None

    def __init__(self, name):
        self.app = Flask(name)
        self.cpsList=[]
        self.cpss=[]

    def run(self):
        self.app.run()

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name, handler)


    def help(self):
        rep={"add":"/add","remove":"/remove","list CPS":"/list"}
        return rep


    def add(self,name=None,type=None,ip="127.0.0.1",port=5001):
        print(type)
        cps={}
        cps["type"] = type
        cps["name"] =name
        cps["ip"] = ip
        cps["port"] = port


        self.cpsList.append(cps)
        simCps = CPS()

        return jsonify(cps)

    def remove(self,name):
        for i in self.cpsList:
            if i['name']==name:
                self.cpsList.remove(i)
                return jsonify(True)
        return jsonify(False)

    def listing(self):
        # Execute anything
        return jsonify(self.cpsList)

class CPSManager:
    def __init__(self):
        self.manager = CPSManagerAPI('manager')
        self.manager.add_endpoint(endpoint='/', endpoint_name='/', handler=self.manager.help)
        self.manager.add_endpoint(endpoint='/add/<name>/<type>/<ip>/<port>', endpoint_name='add', handler=self.manager.add)
        self.manager.add_endpoint(endpoint='/remove/<name>', endpoint_name='remove', handler=self.manager.remove)
        self.manager.add_endpoint(endpoint='/list', endpoint_name='list', handler=self.manager.listing)
        self.manager.run()
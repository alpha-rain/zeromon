import zmq
import json

class manage:
    
    def config(self,jsonConfig):
        # clear list
        self.listComms = [];
        for connections in jsonConfig:
            factory = comms.factory(connections['type'],connections)
            self.listComms.append(factory)
            factory.config(connections)
        print('hi')
        # return listComms

    def send(self, data):
        for listComm in self.listComms:
        	listComm.send(data)

class comms(object):

    def factory(type,connections):
        if type == "zeromq": return zeromq()
        else:
            print('bad type:' + type)
    factory = staticmethod(factory)



class zeromq(comms):

    # set settings for the zeromq link
    def config(self, jsonConfig):
        print('config')
        self.jsonArray = json.loads('[]')
        self.jsonConfig = jsonConfig
        self.intervalsend = self.jsonConfig['interval-send']
        self.context = zmq.Context()
        # set connection type
        if(self.jsonConfig['connection-type'] == 'push'):
            self.socket = self.context.socket(zmq.PUSH)
        elif(self.jsonConfig['connection-type'] == 'pull'):
            self.socket = self.context.socket(zmq.PULL)
        else:
            print('error')
        # set connection point
        if(self.jsonConfig['connection-point'] == 'client'):
            self.socket.connect(jsonConfig['location'])
        elif(self.jsonConfig['connection-point'] == 'server'):
            self.socket.bind(jsonConfig['location'])
        else:
            print('error')

    def send(self, data):
        self.intervalsend -= 1;
        
        if(self.intervalsend == 0):
            self.jsonArray.append(data)
            self.socket.send_string(json.dumps(self.jsonArray))
            self.intervalsend = self.jsonConfig['interval-send']
            self.jsonArray = json.loads('[]')
        else:
            #append json object, don't use strings'
            self.jsonArray.append(data)

    def sendNow(data):
        print(send)

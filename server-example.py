#use the script with the command: python3 server-example.py [ip_address] [port_number] [pubblication_time] [uri]

import uuid
from threading import Thread
import copy
import logging
from datetime import datetime
import time
from math import sin
import sys
import random
from opcua.ua import NodeId, NodeIdType

sys.path.insert(0, "..")

try:
    from IPython import embed
except ImportError:
    import code
    

    def embed():
        myvars = globals()
        myvars.update(locals())
        shell = code.InteractiveConsole(myvars)
        shell.interact()

from opcua import ua, uamethod, Server


class SubHandler(object):
    """
    Subscription Handler. To receive events from server for a subscription
    """

    def datachange_notification(self, node, val, data):
        print("Python: New data change event", node, val)

    def event_notification(self, event):
        print("Python: New event", event)


# method to be exposed through server

def func(parent, variant):
    ret = False
    if variant.Value % 2 == 0:
        ret = True
    return [ua.Variant(ret, ua.VariantType.Boolean)]


# method to be exposed through server
# uses a decorator to automatically convert to and from variants

@uamethod
def multiply(parent, x, y):
    print("multiply method call with parameters: ", x, y)
    return x * y


class VarUpdater(Thread):
    def __init__(self, var):
        Thread.__init__(self)
        self._stopev = False
        self.var = var

    def stop(self):
        self._stopev = True

    def run(self):
        while not self._stopev:
            v = sin(time.time() / 10)
            self.var.set_value(v)
            time.sleep(0.1)


if __name__ == "__main__":
    # optional: setup logging
    logging.basicConfig(level=logging.WARN)
    #logger = logging.getLogger("opcua.address_space")
    # logger.setLevel(logging.DEBUG)
    #logger = logging.getLogger("opcua.internal_server")
    # logger.setLevel(logging.DEBUG)
    #logger = logging.getLogger("opcua.binary_server_asyncio")
    # logger.setLevel(logging.DEBUG)
    #logger = logging.getLogger("opcua.uaprocessor")
    # logger.setLevel(logging.DEBUG)

    # now setup our server
    server = Server()
    #server.disable_clock()
    #server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")

    hostname = str(sys.argv[1])
    port = str(sys.argv[2])

    domain = "opc.tcp://"
    ddd = ":"
    final_address = (domain+hostname+ddd+port)
    server.set_endpoint(final_address)

    server.set_server_name("FreeOpcUa Example Server")
    # set all possible endpoint policies for clients to connect through
    server.set_security_policy([
                ua.SecurityPolicyType.NoSecurity,
                ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt,
                ua.SecurityPolicyType.Basic256Sha256_Sign])

    # setup our own namespace
    #uri = "http://examples.freeopcua.github.io"
    uri = str(sys.argv[4])
    idx = server.register_namespace(uri)

    # create a new node type we can instantiate in our address space
    dev = server.nodes.base_object_type.add_object_type(idx, "MyDevice")
    dev.add_variable(idx, "sensor1", 1.0).set_modelling_rule(True)
    dev.add_property(idx, "device_id", "0340").set_modelling_rule(True)
    ctrl = dev.add_object(idx, "controller")
    ctrl.set_modelling_rule(True)
    ctrl.add_property(idx, "state", "Idle").set_modelling_rule(True)

    # populating our address space

    # First a folder to organise our nodes
    myfolder = server.nodes.objects.add_folder(idx, "myEmptyFolder")
    # instanciate one instance of our device
    mydevice = server.nodes.objects.add_object(idx, "Device0001", dev)
    mydevice_var = mydevice.get_child(["{}:controller".format(idx), "{}:state".format(idx)])  # get proxy to our device state variable 
    
    # create directly some objects and variables
    # READ OBJECTS AND VARIABLE FORM THE JSON FILE
    dim_obj_list = len(data["opcua"][0]["objects"])


    for i in range(0, dim_obj_list):
      dim_var_list = len(data["opcua"][0]["objects"][i]["variables"])
      globals()[f"obj_{i}"] = data["opcua"][0]["objects"][i]["object_name"]           #cration of: obj_0, obj_1
      globals()[f"myobj_{i}"] = server.nodes.objects.add_object(idx, obj_{i})                #creation of: myobj_0, myobj_1
      #print("-----------------------------------------")
      #print("i:", i)
      #print(data["opcua"][0]["objects"][i]["object_name"])
      for j in range(0, dim_var_list):
             globals()[f"variable_{i}_{j}"] = data["opcua"][0]["objects"][i]["variables"][j]      #creation of: variable_0_0, variable_0_1
             globals()[f"myvar_{i}_{j}"] = myobj.add_variable(idx, variable_{i}_{j}, 6.7)                 #creation of: myvar_0_0, myvar_0_1
             myvar_{i}_{j}.set_writable()
             #print(variable_{i}_{j})
             #print(i,j)
             #print(data["opcua"][0]["objects"][i]["variables"][j])


    mysin = myobj.add_variable(idx, sensore2, 0, ua.VariantType.Float)
'''
    obj = str(sys.argv[5])
    myobj = server.nodes.objects.add_object(idx, obj)
    
    #VADO A DEFIENRE I VARI SENSORI
    sensore1 = str(sys.argv[6])
    sensore2 = str(sys.argv[7])
    myvar = myobj.add_variable(idx, sensore1, 6.7)
    mysin = myobj.add_variable(idx, sensore2, 0, ua.VariantType.Float)
    myvar.set_writable()    # Set MyVariable to be writable by clients
    mystringvar = myobj.add_variable(idx, "MyStringVariable", "Really nice string")
    mystringvar.set_writable()  # Set MyVariable to be writable by clients
    myguidvar = myobj.add_variable(NodeId(uuid.UUID('1be5ba38-d004-46bd-aa3a-b5b87940c698'), idx, NodeIdType.Guid),
                                   'MyStringVariableWithGUID', 'NodeId type is guid')
    mydtvar = myobj.add_variable(idx, "MyDateTimeVar", datetime.utcnow())
    mydtvar.set_writable()    # Set MyVariable to be writable by clients
    myarrayvar = myobj.add_variable(idx, "myarrayvar", [6.7, 7.9])
    myarrayvar = myobj.add_variable(idx, "myStronglytTypedVariable", ua.Variant([], ua.VariantType.UInt32))
    myprop = myobj.add_property(idx, "myproperty", "I am a property")
    mymethod = myobj.add_method(idx, "mymethod", func, [ua.VariantType.Int64], [ua.VariantType.Boolean])
    multiply_node = myobj.add_method(idx, "multiply", multiply, [ua.VariantType.Int64, ua.VariantType.Int64], [ua.VariantType.Int64])

    # import some nodes from xml
    server.import_xml("custom_nodes.xml")

    # creating a default event object
    # The event object automatically will have members for all events properties
    # you probably want to create a custom event type, see other examples
    myevgen = server.get_event_generator()
    myevgen.event.Severity = 300
'''
    # starting!
    server.start()
    print("Available loggers are: ", logging.Logger.manager.loggerDict.keys())
    vup = VarUpdater(mysin)  # just  a stupide class update a variable
    vup.start()
    try:
        # enable following if you want to subscribe to nodes on server side
        #handler = SubHandler()
        #sub = server.create_subscription(500, handler)
        #handle = sub.subscribe_data_change(myvar)
        # trigger event, all subscribed clients wil receive it
        var = myarrayvar.get_value()  # return a ref to value in db server side! not a copy!
        var = copy.copy(var)  # WARNING: we need to copy before writting again otherwise no data change event will be generated
        var.append(9.3)
        myarrayvar.set_value(var)
        mydevice_var.set_value("Running")
        myevgen.trigger(message="This is BaseEvent")
        #server.set_attribute_value(myvar.nodeid, ua.DataValue(9.9))  # Server side write method which is a but faster than using set_value
        server.set_attribute_value(myvar_0_0.nodeid, ua.DataValue(9.9))  # Server side write method which is a but faster than using set_value

        sleep = int(sys.argv[3])

        while 15 == 15:
              temp = random.randint(1,10)
              server.set_attribute_value(myvar_0_0.nodeid, ua.DataValue(temp))
              print("Nuovo valore myvar_0_0 : ", temp )
              time.sleep(sleep)

        embed()
    finally:
        vup.stop()
        server.stop()

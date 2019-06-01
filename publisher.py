import sys
import paho.mqtt.client as paho

broker="postman.cloudmqtt.com"
port=16450

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

msg = sys.argv[1] if sys.argv[1] else 'nada'
client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
# client1.username_pw_set(username='yeti', password='@SnowTime')
client1.username_pw_set(username='yeti', password='@SnowTime')
client1.connect("postman.cloudmqtt.com", 16450, 60)
ret = client1.publish("Portao", payload=msg)                   #publish
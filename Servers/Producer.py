
import time
import requests
import threading
import flask
import sys
import random
import socket


ORDER_ID = 1 
queue = []
order_list = []

app = flask.Flask(__name__)
@app.get("/start/")
def start():
    global active_status
    active_status = True
    return flask.redirect(flask.url_for("display_orders"))
@app.get("/stop/")
def stop():
    global active_status
    active_status = False
    return flask.redirect(flask.url_for("display_orders"))
def generate_orders():
    seed_value = random.randrange(sys.maxsize)
    random.seed(seed_value)
    items = []
    
    
    for _ in range(random.randint(1,5)):
        items.append(random.randint(1,10))
    global queue
    global order_number
    order = dict()
    order["id"] = ORDER_ID
    order["items"] = items
    global ORDER_ID
    ORDER_ID += 1


    while True:
        while active_status:
            queue.insert(0, f"{order_number}")
            order_number +=1
            ORDER_ID += 1
            time.sleep(1)
        time.sleep(3)
def queue_order_extractor():
    global queue
    while True:
        if len(queue) > 0:
         order = queue.pop()
         requests.post("http://localhost:5001/orders/", json=order)
         time.sleep(1)
        else:
            time.sleep(1)
    
extractor_served_order_threads = 3
generator_order_threads = 10
order_number = 0
active_status = False
order_extractors = [threading.Thread(target=queue_order_extractor) for i in range(extractor_served_order_threads)]
order_generator = [threading.Thread(target = generate_orders) for i in range(generator_order_threads)]

if __name__ == '__main__':
    for thread in order_extractors:
        thread.start()
    for thread in order_generator:
        thread.start()
    app.run(host='127.0.0.1', port=6000)




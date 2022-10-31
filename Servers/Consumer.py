import threading 
import time 

import flask

import requests

order_stack = []
app = flask.Flask(__name__)
@app.post("/orders/")
def put_order():
    global order_stack
    order_stack.append(flask.request.json)
    return flask.jsonify({"status" : "succes"})
def order_getter():
    global order_stack
    while True:
        if len(order_stack) > 0:
            order = order_stack.pop()
            requests.put("http://localhost:5000/orders/", json = order)
            time.sleep(1)
        else:
            time.sleep(1)
        extractor_served_order_threads = 3
        order_getter = [threading.Thread(target=order_getter)for i in range(extractor_served_order_threads)]
        if __name__ == '__main__':
            for thread in order_getter:
                thread.start()
            app.run(host='127.0.0.1', port=6001)

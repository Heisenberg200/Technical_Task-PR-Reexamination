import threading 
import time 
import flask
import requests
import concurrent.futures

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
        with concurrent.futures.ThreadPoolExecutor() as executor:
            result = [executor.submit(put_order,order_getter) for order_getter in range(extractor_served_order_threads)]
            for f in concurrent.futures.as_completed(result):
                pass
         
       
        if __name__ == '__main__':
            for thread in order_getter:
                thread.start()
            app.run(host='127.0.0.1', port=6001)

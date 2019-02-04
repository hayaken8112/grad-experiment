import sys
from bottle import Bottle,route,post,request, run, HTTPResponse
import base64
import io
import simplejson as json
sys.path.append('./code')
import argparse
import collections as cl

app = Bottle()
sentences_1 = []
sentences_2 = []

@app.post('/save')
def index():
    print(request.remote_addr)
    jsontext = request.forms.get("text")
    print(jsontext)
    mode = json.loads(jsontext)["mode"]
    sentence = json.loads(jsontext)["sentence"]
    if mode == 1:
        sentences_1.append(sentence)
    elif mode == 2:
        sentences_2.append(sentence)
    else:
        print("mode error")
        print(sentence)

    r = HTTPResponse(status=200)
    r.set_header('Content-Type', 'application/json')
    return r


if __name__ == "__main__":
    print('name:')
    name = input('>> ')
    run(app=app, host='10.13.255.14', port=8181, debug=True )
    output = cl.OrderedDict()
    output["name"] = name
    output["data"] = cl.OrderedDict({"1":sentences_1, "2":sentences_2})
    fw = open(f"./data_files/data_{name}.json", 'w')
    json.dump(output,fw)
    print(output)
    fw.close()

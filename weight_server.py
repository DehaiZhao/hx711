from flask import Flask,request,Response
import json
from sensors import get_result,get_all
import base64
import os

app = Flask(__name__)

@app.route('/debug/')
def show_debug():
    result,result_o,ti,tc = get_all()
    return json.dumps({'res':result,'res_o':result_o,'ti':ti,'tc':tc})

@app.route('/speech/',methods=['POST'])
def play():
    tmp_base64 = json.loads(request.json)['mp3_b64']
    tmp_mp3 = base64.b64decode(tmp_base64)
    with open('tmp.mp3','wb') as f:
        f.write(tmp_mp3)
    os.system('omxplayer tmp.mp3')
    return Response('done!')

@app.route('/')
def show_weight():
    result = get_result()
    return json.dumps({'res':result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)

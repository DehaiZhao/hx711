import requests
import time
import json
import base64

if __name__=='__main__':
    upload_url='http://192.168.2.88:8888/speech/'
    with open('auido.mp3','rb') as f:
        tmp_json = json.dumps({'mp3_b64':base64.b64encode(f.read())})
    rest = requests.post(upload_url,json=tmp_json)
    print rest.text

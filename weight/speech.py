#coding:utf-8
from aip import AipSpeech
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
APP_ID = '10698113'
API_KEY = 'ja32ZxALpKiEimuAR79vgucg'
SECRET_KEY = '71poAuMfDopsuCnTv8igL2UBm6TZiCIP'

client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)

result = client.synthesis('你好百度','zh',1,{'vol':5,'spd':5,'per':0,})
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)


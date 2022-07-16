import requests
import json
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import datetime
import collections
api1=requests.get('https://pharmanlp-177020.uc.r.appspot.com/api/1/StudyHack/ae/subject/list',verify=False)
api2=requests.get('https://pharmanlp-177020.uc.r.appspot.com/api/1/StudyHack/cm/subject/list',verify=False)
ae_str=json.loads(api1.text)
cm_str1=json.loads(api2.text)
Sub_id_ae=pd.DataFrame(ae_str)
print(Sub_id_ae.head())
print()
Sub_ID_cm=pd.DataFrame(cm_str1)
print(Sub_ID_cm.head())
#Sub_id_ae['data']
c=requests.get('https://pharmanlp-177020.uc.r.appspot.com/api/1/StudyHack/ae/subject/105792/list', verify=False)
d=requests.get('https://pharmanlp-177020.uc.r.appspot.com/api/1/StudyHack/cm/subject/105792/list',verify=False)
op=json.loads(c.text)
pd.DataFrame(op)

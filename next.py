import requests
import json
import warnings
#warnings.filterwarnings('ignore')
import pandas as pd
import os
api1=requests.get('https://pharmanlp-177020.uc.r.appspot.com/api/1/StudyHack/ae/subject/list', verify=False)
api2=requests.get('https://pharmanlp-177020.uc.r.appspot.com/api/1/StudyHack/cm/subject/list', verify=False)
ae_str=json.loads(api1.text)
cm_str1=json.loads(api2.text)
Sub_id_ae=pd.DataFrame(ae_str)
print(Sub_id_ae.head())
Sub_ID_cm=pd.DataFrame(cm_str1)
print(Sub_ID_cm.head())
ls_data = []
for i in Sub_id_ae['data']:
    c1=requests.get(f'https://pharmanlp-177020.uc.r.appspot.com/api/1/StudyHack/ae/subject/{i}/list', verify=False)
    dct1=json.loads(c1.text)
    count_ae=pd.DataFrame(dct1)
    for j in count_ae['data']:
        ls_data.append(j)
cm_data2 = []
for i in Sub_ID_cm['data']:
    d = requests.get(f'https://pharmanlp-177020.uc.r.appspot.com/api/1/StudyHack/cm/subject/{i}/list', verify=False)
    result_2 = json.loads(d.text)
    data_cm = pd.DataFrame(result_2)
    for j in data_cm['data']:
        cm_data2.append(j)
def type1_check(ae_table, cm_table):
    first_list = []
    for cm_row in cm_table:
        for ae_row in ae_table:
            payload = {}
            payload['formname'] = "Fetch formname from cmrow"
            payload['formid'] = "Fetch formid from cmrow"
            payload['formidx'] = "Fetch formidx from cmrow"
            payload['type'] = 'TYPE1'
            payload['subjectid'] = "Fetch subjid from cmrow"
            first_list.append(payload)
            first_list.to_csv('ae,cm_info_new.csv', sep = '\t')

    return first_list
type1_check()
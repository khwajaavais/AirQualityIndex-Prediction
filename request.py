# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 19:47:21 2020

@author: khwaja
"""


import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'T':2,'TM':2,'Tm':2,'SLP':2,'H':2,'V':2,'VV':2,'VM':2 })

print(r.json())
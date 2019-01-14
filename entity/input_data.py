# -*- coding: utf-8 -*-
import json
class InputData:
     def __init__(self, date, headline, body, label, delta):
        self.date = date
        self.headline = headline
        self.body = body
        self.label = label
        self.delta = delta
        
def __object_decoder(obj):
     if '__type__' in obj and obj['__type__'] == 'InputData':
         return InputData(obj['date'], obj['headline'], obj['body'], obj['label'], obj['delta'])
     return obj
 
def fromJson(data):
     return json.loads(data, object_hook=__object_decoder)
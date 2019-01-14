# -*- coding: utf-8 -*-
import json
class ProcessedData:
    def __init__(self, date, headline, label, delta, unigrams, bigrams):
        self.date = date
        self.headline = headline
        self.label = label
        self.delta = delta
        self.unigrams = unigrams
        self.bigrams = bigrams
    
def __object_decoder(obj):
     if '__type__' in obj and obj['__type__'] == 'ProcessedData':
         return ProcessedData(obj['date'], obj['headline'], obj['label'], obj['delta'], obj['unigrams'], obj['bigrams'])
     return obj
 
def fromJson(data):
     return json.loads(data, object_hook=__object_decoder)

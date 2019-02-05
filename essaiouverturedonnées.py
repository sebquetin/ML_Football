#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 13:45:18 2019

@author: quetin
"""
import matplotlib.pyplot as plt
from pylab import *
import os
import json
import numpy as np
import pandas as pd

with open('open-data-master/data/matches/43.json') as match_data:
    match_dict = json.load(match_data) #la on met dans un dictionnaire les matches de la coupe du monde 

match_str = json.dumps(match_dict)  #la on met dans un string
print(type(match_dict))

#data_dict.get("match_id")
#print(data_dict[0]["match_id"])
print(np.shape(match_dict)[0])
compteur=0
idmatchworldcup=np.zeros(64)
for cle in range(np.shape(match_dict)[0]):
   print(match_dict[cle]["match_id"])
   idmatchworldcup[cle]=match_dict[cle]["match_id"]
   compteur+=1
print("il y a " + str(compteur) + " matches")
   
#for i in range(6):
#    print(i)


with open('open-data-master/data/events/7586.json') as event7586_data:
    event7586_dict = json.load(event7586_data) #la on met dans un dictionnaire les evenements des matches

event7586_str = json.dumps(event7586_dict) 

#print(type(event7586_dict[0]))
#print(event7586_dict[0].values())
print(event7586_dict[6].keys())
#print(event7586_dict[0].items())
#event7586_dict.values
      #event7586_dict.items
eventsidtirmatch7586=[]
eventsidbutmatch7586=[]
compteurtir=0
compteurbut=0
for i in range(np.shape(event7586_dict)[0]):
   if event7586_dict[i]['type']['id']==16:
       compteurtir+=1
       eventsidtirmatch7586+=[event7586_dict[i]['id']]
       if event7586_dict[i]['shot']['outcome']['id']==97:
           compteurbut+=1
           eventsidbutmatch7586+=[event7586_dict[i]['id']]
           
print(eventsidbutmatch7586)
#print(size(eventsidbutmatch7586))
print(eventsidtirmatch7586)

#on voulait trouver un moyen simple de selectionner ce qui nous interesse mais ca marche pas
#print(event7586_dict[9]['type']['id']==16)

#print(event7586_dict[event7586_dict[9]['type']['id']==16])  
   #eventsidmatch7586[cle]=events7586_dict[cle]["match_id"]

print("il y a " + str(compteurtir) + " tirs")

print("il y a " + str(compteurbut) + " buts")




#print(event_dict[id=97])



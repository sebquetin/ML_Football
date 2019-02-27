#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 11:10:31 2019

@author: quetin
"""

import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
import os
import json
import numpy as np


def matchescoupedumonde():
    with open('open-data-master/data/matches/43.json') as match_data:
        match_dict = json.load(match_data) #la on met dans un dictionnaire les matches de la coupe du monde 
        
        world_cup_match=[match['match_id'] for match in match_dict]
    return world_cup_match


def evenements(matches):
    events = []
    for i in matches:
        with open('open-data-master/data/events/{}.json'.format(i), encoding="utf-8") as event_data:
            event = json.load(event_data)
            events += event
    return events

def createdataframe(evenements):
    
    df_events = pd.DataFrame(evenements)
    df_shot = df_events[df_events['type'].map(lambda x: x['id']==16)]
    df_to_study=df_shot[['player','position','play_pattern','period','shot','location','timestamp']]
    df_to_study["outcome"]=df_to_study["shot"].map(lambda x : x["outcome"]["name"])
    df_to_study["technique"]=df_to_study["shot"].map(lambda x : x["technique"]["name"])
    
    df_to_study["environnement"]=df_to_study["shot"].map(lambda x : x["freeze_frame"] if 'freeze_frame' in x else False)
    df_to_study["stat"]=df_to_study["shot"].map(lambda x : x["statsbomb_xg"])
    df_to_study["1V1"]=df_to_study["shot"].map(lambda x : x["one_on_one"] if 'one_on_one' in x else False)
    df_to_study=df_to_study.drop("shot",1)
    df_to_study["poste"]=df_to_study["position"].map(lambda x : x["name"])
    df_to_study=df_to_study.drop("position",1)
    df_to_study["joueur"]=df_to_study["player"].map(lambda x : x["name"])
    df_to_study=df_to_study.drop("player",1)
    
    df_to_study["situation"]=df_to_study["play_pattern"].map(lambda x : x["name"])
    df_to_study=df_to_study.drop("play_pattern",1)
    return df_to_study
    
    
print(createdataframe(evenements(matchescoupedumonde())))


def angle_de_tir(position):
    if position[0]>60:
        if position[1]>44:
            perpendiculaire=np.sqrt((position[0]-120)**2)
            audessus=np.sqrt((position[0]-120)**2+(position[1]-36)**2)
            endessous=np.sqrt((position[0]-120)**2+(position[1]-44)**2)
            angledessus=np.arccos(perpendiculaire/audessus)
            angledessous=np.arccos(perpendiculaire/endessous)
            angledetir=angledessus-angledessous
            
            
        elif position[1]<36:
            perpendiculaire=np.sqrt((position[0]-120)**2)
            audessus=np.sqrt((position[0]-120)**2+(position[1]-36)**2)
            endessous=np.sqrt((position[0]-120)**2+(position[1]-44)**2)
            angledessus=np.arccos(perpendiculaire/audessus)
            angledessous=np.arccos(perpendiculaire/endessous)
            angledetir=angledessous-angledessus
        else:
            perpendiculaire=np.sqrt((position[0]-120)**2)
            audessus=np.sqrt((position[0]-120)**2+(position[1]-36)**2)
            endessous=np.sqrt((position[0]-120)**2+(position[1]-44)**2)
            angledessus=np.arccos(perpendiculaire/audessus)
            angledessous=np.arccos(perpendiculaire/endessous)
            angledetir=angledessus+angledessous
            
        
    else:

        if position[1]>44:
            perpendiculaire=np.sqrt((position[0]-0)**2)
            audessus=np.sqrt((position[0]-0)**2+(position[1]-36)**2)
            endessous=np.sqrt((position[0]-0)**2+(position[1]-44)**2)
            angledessus=np.arccos(perpendiculaire/audessus)
            angledessous=np.arccos(perpendiculaire/endessous)
            angledetir=angledessus-angledessous
            
            
        elif position[1]<36:
            perpendiculaire=np.sqrt((position[0]-0)**2)
            audessus=np.sqrt((position[0]-0)**2+(position[1]-36)**2)
            endessous=np.sqrt((position[0]-0)**2+(position[1]-44)**2)
            angledessus=np.arccos(perpendiculaire/audessus)
            angledessous=np.arccos(perpendiculaire/endessous)
            angledetir=angledessous-angledessus
        else:
            perpendiculaire=np.sqrt((position[0]-0)**2)
            audessus=np.sqrt((position[0]-0)**2+(position[1]-36)**2)
            endessous=np.sqrt((position[0]-0)**2+(position[1]-44)**2)
            angledessus=np.arccos(perpendiculaire/audessus)
            angledessous=np.arccos(perpendiculaire/endessous)
            angledetir=angledessus+angledessous
            
    
    return angledetir*(180/math.pi)

#df["angle_de_tir"]=df["location"].map(lambda x : angle_de_tir(x))
#df[df["angle_de_tir"]>90]
    
def Ratio(environnement):
    if environnement==False:
        result=False
    else:
        df=pd.DataFrame(environnement)
        equipe=df[df["teammate"]==True].shape[0]
        adverse=df[df["teammate"]==False].shape[0]
        result=equipe/adverse
    return result

def Equipiers(environnement):
    if environnement==False:
        result=False
    else:
        df=pd.DataFrame(environnement)
        equipe=df[df["teammate"]==True].shape[0]
        result=equipe
    return result

def Adversaires(environnement):
    if environnement==False:
        result=False
    else:
        df=pd.DataFrame(environnement)
        adverse=df[df["teammate"]==False].shape[0]
        result=adverse
    return result

#df["ratio"]=df["environnement"].map(lambda x: Ratio(x))
#df[df["ratio"]==0]
#df["Equipiers"]=df["environnement"].map(lambda x: Equipiers(x))
#df["Adversaires"]=df["environnement"].map(lambda x: Adversaires(x))


def cercle5(environnement, centre):
    #racine_carre((x_point - x_centre)² + (y_centre - y_point)) < rayon
    total=0
    if environnement==False:
        total=False
    else:
        df=pd.DataFrame(environnement)
        for i in range(df.shape[0]):
           
            location=df["location"].iloc[i]
            distance=math.sqrt((location[0]-centre[0])**2+(location[1]-centre[1])**2)
            if distance<=5:
                total+=1    
    
    return total

def cercle10(environnement, centre):
    #racine_carre((x_point - x_centre)² + (y_centre - y_point)) < rayon
    total=0
    if environnement==False:
        total=False
    else:
        df=pd.DataFrame(environnement)
        for i in range(df.shape[0]):
           
            location=df["location"].iloc[i]
            distance=math.sqrt((location[0]-centre[0])**2+(location[1]-centre[1])**2)
            if distance<=10:
                total+=1    
    
    return total
#df["cercle_5_metre"]=df.apply(lambda x: cercle5(x["environnement"], x["location"]), axis=1)
#df["cercle_10_metre"]=df.apply(lambda x: cercle10(x["environnement"], x["location"]), axis=1)
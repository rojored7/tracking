#importar librerias
import cv2
import sys
from random import randint


#tipos de tracker
tacker_types = ['BOOSTING',
                'MIL',
                'KCF',
                'TLD',
                'MEADIANFLOW',
                'GOTURN',
                'MOSSE',
                'CSRT']

#definir los trackers por el nombre
def tracker_name(tracker_type):

    #crearlos por nombre
    if tracker_types == tracker_types[0]:
        tracker = cv2.TrackerBoosting_create()
    elif tracker_types == tracker_types[1]:
        tracker = cv2.TrackerMIL_create()
    elif tracker_types == tracker_types[2]:
        tracker = cv2.TrackerKFC_create()
    elif tracker_types == tracker_types[3]:
        tracker = cv2.TrackerTLD_create()    
    elif tracker_types == tracker_types[4]:        
        tracker = cv2.TrackerMedianFlow_create()
    elif tracker_types == tracker_types[5]:
        tracker = cv2.TrackerGOTURN_create()
    elif tracker_types == tracker_types[6]:
        tracker = cv2.TrackerMOSSE_create()
    elif tracker_types == tracker_types[7]:
        tracker = cv2.TrackerCSRT_create()

    #else
    else:
        tracker = None
        print('diga algo')
        print('seleccione mijo')
        for tr in tracker_types:
            print(tr)
    #retorna
    return tracker

if __name__ == '__main__':
    print("es lo que hay MOSSE\n")
    for tr in tracker_types:
        print(tr)
    
    
        
    
    

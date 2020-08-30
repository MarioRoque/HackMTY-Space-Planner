# -*- coding: utf-8 -*-

"""
Created on Sat Aug 29 12:41:06 2020

@authors: 
   Ricardo Cazares 
   Mario Roque 
   Greg Espinoza
   Javier Garcia      
"""

"""
    Inputs: 
        -Maximo de personas
        -Numero de mesas
        -Threshold de personas
        -Cuatro puntos para el tamaño del cuarto.
        
    Outputs: 
        - JSON, con Array de coordenadas
"""

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import matplotlib.pyplot as plt
import numpy as np
from flask import request, make_response, jsonify



#Global variables
usableTables = 0
numberTables = 0
percentajeOfUse = 0
minDistance = 0
debugFlag = True

tables_filtered = None
selected_polygon  = None
walking_polygon = None
emergency_doors  = None

polygons = {
    "T": [[0,7],[0,9],[13,9],[13,16],[15,16],[16,0],[13,0],[13,7]],
    "box1" : [ [0,0],[1,0],[1,1],[0,1]],
    "cuña" :[[0,0],[0,2],[3,2],[3,0],[2,0],[2,1],[1,1],[1,0]],
    "church" : [[1,0],[1,2],[0,2],[0,3],[1,3],[1,4],[2,4],[2,3],[3,3],[3,2],[2,2],[2,0]],
    "E": [[0,0],[0,2],[14,2],[14,7],[0,7],[0,9],[14,9],[14,15],[0,15],[0,17.5],[14.5,17.5],[14.5,0]]
}

walkingPath = {
    "test": []
    }

doors = {"box1" : [ [0,0]]}

#layout[0] = Room Corners, #layout[1] = Path para caminar  #layout[2] = Table position
layout = [[0,0],[0,0],[0,0]]


def debug_walkingPath():
    #This function generates a walking path separated on columns by 3 meters
    
    global walkingPath
    
    for i in range(0,15):
        y = i+1.5
        if(isInside([1,y], polygons["box1"])):
            walkingPath['test'].append([1,y])

         
    for i in range(0,15):
        y = i+1.5
        if(isInside([1,y], polygons["box1"])):
            walkingPath['test'].append([4,y])


    for i in range(0,15):
        y = i+1.5
        if(isInside([1,y], polygons["box1"])):
            walkingPath['test'].append([7,y])

    for i in range(0,15):
            y = i+1.5
            if(isInside([1,y], polygons["box1"])):
                walkingPath['test'].append([10,y])


    for i in range(0,15):
            y = i+1.5
            if(isInside([1,y], polygons["box1"])):
                walkingPath['test'].append([13,y])
    return 0


def readInputs():
    global MaxPeople
    global numberTables
    global percentajeOfUse
    global minDistance 
    #roomCorners = input()
    
    MaxPeople = input()
    numberTables = input()
    percentajeOfUse = input()
    minDistance = input()
    
    return 0


    
def createRoom(polygon, walkingPath,tables):
    '''
       Inputs: polygon e.g [[0,0],[1,1],...] and a walking path walkingPath e.g [[0,0],[1,1],...]
    '''
    rx,ry = zip(*polygon)
    px,py = zip(*walkingPath)
    tx,ty = zip(*tables)
    plt.scatter(rx,ry, color = 'k')
    plt.scatter(px,py, color = 'g')
    plt.scatter(tx,ty, color = 'b')

    return [[rx,ry],[px,py],tables]

def distributeRandom(polygon,usableTables, walking_polygon,scaleX,scaleY):
    '''
    this function distributes the tables on random places, it needs to verify the distances
    '''
    global minDistance
    global numberTables
    tables = []

    bigger = scaleX if scaleX > scaleY else scaleY

    point = np.random.random_sample((1, 2))*bigger
    for i in range(0, numberTables):
        point = np.random.random_sample((1, 2))*bigger
        while(not isInside([point[0][0],point[0][1]],polygon)) or (Polygon(polygon).exterior.distance(Point(point[0][0],point[0][1]).buffer(.3)) < minDistance or isInside([point[0][0],point[0][1]],walking_polygon)):
            point = np.random.random_sample((1, 2))*bigger
        
        tables.append([point[0][0], point[0][1]])
        
    return tables


def excludePoints(object_coordinates,polygon, inside=True):
    '''
    Input: Array of coordinates e.g [[0,0],[1,1]] and polygon e.g [[0,0],[1,1],...]
    '''
    for point in object_coordinates:
        if inside:
            exclude_point_inside(point,polygon)
        else:
            exclude_point_outside(point,polygon)
    return



def isInside(point, polygon):

    '''
    Input: Point e.g [0.0] and and polygon e.g [[0,0],[1,1],...]
    return boolean
    '''
    point = Point(point)
    polygon = Polygon(polygon)
    return polygon.contains(point)



def verifyDistace(A,all_points):
    global minDistance
    counter = 0
    list_to_delete = []
    for B in all_points:
        if A != B:
            distance = Point(A).distance(Point(B))
            if distance < minDistance:
                #print("Point too close",A,B,distance)
                list_to_delete.append(counter)
        counter += 1
        
        
    return list_to_delete

def verifyGlobalDistance(all_points):
    list_to_delete = []
    for point in all_points:
        list_to_delete += verifyDistace(point,all_points)

    #print("Found too close",list_to_delete)
    list_to_delete = [all_points[x] for x in list_to_delete ]
    
    return [x for x in all_points if x not in list_to_delete]


def getAvgDistance(A, all_points):
    distances = []
    for B in all_points:
        if A != B:
            distances.append(Point(A).distance(Point(B)))
    print(min(distances))
    return sum(distances)/len(distances)
def getGlobalDistance(all_points):
    distances = []
    for point in all_points:
        distances.append(getAvgDistance(point,all_points))
    return sum(distances)/len(distances)
        

def createJSON():
    response = {

    "tables": tables_filtered,
    "room": selected_polygon,
    "walkingPath": walking_polygon,
    "emergency_doors": emergency_doors,
    "generated" : len(tables_filtered),

    }
    return make_response(jsonify(response)), 200

def main(info):
    global usableTables
    global numberTables
    global percentajeOfUse
    global minDistance
    global tables_filtered
    global selected_polygon
    global walking_polygon
    global emergency_doors
    
    tableSize = info["tableSize"] #Radio de nuestra mesa# <<<<<---------
    numberTables = info["tableNumber"]# <<<<<---------
    percentajeOfUse = info["threshold"]# <<<<<---------
    minDistance = info["distance"] 
    usableTables= int(numberTables* percentajeOfUse/100)
    debug_walkingPath()
    tables_filtered = []
    limit = 50
    counter = 0
    limit_cycles = True
    
    print(info)

    E = polygons[info["walkingPath"]] # <<<<<---------
    selected_polygon = polygons[info["polygonName"]]

    if info["polygonName"] == "box1":
        selected_polygon = [(x[0]*info["scaleX"],x[1]*info["scaleY"]) for x in selected_polygon]

    while len(tables_filtered) < usableTables and limit_cycles:
        
        left_tables = usableTables * 1000
        #print("TO BUILD",left_tables)
        tables = distributeRandom(selected_polygon,left_tables,E,info["scaleX"],info["scaleY"]) # <<<<<---------
        tables = verifyGlobalDistance(tables + tables_filtered)
        if len(tables) > 0:
            createRoom(selected_polygon,E,tables) # <<<<<---------
        
        tables_filtered = tables_filtered + [x for x in tables if x not in tables_filtered]
        counter += 1
        if counter > limit:
            limit_cycles = False
            
        print("ITERATION",counter, len(tables_filtered))

    
    walking_polygon = polygons[info["walkingPath"]]
    emergency_doors = doors[info["polygonName"]]

    #plt.show()
    return createJSON()

   
    
    
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



#Global variables
usableTables = 0
numberTables = 0
percentajeOfUse = 0
minDistance = 0
debugFlag = True

polygons = {
    "box1" : [ [0,0],[15,0],[15,15],[0,15]],
    "cuña" :[[0,0],[0,2],[3,2],[3,0],[2,0],[2,1],[1,1],[1,0]],
    "church" : [[1,0],[1,2],[0,2],[0,3],[1,3],[1,4],[2,4],[2,3],[3,3],[3,2],[2,2],[2,0]]
}

walkingPath = {
    "test": []
    }


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

def distributeRandom(polygon,usableTables):
    '''
    this function distributes the tables on random places, it needs to verify the distances
    '''
    global numberTables
    tables = []
    point = np.random.random_sample((1, 2))*10
    for i in range(0, numberTables):
        point = np.random.random_sample((1, 2))*10
        while(not isInside([point[0][0],point[0][1]],polygon)):
            point = np.random.random_sample((1, 2))*10
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

def exclude_point_inside(point, polygon):
    '''
    Input: Point e.g [0.0] and and polygon e.g [[0,0],[1,1],...]
    '''
    if isInside (point,polygon):
        #Everything is good
        pass
    else:
        #Logic to exclude this point
        pass
    return 

def exclude_point_outside(point, polygon):
    '''
    Input: Point e.g [0.0] and and polygon e.g [[0,0],[1,1],...]
    '''
    if not isInside (point,polygon):
        #Everything is good
        pass
    else:
        #Logic to exclude this point
        pass
    return 

def isInside(point, polygon):

    '''
    Input: Point e.g [0.0] and and polygon e.g [[0,0],[1,1],...]
    return boolean
    '''
    point = Point(point)
    polygon = Polygon(polygon)
    return polygon.contains(point)


def selectTables():
        
    return 0


def verifyDistace():
    
    return 0


def verifyGlobalDistance():
    
    return 0


def regeneratePoints():
    
    return 0

def warnings():

    return 0


def plotPoints():
    
    return 0

def createJSON():
    
    return 0


def receiveFromUnity():

    usableTables = 0
    numberTables = 0
    percentajeOfUse = 0
    minDistance = 0

    return 0


def sendToUnity():
    
    return 0

    
def main():
    global debugFlag
    if(debugFlag):
        debug()
    else:
        pass
    return 0

def debug():
    global usableTables
    global numberTables
    global percentajeOfUse
    global minDistance
    
    numberTables = 20
    percentajeOfUse = 50
    minDistance = 1.5
    usableTables= numberTables* percentajeOfUse/100
    debug_walkingPath()
    tables = distributeRandom(polygons['box1'],usableTables)
    createRoom(polygons['box1'],walkingPath['test'],tables)

 
main()   
    
    
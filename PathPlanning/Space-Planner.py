# -*- coding: utf-8 -*-

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


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
        -Threshold de personas
        -Cuatro puntos para el tamaño del cuarto.
        
    Outputs: 
        - JSON, con Array de coordenadas

"""

polygons = {
    "box1" : [ [0,0],[15,0],[15,15],[0,15]],
    "cuña" :[[0,0],[0,2],[3,2],[3,0],[2,0],[2,1],[1,1],[1,0]],
    "church" : [[1,0],[1,2],[0,2],[0,3],[1,3],[1,4],[2,4],[2,3],[3,3],[3,2],[2,2],[2,0]]
}



def readInputs():
    
    return 0

def createRoom():
    
    
    return 0


def distributeRandom():
    
    return 0

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

def sendToUnity():
    
    return 0

    
def main():
    
    
    return 0
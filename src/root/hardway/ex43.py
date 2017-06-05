'''
Created on Apr 26, 2017

@author: pneela

class hirarchy
* Map
  - next_scene
  - opening_scene
* Engine
  - play
* Scene
  - enter
  * Death
  * Central Corridor
  * Laser Weapon Armory
  * The Bridge
  * Escape Pod

'''

class Scene(object):
    
    def enter(self):
        pass
    
class Engine(object):
    
    def __init__(self, scene_map):
        pass    
            
    def play(self):
        pass
    

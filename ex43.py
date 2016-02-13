# from python import exit and radom integer generator modules
from sys import exit
from random import randint

# class that has-a function "enter" that takes self parameter
class Scene(object):

    def enter(self):
        # this block is empty: pass
        pass


# class with:
class Engine(object):
    
    # has-a _init_ that takes self and scene_map parameters;
    def __init__(self, scene_map):
        pass
    
    # has-a function "play" that takes self as a parameter
    def play(self):
        pass


# make a class "Death" which has function "enter" with self parameter that is-a "Scene" 
class Death(Scene):

    def enter(self):
        pass


# make a class "CentralCorridor" that is-a "Scene" that has a function "enter"
class CentralCorridor(Scene):

    def enter(self):
        pass


# make a class "LaserWeaponArmory" that is-a "Scene" with a function "enter"
class LaserWeaponArmory(Scene):

    def enter(self):
        pass


# make a class "TheBridge" that is-a "Scene" with function "enter"
class TheBridge(Scene):

    def enter(self):
        pass


# make a class "EscapePod" that is-a "Scene" with function "enter"
class EscapePod(Scene):

    def enter(self):
        pass


# make a class "Map" that has-a:
class Map(object):

    # _init_ with self and start_scene parameters
    def __init__(self, start_scene):
        pass

    # function "next_scene" that takes self and scene_name parameters
    def next_scene(self, scene_name):
        pass

    # function "opening_scene" with self
    def opening_scene(self):
        pass


# set "a_map" to an instance of class "Map" with central_corridor parameter 
a_map = Map('central_corridor')
# set "a_game" to an instance of class "Engine" with "a_map" parameter
a_game = Engine(a_map)
# from class "a_game" get function "play" and run it!
a_game.play()
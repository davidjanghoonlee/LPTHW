# from python import exit and radom integer generator modules
from sys import exit
from random import randint

# class that has-a function "enter" that takes self parameter
class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


# class with:
class Engine(object):
    
    # has-a _init_ that takes self and scene_map parameters;
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    # has-a function "play" that takes self as a parameter
    def play(self):
        curretns_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while curretns_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
        # print this out the last scene
        current_scene.enter()


# make a class "Death" that is-a "Scene" which has function "enter" with self parameter
class Death(Scene):
    
    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1]
        exit(1)

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
        self.start_scene = start_scene

    # function "next_scene" that takes self and scene_name parameters
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
        
    # function "opening_scene" with self
    def opening_scene(self):
        return self.next_scene(self.start_scene)


# set "a_map" to an instance of class "Map" with central_corridor parameter 
a_map = Map('central_corridor')
# set "a_game" to an instance of class "Engine" with "a_map" parameter
a_game = Engine(a_map)
# from class "a_game" get function "play" and run it!
a_game.play()


class Scene:
    descriptions = dict(hill="You are on a hill",
                        valley = "You are in a valley",
                        mountain = "You are on a mountain")
    
    def __init__(self, descript):
        self.location = Scene.descriptions[descript]
        self.accepted_actions = ['up','north']
        

def God():
    Adam = Man()
    Eve = Woman()
    return [Adam, Eve]
    
class Human():
    def __init__(self):
        pass

class Man(Human):
    def __init__(self):
        super().__init__()

class Woman(Human):
    def __init__(self):
        super().__init__()
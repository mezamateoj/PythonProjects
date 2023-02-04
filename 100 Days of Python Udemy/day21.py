# How inheritance oop works

class Animal:

    def __init__(self) -> None:
        self.num_eyes = 2

    def breathe(self):
        print('Inhale, exhale')


class Fish(Animal):
    
    def __init__(self) -> None:
        super().__init__()

    def breathe(self):
        super().breathe()
        print('doing this underwater')

    def swin(self):
        print('moving in water')

nemo = Fish()
nemo.swin()
nemo.breathe()
print(nemo.num_eyes)
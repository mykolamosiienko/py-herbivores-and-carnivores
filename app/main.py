class Animal:

    alive = []
    
    def __init__(self, name: str) -> None:
        self.health = 100
        self.name = name
        self.hidden = False
        Animal.alive.append(self)
    
    def __repr__(self) -> str:
        a ={}
        a["Name"] = self.name
        a["Health"] = self.health
        a["Hidden"] = self.hidden
        return f"{a}"


class Carnivore(Animal):
    def bite(self, herby) -> None:
        if isinstance(herby, Herbivore) and not herby.hidden:
            herby.health -= 50
            if herby.health <= 0 and herby in Animal.alive:
                Animal.alive.remove(herby)
    
class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

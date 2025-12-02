class Animal:

    alive = []

    def __init__(self, name: str) -> None:
        self.health = 100
        self.name = name
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        anim ={}
        anim["Name"] = self.name
        anim["Health"] = self.health
        anim["Hidden"] = self.hidden
        return f"{anim}"


class Carnivore(Animal):
    def bite(self, herby: Herbivore) -> None:
        if isinstance(herby, Herbivore) and not herby.hidden:
            herby.health -= 50
            if herby.health <= 0 and herby in Animal.alive:
                Animal.alive.remove(herby)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden

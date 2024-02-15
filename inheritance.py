class Human:
    def james(self):
        print("i can walk")

    def tom(self):
        print("can run")


class Racoon(Human):
    def racoon(self):
        print("can smile")


hh = Racoon()
print(f"mimi hh.james() and hh.tom() but i cant hh.racoon()")

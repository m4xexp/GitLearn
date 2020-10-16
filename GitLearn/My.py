class Me:

    def __init__ (self, name, ign):
        self.name = name
        self.ign = ign

    def Coding (self, whichCode):
        print('{} code {}'.format(self.name, whichCode))

    def play (self, game):
        print('{} play {}'.format(self.ign, game))


if __name__ == "__main__":
    me = Me('Max', 'M4XeXP')
    me.play('Princone')
    me.Coding('Python')
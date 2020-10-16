class Me:

    def __init__ (self, name, ign):
        self.name = name
        self.ign = ign

    def Coding (self, whichCode):
        print('{} code {}'.format(self.name, whichCode))

    def play (self, game):
        print('{} play {}'.format(self.ign, game))

    def Sleep (self, sleepTime):
        print('I sleep for {} hours'.format(sleepTime))

    def wakeup (self, awakeTime):
        print("I wakeup at {} o'clock".format(awakeTime))

if __name__ == "__main__":
    me = Me('Max', 'M4XeXP')
    me.play('Princone')
    me.Coding('Python')
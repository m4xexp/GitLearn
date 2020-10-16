class myPower:
    def __init__(self, atk, hp, gold):
        self.atk = atk
        self.hp = hp
        self.gold = gold
    
    def Attack(self):
        print(' Max attack slime for {} damage!!'.format(self.atk))

if __name__ == "__main__":
    start = myPower("50", "100", "9999")
    start.Attack()
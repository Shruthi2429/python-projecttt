Shruthi.p/1AY24AI104/O Sec
import zombiedice

class MyZombieBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()  # first roll

        brains = 0
        shotguns = 0

        # Simple strategy: stop rolling after 2 shotguns
        while diceRollResults is not None:
            for die in diceRollResults:
                if die['brain']:
                    brains += 1
                elif die['shotgun']:
                    shotguns += 1

            if shotguns >= 2:
                break
            else:
                diceRollResults = zombiedice.roll()  # roll again

# Required list of bots
zombies = (
    MyZombieBot(name='ShrutiBot'),
    zombiedice.examples.RandomCoinFlipZombie(name='RandomBot'),
    zombiedice.examples.MinNumShotgunsThenStops(name='SafeBot'),
    zombiedice.examples.MinNumShotgunsThenStops(name='RecklessBot', minShotguns=3),
)

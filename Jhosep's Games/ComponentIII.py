
#company name
#game name
#team members
#two sentence explanation of the game's objective

from gamelib import*#import game library

#objects and initial settings
game = Game (800,600,"Jumping Smurf")
bk = Image("bk.jpg",game)
bk.resizeTo(game.width, game.height)
smurf = Animation("smurf_sprite.png",16,game,512/4,512/4)

#Level 1 - game loop

while not game.over:
    game.processInput()
    #game.scrollBackground("left",2)
    bk.draw()
    smurf.draw()
    game.update(30)

game.over = False
#Level 2 - game loop
while not game.over:
    game.processInput()
    #game.scrollBackground("left",2)
    bk.draw()
    smurf.draw()
    game.update(30)

game.quit()

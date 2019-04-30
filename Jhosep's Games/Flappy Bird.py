from gamelib import*
game=Game(800,600,"Flappy Bird")
bk=Image("day.png",game)
bk.resizeTo(800,600)
game.setBackground(bk)

bird=Animation("bird.png",3,game,132/3,34)


bar=Animation("bar.png",3,game,2100/3,110)
bar.resizeTo(game.width,bar.height)
bar.y= game.height -50

coin=Animation("coins.png",64,game,512/8,512/8)
coin.moveTo(50,550)

ring= Animation("ring.png",10,game,704/10,90)
ring.x=game.width+50
ring.setSpeed(3,90)
y=randint(150,350)

tpipe=Image("pipe_top.png",game)
bpipe=Image("pipe_bot.png",game)
tpipe.moveTo(ring.x,ring.y-200)
tpipe.moveTo(ring.x,ring.y+200)
tpipe.setSpeed(3,100)
tpipe.setSpeed(4,100)

f=Font(black,48,green,"Comic Sans MS")
f1=Font(red,20,white,"Imapct")

es=Image("EndScreen.png",game)
es.resizeTo(800,600)


gameOver=Image("gameover.png",game)
logo=Image("logo.png",game)
#star screen
while not game.over:
                 game.processInput()
                 game.scrollBackground("left",2)
                 bk.draw()
                 logo.draw()
                 game.drawText("Press [SPACE] to start the game",game.width/2-85,game.height-100,f1)
                 if keys.Pressed[K_SPACE]:
                     game.over=True
                 game.update(30)

game.over=False


 #Game Screen
while not game.over :
             game.processInput()
             game.scrollBackground("left",2)
             bk.draw()
             bird.move()
             bird.y+=2
             coin.draw()
             ring.move()              
             tpipe.move()
             bpipe.move()
             bar.draw()
             coin.draw()
             if ring.isOffScreen("left"):
                ring.x=game.width+50                 
                ring.y=randint(100,350)
                ring.moveTo(game.width+50,y)
                ring.visible= True 
             tpipe.moveTo(ring.x,ring.y-200) 
             bpipe.moveTo(ring.x,ring.y+200)
            
             if keys.Pressed[K_SPACE]:
                bird.y-=5

             if bird.collidedWith(ring):
                game.score+=5
                ring.visible= False

             if tpipe.isOffScreen("left"):
                  y=randint(150,350)
                  bpipe.moveTo(ring.x,ring.y+200)

             if bird.collidedWith(tpipe,"rectangle") or bird.collidedWith(bpipe,"rectangle") or bird.collidedWith(bar,"rectangle"):
                gameOver.draw()
                game.over= True
                
             
             game.drawText("X   "+ str(game.score),100,530,f)
             game.displayScore()
             game.update(30)

             #End Screen
             while game.over:
                        game.processInput()
                        es.draw()
                        game.update(30)



            

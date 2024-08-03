import pgzrun
import random
TITLE= "Flappy ball"
WIDTH= 600
HEIGHT=500
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
CLR=r,g,b

class Ball:
    def __init__(self,initialx,initialy):
        self.x=initialx
        self.y=initialy
        self.vx=200
        self.vy=0
        self.radius=40
    def draw(self):
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,CLR)
ball=Ball(50,100)
GRAVITY=1000.0
def draw():
    screen.clear()
    ball.draw()

def update(dt):
    uy=ball.vy
    ball.vy+=GRAVITY*dt
    ball.y+=(uy+ball.vy)*0.5*dt 

    if ball.y>HEIGHT-ball.radius:
        ball.y=HEIGHT-ball.radius
        ball.vy=-ball.vy*0.5
        #inelastic collision
    ball.x+=ball.vx*dt
    if ball.x<ball.radius or ball.x>WIDTH-ball.radius:
        ball.vx=-ball.vx
    if ball.y<ball.radius:
        ball.vy=-ball.vy
def on_key_down(key):
    if key==keys.B and ball.y>ball.radius:
        ball.vy=-500
pgzrun.go()

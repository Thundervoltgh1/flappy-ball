import pgzrun
import random
TITLE= "Flappy ball"
WIDTH= 800
HEIGHT=600
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
GRAVITY=2000.0
def draw():
    screen.clear()
    ball.draw()

def update(dt):
    uy=ball.vy
    ball.vy+=GRAVITY*dt
    ball.y+=(uy+ball.vy)*0.5*dt 
pgzrun.go()
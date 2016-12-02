#encoding:UTF-8
#María Angélica Hernández Parada

from Graphics import *
from Myro import pickOne, randomNumber, Random
import random
win = Window("galaga", 2000, 700)
win.mode = "physics"
win.gravity = Vector(0,-9.8)

#parte de la fisica
left = Rectangle((650, 650), (680, 680))
left.bodyType = "static"
left.color = Color("green")
left.draw(win)

#Crea el rectangulo de abajo  
x=820
click=0

for x in range(4):
    for y in range(4 - x):
  
        R = Rectangle((600 + y * 100 + x *40, 260 - x * 80),
                      (600 + y * 100 + 80 + x * 40, 280 - x * 80))
        R.bodyType = "static"
        R.fill = Color(pickOne(getColorNames()))
        R.draw(win)
        R.bounce = 0
#son los rectantangulos enemigos de arriba              
def handleSpaceBar(win, event):
    points=0
    global x
    global click
    click+=1
    y = 600
    X = left.getX()
    Y = left.getY() 
    c = Circle((X, Y), 8)
    c.fill = Color("red")
    c.bounce = 1.0
    c.draw(win)
    c.body.ApplyForce( Vector(0,-50))
onMouseDown(handleSpaceBar)
#funcion que permite disparar con un click
hit=None
def collide(myfixture,otherfixture,contact):
    global hit
    hit=otherfixture.Body.UserData
    c.body.OnCollision+=collide
    while True:  
        if hit:  
            if hit.bodyType=="static":
                if hit!=c:
                    hit.undraw()
                    hit=None
#se supone deberia borrar los rectangulos enemigos al tocarlos                    
def main():    
    while True:    
        if getKeyPressed():
            key = getLastKey()
            if key == "Left":
                left.move(-5, 0)
            elif key == "Right":
                left.move(5, 0)
            win.step(.01)    
#permite el movimiento con las felchas    
win.run(main)

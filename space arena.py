#suwarnabiz@gmail.com
import os
import random
import turtle
import time
turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
turtle.setundobuffer(35)
turtle.tracer(35)

class Sprite(turtle.Turtle):
    def __init__(self,spriteshape,color,startx,starty):
        turtle.Turtle.__init__(self,shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx,starty)
        self.speed=1

    def move(self):
        self.fd(self.speed)

        if self.xcor()>290:
            self.setx(290)
            self.rt(60)
        if self.xcor()<-290:
            self.setx(-290)
            self.rt(60)
        if self.ycor()>290:
            self.sety(290)
            self.rt(60)
        if self.ycor()<-290:
            self.sety(-290)
            self.rt(60)


class Player(Sprite):
    def __init__(self,spriteshape,color,startx,starty):
        Sprite.__init__(self,spriteshape,color,startx,starty)
        self.shapesize(stretch_wid=0.6,stretch_len=1.1,outline=None)
        
        self.speed=4
    
    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed-= 1

    def is_collision(self,other):
        if (self.xcor() >=(other.xcor()-20)) and \
        (self.xcor() <=(other.xcor()+20)) and \
        (self.ycor() >=(other.ycor()-20)) and \
        (self.ycor() <=(other.ycor()+20)):
            return True
        else:
            return False
class Enemy(Sprite):
    def __init__(self,spriteshape,color,startx,starty):
        Sprite.__init__(self,spriteshape,color,startx,starty)
        self.speed=6
        self.setheading(random.randint(0,360))

        

class Ally(Sprite):
    def __init__(self,spriteshape,color,startx,starty):
        Sprite.__init__(self,spriteshape,color,startx,starty)
        self.speed=8
        self.setheading(random.randint(0,360))

        def move(self):
            self.fd(self.speed)

            if self.xcor()>290:
                self.setx(290)
                self.lt(60)
            if self.xcor()<-290:
                self.setx(-290)
                self.lt(60)
            if self.ycor()>290:
                self.sety(290)
                self.lt(60)
            if self.ycor()<-290:
                self.sety(-290)
                self.lt(60)


class Powerup(Sprite):
    def __init__(self,spriteshape,color,startx,starty):
        Sprite.__init__(self,spriteshape,color,startx,starty)
        self.speed=20
        self.setheading(random.randint(0,360))

        def move(self):
            self.fd(self.speed)

            if self.xcor()>290:
                self.setx(290)
                self.lt(60)
            if self.xcor()<-290:
                self.setx(-290)
                self.lt(60)
            if self.ycor()>290:
                self.sety(290)
                self.lt(60)
            if self.ycor()<-290:
                self.sety(-290)
                self.lt(60)

        

class Missile(Sprite):
    def __init__(self,spriteshape,color,startx,starty):
        Sprite.__init__(self,spriteshape,color,startx,starty)
        self.shapesize(stretch_wid=0.2,stretch_len=0.2,outline=None)
        self.speed=20
        self.status="ready"
        self.goto(-1000,1000)

        

    def is_collision(self,other):
        if (self.xcor() >=(other.xcor()-20)) and \
        (self.xcor() <=(other.xcor()+20)) and \
        (self.ycor() >=(other.ycor()-20)) and \
        (self.ycor() <=(other.ycor()+20)):
            return True
        else:
            return False


    def fire(self):
        if self.status == "ready":
            self.goto(player.xcor(),player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    def read(self):
        self.status = "ready"


            

    def move(self):
        if self.status=="ready":
            self.goto(-1000,1000)
            

        if self.status == "firing":
            self.fd(self.speed)

        if self.xcor () <-290 or self.xcor()>290 and \
           self.ycor() <-290 or self.xcor()>290:
            self.goto(-1000,1000)
            self.status="ready"
    
class Particle(Sprite):
    def __init__(self,spriteshape,color,startx,starty):
        Sprite.__init__(self,spriteshape,color,startx,starty)
        self.shapesize(stretch_wid=0.1,stretch_len=0.1,outline=None)
        self.goto(-1000,-1000)
        self.frame=0

    def explode(self,startx,starty):
        self.goto(startx,starty)
        self.setheading(random.randint(0,360))

    def move(self):
        self.fd(10)
        
        


class Game():
    def __init__(self):
        self.level=1
        self.score=0
        self.state="playing"
        self.pen=turtle.Turtle()
        self.lives=5

        

    def draw_border(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300,300)
        self.pen.pendown()
        for i in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown() 

    def show_status(self):
        
        self.pen.undo()
        msg ="Score %s" %(self.score),"LiVeS %s" %(self.lives)
        self.pen.goto(-300,310)
        self.pen.write(msg,font=("Arial","16","normal"))

    def show_dead(self):
        self.pen.undo()
        msg =(("You Are Dead"),
              ("Score %s" %(self.score)),
              ( "LiVeS %s" %(self.lives)))
        self.pen.goto(-320,145)
        self.pen.write(msg,font=("Arial","30","normal"))
        


    

        

game=Game()
game.draw_border()

game.show_status()
        
player=Player("triangle","white",0,0)
missile=Missile("triangle","yellow",0,0)
powerup=Powerup("triangle","green",0,0)

enemies=[]
for i in range(6):
    enemies.append(Enemy("circle","red",-290,290))
allies=[]
for i in range(6):
    allies.append(Ally("square","blue",-290,290))
particles=[]
for i in range(20):
    particles.append(Particle("circle","orange",0,0))

def ready():
    missile.status="ready"

turtle.listen()
turtle.onkey(player.turn_left,"Left")
turtle.onkey(player.turn_right,"Right")
turtle.onkey(player.accelerate,"Up")
turtle.onkey(player.decelerate,"Down")
turtle.onkey(missile.fire,"space")
turtle.onkey(ready,"v")


while True:
    time.sleep(0.02)
    
    player.move()
    #ammo.move()
    missile.move()
    #ally.move()
    powerup.move()



    

    for enemy in enemies:
        enemy.move()

        if missile.is_collision(enemy):
            x=random.randint(-250,250)
            y=random.randint(-250,250)
            enemy.goto(x,y)
            game.score+=100
            missile.status ="ready"
            game.score+=50
            game.show_status()
            for particle in particles:
                particle.goto(missile.xcor(),missile.ycor())
                particle.setheading(random.randint(0,360))

        if player.is_collision(enemy):
            x=random.randint(-250,250)
            y=random.randint(-250,250)
            missile.status="ready"
            enemy.goto(x,y)
            game.score-=20
            game.lives-=1
            game.show_status()
            

    for ally in allies:
        ally.move()
        if missile.is_collision(ally):
            x=random.randint(-250,250)
            y=random.randint(-250,250)
            ally.goto(x,y)
            missile.status ="ready"
            game.score-=50
            game.show_status()

    if missile.is_collision(powerup):
            x=random.randint(-250,250)
            y=random.randint(-250,250)
            enemy.goto(x,y)
            game.score+=100
            missile.status ="ready"
            game.score+=500
            game.show_status()
    for particle in particles:
                particle.move()
    
    if game.lives==0:
        game.show_dead()
        break
        


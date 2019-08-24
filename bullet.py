import turtle

bulletTexture = "textures/bullet.gif";

class Bullet:
    def __init__(self, args):
        self.turtle = turtle.Turtle();
        self.turtle.hideturtle();
        self.turtle.left(90);
        self.turtle.speed(0);
        self.turtle.penup();
        self.turtle.setpos(args);
        self.turtle.showturtle();
        self.turtle.shape(bulletTexture);
        self.dead = False;

    def update(self):
        self.turtle.sety(self.turtle.pos()[1] + 10);
        if self.turtle.pos()[1] > 283:
            self.dead = True;

    def isHit(self, array):
        for aliens in array:
            for alien in aliens:
                pos = self.turtle.pos();
                x = pos[0] + 5;
                y = pos[1];

                aPos = alien.turtle.pos();
                if x >= aPos[0] and x <= aPos[0] + 30:
                    if y <= aPos[1] and y >= aPos[1] -22:
                        self.dead = True;
                        alien.dead = True;

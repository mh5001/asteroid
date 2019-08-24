import turtle

class Alien:
    def __init__(self, pos, texture):
        self.turtle = turtle.Turtle();
        self.turtle.hideturtle();
        self.turtle.right(90);
        self.turtle.speed(0);
        self.turtle.penup();
        self.turtle.setpos(pos);
        self.turtle.shape(texture);
        self.dead = False;
        self.direction = 10;

        self.dead = False;
    def move(self, array):
        pos = self.turtle.pos();
        self.turtle.setx(pos[0] + self.direction);
        if pos[0] > 200 and self.direction == 10:
            for alien in array:
                alien.direction = -10;
                alien.turtle.sety(pos[1] - 20);
        if pos[0] < -210 and self.direction == -10:
            self.turtle.setx(pos[0] + 10);
            for alien in array:
                alien.direction = 10;
                alien.turtle.sety(pos[1] - 20);

def spawnAlienRow(x, y, texture):
    pos = [x, y];
    aliens = [];
    for i in range(0, 10):
        alien = Alien(pos, texture);
        pos[0] += 40;
        alien.turtle.showturtle();
        aliens.append(alien);
    return aliens;

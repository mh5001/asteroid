import turtle
import os
import time
import array

from bullet import *
from alien import *

playerTexture = "textures/player.gif";
bulletTexture = "textures/bullet.gif";
alien1Texture = "textures/alien1.gif";

# Setup ------------------------------------------------------------------------
win = turtle.Screen();
turtle.setup(500, 567);
win.bgpic("textures/background.gif");
win.update();
win.title("Space Invader");
bulletArray = [];
alienArray = [];

win.register_shape(playerTexture);
win.register_shape(bulletTexture);
win.register_shape(alien1Texture);

aliens = spawnAlienRow(-230, 200, alien1Texture);
alienArray.append(aliens);

# End Setup --------------------------------------------------------------------

player = turtle.Turtle();
player.hideturtle();
player.shape(playerTexture);
player.penup();
player.speed(0);
player.setposition(0, -230);
player.showturtle();

def keyLeft():
    pos = player.pos()[0];
    if (pos <= -220):
        return;
    player.setx(pos - 10);

def keyRite():
    pos = player.pos()[0];
    if (pos >= 220):
        return;
    player.setx(pos + 10);

def keyShoot():
    bulletArray.append(Bullet(player.pos()));

def updateBullet():
    for bullet in bulletArray:
        bullet.update();
        bullet.isHit(alienArray);
        if (bullet.dead):
            bullet.turtle.hideturtle();
            bulletArray.remove(bullet);
    win.ontimer(updateBullet, 20);

def updateAliens():
    for aliens in alienArray:
        for alien in aliens:
            alien.move(aliens);
            if (alien.dead):
                alien.turtle.hideturtle();
                aliens.remove(alien);
    win.ontimer(updateAliens, 200);

turtle.onkeypress(keyLeft, "a");
turtle.onkeypress(keyRite, "d");
turtle.onkeypress(keyShoot, "space");

updateBullet();
updateAliens();

turtle.listen();
turtle.mainloop();

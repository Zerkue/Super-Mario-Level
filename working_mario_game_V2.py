import pygame
from pygame import *
import math

pygame.init()

# Screen Setup
Screen_Height = 600
Screen_Width = 800
Screen_Size = (Screen_Width, Screen_Height)
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mario")

# Sprites for Mario
marioR1 = pygame.image.load('resources/images/mario_move0.png')
marioR2 = pygame.image.load('resources/images/mario_move1.png')
marioR3 = pygame.image.load('resources/images/mario_move2.png')

marioL1 = pygame.image.load('resources/images/mario_move02.png')
marioL2 = pygame.image.load('resources/images/mario_move12.png')
marioL3 = pygame.image.load('resources/images/mario_move22.png')

char = pygame.image.load('resources/images/mario.png')
char2 = pygame.image.load('resources/images/mario2.png')
jumping = pygame.image.load("resources/images/mario_jump.png")
jumping2 = pygame.image.load("resources/images/mario_jump2.png")
mario_death = pygame.image.load("resources/images/mario_death.png")
size = 40

marioR1 = pygame.transform.scale(marioR1, (size, size))
marioR2 = pygame.transform.scale(marioR2, (size, size))
marioR3 = pygame.transform.scale(marioR3, (size, size))

marioL1 = pygame.transform.scale(marioL1, (size, size))
marioL2 = pygame.transform.scale(marioL2, (size, size))
marioL3 = pygame.transform.scale(marioL3, (size, size))

char = pygame.transform.scale(char, (size, size))
char2 = pygame.transform.scale(char2, (size, size))
jumping = pygame.transform.scale(jumping, (size, size))
jumping2 = pygame.transform.scale(jumping2, (size, size))
mario_death = pygame.transform.scale(jumping2, (size, size))

walkRight = [marioR1, marioR1, marioR2, marioR2, marioR3, marioR3,]
walkLeft = [marioL1, marioL1, marioL2, marioL2, marioL3, marioL3]

#Setup Background
bg = pygame.image.load('resources/images/level_1.png')
bg = pygame.transform.scale(bg, (9000, 600)).convert()
bgWidth, bgHeight = bg.get_rect().size

#brick sprites
spritesheet = pygame.image.load("resources/images/tile_set.png")
spritesheet2= pygame.image.load("resources/images/item_objects.png")
spritesheet3 = pygame.image.load("resources/images/enemies.png")

character = Surface((15, 16), pygame.SRCALPHA)
character.blit(spritesheet, (-17, 0))
character = pygame.transform.scale(character, (44, 44))
brick1 = character

#Mystery block sprites
character = Surface((16,16),pygame.SRCALPHA)
character.blit(spritesheet,(-384,0))
character = pygame.transform.scale(character, (44,44))
mystery1 = character

character = Surface((16,16),pygame.SRCALPHA)
character.blit(spritesheet,(-400,0))
character = pygame.transform.scale(character, (44,44))
mystery2 = character

character = Surface((16,16),pygame.SRCALPHA)
character.blit(spritesheet,(-416,0))
character = pygame.transform.scale(character, (44,44))
mystery3 = character

character = Surface((16,16),pygame.SRCALPHA)
character.blit(spritesheet,(-432,0))
character = pygame.transform.scale(character, (44,44))
mystery4 = character

mystery = [mystery1, mystery1, mystery1, mystery2, mystery3, mystery3 ]

# Flag Slrites
character = Surface((8,24),pygame.SRCALPHA)
character.blit(spritesheet,(-260,-136))
character = pygame.transform.scale(character, (20,60))
flagCirc = character

character = Surface((8,16),pygame.SRCALPHA)
character.blit(spritesheet,(-260,-144))
character = pygame.transform.scale(character, (20,392))
flagPole = character

character = Surface((16,16),pygame.SRCALPHA)
character.blit(spritesheet2,(-128,-32))
character = pygame.transform.scale(character, (45,45))
flagTop = character

character = Surface((16,23), pygame.SRCALPHA)
character.blit(spritesheet3, (-96, -9))
character = pygame.transform.scale(character, (37, 48))
turtle1 = character

character = Surface((16, 24), pygame.SRCALPHA)
character.blit(spritesheet3, (-112, -8))
character = pygame.transform.scale(character, (37, 48))
turtle2 = character

character = Surface((16, 14),pygame.SRCALPHA)
character.blit(spritesheet3, (-160, -18))
character = pygame.transform.scale(character, (37, 35))
turtle3 = character

#Items
character = Surface((16,16),pygame.SRCALPHA)
character.blit(spritesheet2,(0,0))
character = pygame.transform.scale(character, (30,30))
shroom = character



clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1
        self.isJump = False
        self.left = False
        self.right = False
        self.standing = True
        self.walkCount = 0
        self.jumpCount = 10
        self.starting = True
        self.runCount = 0
        self.jumping = 0
        self.currenty = 410
        self.done = True
        self.ableJump = False
        self.scroll = 0 #-6900
        self.x3 = 0
        self.fall = False
        self.rightStop = False
        self.leftStop = False
        self.bug = False
        self.brickCount = 0
        self.brickCount2 = 0
        self.endGame = False
        self.dead = False

    def draw(self, win):

        if self.walkCount + 1 >= 6:
            self.walkCount = 0

        if self.brickCount + .2 >= 5:
            self.brickCount = 0
        else:
            self.brickCount += .2

        if self.runCount >= 9:
            self.runCount = 9

        if self.dead:
            win.blit(mario_death, (self.x, self.y))

        elif self.left and not self.isJump and not self.standing and not self.fall and self.dead == False:
            win.blit(walkLeft[self.walkCount], (self.x, self.y))
            self.walkCount += 1
            if self.runCount < 9:
                self.runCount += 1

        elif self.right and not self.isJump and not self.standing and not self.fall and self.dead == False:
            win.blit(walkRight[self.walkCount], (self.x, self.y))
            self.walkCount += 1
            if self.runCount < 9:
                self.runCount += 1

        if self.standing and self.right and not self.isJump or self.starting and not self.fall and self.dead == False:
            win.blit(char, (self.x, self.y))

        elif self.standing and self.left and not self.isJump and not self.fall and self.dead == False:
            win.blit(char2, (self.x, self.y))

        elif self.isJump or self.fall and self.dead == False:
            if self.right:
                win.blit(jumping, (self.x, self.y))

            elif self.left:
                 win.blit(jumping2, (self.x, self.y))

class Object(object):

    def __init__(self, x, y, width, height, type=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type # OPTIONAL
        self.up = False
        self.opened = False

    def draw(self, win):
        pygame.draw.rect(win, (255,0,0), (self.x, self.y, self.width, self.height), 5)

    def draw_brick(self, win):
        win.blit(brick1,(self.x, self.y, self.width, self.height))

    def draw_mystery(self, win):
        win.blit(mystery[round(man.brickCount)], (self.x, self.y))

    def draw_mystery_opened(self, win):
        win.blit(mystery4, (self.x, self.y))

    def draw_pole(self, win):
        win.blit(flagPole,(self.x, self.y))

    def draw_top(self,win):
        win.blit(flagCirc,(self.x, self.y))

    def draw_flag(self, win):
        win.blit(flagTop, (self.x, self.y))

class Enemy(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 1
        self.vel = -3
        self.hitbox = (self.x + 0, self.y, 32,32)
        self.dead = False
        self.head = self.y
        self.w = 0
        self.x3 = 0

    #def draw_1(self, win):

    def draw(self, win):
        self.move()
        if self.walkCount + .5 >= 2:
            self.walkCount = 0

        if self.dead:
            win.blit(pygame.image.load('resources/images/goombas_dead.png'), (self.x, self.y))

        elif self.vel > 0:
            win.blit(self.walkRight[self.walkCount // 1], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount // 1], (self.x, self.y))
            self.walkCount += 1

        #pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height), 5)

    def move(self):
        self.w += self.vel

        if man.x3 > 480:
            goblins[0].x = man.scroll + 900 + goblins[0].w
        else:
            goblins[0].x = man.scroll + 900
            goblins[0].w = 0

        goblins[1].x = man.scroll + 1700 + goblins[1].w
        goblins[2].x = man.scroll + 2060 + goblins[2].w
        goblins[3].x = man.scroll + 2130 + goblins[3].w

        if man.x3 > 3000:
            goblins[4].x = man.scroll + 3440 + goblins[4].w
            goblins[5].x = man.scroll + 3500 + goblins[5].w
        else:
            goblins[4].x = man.scroll + 3440
            goblins[5].x = man.scroll + 3500

            goblins[4].w = 0
            goblins[5].w = 0

        if man.x3 > 3770:
            goblins[6].x = man.scroll + 4050 + goblins[6].w
            goblins[7].x = man.scroll + 4100 + goblins[7].w
        else:
            goblins[6].x = man.scroll + 4050
            goblins[7].x = man.scroll + 4100

            goblins[6].w = 0
            goblins[7].w = 0

        if man.x3 > 4500:
            goblins[8].x = man.scroll + 5171 + goblins[8].w
            goblins[9].x = man.scroll + 5221 + goblins[9].w
        else:
            goblins[8].x = man.scroll + 5171
            goblins[9].x = man.scroll + 5221

            goblins[8].w = 0
            goblins[9].w = 0

        if man.x3 > 4500:
            goblins[10].x = man.scroll + 5371 + goblins[10].w
            goblins[11].x = man.scroll + 5421 + goblins[11].w
        else:
            goblins[10].x = man.scroll + 5371
            goblins[11].x = man.scroll + 5421

            goblins[10].w = 0
            goblins[11].w = 0

        goblins[12].x = man.scroll + 7000 + goblins[12].w
        goblins[13].x = man.scroll + 7060 + goblins[13].w

        for goblin in goblins:
            if goblin.x < -33:
                goblin.vel = 0

    walkRight = [pygame.image.load('resources/images/goombas_1.png'), pygame.image.load('resources/images/goombas_0.png')]
    walkLeft = [pygame.image.load('resources/images/goombas_1.png'), pygame.image.load('resources/images/goombas_0.png')]
    dead = [pygame.image.load('resources/images/goombas_dead.png')]

class Turtle(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 1
        self.vel = -3
        self.hitbox = (self.x + 0, self.y, 32, 32)
        self.dead = False
        self.head = self.y
        self.w = 0

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 4:
            self.walkCount = 0

        if self.dead:
            win.blit(turtle3, (self.x, self.y))

        elif self.vel > 0:
            win.blit(self.walkRight[self.walkCount // 2], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount // 2], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 0, self.y, 32, 48)

        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height), 5)

    def move(self):
        self.w += self.vel

        if man.x3 > 3620:
            self.x = man.scroll + 4755 + self.w
        else:
            self.x = man.scroll + 4755
            self.w = 0

    walkRight = [turtle1, turtle2]
    walkLeft = [turtle1, turtle2]
    dead = turtle3

class items(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.w = 0
        self.eaten = True
        self.vel = 2

    def move(self):
        self.w += self.vel

        if objs_M_N[0].opened == True:
            shrooms[0].x = man.scroll + 100 + shrooms[0].w
            shrooms[0].x = man.scroll + 100
            shrooms[0].w = 0

    def draw(self, win):
        self.move()

        if self.eaten:
            win.blit((shroom), (self.x, self.y))


def goomba_collide(object, goblin):
    for goblin in goblins:
        if goblin.x <= object.x + object.width and goblin.x + goblin.width >= object.x + object.width:  # right side collision
            if goblin.y + goblin.height >= object.y and goblin.y <= object.y + object.height:
                goblin.x = obj.x + obj.width + 1
                goblin.vel = 3

        elif goblin.x + goblin.width >= object.x and goblin.x <= object.x:  # Left side collision
            if goblin.y + goblin.height > object.y and goblin.y < object.y + object.height:
                goblin.x = obj.x - goblin.width - 1
                goblin.vel = -3

def goomba_fall():
    for goblin in goblins:
        goblin.x3 = -1 * man.scroll + goblins[4].x
        goblin.x4 = -1 * man.scroll + goblins[5].x

        goblin.x5 = -1 * man.scroll + goblins[6].x
        goblin.x6 = -1 * man.scroll + goblins[7].x

    if goblin.x3 < 3376 and goblin.x3 > 3335:
        goblins[4].y += (-5 ** 2) * .5 * -1

    elif goblin.x3 < 3239 and goblin.x3 > 3194:
        goblins[4].y += (-5 ** 2) * .5 * -1

    elif goblin.x3 < 2977 and goblins[4].y < 650:
        goblins[4].y += (-5 ** 2) * .5 * -1

    elif goblin.x3 < 3239 and goblin.x3 > 2977:
        goblins[4].y = 505

#--------------------------------------------------------------

    if goblin.x4 < 3376 and goblin.x4 > 3335:
        goblins[5].y += (-5 ** 2) * .5 * -1

    elif goblin.x4 < 3239 and goblin.x4 > 3194:
        goblins[5].y += (-5 ** 2) * .5 * -1

    elif goblin.x4 < 2977 and goblins[5].y < 650:
        goblins[5].y += (-5 ** 2) * .5 * -1

    elif goblin.x4 < 3239 and goblin.x4 > 2977:
        goblins[5].y = 505

#-----------------------------------------------------

    if goblin.x5 < 3760 and goblins[6].y < 650:
        goblins[6].y += (-5 ** 2) * .5 * -1
        
    if goblin.x6 < 3760 and goblins[7].y < 650:
        goblins[7].y += (-5 ** 2) * .5 * -1

def collideY(man, object):
    if man.x <= object.x + object.width and man.x + man.width >= object.x: # Top check
        if man.y <= object.y + object.height and man.y + man.height >= object.y + object.height:
            return "D"
        elif man.y <= object.y and man.y + man.height >= object.y:
            return "U"
    else:
        return "F"

    return False

def collideX(player, object):
    if man.x + man.width >= object.x and man.x <= object.x: # Left side collision
        if man.y + man.height > object.y and man.y < object.y + object.height:
            return "L"

    elif man.x <= object.x + object.width and man.x + man.width >= object.x + object.width: # right side collision
        if man.y + man.height > object.y and man.y < object.y + object.height:
            return "R"

def basicGrav(collideX, collideY):
    cX = collideX(man, obj)
    cY = collideY(man, obj)
    if man.isJump:
        if cY == "U":
            man.standing = True
            man.isJump = False
            man.ableJump = True
            man.y = obj.y - man.height
        elif cY == "D":
            if man.y < obj.y + obj.height:
                man.y = obj.y + obj.height
            man.ableJump = False
        elif cX == "R" and cY == False:
            man.x = obj.x + obj.width + 1
        elif cX == "L" and cY == False:
            man.x = obj.x - man.width - 1
    else:
        if cX == "R":
            man.x = obj.x + obj.width + 1
        elif cX == "L":
            man.x = obj.x - man.width - 1

def breakBricks(collideX, collideY):
    cX = collideX(man, obj)
    cY = collideY(man, obj)

    if man.isJump:
        if cY == "U":
            man.standing = True
            man.isJump = False
            man.ableJump = True
            man.y = obj.y - man.height
        elif cY == "D":
            obj.y -= 10
            if man.y < obj.y + obj.height:
                man.y = obj.y + obj.height
            man.jumpCount = -1
            man.ableJump = False
            obj.up = True
        elif cX == "R" and cY == False:
            man.x = obj.x + obj.width + 1
        elif cX == "L" and cY == False:
            man.x = obj.x - man.width - 1
    else:
        if cX == "R":
            man.x = obj.x + obj.width + 1
        elif cX == "L":
            man.x = obj.x - man.width - 1

        if obj.up == True:
            obj.y += 10
            obj.up = False

def mysteryBricks(collideX, collideY):
    cX = collideX(man, obj)
    cY = collideY(man, obj)
    if man.isJump:
        if cY == "U":
            man.standing = True
            man.isJump = False
            man.ableJump = True
            man.y = obj.y - man.height
        elif cY == "D":
            if man.y < obj.y + obj.height:
                man.y = obj.y + obj.height
            man.jumpCount = -1
            man.ableJump = False
            if obj.opened == False:
                obj.y -= 10
                obj.up = True
                obj.opened = True
        elif cX == "R" and cY == False:
            man.x = obj.x + obj.width + 1
        elif cX == "L" and cY == False:
            man.x = obj.x - man.width - 1
    else:
        if cX == "R":
            man.x = obj.x + obj.width + 1
        elif cX == "L":
            man.x = obj.x - man.width - 1
        if obj.up == True:
            obj.y += 10
            obj.up = False

def right():
    if not keys[pygame.K_LEFT]:
        if keys[pygame.K_s]:
            if man.x == 400 and not man.fall and man.x3 < 8572:
                man.scroll -= (man.vel * man.runCount) * 1.5
            else:
                man.x += (man.vel * man.runCount) * 1.5
        elif man.x == 400 and not man.fall and man.x3 < 8572:
            man.scroll -= man.vel * man.runCount
        else:
            man.x += man.vel * man.runCount

        if man.x >= 400 and man.x3 < 8572:
            man.x = 400

        man.right = True
        man.left = False
        man.standing = False
        man.starting = False

def left():
    if keys[pygame.K_s]:
        man.x -= (man.vel * man.runCount) * 1.5
    else:
        man.x -= man.vel * man.runCount
    man.left = True
    man.right = False
    man.standing = False
    man.starting = False

def standing():
    if flag.y < 411:
        man.standing = True
        man.done = True
        man.isJump2 = False
        man.walkCount = 0
        man.runCount = 0
        if man.right or man.left:
            if not man.isJump:
                man.alex = 0

def obj_pos():
    objs[0 ].x = man.scroll + 8407
    objs[1 ].x = man.scroll + 1196
    objs[2 ].x = man.scroll + 1622
    objs[3 ].x = man.scroll + 1961
    objs[4 ].x = man.scroll + 2427

    objs[5 ].x = man.scroll + 5817
    objs[6 ].x = man.scroll + 5775
    objs[7 ].x = man.scroll + 5734
    objs[8 ].x = man.scroll + 5690

    objs[9 ].x = man.scroll + 5942
    objs[10].x = man.scroll + 5942
    objs[11].x = man.scroll + 5942
    objs[12].x = man.scroll + 5943

    objs[13].x = man.scroll + 6414
    objs[14].x = man.scroll + 6372
    objs[15].x = man.scroll + 6331
    objs[16].x = man.scroll + 6287

    objs[17].x = man.scroll + 6579
    objs[18].x = man.scroll + 6579
    objs[19].x = man.scroll + 6579
    objs[20].x = man.scroll + 6579

    objs[21].x = man.scroll + 6928
    objs[22].x = man.scroll + 7607

    objs[23].x = man.scroll + 7978
    objs[24].x = man.scroll + 7934
    objs[25].x = man.scroll + 7893
    objs[26].x = man.scroll + 7851
    objs[27].x = man.scroll + 7808
    objs[28].x = man.scroll + 7765
    objs[29].x = man.scroll + 7724
    objs[30].x = man.scroll + 7680

    objs[31].x = man.scroll + 5830
    objs[32].x = man.scroll + 5941
    objs[33].x = man.scroll + 6465

    objs_L[0].x = man.scroll + 800
    objs_L[1].x = man.scroll + 3280
    objs_L[2].x = man.scroll + 3417
    objs_L[3].x = man.scroll + 3857
    objs_L[4].x = man.scroll + 4253
    objs_L[5].x = man.scroll + 5133
    objs_L[6].x = man.scroll + 5441
    objs_L[7].x = man.scroll + 5485
    objs_L[8].x = man.scroll + 7139

    objs_R[0].x = man.scroll + 976
    objs_R[1].x = man.scroll + 3368
    objs_R[2].x = man.scroll + 3681
    objs_R[3].x = man.scroll + 4297
    objs_R[4].x = man.scroll + 5221
    objs_R[5].x = man.scroll + 5573
    objs_R[6].x = man.scroll + 5529
    objs_R[7].x = man.scroll + 7271

    objs_B[0].x = man.scroll + 3989
    objs_B[1].x = man.scroll + 5001

    objs_N[0].x = man.scroll + 888
    objs_N[1].x = man.scroll + 3461
    objs_N[2].x = man.scroll + 3417
    objs_N[3].x = man.scroll + 3467
    objs_N[4].x = man.scroll + 3505
    objs_N[5].x = man.scroll + 3549
    objs_N[6].x = man.scroll + 3593
    objs_N[7].x = man.scroll + 3637
    objs_N[8].x = man.scroll + 3901
    objs_N[9].x = man.scroll + 3945
    objs_N[10].x = man.scroll + 5177
    objs_N[11].x = man.scroll + 5529
    objs_N[12].x = man.scroll + 7183

    objs_M_R[0].x = man.scroll + 3989

    objs_M_B[0].x = man.scroll + 580
    objs_M_B[1].x = man.scroll + 4517
    objs_M_B[2].x = man.scroll + 888
    objs_M_B[3].x = man.scroll + 4649
    objs_M_B[4].x = man.scroll + 4649
    objs_M_B[5].x = man.scroll + 4781

    objs_M_N[0].x = man.scroll + 844
    objs_M_N[1].x = man.scroll + 932
    objs_M_N[2].x = man.scroll + 3324
    objs_M_N[3].x = man.scroll + 5485
    objs_M_N[4].x = man.scroll + 7227

    flag_pole.x = man.scroll + 8416
    flag.x = man.scroll + 8379
    flag_top.x = man.scroll + 8416

def gravity():
    if obj.x > man.x - obj.width - 14 and obj.x + obj.width < man.x + man.width + obj.width + 14:
        if man.x > obj.x - man.width and man.x < obj.x + obj.width:
            man.standing = True
        elif man.y < obj.y + man.height + 2 and man.y > obj.y - man.height - 2 and not man.isJump :
            man.isJump = True
            man.jumpCount = -1

def flag_collide():
    if man.x + man.width >= flag_pole.x and man.x <= flag_pole.x:  # Left side collision
        if man.y + man.height > flag_pole.y and man.y < flag_pole.y + flag_pole.height:
            end_game()
            man.jumpCount = -3

    elif man.x <= flag_pole.x + flag_pole.width and man.x + man.width >= flag_pole.x + flag_pole.width:  # right side collision
        if man.y + man.height > flag_pole.y and man.y < flag_pole.y + flag_pole.height:
            end_game()
            man.jumpCount = -3

def end_game():
    if man.x3 > 8366:
        if flag.y < 411:
            flag.y += 10

        if man.y < 445:
            man.x = flag_pole.x - man.width + 20
        else:
            man.leftStop = True
            man.rightStop = True
            man.right = True
            man.ableJump = False
            if flag.y >= 411:
                man.x += 65

def collisionX(man, turtle):
    if man.x + man.width >= turtle.x and man.x <= turtle.x + turtle.width:
        if man.y + man.height >= turtle.y and man.y <= turtle.y + turtle. height:
            return "man dead"

    return False

def collisionY(man, turtle):
    if man.x + man.width >= turtle.x and man.x <= turtle.x + turtle.width:
        if man.y + man.height >= turtle.y and man.y <= turtle.y + turtle.height:
            return "turtle dead"

    return False

def collisonTur(man, Tur):
    cx2 = collisionX(man, turtle)
    cy2 = collisionY(man, turtle)

    if not man.isJump:
        if cx2 == "man dead":
            if turtle.dead == False:
                man.dead = True
                man.isJump = True
                man.jumpCount = 10
                print("Man ded")

    if man.isJump:
        if cy2 == "turtle dead":
            turtle.dead = True
            turtle.vel = 0
            turtle.y = 450
            print("turtle ded")

    if turtle.dead == True:
        if cy2 == "turtle dead" or cx2 == "man dead":
            turtle.y = 510
            if man.left:
                turtle.vel = -20
                turtle.walkCount = 0
            elif man.right:
                turtle.vel = 20
                turtle.walkCount = 0

def collide_goomba(man, goblin):
    for goblin in goblins:
        if goblin.dead:
            goblin.y = 999
            goblin.vel = 0

        elif man.isJump:
            if man.x <= goblin.x + goblin.width and man.x + man.width >= goblin.x:  # Top check
                if man.y <= goblin.y and man.y + man.height >= goblin.y:
                    goblin.dead = True
                    man.isJump = True
                    man.jumpCount = 5


            return False
        elif not goblin.dead:
            if man.x <= goblin.x + goblin.width and man.x + man.width >= goblin.x:  # Top check
                if man.y <= goblin.y + goblin.height and man.y + man.height >= goblin.y + goblin.height:
                    man.dead = True
                elif man.y <= goblin.y and man.y + man.height >= goblin.y:
                    man.dead = True

def redrawGameWindow():
    if man.endGame:
        if man.walkCount + 1 >= 6:
            man.walkCount = 0

        if man.runCount >= 9:
            man.runCount = 9

        win.blit(walkRight[man.walkCount], (man.x, man.y))
        man.walkCount += 1
        if man.runCount < 9:
            man.runCount += 1
    else:
        man.draw(win)

    #for o in objs:
        #o.draw(win)
    for o in objs_L:
        o.draw_brick(win)
    for o in objs_R:
        o.draw_brick(win)
    for o in objs_B:
        o.draw_brick(win)
    for o in objs_N:
        o.draw_brick(win)

    for o in objs_M_L:
        if o.opened:
            o.draw_mystery_opened(win)
        else:
            o.draw_mystery(win)
    for o in objs_M_R:
        if o.opened:
            o.draw_mystery_opened(win)
        else:
            o.draw_mystery(win)
    for o in objs_M_B:
        if o.opened:
            o.draw_mystery_opened(win)
        else:
            o.draw_mystery(win)
    for o in objs_M_N:
        if o.opened:
            o.draw_mystery_opened(win)
        else:
            o.draw_mystery(win)

    flag.draw_flag(win)

    flag_pole.draw_pole(win)

    flag_top.draw_top(win)

    pygame.display.update()
    win.blit(bg, (man.scroll, 0))

    for goblin in goblins:
        goblin.draw(win)

    turtle.draw(win)

    for shroom in shrooms:
        shroom.draw(win)

# mainloop
man = player(200, 498, size, size)
goblins = [Enemy(600, 505, 32, 32),  #0
           Enemy(600, 505, 32, 32),  #1
           Enemy(600, 505, 32, 32),  #2
           Enemy(600, 505, 32, 32),  #3
           Enemy(600, 154, 32, 32),  #4
           Enemy(600, 154, 32, 32),  #5

           Enemy(600, 495, 32, 32),  #6
           Enemy(600, 495, 32, 32),  #7
           Enemy(600, 505, 32, 32),  #8
           Enemy(600, 505, 32, 32),  #9
           Enemy(600, 505, 32, 32),  #10
           Enemy(600, 505, 32, 32),  #11
           Enemy(600, 505, 32, 32),  #12
           Enemy(600, 505, 32, 32),  #13
           ]
turtle = Turtle(50, 490, 32, 32)

shrooms = [  items(50, 330, 30, 30),
            items(150, 50, 30, 30),

          ]

flag_pole = Object(50, 100, 20, 392)
flag = Object(50, 100, 45, 45)
flag_top = Object(50, 80, 20, 20)

objs = [  # Solid Blocks
        Object(man.scroll + 8407, 491, 40, 40),#0

        Object(man.scroll + 1196, 451, 71, 100),#1
        Object(man.scroll + 1622, 410, 71, 135),#2
        Object(man.scroll + 1961, 368, 71, 185),#3
        Object(man.scroll + 2427, 368, 71, 185),#4

        Object(man.scroll + 5817, 365, 40, 40),#8
        Object(man.scroll + 5775, 408, 80, 40),#7
        Object(man.scroll + 5734, 449, 123, 40),#6
        Object(man.scroll + 5690, 490, 167, 40),#5


        Object(man.scroll + 5942, 365, 40, 40), #12
        Object(man.scroll + 5942, 408, 80, 40), #11
        Object(man.scroll + 5942, 449, 125, 40),#10
        Object(man.scroll + 5942, 490, 167, 40),#9


        Object(man.scroll + 6414, 365, 80, 40),#16
        Object(man.scroll + 6372, 408, 120, 40),#15
        Object(man.scroll + 6331, 449, 163, 40),#14
        Object(man.scroll + 6287, 490, 207, 40),#13


        Object(man.scroll + 6579, 365, 40, 40),#20
        Object(man.scroll + 6579, 408, 80, 40),#19
        Object(man.scroll + 6579, 449, 125, 40),#18
        Object(man.scroll + 6579, 490, 167, 40),  # 17

        Object(man.scroll + 6928, 451, 71, 100),#21
        Object(man.scroll + 7607, 451, 73, 100),#22

        Object(man.scroll + 7978, 194, 88, 40),#30
        Object(man.scroll + 7934, 238, 130, 40),#29
        Object(man.scroll + 7893, 281, 172, 40),#28
        Object(man.scroll + 7851, 324, 214, 40), #27
        Object(man.scroll + 7808, 366, 256, 40),#26
        Object(man.scroll + 7765, 410, 299, 40),#25
        Object(man.scroll + 7724, 452, 341, 40),#24
        Object(man.scroll + 7680, 492, 382, 40),#23

        Object(man.scroll + 5817, 365, 27, 167),#31
        Object(man.scroll + 6579, 365, 27, 167),#32

        Object(man.scroll + 7079, 365, 27, 167),  # 33




       ]

#Bricks
objs_L = [
    Object(man.scroll + 800, 360, 44, 44),#0
    Object(man.scroll + 3280, 360, 44, 44),#1
    Object(man.scroll + 3417, 197, 44, 44),#2
    Object(man.scroll + 3857, 197, 44, 44),#3
    Object(man.scroll + 4253, 360, 44, 44),#4
    Object(man.scroll + 5133, 197, 44, 44),#5
    Object(man.scroll + 5441, 197, 44, 44),#6
    Object(man.scroll + 5485, 360, 44, 44),#7
    Object(man.scroll + 7139, 360, 44, 44),#8

         ]
objs_R = [
    Object(man.scroll + 976, 360, 44, 44),#0
    Object(man.scroll + 3368, 360, 44, 44),#1
    Object(man.scroll + 3681, 197, 44, 44),#2
    Object(man.scroll + 4297, 360, 44, 44),#3
    Object(man.scroll + 5221, 197, 44, 44),#4
    Object(man.scroll + 5573, 197, 44, 44),#5
    Object(man.scroll + 5529, 360, 44, 44),#6
    Object(man.scroll + 7271, 360, 44, 44),#7

         ]
objs_B = [
    Object(man.scroll + 3989, 360, 44, 44),#0
    Object(man.scroll + 5001, 360, 44, 44),#1

         ]
objs_N = [
    Object(man.scroll + 888, 360, 44, 44),#0
    Object(man.scroll + 3461, 197, 44, 44),#1
    Object(man.scroll + 3417, 197, 44, 44),#2
    Object(man.scroll + 3467, 197, 44, 44),#3
    Object(man.scroll + 3505, 197, 44, 44),#4
    Object(man.scroll + 3549, 197, 44, 44),#5
    Object(man.scroll + 3593, 197, 44, 44),#6
    Object(man.scroll + 3637, 197, 44, 44),#7
    Object(man.scroll + 3901, 197, 44, 44),#8
    Object(man.scroll + 3945, 197, 44, 44),#9
    Object(man.scroll + 5177, 197, 44, 44),#10
    Object(man.scroll + 5529, 197, 44, 44),#11
    Object(man.scroll + 7183, 360, 44, 44),#12

]

#Mystery
objs_M_L = [

]
objs_M_R = [
    Object(man.scroll + 3989, 197, 44, 44),#0
]
objs_M_B = [
    Object(man.scroll + 580, 360, 44, 44),#0
    Object(man.scroll + 4517, 360, 44, 44),#1
    Object(man.scroll + 888, 197, 44, 44),#2
    Object(man.scroll + 4649, 360, 44, 44),#3
    Object(man.scroll + 4649, 197, 44, 44),#4
    Object(man.scroll + 4781, 360, 44, 44),#5

]
objs_M_N = [
    Object(man.scroll + 844, 360, 44, 44),#0
    Object(man.scroll + 932, 360, 44, 44),#1
    Object(man.scroll + 3324, 360, 44, 44),#2
    Object(man.scroll + 5485, 197, 44, 44),#3
    Object(man.scroll + 7227, 360, 44, 44),#4
         ]

run = True
while run:
    clock.tick(27)
    obj_pos()
    collisonTur(man, turtle)
    collide_goomba(man, goblins)

    # Able to Quit without crashing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# Jump Height
    if man.standing or man.left or man.right:
        if not man.isJump:
            man.currenty = man.y
    jumpHeight = man.currenty - man.y
    jumpHeight = int(jumpHeight)

    goomba_fall()

# Collisions / interactions for solid blocks(Pipes and floor bricks)
    for obj in objs:
        basicGrav(collideX, collideY)
        goomba_collide(obj, goblins)
        gravity()

# Collision / with gravity on left side
    for obj in objs_L:
        breakBricks(collideX, collideY)
        gravity()

    for obj in objs_M_L:
        mysteryBricks(collideX, collideY)
        gravity()

# Collision / with gravity on right side
    for obj in objs_R:
        breakBricks(collideX, collideY)
        gravity()

    for obj in objs_M_R:
        mysteryBricks(collideX, collideY)
        gravity()

# Collision / with gravity on both side
    for obj in objs_B:
        breakBricks(collideX, collideY)
        gravity()

    for obj in objs_M_B:
        mysteryBricks(collideX, collideY)
        gravity()

# Collision / with gravity on neither side
    for obj in objs_N:
        breakBricks(collideX,collideY)
        gravity()

    for obj in objs_M_N:
        mysteryBricks(collideX, collideY)
        gravity()

#collision with flag
    flag_collide()

# X.3 is the equivalent x cordinate on the map
    man.x3 = -1 * man.scroll + man.x

# Defies the movement keys
    keys = pygame.key.get_pressed()

# Left movement
    if keys[pygame.K_LEFT] and man.x > 4 and not man.leftStop:
        left()

# Right movement
    elif keys[pygame.K_RIGHT] and man.x3 < 8956 and not man.rightStop:
        right()

    elif not man.isJump:
        standing()

# Jump mechanics
    if keys[pygame.K_UP] and man.ableJump:
        if jumpHeight < 200:
            man.isJump = True
            man.runCount = 9
            man.jumpCount = 6
            man.bug = False

        else:
            man.ableJump = False
    elif man.isJump:
        man.ableJump = False

    if man.isJump:
        if man.jumpCount >= -8:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.jumpCount -= 1
        else:
            man.jumpCount = -8
        man.y -= (man.jumpCount ** 2) * 0.5 * neg

# Ground floor
    if man.y >= 498 and not man.dead:
        if man.x3 > 2927 and man.x3 < 2985 or man.x3 > 3649 and man.x3 < 3750 or man.x3 > 6492 and man.x3 < 6552:
            man.fall = True
            man.y -= (man.jumpCount ** 2) * 0.3 * -1
        elif not man.fall:
            man.bug = True
            man.y = 498
            man.isJump = False
            man.ableJump = True

#End game flag
    if man.x3 > 8398 and man.x3 < 8660 and flag.y >= 411:
        man.endGame = True
        man.ableJump = False
        man.leftStop = True
        man.rightStop = True
        man.right = True
        man.y = 498
        man.x += 5
    elif man.x3 > 8660:
        man.y = -1000

#Determin if you won or lost
    if man.y < -500:
        print("You win")
    if man.y > 500:
        print("You lose")
    redrawGameWindow()

pygame.quit()




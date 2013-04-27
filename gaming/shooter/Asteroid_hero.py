import sys, pygame, random
pygame.init()

clock = pygame.time.Clock()
Asteroidlist = []
Asteroidrectlist = []
Asteroidspeed = []
timetrack = []
initialize = []


class Ship(object):
    def __init__(self,position=(0,0),speed=[0,0]):
        self.position = position
        self.speed = speed
    def shippopulate(self):
        Game.screen.blit(Game.ball, Game.ballrect)
        

class Asteroids(object):
    def __init__(self, number=10,speed=[2,2]):
        self.number = number
        self.speed = speed
    def populate(self,number):
        for i in range(number):
            s = 'enemy' + str(i)
            t = 'enemyrect' + str(i)
            self.s = pygame.image.load("bcwarrior.png")
            self.t = self.s.get_rect()
            xpos = random.randrange(0,(Game.width-self.t.width),self.t.width)
            ypos = random.randrange(0,(Game.height-self.t.height),self.t.height)
            while xpos > ((Game.width/2)-(2*Game.ballrect.width)) and xpos < ((Game.width/2)+(2*Game.ballrect.width)) and ypos > ((Game.height/2)-(2*Game.ballrect.height)) and ypos < ((Game.height/2)+(2*Game.ballrect.height)):
               xpos = random.randrange(0,(Game.width-self.t.width),self.t.width)
               ypos = random.randrange(0,(Game.height-self.t.height),self.t.height)
            self.t.topleft = (xpos,ypos)
            Game.screen.blit(self.s, self.t)
            while self.t.collidelistall(Asteroidrectlist):
                xpos = random.randrange(0,(Game.width-self.t.width),self.t.width)
                ypos = random.randrange(0,(Game.height-self.t.height),self.t.height)
                self.t.topleft = (xpos,ypos)
                Game.screen.blit(self.s, self.t)
                if self.t.colliderect(Game.ballrect):
                    xpos = random.randrange(0,(Game.width-self.t.width),self.t.width)
                    ypos = random.randrange(0,(Game.height-self.t.height),self.t.height)
                    self.t.topleft = (xpos,ypos)
                    Game.screen.blit(self.s, self.t)
            Asteroidlist.append(self.s)
            Asteroidrectlist.append(self.t)
            xx = random.randint(-3,3)
            yy = random.randint(-3,3)
            while xx == 0: xx = random.randint(-3,3)
            while yy == 0: yy = random.randint(-3,3)
            Asteroidspeed.append([xx,yy])
    def move_asteroids(self,number):
        speed = [2,2]
        for i in number:
            pass
    def add_asteroid(self,number):
        pass


class Game(object):
    size = width,height = 520,640
    screen = pygame.display.set_mode(size)
    ball = pygame.image.load("kanye.bmp")
    ballrect = ball.get_rect()
    def __init__(self,mysize=size,myscreen=screen,myball=ball,myrect=ballrect):
        pygame.display.set_caption('Monkey Fever')
        pygame.mouse.set_visible(1)
        #ship = Ship()
        self.size = mysize
        self.size = self.width, self.height
        self.black = 0, 0, 0

        self.screen = myscreen

        self.ball = myball
        self.ballrect = myrect
        self.ballrect.midtop = ((self.width/2),(self.height - self.ballrect.height)/2)
        #self.loop()
        self.whoopi()
    
    def shooting(self,lazkey,time):
        #print lazkey
        time_passed_raw = time
        attack_priority = 1
        ship = Ship()
        newpos = self.ballrect.midtop
        lazpos = self.ballrect.midbottom
        lazpos2 = ((lazpos[0]-2),(lazpos[1]-10))
        lazspeed = [0,0]
        self.screen.fill(self.black)
        self.ballopen = pygame.image.load("kanye_open.bmp")
        self.ballopenrect = self.ballopen.get_rect()
        self.ballopenrect.midtop = newpos
        self.screen.blit(self.ballopen, self.ballopenrect)
        for i in range(len(Asteroidlist)):
            self.screen.blit(Asteroidlist[i], Asteroidrectlist[i])
        pygame.display.flip()
        #
        self.laz = pygame.image.load("laser_4.png")
        self.laz = pygame.transform.flip(self.laz,1,0)
        self.lazrect = self.laz.get_rect()
        self.lazrect.bottomright = lazpos
        self.screen.blit(self.laz, self.lazrect)
        pygame.display.flip()
        
        h = 0
        asteroid_pos = []
        for ast in range(len(Asteroidrectlist)):
            asteroid_pos.append(Asteroidrectlist[ast].midtop)
        #
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
        pew_wav_file = "pew.wav"
        pew_wav = pygame.mixer.Sound(pew_wav_file)
        pew_wav.play(loops=0, fade_ms=0)
        while h <30:
            h +=1
            self.screen.fill(self.black)
            #shoot the lazer
            if lazkey == 1:
                if h>2 and h<4:
                    self.laz = pygame.image.load("laser_3.png")
                    self.laz = pygame.transform.flip(self.laz,1,0)
                    self.lazrect = self.laz.get_rect()
                    self.lazrect.bottomright = lazpos
                elif h>4 and h<6:
                    self.laz = pygame.image.load("laser_2.png")
                    self.laz = pygame.transform.flip(self.laz,1,0)
                    self.lazrect = self.laz.get_rect()
                    self.lazrect.bottomright = lazpos
                elif h==6:
                    self.laz = pygame.image.load("laser_1.png")
                    self.laz = pygame.transform.flip(self.laz,1,0)
                    self.lazrect = self.laz.get_rect()
                    self.lazrect.bottomright = lazpos
                elif h>6:
                    self.lazrect = self.lazrect.move([-10,0])
            elif lazkey == 2:
                if h>2 and h<4:
                    self.laz = pygame.image.load("laser_3.png")
                    self.lazrect = self.laz.get_rect()
                    self.lazrect.bottomleft = lazpos
                elif h>4 and h<6:
                    self.laz = pygame.image.load("laser_2.png")
                    self.lazrect = self.laz.get_rect()
                    self.lazrect.bottomleft = lazpos
                elif h==6:
                    self.laz = pygame.image.load("laser_1.png")
                    self.lazrect = self.laz.get_rect()
                    self.lazrect.bottomleft = lazpos
                elif h>6:
                    self.lazrect = self.lazrect.move([10,0])
            elif lazkey == 3:
                if h>2 and h<4:
                    self.laz = pygame.image.load("laser_3.png")
                    self.laz = pygame.transform.rotate(self.laz, 270)
                    self.lazrect = self.laz.get_rect()
                    self.lazrect.midtop = lazpos2
                elif h>4 and h<6:
                    self.laz = pygame.image.load("laser_2.png")
                    self.laz = pygame.transform.rotate(self.laz, 270)
                    self.lazrect = self.laz.get_rect()
                    self.lazrect.midtop = lazpos2
                elif h==6:
                    self.laz = pygame.image.load("laser_1.png")
                    self.laz = pygame.transform.rotate(self.laz, 270)
                    self.lazrect = self.laz.get_rect()
                    self.lazrect.midtop = lazpos2
                elif h>6:
                    self.lazrect = self.lazrect.move([0,10])
            elif lazkey == 4:
                if h>2 and h<4:
                    self.laz = pygame.image.load("laser_3.png")
                    self.laz = pygame.transform.rotate(self.laz, 90)
                    self.lazrect = self.laz.get_rect()
                    self.lazrect.midbottom = lazpos2
                elif h>4 and h<6:
                    self.laz = pygame.image.load("laser_2.png")
                    self.laz = pygame.transform.rotate(self.laz, 90)
                    self.lazrect = self.laz.get_rect()
                    self.lazrect.midbottom = lazpos2
                elif h==6:
                    self.laz = pygame.image.load("laser_1.png")
                    self.laz = pygame.transform.rotate(self.laz, 90)
                    self.lazrect = self.laz.get_rect()
                    self.lazrect.midbottom = lazpos2
                elif h>6:
                    self.lazrect = self.lazrect.move([0,-10])
                
            #check for movement
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    ship.speed[0] = -4
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    ship.speed[0] = 4
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    ship.speed[1] = -4
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    ship.speed[1] = 4
                
                if event.type == pygame.KEYUP and event.key == pygame.K_a:
                    ship.speed[0] = 4
                if event.type == pygame.KEYUP and event.key == pygame.K_d:
                    ship.speed[0] = -4
                if event.type == pygame.KEYUP and event.key == pygame.K_w:
                    ship.speed[1] = 4
                if event.type == pygame.KEYUP and event.key == pygame.K_s:
                    ship.speed[1] = -4
                if event.type == pygame.KEYUP and not key[pygame.K_a] and not key[pygame.K_d]:
                    ship.speed[0] = 0
                if event.type == pygame.KEYUP and not key[pygame.K_w] and not key[pygame.K_s]:
                    ship.speed[1] = 0
    
            if (self.ballopenrect.right+ship.speed[0]) >= self.width:
                diff = self.width - (self.ballopenrect.right+ship.speed[0])
                self.ballopenrect = self.ballopenrect.move([diff,0])
            if (self.ballopenrect.left+ship.speed[0]) <= 0:
                diff2 = -(self.ballopenrect.left+ship.speed[0])
                self.ballopenrect = self.ballopenrect.move([diff2,0])
            if (self.ballopenrect.bottom+ship.speed[1]) >= self.height:
                diff3 = self.height - (self.ballopenrect.bottom+ship.speed[1])
                self.ballopenrect = self.ballopenrect.move([0,diff3])
            if (self.ballopenrect.top+ship.speed[1]) <= 0:
                diff4 = -(self.ballopenrect.top+ship.speed[1])
                self.ballopenrect = self.ballopenrect.move([0,diff4])
            
            for i in range(len(Asteroidlist)):
                Asteroidrectlist[i] = Asteroidrectlist[i].move(Asteroidspeed[i])
                if Asteroidrectlist[i].left < 0 or Asteroidrectlist[i].right > self.width:
                    Asteroidspeed[i][0] = -Asteroidspeed[i][0]
                if Asteroidrectlist[i].top < 0 or Asteroidrectlist[i].bottom > self.height:
                    Asteroidspeed[i][1] = -Asteroidspeed[i][1]
            for i in range(len(Asteroidlist)):
                self.screen.blit(Asteroidlist[i], Asteroidrectlist[i])
            
            #time
            clock.tick(60)
            time_passed_raw += clock.get_rawtime()
            time_passed = time_passed_raw/1000
            if h == 30:
                timetrack.append(time_passed_raw)
            #
            self.ballopenrect = self.ballopenrect.move(ship.speed)
            self.ballrect = self.ballrect.move(ship.speed)
            self.screen.blit(self.ballopen, self.ballopenrect)
            self.screen.blit(self.laz, self.lazrect)
            pygame.display.flip()




    def whoopi(self):
        ship = Ship()
        asteroids = Asteroids()
        ship.position = self.ballrect.midtop
        asteroids.populate(asteroids.number)
        ship.shippopulate()
        attack_priority = 0
        keeptrack = []
        yoloswag = 0
        while True:
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                    ship.speed[0] = -4
                if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    ship.speed[0] = 4
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    ship.speed[1] = -4
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    ship.speed[1] = 4

                if event.type == pygame.KEYUP and event.key == pygame.K_a:
                    ship.speed[0] = 4
                if event.type == pygame.KEYUP and event.key == pygame.K_d:
                    ship.speed[0] = -4
                if event.type == pygame.KEYUP and event.key == pygame.K_w:
                    ship.speed[1] = 4
                if event.type == pygame.KEYUP and event.key == pygame.K_s:
                    ship.speed[1] = -4
                if event.type == pygame.KEYUP and not key[pygame.K_a] and not key[pygame.K_d]:
                    ship.speed[0] = 0
                if event.type == pygame.KEYUP and not key[pygame.K_w] and not key[pygame.K_s]:
                    ship.speed[1] = 0
                    #if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                        #self.shoot()
                #animation for shooting
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or  event.key == pygame.K_DOWN):
                    if event.key == pygame.K_LEFT:
                        self.shooting(1,time_passed_raw)
                        keeptrack.append(1)
                    if event.key == pygame.K_RIGHT:
                        self.shooting(2,time_passed_raw)
                        keeptrack.append(1)
                    if event.key == pygame.K_DOWN:
                        self.shooting(3,time_passed_raw)
                        keeptrack.append(1)
                    if event.key == pygame.K_UP:
                        self.shooting(4,time_passed_raw)
                        keeptrack.append(1)
                    #clock.tick
                    #self.shooting()
                    
            #Keeps the ship in the frame of the window
            if (self.ballrect.right+ship.speed[0]) >= self.width:
                diff = self.width - (self.ballrect.right+ship.speed[0])
                self.ballrect = self.ballrect.move([diff,0])
            if (self.ballrect.left+ship.speed[0]) <= 0:
                diff2 = -(self.ballrect.left+ship.speed[0])
                self.ballrect = self.ballrect.move([diff2,0])
            if (self.ballrect.bottom+ship.speed[1]) >= self.height:
                diff3 = self.height - (self.ballrect.bottom+ship.speed[1])
                self.ballrect = self.ballrect.move([0,diff3])
            if (self.ballrect.top+ship.speed[1]) <= 0:
                diff4 = -(self.ballrect.top+ship.speed[1])
                self.ballrect = self.ballrect.move([0,diff4])


            

            #moves asteroids
            for i in range(len(Asteroidlist)):
                #print Asteroidrectlist.index(Asteroidrectlist[i])
                #print Asteroidrectlist[:(i-1)], i
                Asteroidrectlist[i] = Asteroidrectlist[i].move(Asteroidspeed[i])
                if Asteroidrectlist[i].left < 0 or Asteroidrectlist[i].right > self.width:
                    Asteroidspeed[i][0] = -Asteroidspeed[i][0]
                if Asteroidrectlist[i].top < 0 or Asteroidrectlist[i].bottom > self.height:
                    Asteroidspeed[i][1] = -Asteroidspeed[i][1]
                    #if Asteroidrectlist[i].collidelistall(Asteroidrectlist[:(i)]):
                    #               Asteroidspeed[i][0] = -Asteroidspeed[i][0]
                    #     Asteroidspeed[i][1] = -Asteroidspeed[i][1]



            

            #time
            if not keeptrack and not initialize:
                time_passed_raw = 0
                initialize.append(1)
            else:
                if not timetrack:
                    pass
                else:
                    time_passed_raw = timetrack[0]
                    timetrack.pop(0)
            clock.tick(60)
            time_passed_raw += clock.get_time()
            time_passed = time_passed_raw/1000
                #print timetrack
#print time_passed_raw
                        # if time_passed%15 == 0:
                        #print "whatcha"
                    #elif time_passed%30 == 1:
                    #     print "verbatos"



            #add asteroids
            if time_passed%5 == 0 and time_passed != 0 and yoloswag == 0:
                yoloswag = 1
                asteroids.populate(1)
            elif time_passed%5 != 0 and time_passed != 0 and yoloswag == 1:
                yoloswag = 0 
            #draw the asteroids and kanye
            self.ballrect = self.ballrect.move(ship.speed)
            self.screen.fill(self.black)
            self.screen.blit(self.ball, self.ballrect)
            for i in range(len(Asteroidlist)):
                self.screen.blit(Asteroidlist[i], Asteroidrectlist[i])
            pygame.display.flip()
            


            
    def shoot(self):
        print "yellow"

    def loop(self):
        while 1:
            for event in pygame.event.get(): #pygame.quit is what happens when you quit the red quit button. At which point sys.exit() is executed. While 1 is an infinite loop, so this is needed to actually quit the code.
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    print "down"
                    key = pygame.key.get_pressed()
                    right_edge = self.ballrect.right + self.x_speed[0]
                    left_edge = self.ballrect.left + self.neg_x_speed[0]
                    top_edge = self.ballrect.top - self.y_speed[1]
                    bottom_edge = self.ballrect.bottom + self.y_speed[1]
                    if key[pygame.K_d]:
                        if right_edge > self.width:
                            self.x_speed[0] = -self.x_speed[0]
                        else:
                            pass
                        self.ballrect = self.ballrect.move(self.x_speed)
                    if key[pygame.K_a]:
                        print left_edge
                        if left_edge < 0:
                            self.neg_x_speed[0] = -self.neg_x_speed[0]
                        else:
                            pass
                        self.ballrect = self.ballrect.move(self.neg_x_speed)
                    if key[pygame.K_w]:
                        if right_edge > self.width:
                            self.x_speed[0] = -self.x_speed[0]
                        else:
                            self.ballrect = self.ballrect.move(self.x_speed)
                    if key[pygame.K_s]:
                        if right_edge > self.width:
                            self.x_speed[0] = -self.x_speed[0]
                        else:
                            self.ballrect = self.ballrect.move(self.x_speed)
                if event.type == pygame.KEYUP:
                    print "up"
            
                clock.tick(60)
                self.screen.fill(self.black)
                self.screen.blit(self.ball, self.ballrect)
                self.screen.blit(self.s, self.enemyrect)
                pygame.display.flip()

if __name__=='__main__':
    game = Game()
from scripts.settings import *


class Player(pg.sprite.Sprite):#must be a sprite inherited otherwise it won't fit in groups

    def __init__(self,game,x,y,img_dir,color_key):
        super(Player,self).__init__()
        self.game = game  # adds reference to the game
        # self.player_img = pg.transform.flip(self.player_img, True, True) #this flips the image along the x,y axis
        self.image = self.get_image(img_dir)
        self.image.set_colorkey(color_key)#gets rid of black color and makes it transparent
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.vx,self.vy = 0,0
        self.x = x *TILESIZE
        self.y = y * TILESIZE
        self.addToGroups()

    def get_keys(self):
        self.vx,self.vy = 0,0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def addToGroups(self):
        self.game.all_sprites.add(self)
        self.game.player_group.add(self)

    def get_image(self,img_dir):
        self.img = pg.image.load(img_dir).convert()
        self.img = pg.transform.scale(self.img, (TILESIZE, TILESIZE))
        return self.img



    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.wall_group, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.wall_group, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt #multiply by the game delta time so movement constant besides framerate
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')



class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.addToGroups()

    def addToGroups(self):
        self.game.all_sprites.add(self)
        self.game.wall_group.add(self)

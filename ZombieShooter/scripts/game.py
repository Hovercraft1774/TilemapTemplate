from scripts.settings import *
from scripts.player import *
from scripts.enemy import *
from scripts.tile_map import *

class Game(object):

    def __init__(self):
        self.playing = True
        pg.init()
        pg.mixer.init() #if using online editor, take this out
        # creates a screen for the game
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE) #Title of the screen window
        # creates time
        self.clock = pg.time.Clock()
        self.defaultColor = DEFAULT_COLOR
        pg.key.set_repeat(200,200)
        self.load_data()







    def load_data(self):
        self.map = Map(MAP2)

    def new(self):
        # create Sprite Groups
        self.all_sprites = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.player_group = pg.sprite.Group()
        self.wall_group = pg.sprite.Group()

        # create player player objects


        #create walls
        for row, tiles in enumerate(self.map.data): #enumerate gives both the index value and the item
            for col,tile in enumerate(tiles):
                if tile == '1':
                    Wall(self,col,row)
                if tile == 'P':
                    self.player = Player(self, col, row, player_img, self.defaultColor)
        self.camera = Camera(self.map.width,self.map.height)


    def gameLoop(self):
        while self.playing:
            self.dt = self.clock.tick(fps)/1000
            #tick clock
            self.clock.tick(fps)

            #check events
            self.check_Events()

            #update all
            self.update()

            #draw
            self.draw()


    def check_Events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()


    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHT_GRAY, (x,0), (x,HEIGHT))
        for y in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHT_GRAY, (0,y), (WIDTH,y))


    def draw(self):
        self.screen.fill(self.defaultColor)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))


        # think whiteboard, must be last line
        pg.display.flip()

    def start_Screen(self):
        pass
    def end_Screen(self):
        pass
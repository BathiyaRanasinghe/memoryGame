# Memory v1
#
# Memory is a game where a player tries to mach tiles together. The tiles are hidden at first
# but when a player clicks a tile the tile is revealed. If a player matches two similar tiles they
# remain revealed and if a player matches two different tiles they are hidden again after a slight delay.
# The timer is constantly increasing each second until all tiles are correctly selected.
#
# Version 1
# The first version must contain the complete tile grid and the black panel on the right,
# but there should be no score in the black panel. All 8 pairs of two tiles must be exposed 
# when the game starts. Each time the game is played, the tiles must be in random locations in 
# the grid. Player actions are ignored.

# imports all required modules
import pygame
import random
import os 

# User-defined functions

def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((500, 400))
    # set the title of the display window
    pygame.display.set_caption('Memory')   
    # get the display surface
    w_surface = pygame.display.get_surface() 
    # create a game object
    game = Game(w_surface)
    # start the main game loop by calling the play method on the game object
    game.play() 
    # quit pygame and clean up the pygame window
    pygame.quit() 


# User-defined classes

class Game:
    # An object in this class represents a complete game.

    def __init__(self, surface):
        # Initialize a Game.
        # - self is the Game to initialize
        # - surface is the display window surface object

        # === objects that are part of every game that we will discuss
        self.surface = surface
        self.bg_color = pygame.Color('black')

        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True

        # === game specific objects

        # Call to the class method to set the surface for the Tile objects
        Tile.set_surface(self.surface)
        
        # creating board and image list
        self.board_size = 4
        self.board = []
        self.create_board()
        self.images_list = []

    def create_board(self):
        # Creating the board
        # - self is the Game list which holds the images       
        
        # load the images into a list
        self.images_list = [pygame.image.load(os.path.join('image' + str(number) + ".bmp")) \
                           for number in range(1, 9)] 
        
        # Duplicate the image list with concatination and randomize the list with a shuffle
        self.images_list += self.images_list
        random.shuffle(self.images_list)
                
        # get the width and height of the first tile on the tile list
        first_tile = 0
        width = self.images_list[first_tile].get_width()
        height = self.images_list[first_tile].get_height()
        
        # create the tiles onto the board
        index = 0
        for row_index in range(0,self.board_size):
            row = [ ]
            for col_index in range(0,self.board_size):
                #item = (row_index,col_index) # 2 number in a tuple
                # replace item with a Tile object
                x = width * col_index 
                y = height * row_index 
                tile = Tile(x, y, self.images_list[index])
                index += 1
                row.append(tile)
            self.board.append(row)


    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.

        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            self.draw()            
            if self.continue_game:
                self.update()
                self.decide_continue()
            self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 

    def handle_events(self):
        # Handle each user event by changing the game state appropriately.
        # - self is the Game whose events will be handled

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.surface.fill(self.bg_color) # clear the display surface first
        # Draw the grid
        for row in self.board :
            for tile in row:
                tile.draw()
        pygame.display.update() # make the updated surface appear on the display

    def update(self):
        # Update the game objects for the next frame.
        # - self is the Game to update
        pass

    def decide_continue(self):
        # Check and remember if the game should continue 
        # - self is the Game to check
        pass

class Tile:
    # Class attributes are attributes that are same for all Tile object
    surface = None
    border_width = 10
    side_shift = 3
    border_color = pygame.Color('black')
    

    @classmethod
    # A class method is used to set or change the value of a class attribute
    def set_surface(cls,surface_from_Game):
        # -cls is a parameter gets bound to the name of the class which is Tile
        # -surface_from_Game get bound to the object the argument self.surface is bound to
        cls.surface = surface_from_Game
        
    # Instance Methods
    def __init__(self, x, y, image):
        self.image = image
        self.width = image.get_width()  
        self.height = image.get_height()  
        self.rect = pygame.Rect(x + self.side_shift, y + self.side_shift, self.width, self.height)        
        

    def draw(self):
        # draw the tile to the surface
        # - self is the tile
        pygame.draw.rect(Tile.surface, Tile.border_color, self.rect, Tile.border_width)
        Tile.surface.blit(self.image, self.rect)

main()
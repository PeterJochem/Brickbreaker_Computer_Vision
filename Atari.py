##################




from graphics import *


##################


# Describe this method here 
class brick:

    def __init__(self, x1, y1, x2, y2, color):
        
        self.alive = True
        self.graphic = Rectangle(Point(x1, y1), Point(x2, y2) )
        self.graphic.setFill(color)
        self.color = color

class Ball:
    
    # Describe here
    def init_Ball(self, game):

        radius = float(game.window_height) / 70.0

        x = float(game.window_width) / 2.0
        y = game.window_height * 0.70


        self.ball = Circle(Point(x , y), radius)
        self.ball.setFill("white")

        self.ball.draw(game.win)



    def __init__(self, game):
        self.alive = True
        
        self.game = game
        self.ball = None
        
        self.init_Ball(self.game)


# Describe here
class Paddle:
    
    # Describe here
    def init_Paddle(self):

        paddleWidth = float(self.game.window_width) / 20.0
        paddleHeight = float(self.game.window_height) / 100.0

        paddle_Y = self.game.window_height * 0.80

        x1 = ( float(self.game.window_width)  / 2.0) - (paddleWidth / 2.0)
        y1 = paddle_Y - ( float( paddleHeight )  / 2.0)

        x2 = ( float(self.game.window_width)  / 2.0) + (paddleWidth / 2.0)
        y2 = paddle_Y + (float(paddleHeight) / 2.0) 

        self.graphic = Rectangle(Point(x1, y1), Point(x2, y2) )
        self.graphic.setFill("purple")
        self.graphic.draw(self.game.win)

    def __init__(self, game):

        # Store the current location
        self.leftX = 0
        self.leftY = 0
        
        self.game = game
        
        self.init_Paddle() 
    




# This class describes a game and its info
class game:
    

    # Describe method here
    def init_Bricks(self):
            
        bricks_per_row = 15
        total_height_of_bricks = 0.10
        num_rows = 5
    
        # Save 20% of the window's heigth for the space above the bricks
        space_above_bricks = 0.15
        topRow_Y = float(self.window_height) * space_above_bricks

        brickWidth = ( float(self.window_width) ) / ( bricks_per_row  )
        brickHeight = ( float(self.window_height) * total_height_of_bricks) / ( float(num_rows)  )
            
        # Define the color order
        colorOrder = ["red", "blue", "green", "yellow", "purple"]
        

        for i in range(num_rows):
            
            currentRow = []
            currentColor = colorOrder[i]  

            for j in range(bricks_per_row):
                x1 = (j * brickWidth)
                y1 = (i * brickHeight) + topRow_Y
                x2 = ( (j + 1) * brickWidth)
                y2 = ( (i + 1) * brickHeight) + topRow_Y
               
                currentRow.append( brick( x1, y1, x2, y2, currentColor) ) 


            self.bricks.append( currentRow  )
            
    
    # Describe here
    def init_Ball(self):
        
        radius = float(self.window_height) / 70.0 
         
        x = float(self.window_width) / 2.0
        y = self.window_height * 0.70 
        

        self.ball = Circle(Point(x , y), radius)
        self.ball.setFill("white")

        self.ball.draw(self.win)

    
    # Describe method here
    def init_Paddle(self):
        
        paddleWidth = float(self.window_width) / 20.0 
        paddleHeight = float(self.window_height) / 100.0
        
        paddle_Y = self.window_height * 0.80

        x1 = ( float(self.window_width)  / 2.0) - (paddleWidth / 2.0)
        #y1 =  

        x2 = ( float(self.window_width)  / 2.0) + (paddleWidth / 2.0)
        #y2 = 

        #self.graphic = Rectangle(Point(x1, y1), Point(x2, y2) )
        #self.paddle.setFill("purple")

        #self.paddle.draw(self.win)

    # describe method here
    def drawBricks(self):
            
        # Rectangle(Point(100, 10), Point(200, 100) ).draw(self.win)
        # Rectangle( 100, 10, 200, 20).draw(self.win)
        
        for i in range(len(self.bricks) ):
            for j in range(len(self.bricks[i] ) ):
                 
               self.bricks[i][j].graphic.draw(self.win)

                
        

    def __init__(self, Player1Name):

        # Set up the window
        self.window_height = 800
        self.window_width = 800

        self.win = GraphWin("Brickbreaker", self.window_width, self.window_width)
        self.win.setBackground("black")
         

        #  Set up the intial configuration
        self.bricks = []

        # Display your face
        # Take screen shot of face when you lose??
        self.player1 = "Player1"
        
        # Set up the bricks
        self.init_Bricks() 
        self.drawBricks()
                    
        self.ball = Ball(self)
        self.paddle = Paddle(self)
            

    # Describe function here
    def getUserInput(self):
    
        global win
        keyString = win.checkKey()
    
     






# Main Function

# Create a game
currentGame = game("Peter")



# Keep the program running so we can 
# see the window
while(True):
    pass














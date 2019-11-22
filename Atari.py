##################



import math
from graphics import *


##################


# Describe this method here 
class brick:

    def __init__(self, x1, y1, x2, y2, color):
        
        self.alive = True
        self.x1 = x1
        self.y1 = y1
        self.graphic = Rectangle(Point(x1, y1), Point(x2, y2) )
        self.graphic.setFill(color)
        self.color = color


# describe the class here
class Ball:
    
    # Describe here
    def init_Ball(self, game):

        radius = float(game.window_height) / 95.0

        self.x = float(game.window_width) / 2.0
        self.y = game.window_height * 0.70


        self.graphic = Circle(Point(self.x , self.y), radius)
        self.graphic.setFill("white")

        self.graphic.draw(game.win)


    # Constructor
    def __init__(self, game):
        self.alive = True
        
        self.game = game
        self.ball = None
        
        # Records where the ball is at this time
        self.x = 0
        self.y = 0

        self.init_Ball(self.game)
    
        self.speed = 0.2 
        self.x_velocity = 0.02 
        self.y_velocity = 0.1


# Describe here
class Paddle:
    
    # Describe here
    def init_Paddle(self):
        
        self.paddleWidth = float(self.game.window_width) / 8.0
        paddleHeight = float(self.game.window_height) / 100.0

        paddle_Y = self.game.window_height * 0.95
            
        x1 = ( float(self.game.window_width)  / 2.0) - (self.paddleWidth / 2.0)
        y1 = paddle_Y - ( float( paddleHeight )  / 2.0)

        x2 = ( float(self.game.window_width)  / 2.0) + (self.paddleWidth / 2.0)
        y2 = paddle_Y + (float(paddleHeight) / 2.0) 
        

        # Data structure records where the left point is
        self.leftX = x1
        self.leftY = y1

        self.graphic = Rectangle(Point(x1, y1), Point(x2, y2) )
        self.graphic.setFill("purple")
        self.graphic.draw(self.game.win)

    def __init__(self, game):

        # Store the current location
        self.leftX = 0
        self.leftY = 0
        
        self.paddleWidth = 0

        # how far the paddle moves when a key is pressed
        self.delta = game.window_width / 25.0

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

    
    # Describe here
    def checkPaddleBall(self):
        
        # totalVelocity = math.sqrt( (self.ball.x_velocity**2) + (self.ball.y_velocity**2) )
    
        x_distance = self.ball.x - self.paddle.leftX

        threshold = 0
        if (x_distance < 0):
            threshold = 0.1
        else:
            threshold = self.paddle.paddleWidth

        if ( (self.ball.y > self.paddle.leftY) and ( abs(x_distance) < threshold)   ):

            if (  self.distance(self.ball.x, self.ball.y, self.paddle.leftX, self.paddle.leftY) < ( self.paddle.paddleWidth / 2.0 )  ):
                self.ball.x_velocity = -1 * self.ball.x_velocity    
            else:
                self.ball.x_velocity = self.ball.x_velocity 
            

            self.ball.y_velocity = -1 * self.ball.y_velocity

    
    # Describe the method here
    def distance(self, x1, y1, x2, y2):
            
        distance = (x2 - x1)**2 + (y2 - y1)**2

        distance = math.sqrt(distance)

        return distance

    # Describe here
    def checkBricksBall(self):
        
        # Describes how close we need to be to the given brick to "collide"
        distance_threshold = 50
        
        for i in range( len(self.bricks) - 1, -1, -1  ): 
          for j in range( len(self.bricks[0] ) ):
                
                if (self.bricks[i][j].alive == True):
                    if ( self.distance( self.bricks[i][j].x1,  self.bricks[i][j].y1, self.ball.x, self.ball.y ) < distance_threshold ):
                        # We have a collision
                        self.bricks[i][j].graphic.undraw()
                        
                        self.bricks[i][j].alive = False

                        self.ball.x_velocity = -1 * self.ball.x_velocity
                        self.ball.y_velocity = -1 * self.ball.y_velocity
                        return

    # Describe method here 
    def checkBallWalls(self):
 
        if ( (self.ball.x < 0) or ( self.ball.x > self.window_width) ):
            self.ball.x_velocity = -1 * self.ball.x_velocity
            # self.ball.y_velocity = -1 * self.ball.y_velocity
        
        if (self.ball.y < 0):
            self.ball.y_velocity = -1 * self.ball.y_velocity
        
        # Check for the lost ball scenario??


    def __init__(self, Player1Name):

        # Set up the window
        self.window_height = 800
        self.window_width = 800

        self.win = GraphWin("Brickbreaker", self.window_width, self.window_width)
        self.win.setBackground("black")
         

        ########  Set up the intial configuration ############
        self.bricks = []

        # Display your face
        # Take screen shot of face when you lose??
        self.player1 = "Player1"
        
        # Set up the bricks
        self.init_Bricks() 
        self.drawBricks()
                    
        self.ball = Ball(self)
        self.paddle = Paddle(self)
           
        ######### End of initial setup ############
        
        
        # Let the game logic run
        while(True):
            
            keyString = self.win.checkKey()
            if ( keyString == "h" ):
                self.paddle.graphic.move( self.paddle.delta, 0)
                
                self.paddle.leftX += self.paddle.delta

            elif ( keyString == "g" ):
                self.paddle.graphic.move( -1 * self.paddle.delta, 0)
                self.paddle.leftX =  self.paddle.leftX - self.paddle.delta  
            
            # Move the ball and update it's data structures
            self.ball.graphic.move( self.ball.x_velocity, self.ball.y_velocity  ) 
            self.ball.x = self.ball.x + self.ball.x_velocity
            self.ball.y = self.ball.y + self.ball.y_velocity
            
            # Check for collisions
            self.checkPaddleBall()
            
            self.checkBricksBall()
    
            self.checkBallWalls()



# Main Function

# Create a game
currentGame = game("Peter")



# Keep the program running so we can 
# see the window
while(True):
    pass














# How To Run My Code
To run my code, simply clone my repo and run ```python3 Atari.py```
Dependencies: OpenCV

# Description
I built the classic Atari game, Brickbreaker from scratch. I then used OpenCV functions to detect the location of a tennis ball in the user's hand. This allows the user to control the game's paddle with the tennis ball. 

## Image Processing Pipeline
I first get the image from the webcam, then threshold the image's hue values over a range that is roughly yellow and green. Then, I used OpenCV's findCountour's function to find the largest contour in the image. I get back a list of moments of contours. I simply choose the largest and update the game's paddle proportionally. 

I could not get good results using the Hough transformation for circle detection. This is a more comutationally expensive approach and the real time nature of the game made it impractical. Moreover, since we need to know the radius of the circle as it appears in the image, one needs to try many guesses of the radius and see which one aligns best with the data.

# Results
The game play is really smooth! I am really excited about how this turned out. 

Here is an image of the game at it's start

![Game At Start Position](  ).

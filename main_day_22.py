# step 1 :- create the screen
# step 2 :- create and move a paddle (can make a single paddle class and make it move by different keys )
# step 3 :- create another paddle
# step 4 :- create the ball and make it move (another class)
# step 5 :- detect coalition with the wall and bounce
# step 6 :- detect when paddle misses
# step 7 :- keep score

from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import Scoreboard




screen = Screen()   #creating the screen
screen.bgpic('ezgif.com-animated-gif-maker.gif')  # bg img of screen

screen.setup(width=800,height=600)  #setting height and width for the screen
screen.bgcolor("black")  #making the background color of screen black
screen.title("Pong Game")   # giving title to the screen
screen.tracer(0)  # turning the animation off and makes it like appearing instantly
screen.listen()   # to make the screen listen

# creating the paddle
right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

# ball
ball = Ball()


#score
score = Scoreboard()


# movement of the paddle by keys    1st player
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")

# controls  of second player
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")



# Game loop
game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()  #update the screen
    ball.move()

    #detect the collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
    #bounce
        ball.bounce_y()


    # to detect collision  with right paddle
    # to detect collision  with left paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()




    #right side paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        screen.update()



    #left side paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        screen.update()






screen.exitonclick() # screen with exist after click
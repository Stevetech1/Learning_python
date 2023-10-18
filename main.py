import turtle
import time
from turtle import Turtle, Screen
from bricks import Brick
from paddle import Paddle
from ball import Ball

# Import Paddle, Brick, and Ball classes here

class Main:
    def __init__(self):
        # Initialize the screen
        self.screen = turtle.Screen()
        self.screen.title("Ping Pong Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)  # Turn off automatic screen updates

        # Create a Paddle
        self.paddle = Paddle()
        
        # Create a list of Bricks
        self.bricks = [Brick() for _ in range(5)]  # Create 5 bricks as an example

        # Create a Ball
        self.ball = Ball()

    def game_over(self):
        # Display "GAME OVER" message
        game_over_text = turtle.Turtle()
        game_over_text.color("white")
        game_over_text.penup()
        game_over_text.hideturtle()
        game_over_text.goto(0, 0)
        game_over_text.write("GAME OVER", align="center", font=("Segoe UI", 36, "normal"))

    def you_win(self):
        # Display "CONGRATULATIONS, YOU WIN" message
        win_text = turtle.Turtle()
        win_text.color("white")
        win_text.penup()
        win_text.hideturtle()
        win_text.goto(0, 0)
        win_text.write("CONGRATULATIONS, YOU WIN", align="center", font=("Segoe UI", 36, "normal"))

    def run_game(self):
        running = True
        game_over = False
        win_condition = False

        while running:
            self.screen.update()

            # Handle user input for paddle movement
            self.screen.listen()
            self.screen.onkeypress(self.paddle.move_left, "Left")
            self.screen.onkeypress(self.paddle.move_right, "Right")

            # Update the game state (e.g., check for collisions and update the ball's position)
            if not game_over and not win_condition:
                self.ball.move()

                # Check for collisions with bricks
                for brick in self.bricks:
                    if self.ball.is_collision(brick):
                        brick.destroy()
                        self.ball.bounce_y()

                # Check for paddle collision and game over
                if self.ball.is_collision(self.paddle):
                    self.ball.bounce_y()
                elif self.ball.is_miss():
                    game_over = True

                # Check for win condition
                if all(brick.is_destroyed() for brick in self.bricks):
                    win_condition = True

            # Render the game elements (bricks, paddle, ball)
            self.paddle.render()
            for brick in self.bricks:
                brick.render()
            self.ball.render()

            # Check for win/loss conditions
            if game_over:
                self.game_over()
            elif win_condition:
                self.you_win()

            time.sleep(0.02)  # Add a small delay to control game speed

if __name__ == "__main__":
    game = Main()
    game.run_game()
    turtle.done()

import random

varUserName = input("Hello! What's your name? ")

print(f"Hi, {varUserName}! Here are your lucky PowerBall numbers:")

white_ball_1 = random.randint(1, 69)
white_ball_2 = random.randint(1, 69)
white_ball_3 = random.randint(1, 69)
white_ball_4 = random.randint(1, 69)
white_ball_5 = random.randint(1, 69)

power_ball = random.randint(1, 26)

print(f"{white_ball_1}  {white_ball_2}  {white_ball_3}  {white_ball_4}  {white_ball_5}    {power_ball}")

print("Good luck! Hope you win big!")
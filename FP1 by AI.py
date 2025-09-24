import random
import time
from colorama import Fore, Style, init

init()

varUserName = input("Hello! What's your name? ")

print(f"Hi, {varUserName}! Here are your lucky PowerBall numbers:")

white_ball_1 = random.randint(1, 69)
white_ball_2 = random.randint(1, 69)
white_ball_3 = random.randint(1, 69)
white_ball_4 = random.randint(1, 69)
white_ball_5 = random.randint(1, 69)

print(white_ball_1, end="  ", flush=True)
time.sleep(0.25)
print(white_ball_2, end="  ", flush=True)
time.sleep(0.25)
print(white_ball_3, end="  ", flush=True)
time.sleep(0.25)
print(white_ball_4, end="  ", flush=True)
time.sleep(0.25)
print(white_ball_5, end="    ", flush=True)
time.sleep(0.25)

power_ball = random.randint(1, 26)

print(f"{Fore.RED}{power_ball}{Style.RESET_ALL}")

print("Good luck! Hope you win big!")
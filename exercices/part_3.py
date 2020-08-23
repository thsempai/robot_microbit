from robot_microbit import Robot, Color
from microbit import sleep, pin1
from random import randint
from time import ticks_ms, ticks_diff


robot = Robot()
robot.speed = 50

# Maintenant quand le robot rencontre du noir, il va tourner jusqu'à ce qu'il rencontre du blanc à nouveau
while True:
    # your code here


    if robot.on_ground():
        robot.go_forward()
        robot.change_all_led_color(Color.green)
    else:
        robot.turn_right()
        robot.change_all_led_color(Color.red)
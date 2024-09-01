
#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

ObstaclePin = 18  # GPIO24 for IR
motor_pin = 16  # GPIO23 for vibrating motor
tilt_switch_pin = 11  # GPIO17 for tilt switch
buzzer_pin = 12  # GPIO18 for buzzer

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(motor_pin, GPIO.OUT)
GPIO.setup(tilt_switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buzzer_pin, GPIO.OUT)


def loop():
    while True:
        # obstacle detection
        if (GPIO.input(ObstaclePin) == 0) and not (GPIO.input(tilt_switch_pin) == GPIO.LOW):
            GPIO.output(motor_pin, GPIO.HIGH)
            print("Detected Barrier!, Motor ON!!")
        else:
            GPIO.output(motor_pin, GPIO.LOW)

        # tilt switch detection
        if GPIO.input(tilt_switch_pin) == GPIO.LOW and not (GPIO.input(ObstaclePin) == 0):
            print("Tilt switch triggered!")
            GPIO.output(buzzer_pin, GPIO.LOW)
            time.sleep(0.5)
        else:
            GPIO.output(buzzer_pin, GPIO.HIGH)
            
        if (GPIO.input(ObstaclePin) == 0) and (GPIO.input(tilt_switch_pin) == GPIO.LOW):
            print("Both Obstacle and Tilt Detected")
            GPIO.output(buzzer_pin, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(buzzer_pin, GPIO.HIGH)
            time.sleep(0.5)
        else:
            GPIO.output(motor_pin, GPIO.LOW)
            GPIO.output(buzzer_pin, GPIO.HIGH)


def destroy():
    GPIO.cleanup()

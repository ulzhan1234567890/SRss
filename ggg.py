import time
import pygame

def play_alarm(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def set_alarm(alarm_time, sound_file):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            play_alarm(sound_file)
            break
        time.sleep(1)

if __name__ == "__main__":3
    alarm_time = input("Enter the alarm time (in HH:MM:SS format): ")
    sound_file = input("Enter the path to the sound file: ")
    set_alarm(alarm_time, sound_file)

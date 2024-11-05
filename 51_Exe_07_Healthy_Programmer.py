# Healthy Programmer

# 9AM -- 5PM
# Water - water.mp3 (3.5 L) with glass of 200ml
# to stop water.mp3 we need input - Drank - log in text file
water_mp3 = "51_Healthy_Programmer\\asetes\\water.mp3"

to_do_list = ("drank", "eydone", "exdone")


water_glass_count = 0


# Eyes - eyes.mp3
eye_mp3 = "51_Healthy_Programmer\\asetes\\eyes.mp3"
# at every 30 min
# to stop eyes.mp3 we need input - EyDone - log in text file


# Physical Activity - physical.mp3
physical_mp3 = "51_Healthy_Programmer\\asetes\\physical.mp3"
# at every 45 min
# to stop physical.mp3 we need input - ExDone - log in text file

# Rules
# Pygame module to play audio
# Time Should not collaspe if they have same time then second should wait for first


# playing music
def play_music(music_path):
    from pygame import mixer

    mixer.init()
    mixer.music.load(music_path)
    mixer.music.play()
    saveInput()


def saveInput():
    while True:
        stoper = input(
            """Please enter appropiate Message according to 
                      .1 For Drinking Water Enter Drank
                      .2 For Eye Exercise Enter EyDone
                      .3 For Physical Exercise Enter ExDone
                      """
        ).lower()

        if stoper in to_do_list:
            save_log(stoper)
            break
        else:
            print("Invalid Input Please Enter Correct Input")
            continue


# Saving log in log_file
def save_log(writing_in_log):
    from datetime import datetime

    currTime = datetime.now().replace(microsecond=0)
    with open("51_Healthy_Programmer\\asetes\\log.txt", "+a") as f:

        f.write(f"{writing_in_log}\t[{currTime}]\n")

        if writing_in_log == "drank":
            global water_glass_count
            water_glass_count += 1
            f.write(f"{water_glass_count} drank tell now\t[{currTime}]\n")
        pass


def getTime():
    from datetime import datetime

    current_time = datetime.now().time().replace(second=0, microsecond=0)
    current_minute_time = current_time.hour * 60 + current_time.minute
    return current_minute_time


def healthy_logic():
    currentTime = getTime()
    if currentTime % 30 == 0:
        play_music(eye_mp3)
        pass
    elif currentTime % 40 == 0:
        play_music(water_mp3)
        pass
    elif currentTime % 45 == 0:
        play_music(physical_mp3)
        pass

    pass


if __name__ == "__main__":
    from datetime import datetime
    import time

    while True:
        now = datetime.now()
        if 0 <= now.hour and now.hour <= 2:
            healthy_logic()
            time.sleep(60)
            
        else:
            break

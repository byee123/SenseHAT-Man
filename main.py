from sense_hat import SenseHat
import time
import sensible_colours
from ghost_blinky import blinky_frames
from ghost_inky import inky_frames
from ghost_clyde import clyde_frames


def fill_pixels(the_sense_hat, the_animation):
    the_sense_hat.low_light = True

    num_frames = len(the_animation)
    count = 0
    while True:
        pixels = the_animation[count % num_frames]
        the_sense_hat.set_pixels(pixels)
        time.sleep(1 / 4)
        count += 1


if __name__ == '__main__':
    # Initialise the SenseHAT and clear the LED matrix
    sense = SenseHat()
    sense.clear([0, 0, 0])
    sense.low_light = True

    frames = []

    for frame in blinky_frames:
        frames.append(frame)

    for frame in inky_frames:
        frames.append(frame)

    for frame in clyde_frames:
        frames.append(frame)

    fill_pixels(sense, frames)

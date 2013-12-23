import RPi.GPIO as GPIO
import time

# rpi-pcspeaker by jsubirat
#
# Connections:
#       * Speaker + - GPIO 23 (can be modified in SPEAKERPORT variable)
#       * Speaker - - GND
#
# The polarity doesn't matter as long as it is a classical PC speaker. Note that GPIO v0.5.2a is required to have software-PWM.

# GPIO speaker output port in the BCM numbering scheme. You can choose any appropiate output port.
SPEAKERPORT = 23

# Number of steps from A3. Font: http://www.phy.mtu.edu/~suits/NoteFreqCalcs.html
NOTES = {'A2': -12.0, 'Bb2': -11.0, 'B2': -10.0, 'C3': -9.0, 'Db3': -8.0, 'D3': -7.0, 'Eb3': -6.0, 'E3': -5.0, 'F3': -4.0, 'Gb3': -3.0, 'G3': -2.0, 'Ab3': -1.0, 'A3': 0.0, 'Bb3': 1.0, 'B3': 2.0, 'C4': 3.0, 'Db4': 4.0, 'D4': 5.0, 'Eb4': 6.0, 'E4': 7.0, 'F4': 8.0, 'Gb4': 9.0, 'G4': 10.0, 'Ab4': 11.0, 'A4': 12.0, 'Bb4': 13.0, 'B4': 14.0, 'C5': 15.0, 'Db5': 16.0, 'D5': 17.0, 'Eb5': 18.0, 'E5': 19.0, 'F5': 20.0, 'Gb5': 21.0, 'G5': 22.0, 'Ab5': 23.0}

# Key to note mapping
KEYS = {'z': 'A2', 's': 'Bb2', 'x': 'B2', 'c': 'C3', 'f': 'Db3', 'v': 'D3', 'g': 'Eb3', 'b': 'E3', 'n': 'F3', 'j': 'Gb3', 'm': 'G3', 'k': 'Ab3', 'q': 'A3', '2': 'Bb3', 'w': 'B3', 'e': 'C4', '4': 'Db4', 'r': 'D4', '5': 'Eb4', 't': 'E4', 'y': 'F4', '7': 'Gb4', 'u': 'G4', '8': 'Ab4', 'i': 'A4', '9': 'Bb4', 'o': 'B4', 'p': 'C5'} #etc.

# Sets the desired note at the speaker
def tone(speaker, note):
    
    # Font: http://www.phy.mtu.edu/~suits/NoteFreqCalcs.html
    frequency = 440.0 * (1.05946309435929530984310531 ** NOTES[note])
    
    p = GPIO.PWM(speaker, frequency)    # 50 Hertz PWM
    p.start(50) #Duty cicle: 50%
    time.sleep(3)
    p.stop()

# Main code

GPIO.setmode(GPIO.BCM)
GPIO.setup(SPEAKERPORT, GPIO.OUT)

key = ''
while key != ' ':
    key = raw_input('Enter a note: ')
    if key in KEYS.keys():
        tone(SPEAKERPORT, KEYS[key])
    else:
        if key == ' ':
            break
        else:
            print "Invalid note (space to exit)!"

GPIO.cleanup()

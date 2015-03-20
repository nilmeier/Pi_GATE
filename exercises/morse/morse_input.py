#!/usr/bin/python
import pygame, time, RPi.GPIO as GPIO, thread
from array import array
from pygame.locals import *
from morse_lookup import  *

pygame.mixer.pre_init(44100, -16, 1, 1024)
pygame.init()

class ToneSound(pygame.mixer.Sound):
    def __init__(self, frequency, volume):
        self.frequency = frequency
        pygame.mixer.Sound.__init__(self, self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(pygame.mixer.get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(pygame.mixer.get_init()[1]) - 1) - 1
        for time in xrange(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples


def wait_for_keydown(pin):
    global end_thread # terminating wait if thread exits
    while GPIO.input(pin) and not(end_thread):
        time.sleep(0.01)

def wait_for_keyup(pin):
    global end_thread # terminating if thread exits
    while not GPIO.input(pin) and not(end_thread):
        time.sleep(0.01)

def decoder_thread():
    global key_up_time
    global buffer
    new_word = False
    global word
    global end_thread
    
    while True:
        time.sleep(.01)
        key_up_length = time.time() - key_up_time
        if len(buffer) > 0 and key_up_length >= 1.5:
            new_word = True
            bit_string = "".join(buffer)
            letter=try_decode(bit_string)
            print "( "+' '.join(buffer) + " )->" +letter
            word.append(letter)
            print ''.join(word)
            del buffer[:]
        elif new_word and key_up_length >= 4.5:
            new_word = False
            sys.stdout.write("(word complete.)")
            sys.stdout.flush()
            end_thread=True
            return 

db=False
DASH, DOT = "-","."

tone_obj = ToneSound(frequency = 800, volume = .5)

pin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# global variables used
end_thread=False
key_down_time = 0
key_down_length = 0
key_up_time = 0
buffer = []
word = []
db=False


thread.start_new_thread(decoder_thread,())

print "Ready"

def get_morse_word():
  # everything has global scope
  global end_thread, key_down_time,key_down_length,key_up_time,buffer,word,db
  while end_thread==False:
      wait_for_keydown(pin)
      if db: print "down"
      key_down_time=time.time()
      tone_obj.play(-1) #the -1 means to loop the sound
      wait_for_keyup(pin)
      # get lenght of time held down
      key_up_time = time.time()
      key_down_length = key_up_time-key_down_time 
      tone_obj.stop()
      buffer.append(DASH if key_down_length > 0.15 else DOT)  
      print str(' '.join(buffer))
      if end_thread:
        if db: print ''.join(word)
        return ''.join(word)
        thread.exit() 


#word=get_morse_word() 
#print 'word: ' + str(word)     
       

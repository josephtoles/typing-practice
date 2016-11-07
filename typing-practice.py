#!/usr/bin/python
import random
import sys
import datetime
import signal

keys_without_space = ('abcdefghijklmnopqrstuvwxyz'
        #'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        '`1234567890-='
        '~!@#$%^&*()_+'
        '[]\\'
        '{}|'
        ';\''
        ':"'
        ',./'
        '<>?')

keys = keys_without_space + ' '

if ('--letters-only' in sys.argv[1:]):
    keys = 'abcdefghijklmnopqrstuvwxyz'

keystrokes_per_try = 16

def get_random_characters(keystrokes_per_try=keystrokes_per_try):
    output = ''
    for i in range(0, keystrokes_per_try - 1):
        output += random.choice(keys)
    output += random.choice(keys_without_space)
    return output

def test_player(test_letters):
    global correct
    global incorrect
    start_time = datetime.datetime.now()
    player_letters = raw_input(test_letters + '\n')
    if (player_letters == test_letters):
        end_time = datetime.datetime.now()
        delta = end_time - start_time
        if (delta > datetime.timedelta(minutes=1)):
            print 'correct, but you took too long'
        else:
            seconds = delta.seconds
            micros = delta.microseconds
            print 'good job with time ' + str(seconds) + '.' + str(micros)
            correct += 1
    else:
        print 'mistake. try again'
        incorrect += 1
        test_player(test_letters)

correct = 0
incorrect = 0

# Ctrl+C handling
def end_game(signal, frame):
    correct
    incorrect
    if (correct != 0 or incorrect != 0):
        print 'You got ' + str(correct) + ' correct and ' + str(incorrect) + ' incorrect'
    else:
        print '' # starts newline after ^C
    sys.exit(0)
signal.signal(signal.SIGINT, end_game)

# Event loop
while (True):
    test_letters = get_random_characters()
    test_player(test_letters)


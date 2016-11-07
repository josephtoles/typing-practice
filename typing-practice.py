#!/usr/bin/python
import random
import sys
import datetime

keys = ('abcdefghijklmnopqrstuvwxyz'
        #'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        '`1234567890-='
        '~!@#$%^&*()_+'
        '[]\\'
        '{}|'
        ';\''
        ':"'
        ',./'
        '<>?'
        ' ')

if ('--letters-only' in sys.argv[1:]):
    keys = 'abcdefghijklmnopqrstuvwxyz'

keystrokes_per_try = 12

def get_random_character():
    return random.choice(keys)

def get_random_characters(keystrokes_per_try=keystrokes_per_try):
    output = ''
    for i in range(0, keystrokes_per_try):
        output += get_random_character()
    return output

def test_player(test_letters):
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
    else:
        print 'mistake. try again'
        test_player(test_letters)

while (True):
    test_letters = get_random_characters()
    test_player(test_letters)


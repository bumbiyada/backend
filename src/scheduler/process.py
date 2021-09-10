import sys
import time



def process():
    sys.stdout.write('scheduler works')


def process_2():
    try:
        sys.stdout.write('scheduler works')
    except:
        sys.stdout.write('aboba\n')

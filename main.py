#!/usr/bin/python

import time
import argparse
from datetime import datetime, timedelta


class CountDown:

    def __init__(self, time, step):
        self.time = time
        self.step = step

    def set_step(self, step):
        self.step = step

    def tick(self):
        self.time = self.time - timedelta(hours=self.step)

    def format(self):
        # Use isoformat, because strftime doesn't work for year < 1900
        # Manually format the date if another format is needed
        return self.time.isoformat(' ').split('.')[0]


class Printer:

    def write(self, string):
        print(string)


def validate_step(val):
    try:
        val = int(val)
    except ValueError:
        raise argparse.ArgumentTypeError('%s is an invalid integer' % val)

    if val <= 0:
        raise argparse.ArgumentTypeError('Step needs to be a positive value')

    return val


def run(counter, printer=None):
    printer = printer or Printer()

    while True:
        printer.write('Time is %s' % counter.format())
        time.sleep(0.02)  # Delay printing so we can somewhat see the output
        try:
            counter.tick()
        except OverflowError:
            printer.write('You have reached the beginning of the common era')
            break


def main():
    parser = argparse.ArgumentParser(description='Countdown timer')
    parser.add_argument('step', type=validate_step, help='Countdown step in hours')
    args = parser.parse_args()

    run(CountDown(datetime.now(), args.step))


if __name__ == '__main__':
    main()

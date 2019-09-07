import unittest
import argparse
from main import CountDown, validate_step, run
from datetime import datetime, timedelta


class TestPrinter:
    def __init__(self):
        self.outputs = []

    def write(self, msg):
        self.outputs.append(msg)


class TestCountDown(unittest.TestCase):

    def test_timer_deduction(self):
        now = datetime.now()
        c = CountDown(now, 1)

        c.tick()
        self.assertEqual(c.time - now, timedelta(hours=-1), 'Timer should go down by 1 hour')

        c.tick()
        self.assertEqual(c.time - now, timedelta(hours=-2), 'Timer should go down by 2 hour')

        c.set_step(123)
        c.tick()
        self.assertEqual(c.time - now, timedelta(hours=-125), 'Timer should go down by 125 hour')

    def test_time_formatting(self):
        t = datetime(2019, 1, 1, 1, 2, 3)
        c = CountDown(t, 1)
        self.assertEqual(c.format(), '2019-01-01 01:02:03')

    def test_steps_validation(self):
        self.assertRaises(argparse.ArgumentTypeError, validate_step, '1.5')
        self.assertRaises(argparse.ArgumentTypeError, validate_step, '-1')
        self.assertRaises(argparse.ArgumentTypeError, validate_step, 'ABC')

        val = validate_step('1')
        self.assertEqual(1, val)

    def test_ticks_limit(self):
        t = datetime(1, 1, 1, 10, 2, 3)
        c = CountDown(t, 11)
        self.assertRaises(OverflowError, c.tick)

    def test_runner(self):
        printer = TestPrinter()
        counter = CountDown(datetime(1, 1, 1, 10, 0, 0), 1)
        run(counter, printer)

        # Prints 11 timestamps (10 - 0, inclusive) and end of time statement
        self.assertEqual(len(printer.outputs), 12)
        self.assertEqual(printer.outputs[-2], 'Time is %s' % counter.format())
        self.assertEqual(printer.outputs[-1], 'You have reached the beginning of the common era')


if __name__ == '__main__':
    unittest.main()

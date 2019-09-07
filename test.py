import unittest
import argparse
from main import CountDown, validate_step
from datetime import datetime, timedelta


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


if __name__ == '__main__':
    unittest.main()

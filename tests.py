import unittest
import time

from expiring_object import object_factory, Dispatcher


class Stub:
    pass


class MyTestCase(unittest.TestCase):
    def test_dispatcher(self):
        """test a functionality of dispatcher and weak referencing"""
        with Dispatcher(2) as dp:
            myobj = object_factory(Stub(), dp)
            time.sleep(2)
            with self.assertRaises(ReferenceError):
                print(myobj)
            self.assertEqual(len(dp.container), 0)


if __name__ == '__main__':
    unittest.main()

from tools import *

import os
import pymailsort

class TestPyMailSort:

    def test_pymailsort(self):
        pymailsort.LOGFILENAME = "./test.log"
        print(pymailsort.LOGFILENAME)

        for root, dirs, files in os.walk("./tests/data", topdown=False):
            files = sorted(files)
            for name in files:
                expected = ".".join(os.path.basename(name).split(".")[:-2])
                self.do_file(os.path.join(root, name), expected)

    def do_file(self, filename, expected):
        f = open(filename, 'r')
        actual = pymailsort.process_mail(f)
        same("%s should go to %s" % (filename, expected), expected, actual)

import unittest
from ..FileToListUtil import *
import os


class MyTestCase(unittest.TestCase):
    def test_read_simple_input(self):
        file_reader_util = FileToListUtil()
        file_path = os.path.abspath("jl_advent_of_code_utils/testData/readmeFile1")
        input_list = file_reader_util.readInputFileToList(file_path)
        self.assertEqual(11, len(input_list))
        self.assertEqual(6,  int(input_list[5]))


if __name__ == '__main__':
    unittest.main()

from utils import execute_process
import unittest
import random

class TestAddListElements(unittest.TestCase):
    def test_one_empty_list(self):
        my2dlist=[[]]
        output=execute_process(my2dlist)
        self.assertEqual(output,["empty"])

    def test_empty_bothlist(self):
        my2dlist=[[],[]]
        output=execute_process(my2dlist)
        self.assertEqual(output,["empty","empty"])

    def test_extending_list(self):
        my2dlist=[[-1,-1],[-5,-6]]
        my2dlist.extend([[10]])
        output=execute_process(my2dlist)
        self.assertEqual(output,[-2, -11, 10])

    def test_withsingle_ele(self):
        my2dlist=[[-1,-1],[-5,-6]]
        my2dlist.extend([10])
        output=execute_process(my2dlist)
        self.assertEqual(output,[-2, -11, 'empty'])

    def test_with_str(self):
        my2dlist=[[-1,-1],["abc","def"]]
        output=execute_process(my2dlist)
        self.assertEqual(output,[-2, 'empty'])

    def test_multiple_ele(self):
        my2dlist=[[1,2,3,4,5,6,6,7,8],[4,5,6,7,8,9,9,100,200,300],[100,200,300,500,700,900,10000]]
        output=execute_process(my2dlist)
        self.assertEqual(output,[42, 648, 12700])

    def test_empty_string_special_case(self):
        my2dlist=[['^^^$$@@@@@@@','^^^^^^#@#@#@#@#@#@#@#'],['~~~~~~~~~~~~~~~~~~~~']]
        output=execute_process(my2dlist)
        self.assertEqual(output,['empty','empty'])

    def test_float_values(self):
        my2list=[[0.1,0.2,0.4,0.5],[1.0,1.1,1.4,1.5,1.8],[9.0,9.9999]]
        output=execute_process(my2list)
        self.assertEqual(output,[1.2000000000000002, 6.8, 18.9999])

    def test_int_float_values(self):
        my2list=[[0.1,0.2,1,2],[9,9.9999]]
        output=execute_process(my2list)
        self.assertEqual(output,[3.3,18.9999])

if __name__ == '__main__':
    unittest.main()
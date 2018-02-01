import unittest;
from lab1_1 import vowelsRemover;
from lab1_2 import characterLocator;
from lab1_3 import multiplyTable;
from lab1_4 import calcArea;
from lab1_5 import dictionary;
from lab1_6 import arc;
class Test_lab1(unittest.TestCase):
    
    def test_vowelsRemover(self):
        res = vowelsRemover("mobile");
        self.assertEqual(res,"mbl");

    def test_characterLocator(self):
        res = characterLocator("this is javaScript",'i');
        out=[2,5,15];
        self.assertEqual(res,out);

    def test_multiplyTable(self):
        res = multiplyTable(3);
        out=[[1],[2,4],[3,6,9]];
        self.assertEqual(res,out);

    def test_calcArea(self):
        res = calcArea("c",10);
        self.assertEqual(res,314.0);

    def test_dictionary(self):
        l=["zinab","wael","ahmed","fatma","ibrahim","ali","islam"];
        res = dictionary(l);
        out={'a': ['ahmed', 'ali'], 'i': ['ibrahim', 'islam'], 'z': ['zinab'], 'w': ['wael'], 'f': ['fatma']};
        self.assertEqual(res,out);

    def test_arc(self):
        res =arc(4);
        out=['   *', '  **', ' ***','****'];
        self.assertEqual(res,out);

if __name__ == '__main__':
    unittest.main();

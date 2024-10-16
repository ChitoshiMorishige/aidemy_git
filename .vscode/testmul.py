import unittest
import mul # 対象ファイルのインポート

class Test(unittest.TestCase):
    def test_first(self):
        self.assertEqual(mul.mul(1,12),12)
        self.assertEqual(mul.mul(2,5),10)

if __name__ == '__main__':
    unittest.main()
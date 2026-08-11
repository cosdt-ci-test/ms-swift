# 测试 ascend npu 的 quick start
import unittest


class TestNpuSupport(unittest.TestCase):

    def test_placeholder(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
import unittest

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(*args):
    return True

class TestCases(unittest.TestCase):
    def test_input_txt(self):
        answer = read_file('<path_to_file>')
        self.assertEqual(main(), answer)


if __name__ == '__main__':
    unittest.main()
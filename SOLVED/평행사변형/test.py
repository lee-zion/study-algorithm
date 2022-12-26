import unittest
from traceback import print_exception
import sys, math

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(inputs):
    answers = []
    try:
        for input in inputs:
            # your code here
            # A 기준의 방향벡터 vec{ab}, vec{ac}를 찾음
            # c +- vec{ab}, b +- vec{ac}를 d의 set에 추가
            # 각 경우에 대해 둘레의 길이 / 2를 구하면 아래와 같음
            # c +- vec{ab} --> vec{ab} + vec{ac}, vec{ab} + vec{ad}
            # b +- vec{ac} --> vec{ac} + vec{ab}, vec{ac} + vec{ad}
            # 즉, 어떤 경우에도 아래 3가지를 벗어나지 못함 == D는 최대 3개 존재
            # vec{ab} + vec{ac}, vec{ab} + vec{ad}, vec{ac} + vec{ad}
            points = list(map(int, input[0].split()))

            def get_vector(x, y):
                # vector from x to y
                vec = [0, 0]
                for i in range(2):
                    vec[i] = y[i] - x[i]
                return vec

            def add_vector(x, y):
                vec = [0, 0]
                for i in range(2):
                    vec[i] = x[i] + y[i]
                return vec
            
            def flip_vector(x):
                for i in range(2):
                    x[i] = -x[i]
                return x
            
            def len_vector(x):
                length = 0
                for i in range(2):
                    pow(x[i], 2)
                    
            a = points[0:2]
            b = points[2:4]
            c = points[4:6]
            ab = get_vector(a, b)
            ac = get_vector(a, c)
            
            def is_parallel(a, b, c):
                x1, y1 = a
                x2, y2 = b
                x3, y3 = c
                # ab is parallel to ac: y2-y1/x2-x1 = y3-y1/x3-x1
                # (y2-y1)*(x3-x1) = (y3-y1)*(x2-x1)
                # -x1y2 +x1y1 -x3y1 +x3y2 = x1y1 +x2y3 -x1y3 -x2y1
                # -> -x1y2 -x3y1 +x3y2 = -x1y3 -x2y1 +x2y3
                # x1(y3 -y2) + x2(y1 -y3) + x3(y2 -y1) = 0
                if math.fabs(x1*(y3 - y2) + x2*(y1 - y3) + x3*(y2 - y1)) <= 1e-9:
                    return True
                return False
            
            # answer = None            
            if is_parallel(a, b, c):
                answer = -1.0
            else:
                # ds = []
                rect = []

                d = add_vector(c, ab) # ab, ac
                rect.append((math.dist(a, b) + math.dist(a, c)) * 2)

                d = add_vector(c, flip_vector(ab)) # ab, ad
                rect.append((math.dist(a, b) + math.dist(a, d)) * 2)
                
                # ds.append(add_vector(b, ac)) # the same with add_vector(c, ab)
                # b + c - a = c + b - a
                
                d = add_vector(b, flip_vector(ac)) # ac, ad
                rect.append((math.dist(a, c) + math.dist(a, d)) * 2)
                
                answer = max(rect) - min(rect)
            answers.append(answer)
        return answers
    except Exception:
        print(f"===========================================================================")
        print(f"Failed in the case below")
        print(f"input: {input}")
        exc_info = sys.exc_info()
        print_exception(*exc_info)
        print(f"===========================================================================")
        del exc_info
class TestCases(unittest.TestCase):
    def test_input_txt(self):
        inputs, answers = [], []
        for i in range(1, 5 + 1):
            inputs.append(read_file(f"평행사변형/input{i}.txt"))
            answers.append(float(read_file(f"평행사변형/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()
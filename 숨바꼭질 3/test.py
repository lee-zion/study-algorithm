import unittest
from traceback import print_exception
import sys
from collections import deque

def read_file(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret

def main(inputs):
    """
    case 1) departure > arrival
    answer += (departure - arrival)

    case 2) departure < arrival
    d = { d+1, d-1, d*2 }
    """
    answers = []
    try:
        for ti in inputs:
            departure, arrival = map(int, ti[0].split())
            INF = max(departure, arrival)
            dist = [INF] * INF * 2
            answer = INF
            q = deque([departure])
            dist[departure] = 0
            while q:
                current = q.popleft()
                if current == arrival:
                    answer = dist[arrival]
                    break
                warp = current * 2
                # if only current is faster than warped
                if warp < INF * 2 and dist[warp] > dist[current]:
                    dist[warp] = dist[current] 
                    q.append(warp)
                left, right = current - 1, current + 1
                if left >= 0 and dist[left] > dist[current]:
                    dist[left] = dist[current] + 1
                    q.append(left)
                if right < INF * 2 and dist[right] > dist[current]:
                    dist[right] = dist[current] + 1
                    q.append(right)
            answers.append(answer)
        return answers
    except Exception:
        print(f"===========================================================================")
        print(f"Failed in the case below")
        print(f"input: {ti}")
        exc_info = sys.exc_info()
        print_exception(*exc_info)
        print(f"===========================================================================")
        del exc_info
class TestCases(unittest.TestCase):
    def test_input_txt(self):
        inputs, answers = [], []
        for i in range(1, 1 + 1):
            inputs.append(read_file(f"숨바꼭질 3/input{i}.txt"))
            answers.append(int(read_file(f"숨바꼭질 3/output{i}.txt")[0]))
        self.assertEqual(main(inputs), answers)


if __name__ == '__main__':
    unittest.main()
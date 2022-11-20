import unittest, copy


def read_file(filename):
    file = open(filename, "r")
    ret = file.readlines()
    for i, l in enumerate(ret):
        ret[i] = l.strip()
    file.close()
    return ret


def main(reference, track):
    # subset이 너무 많으니까, hash dict로 만들기?
    # -> ㄴㄴ DP문제
    subsets = set()
    lr = len(reference)
    for i in range(lr):
        for l in range(1, lr + 1 - i):
            subsets.add(reference[i : i + l])

    lt = len(track)
    # track_dp = [0] * lt
    dp = [lt + 1] * (lt + 1)
    dp[0] = 0
    # DP
    # track_dp[i] = i번째 문자까지 오는데 필요한 최소 점프 횟수
    
    # 속할 경우? i에서 i+l은 원점프로 이동가능
    # -> dp[i+l] = dp[i] + 1

    # 없을 경우? 시작점 바꿔서 원점프가 가능한지 다시 확인
    # 끝까지 없을 경우? 최저점 1이니까 더 확인할거 없이 종료 (점프 못하는 경우는 없으니까)

    # 시작점 curr 고정
    dp_prev = [0]*(lt+1)
    for curr in range(lt):
        # 길이 l 늘리면서 substr 증가
        dp_prev = copy.deepcopy(dp)
        for l in range(1, lt + 1 - curr):
            # substr이 subset에 속하는지 확인
            if track[curr : curr + l] in subsets:
                dp[curr + l] = min(dp[curr + l], dp[curr] + 1)
            dp[curr + l] = min(dp[curr + l], dp[curr + l - 1] + 1)
                # track_dp[i] = min(track_dp[i], current)
    return dp[-1]


class TestCases(unittest.TestCase):
    def test_input_txt(self):
        references = ["abc", "vxrvip"]
        tracks = ["bcab", "xrviprvipvxrv"]
        answers = [2, 3]
        # self.assertEqual(main(references[0], tracks[0]), answers[0])
        self.assertEqual(main(references[1], tracks[1]), answers[1])
        # for i in range(len(answers)):
        #     self.assertEqual(main(references[i], tracks[i]), answers[i])


if __name__ == "__main__":
    unittest.main()

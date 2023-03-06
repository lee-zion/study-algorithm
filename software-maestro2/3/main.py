from collections import deque

def solution(n, k, infos):
    """
    n in [2**2, 2**12]
    k in [n, 2**12]
    infos = [[time, position]], time is unique key in infos, sorted in ascending order
    time in [1, 10**12]
    position in [0, 1] == [Enterance, Exit]

    people need n/2 step to exit the door
    n k infos
    4 5 10 51 61 100 170
    3 7 8 18 19
    12 25 71 250 260 270 280 290 300 310
    """
    answer = []
    rotate_id = deque()
    rotate_enter = deque()
    rotate_dist = deque()

    time, time_prev = 0, -5
    cnt = 0
    goal_dist = n/2

    for id, info in enumerate(infos):
        time, pos = info
        rotate_id.append(id)
        rotate_enter.append(time)
        rotate_dist.append(0)

        # print(f"ids: {rotate_id}")
        # print(f"ent: {rotate_enter}")
        # print(f"dis: {rotate_dist}")

        # time >= time_prev + 6: rotate again
        t_diff = time - time_prev
        if t_diff >= 6:
            is_rotating = True
        else:
            # this person should go for t_diff step
            rotate_dist[-1] += t_diff
        # update state
        time_prev = time

        if is_rotating:
            for i in range(len(rotate_dist)):
                rotate_dist[i] += 6

        while True:
            break
            top = rotate_dist.popleft()
            if top >= goal_dist:
                entered = rotate_enter.popleft()
                answer.append(entered + top)
                continue
            rotate_dist.appendleft(top)
            break

    for i in range(len(rotate_id)):
        answer.append(-1)

    return answer
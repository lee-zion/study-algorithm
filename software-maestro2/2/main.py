from collections import deque

def solution(t, e, charge, dist):
    """
    [1, e, t, 100]
    [3, n, 3000]
    dist = charge - 1

    charge[i] = charger[i+1].supply
    dist[i] = charger[i+2].x - charger[i+1].x
    """

    dist_plan = deque([])

    base = max(charge[:-1])
    base_idx = charge.index(base)
    hungry_dist = sum(dist[:base_idx])
    boost_dist = sum(dist[base_idx:])
    dist_plan.appendleft(boost_dist)

    charger = charge
    while base_idx > 0:
        charger = charger[:base_idx]
        dist = dist[:base_idx]
        base = max(charger)
        base_idx = charger.index(base)
        hungry_dist = sum(dist[:base_idx])
        boost_dist = sum(dist[base_idx:])
        dist_plan.appendleft(boost_dist)

    goal = dist[-1]
    pos_x = 0
    time = 0
    dist_idx = 0
    station_idx = 0
    battery_level = 0
    while True:
        if dist_idx >= len(dist_plan):
            break
        time += 1
        res = time % t
        to_go = dist_plan[dist_idx]

        if to_go + 1 <= battery_level + ((res + to_go) // t) * e:
            time -= 1
            # print(f"on to go: {to_go} to_gen: {((res + to_go)//t*e)} batt: {battery_level}")
            pos_x += to_go
            time += to_go
            battery_level -= to_go
            battery_level += ((res + to_go) // t) * e
            station_idx += 1
            dist_idx += 1
            # print("Jump")
            # print(f"time: {time} x: {pos_x}, battery: {battery_level}, station {station_idx}")
        else:
            if res == 0:
                battery_level += e
            battery_level += charge[station_idx]
            # print(f"time: {time} res: {res} x: {pos_x} battery: {battery_level}, station {station_idx}")
            # print(f"to go: {to_go} to_gen: {((res + to_go)//t*e)} batt: {battery_level}")
            if to_go + 1 <= battery_level + ((res + to_go) // t) * e:
                # print(f"on to go: {to_go} to_gen: {((res + to_go)//t*e)} batt: {battery_level}")
                pos_x += to_go
                time += to_go
                battery_level -= to_go
                battery_level += ((res + to_go) // t) * e
                station_idx += 1
                dist_idx += 1
                # print("Jump")
                # print(f"time: {time} x: {pos_x}, battery: {battery_level}, station {station_idx}")

    answer = [time, battery_level]
    return answer

t = 3
e = 1
charge = [2, 4, 4]
dist = [4, 16]
answer = solution(t, e, charge, dist)
print(answer)
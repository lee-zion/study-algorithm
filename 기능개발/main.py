import math

def solution(progresses, speeds):
    day_needed = []
    for i in range(len(progresses)):
        day_needed.append(math.ceil((100 - progresses[i])/speeds[i]))
    
    answer = []
    head = 0
    num_released = 1
    
    if len(day_needed) == 1:
        return [1]
    
    for i in range(1, len(day_needed)):
        if day_needed[head] >= day_needed[i]:
            num_released += 1
        else:
            answer.append(num_released)
            head = i
            num_released = 1
        
        if i == len(day_needed) - 1:
            answer.append(num_released)
    
    return answer
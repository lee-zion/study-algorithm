def solution(image):
    """
    <- : 먼저 <를 찾으면 검색 가능. 반드시 다음 <를 만나기 전까지는 -만 있으므로 <를 찾으면 됨. 반대로 말하면, >를 만나는 순간 <- 이 아니라 <->임
    -> : <가 없는데 
    """
    answer = []
    cnt_len = 0
    type = None
    for s in image:
        if s == "-":
            cnt_len += 1
            continue
        if s == "<":
            if type == -1:
                answer.append([-1, cnt_len])
            type = -1
            cnt_len = 0
        elif s == ">":
            if type == -1:
                answer.append([0, cnt_len])
            elif type == 1 or type == None:
                answer.append([1, cnt_len])
            type = 1
            cnt_len = 0
    if cnt_len:
        answer.append([-1, cnt_len])
    return answer
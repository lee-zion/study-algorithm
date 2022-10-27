def solution(lines):
    S, E = [], []
    for line in lines:
        (d, s, t) = line.split(" ")
        (hh, mm, ss) = s.split(":")
        endedms = int(hh)*3600 + int(mm)*60 + float(ss)
        tms = float(t[0:-1])
        beginedms = endedms - tms + 0.001
        E.append(endedms+1)
        S.append(beginedms)
    
    S.sort()
    
    answer, ei, si, num_processed = 1, 0, 0, 0
    while (ei < len(lines) and si < len(lines)):
        if E[ei] > S[si]:
            num_processed += 1
            answer = max(answer, num_processed)
            si += 1
        else:
            num_processed -= 1
            ei += 1
    
    return answer
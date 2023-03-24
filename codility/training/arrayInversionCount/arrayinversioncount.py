import sys
import heapq
sys.setrecursionlimit(10**6)

def solution(A):
    def find_inversion(pivot: int, l: list):
        """
        1) find the smallest element from list at index m1, set the value as pivot p
        2) update ltm(lower_than_me: list)
        definition of lower_than_me[i] at pivot p
        : accumulated number of elements lower than p until index i
        3) get the second smallest at index m2, set the value as pivot p
        4) update ltm
        if m1 > m2:
            m1 is located at right-side
            ltm(m2) will update l[m2:m1] only. Because l[m1:] is already counted
        if m1 < m2:
            m2 is located at right-side
            ltm(m2) loops for every element
        5) find the third smallest at index m3, set the value as pivot p
        ...
        """

        """
        ltm[i]: i가 inversion end로 처리된 횟수
        
        For example,

        [[input]]
        A  : [-1 6 3 4 7 4]
        [[output]]
        inv: [ 0 0 1 1 0 2]

        [[debug]]
        init    [0 0 0 0 0 0]
        -1,(-)0    [0 0 0 0 0 0] (i=x)
         3,(-)2    [0 0 0 0 0 0] (i=3,4,5)
         4,(-)5    [0 0 0 0 0 0] (i=x)
         4,(-)3    [0 0 0 0 0 0] (i=4)
         6,(-)1    [0 0 1 1 0 1] (i=2,3,4,5)
         7,(-)4    [0 0 1 1 0 2] (i=5)
         or
         7,(-)4    [0 0 0 0 0 1] (i=5)

        for efficiency, merge duplicated iterations by making a log and execute loop at the last step
        """
        def get_heap_inv(l: list):
            heap = []
            for i, e in enumerate(l):
                heapq.heappush(heap, (e, -i))
            return heap
        
        def update_ltm(h: list, m: int, i_m: int):
            nonlocal ltm, A
            n, i_n = heapq.heappop(heap)
            if i_m > i_n:
                # update_ltm(h[i_n:i_m])
                for i in range(i_n + 1, i_m):
                    if n > A[i]:
                        ltm[i] += 1
            

        l = len(A)
        heap = get_heap_inv(A)
        ltm = [0] * l
        e, i = heapq.heappop(heap)
        update_ltm(heap, e, -i)

        """
        ltm algorithm for a given example
        [-1 6 3 4 7 4]
        [ 0 1 2 3 4 5]
        
        

        ltm = [0] * 6
        e, i = -1, 0
        update_ltm(heap, -1, 0) current pivot is -1 at index 0
        m, i_m = -1,  0
        n, i_n =  3, -2
        
        # ALWAYS: n >= m
        # if new is located LHS to minimum, update ltm[i_n+1:i_m]
        # else, update ltm[i_n+1:]
        # in other words
        for i in range(i_n+1, len(ltm)):
            inc = 1 if n > A[i] else 0
            ltm[i] += inc
        if i_m = 0 > i_n = -2: # new is located right side of current minimum



        """
    pass

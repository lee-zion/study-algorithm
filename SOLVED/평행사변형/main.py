import sys, math

def main():
    points = list(map(int, sys.stdin.readline().split()))
    
    def get_vector(x, y):
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

    def is_parallel(a, b, c):
        x1, y1 = a
        x2, y2 = b
        x3, y3 = c
        if math.fabs(x1*(y3 - y2) + x2*(y1 - y3) + x3*(y2 - y1)) <= 1e-9:
            return True
        return False
    
    a, b, c = points[0:2], points[2:4], points[4:6]
    ab = get_vector(a, b)
    ac = get_vector(a, c)
    
    if is_parallel(a, b, c):
        print(-1.0)
    else:
        rect = []
        d = add_vector(c, ab)
        rect.append((math.dist(a, b) + math.dist(a, c)) * 2)
        d = add_vector(c, flip_vector(ab))
        rect.append((math.dist(a, b) + math.dist(a, d)) * 2)
        d = add_vector(b, flip_vector(ac))
        rect.append((math.dist(a, c) + math.dist(a, d)) * 2)
        print(max(rect) - min(rect))

if __name__ == "__main__":
    main()
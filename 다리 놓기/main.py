def readFile(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for line in range(len(ret)):
        ret[line] = ret[line].strip()
    file.close()
    return ret

def main(*args, **kwargs):
    file_raw = readFile('test.txt')
    print(file_raw)
    num_cases = file_raw[0]

def test():
    arr = [1, 2, 3, 4]
    for e in arr:
        e += 1
        print(e, arr)
    print(arr)

if __name__ == '__main__':
    main()
    # test()
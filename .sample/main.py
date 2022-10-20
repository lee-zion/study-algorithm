def readFile(filename):
    file = open(filename, 'r')
    ret = file.readlines()
    for line in range(len(ret)):
        ret[line] = ret[line].strip()
    file.close()
    return ret
    
def main(*args, **kwargs):
    file_raw = readFile('input.txt')
    print(file_raw)

if __name__ == "__main__":
    main()
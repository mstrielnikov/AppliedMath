from sys import argv

def WalshHadamard(vector) -> list:
    vectorLen = len(vector)
    transform = []
    h = 1
    while h < vectorLen:
        for i in range(0, vectorLen, h * 2):
            for j in range(i, i + h):
                x = vector[j]
                y = vector[j + h]
                transform[j] = x + y
                transform[j + h] = x - y
        h *= 2
    return transform
  
if __name__ == "__main__":
    print(WalshHadamard(sys.argv[1]))
  

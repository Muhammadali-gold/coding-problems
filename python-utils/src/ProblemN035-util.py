

def main():
    with open('./resources/data.txt') as f:
        data = f.readline().split(',')
    with open('./resources/output.txt','w') as output:
        output.write(','.join([a + 'L' for a in data]))



if __name__ == '__main__':
    main()

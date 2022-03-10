testcases =int(input().strip())
while testcases!=0:
    sizes,times =map(int,input().split())
    binary_string =input()
    current_string=" "
    count=-1
    for i in range(sizes):
        if current_string <binary_string:
            current_string=binary_string
            shifts=i
        elif current_string ==binary_string:
            count= i-shifts
            break
        binary_string= binary_string[1:] + binary_string[:1]

    if count==-1:
        print (shifts +(times-1)*sizes)
    else:
        print (shifts+ (times-1)*count)
    print(" ") 
    testcases -=1

def check(sym):
    for i in range(3):
        cnt1 = 0
        cnt2 = 0
        for j in range(3):
            if arr[i][j] == sym:
                cnt1+=1
            if arr[j][i] == sym:
                cnt2+=1
        if cnt1 == 3:
            return True
        if cnt2 == 3:
            return True

    if arr[0][0] == arr[1][1] == arr[2][2] == sym:
        return True

    if arr[2][0] == arr[1][1] == arr[0][2] == sym:
        return True
    return False

while True:
    _input = input()
    if _input == "end":
        break

    xcnt = 0
    ocnt = 0
    index = 0
    arr = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            arr[i][j] = _input[index]
            if _input[index] == 'X':
                xcnt+=1
            if _input[index] == 'O':
                ocnt+=1
            index += 1

    if xcnt > ocnt + 1:
        print("invalid")
        continue
    if ocnt > xcnt:
        print("invalid")
        continue
    if ocnt == xcnt:
        if check('O') and not check('X'):
            print("valid")
            continue

    if ocnt+1 == xcnt:
        if check('X') and not check('O'):
            print("valid")
            continue
    if xcnt==5 and ocnt ==4:
        if not check("O"):
            print("valid")
            continue
    print("invalid")

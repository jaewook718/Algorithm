T = int(input())
for _ in range(T):
    W = input()
    K = int(input())
    word_dict = {}
    for i in range(len(W)):
        if W[i] in word_dict.keys():
            word_dict[W[i]].append(i)
        else:
            word_dict[W[i]] = [i]
    _max = 0
    _min = int(1e9)
    flag = False
    for key, value in word_dict.items():

        if len(value) == K:
            _len = value[-1] - value[0] + 1
            _max = max(_len, _max)
            _min = min(_len, _min)
            flag = True
        elif len(value) > K:
            for i in range(len(value) - K + 1):
                _len = value[i+K-1] - value[i] + 1
                _max = max(_len, _max)
                _min = min(_len, _min)
                flag = True
    if flag:
        print(_min, _max)
    else:
        print(-1)
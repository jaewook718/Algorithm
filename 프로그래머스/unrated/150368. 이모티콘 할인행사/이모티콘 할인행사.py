def solution(users, emoticons):
    max_plus = 0
    payment = 0
    discount_list = []
    ratio = [10, 20, 30 ,40]
    def dfs(arr, index):
        if index == len(arr):
            discount_list.append(arr[:])
            return
        for r in ratio:
            arr[index] = r
            dfs(arr, index+1)
            arr[index] = 0
    dfs([0]* len(emoticons) , 0)
    
    for discount in discount_list:
        cnt = 0
        emoticons_pay = 0
        for user in users:
            pay = 0
            for i in range(len(discount)):
                if user[0] <= discount[i]:
                    pay += emoticons[i] * (100 - discount[i]) / 100
                if pay >= user[1]:
                    pay = 0
                    cnt += 1
                    break
            emoticons_pay += pay
        if cnt >= max_plus:
            if cnt == max_plus:
                payment = max(payment, emoticons_pay)
            else:
                payment = emoticons_pay
                max_plus = cnt
            
        
    return [max_plus, payment]
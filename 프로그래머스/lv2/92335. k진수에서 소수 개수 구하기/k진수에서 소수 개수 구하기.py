def make(n, k):
    word = ""
    while n:
        word = str(n%k)+ word
        n //= k
    return word

def check(num):
    for i in range(2, int(num**.5) + 1):
        if not num % i:
            return False
        
    return True

def solution(n, k):
    answer = 0
    word = make(n, k)
    split_words = word.split("0")
    for split_word in split_words:
        if split_word:
            if int(split_word)>=2 and check(int(split_word)):
                answer+=1
    return answer
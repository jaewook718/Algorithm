def recursion(word):
    global ans

    if word == word1:
        ans = 1
        return

    if len(word) == 0:
        return

    if word[-1] == 'A':
        recursion(word[:-1])

    if word[0] == 'B':
        recursion(word[1:][::-1])


word1 = list(input())
word2 = list(input())
ans = 0
recursion(word2)
print(ans)




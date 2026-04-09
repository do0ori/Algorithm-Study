from collections import Counter

word1 = Counter(input())
word2 = Counter(input())

answer = 0
base = ord("a")
for i in range(26):
    answer += abs(word1[chr(base + i)] - word2[chr(base + i)])

print(answer)

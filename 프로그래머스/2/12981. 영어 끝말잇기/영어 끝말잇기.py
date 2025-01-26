def solution(n, words):
    visit = set()
    last_word = None
    for i, word in enumerate(words):
        # 첫 단어는 스킵, 이미 사용한 단어거나 단어가 이어지지 않으면
        if i != 0 and (word in visit or last_word[-1] != word[0]):
            return [i % n + 1, i // n + 1]
        else:
            visit.add(word)
            last_word = word
    
    return [0, 0]
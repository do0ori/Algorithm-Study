# 문자열로 처리
"""
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        filtered_skill_tree = ''.join(filter(lambda x: x in skill, skill_tree))
        if skill.find(filtered_skill_tree) == 0:
            answer += 1
    return answer
"""
# 순서체크
def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skill_list = list(skill)
        for s in skill_tree:
            if s in skill_list:
                if skill_list.pop(0) != s:
                    break
        else:   # break 없이 모두 순회 완료하면
            answer += 1
    
    return answer
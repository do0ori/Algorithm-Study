def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        filtered_skill_tree = ''.join(filter(lambda x: x in skill, skill_tree))
        if skill.find(filtered_skill_tree) == 0:
            answer += 1
    return answer
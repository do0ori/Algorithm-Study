"""
HEAD-NUMBER-TAIL
문자-숫자-나머지

* 대소문자 구분 X
* NUMBER까지 동일하면 기존 files에서 주어진 순서 그대로
"""
import re

def split_file_name(file_name):
    # HEAD: 숫자 전까지, NUMBER: 숫자 연속, TAIL: 나머지
    match = re.match(r'([^0-9]+)(\d+)(.*)', file_name, re.IGNORECASE)
    if match:
        head, number, tail = match.groups()
        return head, number, tail
    else:
        print("매칭 실패:", file_name)
        return None
    
def solution(files):
    splited_files = [split_file_name(file) for file in files]
    splited_files.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(file) for file in splited_files]
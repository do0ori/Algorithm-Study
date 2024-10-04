# [D3] 수열 합치기 - 5110

[문제 링크](https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ1r6qfkDFAWg) 6차시

### 성능 요약

모의 테스트에서는 제공되지 않습니다.

### 제출 일자

2024-10-04 20:42

### 문제 설명

여러 개의 수열을 정해진 규칙에 따라 합치려고 한다. 다음은 3개의 수열이 주어진 경우의 예이다.

![image](https://github.com/user-attachments/assets/1c4978d8-318c-47d3-b79f-903b6e1d6c14)

수열 2의 첫 숫자 보다 큰 숫자를 수열 1에서 찾아 그 앞에 수열 2를 끼워 넣는다.

![image](https://github.com/user-attachments/assets/c1f35a00-6521-485d-8d3b-6e5c74a6c8ba)

합쳐진 수열에 대해, 수열 3의 첫 숫자보다 큰 숫자를 찾아 그 앞에 수열 3을 끼워 넣는다. 큰 숫자가 없는 경우 맨 뒤에 붙인다.

![image](https://github.com/user-attachments/assets/1cb33910-45b8-4780-971e-bff924359d9c)

마지막 수열까지 합치고 나면, 맨 뒤의 숫자부터 역순으로 10개를 출력한다.

![image](https://github.com/user-attachments/assets/4575d035-3fc2-4978-b276-234c7150cecf)

#### [입력]

첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

다음 줄부터 테스트 케이스의 별로 첫 줄에 수열의 길이 N, 수열의 개수 M, 이후 M개의 줄에 걸쳐 1000이하의 자연수로 구성된 수열이 주어진다. 4<=N<=1000, 1<=M<=1000

#### [출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 완성된 수열의 맨 뒤부터 10개의 숫자를 역순으로 출력한다.

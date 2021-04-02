'''
리스트 뒤집기

리스트에 있는 데이터의 순서를 거꾸로 뒤집는 방법을 생각해내려고 합니다.

numbers = [2, 4, 6, 8, 10, 12, 14]

# 리스트 뒤집기
# 코드를 입력하세요.

print("뒤집어진 리스트: " + str(numbers))
위와 같이 numbers라는 리스트가 주어졌을 때, for문을 사용하여 리스트를 거꾸로 뒤집어 아래의 내용이 출력되게 하세요.

<주의> 새로운 리스트를 만들면 안 됩니다. numbers 리스트 하나만 사용하세요.
<주의> reverse 메소드, insert 메소드, append 메소드, del 함수 등을 사용하지 마세요.
<주의> 자동 채점 과제이기 때문에, 문제의 조건에 정확히 따라주시기 바랍니다. 띄어쓰기도 일치해야 합니다.
'''

numbers = [2, 4, 6, 8, 10, 12, 14]

# 리스트 뒤집기
# 코드를 입력하세요.
j = len(numbers)
for i in range(int(j / 2)):
    temp = numbers[i]
    numbers[i] = numbers[j - 1]
    numbers[j - 1] = temp
    j -= 1

print("뒤집어진 리스트: " + str(numbers))

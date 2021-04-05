'''
팔린드롬

"토마토"나 "기러기"처럼 거꾸로 읽어도 똑같은 단어를 팔린드롬(palindrome)이라고 부릅니다. 문자열 word가 팔린드롬인지 확인하는 함수 is_palindrome를 쓰세요. is_palindrome은 word가 팔린드롬이면 True를, 팔린드롬이 아니면 False를 리턴합니다.
"racecar"과 "토마토"는 거꾸로 읽어도 똑같기 때문에 True가 출력되어야 하고, "hello"는 거꾸로 읽으면 "olleh"가 되기 때문에 False가 나와야합니다.

<주의> 반드시 for문을 사용하셔야 합니다.
<주의> append, insert 메소드와 del 함수를 사용하면 안됩니다.
<주의> 자동 채점 과제이기 때문에, 문제의 조건에 정확히 따라주시기 바랍니다. 띄어쓰기도 일치해야 합니다.
'''

def is_palindrome(word):
    word_ = list(word)
    l = len(word_)
    for i in range(int(len(word_) / 2)):
        temp = word_[i]
        word_[i] = word_[l - 1]
        word_[l - 1] = temp
        l -= 1
    word_ = ''.join(word_)
    return word == word_

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))

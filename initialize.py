'''
initialize
정의되어 있지 않은 인스턴스 변수를 쓰려고 하면 오류가 나오기 때문에 꼭 모든 인스턴스 변수를 정의해야 한다고 말했었습니다.
만약 User 인스턴스를 네개 만들고 초기값들을 설정해주려면 아래처럼 쓰면 됩니다.
'''

class User:
    pass

user1 = User()
user1.name = "Young"
user1.email = "young@codeit.kr"
user1.password = "123456"

user2 = User()
user2.name = "Yoonsoo"
user2.email = "yoonsoo@codeit.kr"
user2.password = "abcdef"

user3 = User()
user3.name = "Taeho"
user3.email = "taeho@codeit.kr"
user3.password = "123abc"

user4 = User()
user4.name = "Lisa"
user4.email = "lisa@codeit.kr"
user4.password = "abc123"


'''
그런데 딱 봐도 뭔가 쓸데없이 길어보이고 반복적입니다.
이 문제를 해결하기 위해, 모든 인스턴스 변수를 초기값으로 설정해주는 initialize 메소드를 써보세요.
아래의 코드는 위의 코드와 똑같은 역할을 해야합니다.
'''

class User:
    # initialize 메소드를 여기 쓰세요
    # def initialize...

user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")

user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User()
user3.initialize("Taeho", "taeho@codeit.kr", "123abc")

user4 = User()
user4.initialize("Lisa", "lisa@codeit.kr", "abc123")

print(user1.email)
print(user2.name)

'''
young@codeit.kr
Yoonsoo
123abc
lisa@codeit.kr
'''






class User:
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")

user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User()
user3.initialize("Taeho", "taeho@codeit.kr", "123abc")

user4 = User()
user4.initialize("Lisa", "lisa@codeit.kr", "abc123")

print(user1.email)
print(user2.name)
print(user3.password)
print(user4.email)

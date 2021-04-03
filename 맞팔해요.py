'''
#맞팔해요
인스타그램이나 트위터같은 sns에서, 관심 있는 유저의 글을 자주 보고 싶으면 "팔로우"를 할 수 있습니다. 우리도 트렌드에 뒤쳐지지 않기 위해서 "팔로우" 기능을 넣으려고 합니다.

User 클래스의 인스턴스가 갖게될 모든 인스턴스 변수는 __init__에 정의되어야 하기 때문에 __init__에서 following_list와 followers_list에 일단 빈 리스트를 지정해줬습니다.

그리고 팔로우 기능을 위해서 follow 메소드를 만들어야합니다. follow 메소드는 self에 추가로 다른 User 인스턴스 another_user를 파라미터로 받습니다.
self의 following_list에 another_user를 추가하고, another_user의 followers_list에 self를 추가하면 되겠죠?

마지막으로 유저가 몇명을 팔로우하는지 리턴하는 num_following 메소드와, 유저를 팔로우하는 사람이 몇명인지 리턴하는 num_followers 메소드도 써줍시다.
'''

class User:
    # 초기값 설정
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.following_list = []    # 이 유저가 팔로우하는 유저 리스트
        self.followers_list = []    # 이 유저를 팔로우하는 유저 리스트

    # 팔로우
    def follow(self, another_user):
        # 코드를 입력하세요.

    # 몇명을 팔로우하는지 리턴
    def num_following(self):
        # 코드를 입력하세요.

    # 팔로워가 몇명인지 리턴
    def num_followers(self):
        # 코드를 입력하세요.

# 유저들 생성
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

'''아래의 테스트 코드를 추가하고 실행하면,'''

# 테스트
user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user2.follow(user4)
user4.follow(user1)

print(user1.name, user1.num_followers(), user1.num_following())
print(user2.name, user2.num_followers(), user2.num_following())
print(user3.name, user3.num_followers(), user3.num_following())
print(user4.name, user4.num_followers(), user4.num_following())

'''이런 결과가 나와야합니다'''

Young 2 2
Yoonsoo 1 3
Taeho 2 0
Lisa 1 1
------------------------------------------------------

class User:
    # 초기값 설정
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.following_list = []    # 이 유저가 팔로우하는 유저 리스트
        self.followers_list = []    # 이 유저를 팔로우하는 유저 리스트

    # 팔로우
    def follow(self, another_user):
        self.following_list.append(another_user)
        another_user.followers_list.append(self)


    # 몇명을 팔로우하는지 리턴
    def num_following(self):
        return len(self.following_list)

    # 팔로워가 몇명인지 리턴
    def num_followers(self):
        return len(self.followers_list)

# 유저들 생성
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# 테스트
user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user2.follow(user4)
user4.follow(user1)

print(user1.name, user1.num_followers(), user1.num_following())
print(user2.name, user2.num_followers(), user2.num_following())
print(user3.name, user3.num_followers(), user3.num_following())
print(user4.name, user4.num_followers(), user4.num_following())

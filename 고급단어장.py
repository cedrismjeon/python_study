'''
고급 단어장
학생들이 저번에 만든 단어장 퀴즈 프로그램은 늘 순서가 같아서 재미가 없다고 합니다. 이번에는 randint 함수와 사전(dictionary)을 이용해서 vocabulary.txt의 단어들을 랜덤한 순서로 테스트하는 프로그램을 써보세요.

같은 단어를 여러번 물어봐도 괜찮고, 프로그램은 알파벳 q를 입력할 때까지 실행됩니다.
'''
in_file = open('vocabulary.txt', 'r')
voca_dict = {}
for line in in_file:
    word = line.strip().split(": ")
    voca_dict[str(word[1])] = str(word[0])
voca_list = list(voca_dict.keys())
index_number = len(voca_list)

from random import randint

while true:
    random_index = randint(0, index_number - 1)
    guess_word = voca_list[random_index]
    guess_answer = voca_dict[guess_word]
    game = input("%s: " % guess_word)
    if game == guess_answer:
        print("맞았습니다.")
    elif game == "q":
        break
    else:
        print("틀렸습니다. 정답은 %s입니다." % guess_answer)

in_file.close()

'''
Station 클래스

init 메소드
파라미터로 받은 name을 인스턴스 변수 name에 지정해주고, neighbors는 일단 빈 리스트로 설정해줍니다.
'''

def __init__(self, name):
    self.name = name
    self.neighbors = []

#add_connection 메소드
def add_connection(self, another_station):
    self.neighbors.append(another_station)
    another_station.neighbors.append(self)

'''
파일 읽기

각 줄에 각 호선이 정리되어 있고, 각 역은 "-"으로 나누어져 있습니다. split을 이용해서 사용할 수 있는 형태로 바꿔줍니다.

또, 역들을 연결하기 위해 가장 최근 본 역을 previous_station에 보관합니다.
'''
# 파일 읽기
stations = {}
in_file = open('stations.txt')

for line in in_file:
    previous_station = None
    data = line.strip().split("-")


'''
그리고 각 역을 보고, 이미 봤던 역이면 stations 사전에서 찾아 쓰고, 새로 보는 역이면 새로운 Station 인스턴스를 만들어서 stations 사전에 추가합니다.

그리고 previous_station과 current_station을 연결해주면 되겠죠?
'''
for line in in_file:
    previous_station = None
    data = line.strip().split("-")

    for name in data:
        station_name = name.strip()
        if station_name not in stations.keys():
            current_station = Station(station_name)
            stations[station_name] = current_station
        else:
            current_station = stations[station_name]

        if previous_station != None:
            current_station.add_connection(previous_station)

        previous_station = current_station

in_file.close()

'''
BFS 알고리즘
Pseudocode를 파이썬 코드로 변형시켜보겠습니다.
'''

def bfs(start, goal):
    # 변수 정의
    previous = {}
    queue = deque()
    current = None

    # 초기 설정
    previous[start] = None
    queue.append(start)

    # 탐색
    while len(queue) > 0 and current != goal:
        current = queue.popleft()

        for neighbor in current.neighbors:
            if neighbor not in previous.keys():
                queue.append(neighbor)
                previous[neighbor] = current

    # 길이 있으면 경로를 만들어서 리턴
    if current == goal:
        path = [goal]
        x = goal

        while previous[x] != None:
            x = previous[x]
            path.append(x)

        return path

    # 길이 없으면 None 리턴
    return None


#모범 답안

from collections import deque

# 지하철역 클래스
class Station:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_connection(self, another_station):
        self.neighbors.append(another_station)
        another_station.neighbors.append(self)


# Breadth-First Search 알고리즘
def bfs(start, goal):
    # 변수 정의
    previous = {}
    queue = deque()
    current = None

    # 초기 설정
    previous[start] = None
    queue.append(start)

    # 탐색
    while len(queue) > 0 and current != goal:
        current = queue.popleft()

        for neighbor in current.neighbors:
            if neighbor not in previous.keys():
                queue.append(neighbor)
                previous[neighbor] = current

    # 길이 있으면 경로를 만들어서 리턴
    if current == goal:
        path = [goal]
        x = goal

        while previous[x] != None:
            x = previous[x]
            path.append(x)

        return path

    # 길이 없으면 None 리턴
    return None


# 파일 읽기
stations = {}
in_file = open('stations.txt')

for line in in_file:
    previous_station = None
    data = line.strip().split("-")

    for name in data:
        station_name = name.strip()
        if station_name not in stations.keys():
            current_station = Station(station_name)
            stations[station_name] = current_station
        else:
            current_station = stations[station_name]

        if previous_station != None:
            current_station.add_connection(previous_station)

        previous_station = current_station

in_file.close()


# 테스트
start_name = "이태원"
goal_name = "잠원"

start = stations[start_name]
goal = stations[goal_name]

path = bfs(start, goal)
for station in path:
    print(station.name)


잠원
신사
압구정
옥수
금호
약수
버티고개
한강진
이태원

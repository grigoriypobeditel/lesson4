# Задание 1

'''name = input('Введите имя: ')
surname = input('Введите фамилию: ')
group_number = input('Введите номер группы: ')
print(name, surname, '('+group_number+')')

# Задание 2

Year = int(input('Введите год в числовом виде: '))
if (Year % 4 == 0 or Year % 400 == 0) and Year % 100 != 0:
    print(Year,'год является високосным')
else:
    print(Year,'год не является високосным')'''

# Задание 3

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'Точки с координатами {self.x}, {self.y}'
    def get_distance(self, other_point):
        x1 = self.x
        x2 = other_point.x
        y1 = self.y
        y2 = other_point.y
        dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
        return dist

dictpoints = {}
Points = int(input('Введите количество точек: '))
for i in range(Points):
    name = input('Введите название точки: ')
    x = int(input('Введите координату х: '))
    y = int(input('Введите координату y: '))
    dictpoints[name] = Point(x,y)

distance_dict = {}
for a in (dictpoints):
    for b in (dictpoints):
        if dictpoints[a] != dictpoints[b] and int(name)>=2:
            way = dictpoints[a].get_distance(dictpoints[b])
            print('min distance between:', min(distance_dict.keys()))
            print('max distance between:', max(distance_dict.keys()))
        else:
            print('Incorrect')












songs = {
    'Bad Guy': 3,
    'Thunder': 3,
    'Sweater Weather': 4,
    'Numb': 3,
    'Karma Police': 4,
    'Enjoy the Silence': 4,
    'Obstacles': 3,
    'Crosses': 2,
    'Unnamed Feeling': 7
}
n =  int(input("Введите количество песен, которое вы желаете послушать: "))
total_time = 0
for i in range(n):
    song_name = input("Введите название песни: ")
    if song_name in songs:
        total_time += songs[song_name]
    else:
        print("Такая песня не существует")
print(f'Общее время воспроизведения песен: {total_time} минут')
from random import randint

players = open("players.txt", "r")
user_data=[]
for line in players.readlines():
    line=line.replace("\n","")
    user_data.append(line)
players.close()

login = 0
while login != 1:
    username = str(input("enter your name (case is important)"))
    password = str(input("enter your password (case is important)"))

    if username + password in user_data:
        login = 1
    else:
        print("Username or password is incorect")
        print("Try again\n")

songs = open("songs.txt", "r")
line_count = 0
songs_list = []

for line in songs.readlines():
    line_count += 1
    line = line.replace("\n", "")
    songs_list.append(line)
songs.close()

turn = 1
points = 0
trying = 0
while turn != 10:
    song_number = randint(0, line_count - turn)
    chosen = songs_list[song_number]
    chosen = chosen.split("-")
    del songs_list[song_number]
    turn += 1

    print("Artist is: ", chosen[0])
    title = chosen[1]
    print('First letter of title is ', '"', title[0], '"')
    for trying in range(1, 3):
        song_user = str(input("What is this song name? "))
        if song_user == title:
            print("you pass")
            if trying == 1:
                points += 3
            else:
                points += 1
            trying = 0
            break
        else:
            print("wrong")
    if trying == 2:
        break
print("Your points is: ", points)

scores = open("scores.txt", "a")
scores.write(username + "-" + str(points) + "\n")
scores.close()

user_scores=[]
scores = open("scores.txt")
for line in scores.readlines():
    if username in line:
        line = line.replace("\n", "")
        line = line.replace("-", "")
        line = line.replace(username, "")
        user_scores.append(int(line))
scores.close()

maxscore=max(user_scores)
maxscores=[]
for i in range(maxscore,0,-1):
    if i in user_scores:
        maxscores.append(username+"-"+str(i))
        if len(maxscores)>=5:
            break
print(maxscores)
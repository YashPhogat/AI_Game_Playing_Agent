import os
import time
fileread = open("input.txt")

game_type = fileread.readline().strip()
my_color = fileread.readline().strip()
max_time = float(fileread.readline().strip())

grid = {}
for row in range(16):
    grid[row] = list(fileread.readline().strip())

f1 = open("output.txt")

black_list_1 = []
white_list_1 = []
for i in range(16):
    for j in range(16):
        if grid[i][j] == "B" :
            black_list_1.append((j,i))
        elif grid[i][j] == "W" :
            white_list_1.append((j,i))

ans = []
while True:
    read = f1.readline()
    # ans += read
    if read =='':
        break
    else:
        ans += read.split()

# print(white_list_1, eval(ans[1]))
if my_color == "WHITE":
    white_list_1.remove(eval(ans[1]))
    white_list_1.append(eval(ans[-1]))
else:
    black_list_1.remove(eval(ans[1]))
    black_list_1.append(eval(ans[-1]))

# print(white_list)

board = ""
new_cof = str(game_type) + "\n"
if my_color == "WHITE":
    new_cof += "BLACK\n"
else:
    new_cof += "WHITE\n"
new_cof += str(max_time) + "\n"
for i in range(16):
    for j in range(16):
        if (j,i) in black_list_1:
            board += "B"
            new_cof += "B"
        elif (j,i) in white_list_1:
            board += "W"
            new_cof += "W"
        else:
            board += '.'
            new_cof += "."
    board+=","
    new_cof += "\n"

file_write = open("board.txt", 'w')
file_write.write(board)
# time.sleep(5)
inp_write = open("input.txt", 'w')
# print(new_cof)
inp_write.write(new_cof)

# os.system('python Display.py')

print("# ------------------------- TIC TAC TOE ------------------------- #")
def low_intesity(x):
    return f'\033[2m{x}\033[0m'
moves = [[f'{low_intesity(1)}',f'{low_intesity(2)}',f'{low_intesity(3)}'],[f'{low_intesity(4)}',f'{low_intesity(5)}',f'{low_intesity(6)}'],[f'{low_intesity(7)}',f'{low_intesity(8)}',f'{low_intesity(9)}']]
all_moves = []
def print_board():
    print(f'''
{moves[0][0]} ┃ {moves[0][1]} ┃ {moves[0][2]}
──┃───┃──
{moves[1][0]} ┃ {moves[1][1]} ┃ {moves[1][2]}
──┃───┃──
{moves[2][0]} ┃ {moves[2][1]} ┃ {moves[2][2]}
''')

pti = {
    1:"0,0",
    2:"0,1",
    3:"0,2",
    4:"1,0",
    5:"1,1",
    6:"1,2",
    7:"2,0",
    8:"2,1",
    9:"2,2"
}
def get_pos(p):
    i1 = int(pti[p].split(",")[0])
    i2 = int(pti[p].split(",")[1])

    return (i1,i2)



def correct_input(c):
    i = input(f"Enter Position for {c}: ")
    while not i.isnumeric() or int(i)>9 or int(i)<1 or (i in all_moves):
        i = input(f"Enter Correct Position for {c}: ")

    all_moves.append(i)
    return int(i)
    

def check_win():
    if len(set(moves[0])) == 1:
        moves[0][0] = f"\033[32m{moves[0][0]}\033[0m"
        moves[0][1] = f"\033[32m{moves[0][0]}\033[0m"
        moves[0][2] = f"\033[32m{moves[0][0]}\033[0m"
        return moves[0][0]
    if len(set(moves[1])) == 1:
        moves[1][0] = f"\033[32m{moves[1][0]}\033[0m"
        moves[1][1] = f"\033[32m{moves[1][0]}\033[0m"
        moves[1][2] = f"\033[32m{moves[1][0]}\033[0m"
        return moves[1][0]
    if len(set(moves[2])) == 1:
        moves[2][0] = f"\033[32m{moves[2][0]}\033[0m"
        moves[2][1] = f"\033[32m{moves[2][0]}\033[0m"
        moves[2][2] = f"\033[32m{moves[2][0]}\033[0m"
        return moves[2][0]
    if moves[0][0] == moves[1][0] and moves[0][0] == moves[2][0]:
        moves[0][0] = f"\033[32m{moves[0][0]}\033[0m"
        moves[1][0] = f"\033[32m{moves[0][0]}\033[0m"
        moves[2][0] = f"\033[32m{moves[0][0]}\033[0m"
        return moves[0][0]
    if moves[0][1] == moves[1][1] and moves[0][1] == moves[2][1]:
        moves[0][1] = f"\033[32m{moves[0][1]}\033[0m"
        moves[1][1] = f"\033[32m{moves[0][1]}\033[0m"
        moves[2][1] = f"\033[32m{moves[0][1]}\033[0m"
        return moves[0][1]
    if moves[0][2] == moves[1][2] and moves[0][2] == moves[2][2]:
        moves[0][2] = f"\033[32m{moves[0][2]}\033[0m"
        moves[1][2] = f"\033[32m{moves[0][2]}\033[0m"
        moves[2][2] = f"\033[32m{moves[0][2]}\033[0m"
        return moves[0][2]
    if moves[0][0] == moves[1][1] and moves[0][0] == moves[2][2]:
        moves[0][0] = f"\033[32m{moves[0][0]}\033[0m"
        moves[1][1] = f"\033[32m{moves[0][0]}\033[0m"
        moves[2][2] = f"\033[32m{moves[0][0]}\033[0m"
        return moves[0][0]
    if moves[2][0] == moves[1][1] and moves[2][0] == moves[0][2]:
        moves[2][0] = f"\033[32m{moves[2][0]}\033[0m"
        moves[1][1] = f"\033[32m{moves[2][0]}\033[0m"
        moves[0][2] = f"\033[32m{moves[2][0]}\033[0m"
        return moves[2][0]
    return None

print_board()
running = True
while running:
    xc = correct_input("X")
    i1 ,i2 = get_pos(xc)
    moves[i1][i2] = "X"
    print_board()
    if check_win() != None:
        print(f"\033[31m-------------- X Wins! --------------\033[0m")
        print_board()
        break
    if len(all_moves) == 9:
        print("Draw!")
        break

    yc = correct_input("Y")
    i1 ,i2 = get_pos(yc)
    moves[i1][i2] = "Y"
    print_board()
    if check_win() != None:
        print(f"\033[31m-------------- Y Wins! --------------\033[0m")
        print_board()
        break
    if len(all_moves) == 9:
        print("Draw!")
        break
print("# ------------------------- END ------------------------- #")
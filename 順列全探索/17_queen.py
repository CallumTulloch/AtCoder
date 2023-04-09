#import itertools
#
#def get_coords(r,c):
#    r_coords = [(i, c) for i in range(8)].remove((r,c))
#    c_coords = [(r, i) for i in range(8)].remove((r,c))
#    n_coords=[]
#    for i, j in [(1,1), (1,-1), (-1,1), (-1,-1)]:
#        dx, dy = c+i, r+i
#        while(0<=dx<8 and 0<=dy<8):
#            n_coords.append((dy, dx))
#            dx, dy = dx+i, dy+i
#    return r_coords + c_coords + n_coords
#    
#K = int(input())
#RC = [list(map(int, input())) for _ in range(K)]
#place_taken = []
#
#for rc in itertools.permutations(range(8)):
#    if 


"""
再帰
"""
# 入力
k = int(input())
queens = [list(map(int, input().split())) for _ in range(k)]

# チェス盤の初期化
board = [["."]*8 for _ in range(8)]

# 既に配置されているクイーンのマスには "Q" をセットする
for r, c in queens:
    board[r][c] = "Q"

# 残りのクイーンを配置する
def place_queens(r=0):
    if r == 8:
        # すべての行にクイーンを配置できたら、結果を出力する
        for row in board:
            print("".join(row))
        return True
    
    for c in range(8):
        # 同じ列にクイーンがある場合、その列には配置できない
        if any(board[i][c] == "Q" for i in range(8)):
            continue
        
        # 左上から右下への対角線にクイーンがある場合、そのマスには配置できない
        if any(board[i][i-(r-c)] == "Q" for i in range(8) if 0 <= i-(r-c) < 8):
            continue
        
        # 右上から左下への対角線にクイーンがある場合、そのマスには配置できない
        if any(board[i][r+c-i] == "Q" for i in range(8) if 0 <= r+c-i < 8):
            continue
        
        # クイーンを配置する
        board[r][c] = "Q"
        
        # 次の行にクイーンを配置する
        if place_queens(r+1):
            return True
        
        # クイーンを取り除く
        board[r][c] = "."
    
    # クイーンを配置できなかった場合
    return False

place_queens()



"""
順列
"""
import itertools

n = int(input())
queen = [list(map(int, input().split())) for _ in range(n)]


def find_if(iterable, predicate):
    for v in iterable:
        if predicate(v):
            return v
    return None


def is_valid(queens):
    for i in range(8):
        for j in range(i):
            if i - j == abs(queens[i] - queens[j]):
                return False
    return True


def all_of(iterable, predicate):
    for v in iterable:
        if not predicate(v):
            return False
    return True


result = find_if(list(itertools.permutations(range(8))), lambda queens: all_of(queen, lambda q: queens[q[0]] == q[1]) and is_valid(queens))

state = [['.'] * 8 for _ in range(8)]

for r, c in enumerate(result):
    state[r][c] = 'Q'

for line in state:
    print("".join(line))
    
"""
それは2つのクイーンが配置されており、最初のクイーンは2行2列に、2番目のクイーンは5行3列にあります。
このプログラムは、itertoolsモジュールを使って、8つの数字の全順列を作成します。
次に、find_if関数を使用して、lambda関数を使って、クイーンがすべての正しい位置にあるかどうかを確認します。
そして、is_valid関数を使用して、クイーンの位置が相互に襲撃しないかどうかを確認します。
最後に、解が見つかったら、state配列に解を反映し、出力します。
"""
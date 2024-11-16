import ctypes
import random
import time

def raise_if_0(result, func, arguments):
    if result == 0:
        exit()

def color_print(text, color):
    _k32 = ctypes.WinDLL('kernel32', use_last_error=True)
    _GetStdHandle = _k32.GetStdHandle
    _GetStdHandle.restype = ctypes.c_void_p
    _GetStdHandle.argtypes = [ctypes.c_void_p]
    _SetConsoleTextAttribute = _k32.SetConsoleTextAttribute
    _SetConsoleTextAttribute.restype = ctypes.c_bool
    _SetConsoleTextAttribute.argtypes = [ctypes.c_void_p, ctypes.c_uint16]
    _SetConsoleTextAttribute.errcheck = raise_if_0            
    hout = _GetStdHandle(ctypes.c_void_p(-11))
    _SetConsoleTextAttribute(hout, color)
    print(text, end='', flush=True)
    _SetConsoleTextAttribute(hout, 7)

def goto_xy(x,y):
    _k32 = ctypes.WinDLL('kernel32', use_last_error=True)
    _GetStdHandle = _k32.GetStdHandle
    _GetStdHandle.restype = ctypes.c_void_p
    _GetStdHandle.argtypes = [ctypes.c_void_p]
    _SetConsoleCursorPosition = _k32.SetConsoleCursorPosition
    _SetConsoleCursorPosition.restype = ctypes.c_bool
    _SetConsoleCursorPosition.argtypes = [ctypes.c_void_p, ctypes.c_ulong]
    _SetConsoleCursorPosition.errcheck = raise_if_0            
    hout = _GetStdHandle(ctypes.c_void_p(-11))
    _SetConsoleCursorPosition(hout, ctypes.c_ulong(x + (y << 16)))

def reset(mat):
    for i in range(len(mat)):
        mat[i] = [0]*len(mat[0])

def my_print(x, y, mat, pixx):
    pix = pixx+1
    for i in range(len(mat)*pix if pixx > 1 else 1):
        goto_xy(x, y+i)
        if pixx == 1:
            color_print(' '*len(mat[0]), 0x1f)    
        else:
            color_print(' '*len(mat[0])*pix, 0x1f)  

    for i in range(len(mat)):        
        if pixx == 1:
            line = "".join([b'\xdb'.decode('cp437') if mat[i][j] == 1 else ' ' for j in range(len(mat[0]))])
            goto_xy(x, y+i)
            color_print(line, 0x1f)    
        else:
            for j in range(len(mat[i][0])):                        
                if mat[i][j] == 1:       
                    for k in range(pixx):
                        goto_xy(x + j * pix, y + i * pix + k)
                        color_print('#'*pixx + ' ', 0x1f)    
                else:
                    for k in range(pixx):
                        goto_xy(x + j * pix, y + i * pix + k)
                        color_print(' '*(pixx+1), 0x1f)    

def first_gen(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = random.choice(range(2))

def gen_intersting(mat, id):
    r = len(mat)//2
    c = len(mat[0])//2
    if id == 0:
        mat[r][c+1] = 1
        mat[r+1][c] = 1
        mat[r+1][c+1] = 1
        mat[r+2][c+1] = 1
        mat[r+2][c+2] = 1
    elif id == 1:
        mat[r+6][c+1] = 1
        mat[r+6][c+3] = 1
        mat[r+5][c+3] = 1
        mat[r+2][c+5] = 1
        mat[r+3][c+5] = 1
        mat[r+4][c+5] = 1
        mat[r+1][c+7] = 1
        mat[r+2][c+7] = 1
        mat[r+3][c+7] = 1
        mat[r+2][c+8] = 1
    elif id == 2:
        mat[r+1][c+1] = 1
        mat[r+1][c+2] = 1
        mat[r+2][c+1] = 1
        mat[r+2][c+2] = 1

        mat[r+1][c+8] = 1
        mat[r+1][c+9] = 1
        mat[r+2][c+8] = 1
        mat[r+2][c+9] = 1

        mat[r+4][c+5] = 1
        mat[r+4][c+6] = 1
        mat[r+5][c+5] = 1
        mat[r+5][c+6] = 1

        mat[r+12][c+32] = 1
        mat[r+12][c+33] = 1
        mat[r+13][c+32] = 1
        mat[r+13][c+33] = 1

        mat[r+18][c+21] = 1
        mat[r+18][c+22] = 1
        mat[r+19][c+21] = 1
        mat[r+20][c+22] = 1
        mat[r+20][c+23] = 1
        mat[r+20][c+24] = 1
        mat[r+21][c+24] = 1

        mat[r+10][c+23] = 1
        mat[r+10][c+24] = 1
        mat[r+11][c+22] = 1
        mat[r+12][c+22] = 1
        mat[r+13][c+22] = 1
        mat[r+13][c+23] = 1
        mat[r+13][c+24] = 1        

        mat[r+18][c+26] = 1
        mat[r+18][c+27] = 1
        mat[r+19][c+28] = 1
        mat[r+20][c+29] = 1
        mat[r+21][c+28] = 1
        mat[r+22][c+27] = 1       

def count_live_neighbour(mat, r, c):
    dirs = [(-1,-1),(-1,1), (1,-1),(1,1),(-1,0),(1,0),(0,-1),(0,1)]
    cnt = sum([mat[r+dir[0]][c+dir[1]] for dir in dirs if r+dir[0] >= 0 and r+dir[0] < len(mat) and c+dir[1] >= 0 and c+dir[1]<len(mat[0])])
    return cnt

def next_gen(mat):
    next = [mat[i].copy() for i in range(len(mat))]

    for i in range(len(mat)):
        for j in range(len(mat[0])): 
            cnt = count_live_neighbour(mat, i, j)
            if mat[i][j] == 1:
                if cnt < 2 or cnt > 3:
                    next[i][j] = 0                
            else:
                if cnt == 3:
                    next[i][j] = 1
    return next

_4k = (476, 169)
_hd = (239, 80)

crt_res = _4k
mat = [[0]*crt_res[0]]*crt_res[1]
reset(mat)
first_gen(mat)
#gen_intersting(mat, 1)
mat_1 = mat
mat_2 = None
while True: 
    my_print(0, 0, mat, 1)
    print()
    mat = next_gen(mat)
    if mat == mat_1 or mat == mat_2:
        break
    if mat_2 is None:
        mat_2 = mat
    else:
        mat_1 = mat_2
        mat_2 = mat

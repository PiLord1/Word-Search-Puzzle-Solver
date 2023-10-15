def get_words(n, words):
    while n.isnumeric() == False or int(n) < 1:
        print("Input should be positive integers only")
        n = input("Get n: ")
    if int(n) != 0:
        count = 0
        while count != int(n):
            if int(n)>0 and int(n)<10:
                stop = 1
                while stop <= int(n) and stop <= 9:
                    count += 1
                    a = str(stop)
                    b = "Enter word #0"
                    final = b + a + ": "
                    def error_check(final):
                        add_word = input(final)
                        temp = []
                        temp.append(add_word)
                        for i in temp:
                            if i.isalpha() and len(i) <= 15 :
                                words.append(add_word.upper())
                            else:
                                print("Input should be alphabets only and should not exceed than 15 characters")
                                error_check(final)
                    error_check(final)
                    stop += 1
            elif int(n)>=10:
                stop = 1
                while stop <= int(n):
                    while stop <= 9:
                        count += 1
                        a = str(stop)
                        b = "Enter word #0"
                        final = b + a + ": "
                        def error_check(final):
                            add_word = input(final)
                            temp = []
                            temp.append(add_word)
                            for i in temp:
                                if i.isalpha() and len(i) <= 15 :
                                    words.append(add_word.upper())
                                else:
                                    print("Input should be alphabets only and should not exceed than 15 characters")
                                    error_check(final)
                        error_check(final)
                        stop += 1
                    while stop >= 10 and stop <= int(n):
                        count += 1
                        a = str(stop)
                        b = "Enter word #"
                        final = b + a + ": "
                        def error_check(final):
                            add_word = input(final)
                            temp = []
                            temp.append(add_word)
                            for i in temp:
                                if i.isalpha() and len(i) <= 15 :
                                    words.append(add_word.upper())
                                else:
                                    print("Input should be alphabets only and should not exceed than 15 characters")
                                    error_check(final)
                        error_check(final)      
                        stop += 1
    return n, words

def sort_words(n, words):
    words.sort()
    return n, words
    
def print_words(n, words):
    print("\nSorted words:")
    for i in words:
        print(i, end = "\n")
    return n, words

def populate_board(m, board):
    while m.isnumeric() == False or int(m) < 1:
        print("Input should be positive integers only")
        m = input("Get m: ")
    if int(m) != 0:
        count = 0
        while count != int(m):
            if int(m)>0 and int(m)<10:
                stop = 0
                while stop != int(m):
                    stop += 1
                    count += 1
                    a = str(stop)
                    b = "Enter row #0"
                    final = b + a + ": "
                    def error_check(final):
                        add_row = input(final)
                        temp = []
                        temp.append(add_row)
                        for i in temp:
                            if i.isalpha() and len(i) == int(m):
                                x = add_row.upper()
                                board.append(x)
                            else:
                                print("Input should be alphabets only and be greater than or equal to", m, "characters")
                                error_check(final)
                    error_check(final)       
            elif int(m)>=10:
                stop = 1
                while stop <= int(m):
                    while stop <= 9:
                        count += 1
                        a = str(stop)
                        b = "Enter row #0"
                        final = b + a + ": "
                        def error_check(final):
                            add_row = input(final)
                            temp = []
                            temp.append(add_row)
                            for i in temp:
                                if i.isalpha() and len(i) == int(m):
                                    x = add_row.upper()
                                    board.append(x)
                                else:
                                    print("Input should be alphabets only and be greater than or equal to", m, "characters")
                                    error_check(final)
                        error_check(final)       
                        stop += 1
                    while stop >= 10 and stop <= int(m):
                        count += 1
                        a = str(stop)
                        b = "Enter row #"
                        final = b + a + ": "
                        def error_check(final):
                            add_row = input(final)
                            temp = []
                            temp.append(add_row)
                            for i in temp:
                                if i.isalpha() and len(i) == int(m):
                                    x = add_row.upper()
                                    board.append(x)
                                else:
                                    print("Input should be alphabets only and be greater than or equal to", m, "characters")
                                    error_check(final)
                        error_check(final)              
                        stop += 1
    return m, board

def print_board(m, board):
    print("")
    for i in board:
        x = " ".join(i)
        print(x, end = "\n")

def search_words(m, board, n, words, solutions):
    combi = []
    for word in words:
        for row in board:
            if word in row:
                x_axis = str(row.index(word))
                y_axis = str(board.index(row))
                locate = "right"
                coordinates = [x_axis, y_axis]
                combi = [word, coordinates, locate]
                solutions[word] = combi
                coordinates.clear
                combi.clear
            elif word[::-1] in row:
                x_axis = str(row.index(word[::-1]) + len(word) - 1)
                y_axis = str(board.index(row))
                locate = "left"
                coordinates = [x_axis, y_axis]
                combi = [word, coordinates, locate]
                solutions[word] = combi
                coordinates.clear
                combi.clear
    board_col = []
    for i in range(len(board)):
        for a in range(len(board)):
            x = board[a][i]
            board_col.append(x)
    col = "".join(board_col)
    m = int(m)
    col_new = []
    col_1 = []
    for index in range(0, len(col), m):
        x = col[index:m+index]
        col_1.append(x)
    col_new.extend(col_1)
    for word in words:
        for col in col_new:
            if word in col:
                x_axis = str(col_new.index(col))
                y_axis = str(col.index(word))
                locate = "down"
                coordinates = [x_axis, y_axis]
                combi = [word, coordinates, locate]
                solutions[word] = combi
                coordinates.clear
                combi.clear
            elif word[::-1] in col:
                x_axis = str(col_new.index(col))
                y_axis = str(col.index(word[::-1][-1]))
                locate = "up"
                coordinates = [x_axis, y_axis]
                combi = [word, coordinates, locate]
                solutions[word] = combi
                coordinates.clear
                combi.clear
    a = 0
    b = 0
    c = 0
    d = 0
    list_count = 0
    basis = 0
    diag_upright = []
    final_upright = []
    total = (m/2)*(1+m)
    while list_count != total:
        if board[a][b] == col_new[c][d]:
            diag_upright.append(board[a][b])
            a += 1
            b += 1
            c += 1
            d += 1
            list_count += 1
            if a > (m-1) or b > (m-1) or c > (m-1) or d > (m-1):
                final = "".join(diag_upright)
                final_upright.append(final)
                diag_upright.clear()
                a = 0
                b = 0
                c = 0
                d = 0
                basis += 1
                b += basis
                c += basis
    a = m-1
    b = 0
    c = 0
    d = m-1
    basis = 0
    list_count = 0
    diag_lowright = []
    final_lowright = []
    total_1 = ((m-1)/2)*(m)
    while list_count != total_1:
        if board[a][b] == col_new[c][d]:
            diag_lowright.append(board[a][b])
            a += 1
            b += 1
            c += 1
            d += 1
            list_count += 1
            if a > (m-1) or b > (m-1) or c > (m-1) or d > (m-1):
                final = "".join(diag_lowright)
                final_lowright.append(final)
                diag_lowright.clear()
                a = m-1
                b = 0
                c = 0
                d = m-1
                basis -= 1
                a += basis
                d += basis
    final_lowright.extend(final_upright)
    a = 0
    b = 0
    c = 0
    d = 0
    y = 0
    basis = 0
    list_count = 0
    diag_upleft = []
    final_upleft = []
    total = ((m-1)/2)*(1+m)
    while list_count != total_1:
        if board[a][b] == col_new[c][d]:
            diag_upleft.append(board[a][b])
            list_count += 1
            a += 1
            b -= 1
            c -= 1
            d += 1
            if b < y or c < y:
                final = "".join(diag_upleft)
                final_upleft.append(final)
                diag_upleft.clear()
                basis += 1
                a = 0
                b = 0
                b += basis
                c = 0
                c += basis
                d = 0
    a = 0
    b = m-1
    c = m-1
    d = 0
    y = 0
    basis = 0
    list_count = 0
    diag_upleftmid = []
    final_upleftmid = []
    while list_count != total:
        if board[a][b] == col_new[c][d]:
            diag_upleftmid.append(board[a][b])
            list_count += 1
            a += 1
            b -= 1
            c -= 1
            d += 1
            if b < y or c < y:
                final = "".join(diag_upleftmid)
                final_upleftmid.append(final)
                diag_upleftmid.clear()
                break
    final_upleft.extend(final_upleftmid)
    a = 1
    b = m-1
    c = m-1
    d = 1
    y = 0
    basis = 0
    list_count = 0
    diag_lowleft = []
    final_lowleft = []
    total_1 = ((m-1)/2)*(m)
    while list_count != total_1:
        if board[a][b] == col_new[c][d]:
            diag_lowleft.append(board[a][b])
            list_count += 1
            a += 1
            b -= 1
            c -= 1
            d += 1
            if a > (m-1) or d > (m-1):
                final = "".join(diag_lowleft)
                final_lowleft.append(final)
                diag_lowleft.clear()
                basis += 1
                a = 1
                b = m-1
                c = m-1
                d = 1
                a += basis
                d += basis
    final_upleft.extend(final_lowleft)
    for word in words:
        for diag in final_upleft:
            if word in diag:
                if m%2 == 0:
                    if final_upleft.index(diag) < m//2 + m//2:
                        x_axis = str(final_upleft.index(diag) - diag.index(word))
                        y_axis = str(diag.index(word))
                        locate = "left-down"
                        coordinates = [x_axis, y_axis]
                        combi = [word, coordinates, locate]
                        solutions[word] = combi
                        coordinates.clear
                        combi.clear
                    else:
                        x_axis = str(m - 1 - diag.index(word))
                        y_axis = str(diag.index(word) + final_upleft.index(diag) - (2*(m//2) - 1))
                        locate = "left-down"
                        coordinates = [x_axis, y_axis]
                        combi = [word, coordinates, locate]
                        solutions[word] = combi
                        coordinates.clear
                        combi.clear
                else:
                    if final_upleft.index(diag) < m//2 + m//2 + 1:
                        x_axis = str(final_upleft.index(diag) - diag.index(word))
                        y_axis = str(diag.index(word))
                        locate = "left-down"
                        coordinates = [x_axis, y_axis]
                        combi = [word, coordinates, locate]
                        solutions[word] = combi
                        coordinates.clear
                        combi.clear
                    else:
                        y_axis = str(diag.index(word) + final_upleft.index(diag) - (2*(m//2)))
                        x_axis = str(m - 1 - diag.index(word))
                        locate = "left-down"
                        coordinates = [x_axis, y_axis]
                        combi = [word, coordinates, locate]
                        solutions[word] = combi
                        coordinates.clear
                        combi.clear
            elif word[::-1] in diag:
                if m%2 == 0:
                    if final_upleft.index(diag) < m//2 + m//2:
                        x_axis = str(abs(diag.index(word[::-1]) + len(word) - len(diag)))
                        y_axis = str(diag.index(word[::-1]) + len(word) - 1)
                        locate = "right-up"
                        coordinates = [x_axis, y_axis]
                        combi = [word, coordinates, locate]
                        solutions[word] = combi
                        coordinates.clear
                        combi.clear
                    else:
                        y_axis = str(m - 1 - abs(diag.index(word[::-1]) + len(word) - len(diag)))
                        x_axis = str(m - len(word) - diag.index(word[::-1]))
                        locate = "right-up"
                        coordinates = [x_axis, y_axis]
                        combi = [word, coordinates, locate]
                        solutions[word] = combi
                        coordinates.clear
                        combi.clear
                else:
                    if final_upleft.index(diag) < m//2 + m//2 + 1:
                        x_axis = str(abs(diag.index(word[::-1]) + len(word) - len(diag)))
                        y_axis = str(diag.index(word[::-1]) + len(word) - 1)
                        locate = "right-up"
                        coordinates = [x_axis, y_axis]
                        combi = [word, coordinates, locate]
                        solutions[word] = combi
                        coordinates.clear
                        combi.clear
                    else:
                        y_axis = str(m - 1 - abs(diag.index(word[::-1]) + len(word) - len(diag)))
                        x_axis = str(m - len(word) - diag.index(word[::-1]))
                        locate = "right-up"
                        coordinates = [x_axis, y_axis]
                        combi = [word, coordinates, locate]
                        solutions[word] = combi
                        coordinates.clear
                        combi.clear
    for word in words:
        for diag in final_lowright:
            if word in diag:
                if m%2 == 0:
                    if final_lowright.index(diag) > m//2 + m//2 - 2:
                        y_axis = str(diag.index(word))
                        x_axis = str(final_lowright.index(diag) - (m-1) + diag.index(word))
                        locate = "right-down"
                        coordinates = [x_axis, y_axis]
                        combi = [word, coordinates, locate]
                        solutions[word] = combi
                        coordinates.clear
                        combi.clear
                    else:
                        y_axis = str(m - 1 - final_lowright.index(diag) + diag.index(word))
                        x_axis = str(diag.index(word))
                        locate = "right-down"
                        coordinates = [x_axis, y_axis]
                        combi = [word, coordinates, locate]
                        solutions[word] = combi
                        coordinates.clear
                        combi.clear
                else:
                    if final_lowright.index(diag) > m//2 + m//2 - 1:
                        y_axis = str(diag.index(word))
                        x_axis = str(final_lowright.index(diag) - (m-1) + diag.index(word))
                        locate = "right-down"
                        coordinates = [x_axis, y_axis]
                        combi = [word, coordinates, locate]
                        solutions[word] = combi
                        coordinates.clear
                        combi.clear
                    else:
                        y_axis = str(m - 1 - final_lowright.index(diag) + diag.index(word))
                        x_axis = str(diag.index(word))
                        locate = "right-down"
                        coordinates = [x_axis, y_axis]
                        combi = [word, coordinates, locate]
                        solutions[word] = combi
                        coordinates.clear
                        combi.clear
                        
            elif word[::-1] in diag:
                if m%2 == 0:
                    if final_lowright.index(diag) > m//2 + m//2 - 2:
                        y_axis = str(diag.index(word[::-1]) + len(word) - 1)
                        x_axis = str(final_lowright.index(diag) - (m-1) + diag.index(word[::-1]) + len(word) - 1)
                        locate = "left-up"
                        coordinates = [x_axis, y_axis]
                        combi = [word, coordinates, locate]
                        solutions[word] = combi
                        coordinates.clear
                        combi.clear
                    else:
                        y_axis = str(m - 1 - final_lowright.index(diag) + diag.index(word[::-1]) + len(word) - 1)
                        x_axis = str(diag.index(word[::-1]) + len(word) - 1)
                        locate = "left-up"
                        coordinates = [x_axis, y_axis]
                        combi = [word, coordinates, locate]
                        solutions[word] = combi
                        coordinates.clear
                        combi.clear
                else:
                    if final_lowright.index(diag) > m//2 + m//2 - 1:
                        y_axis = str(diag.index(word[::-1]) + len(word) - 1)
                        x_axis = str(final_lowright.index(diag) - (m-1) + diag.index(word[::-1]) + len(word) - 1)
                        locate = "left-up"
                        coordinates = [x_axis, y_axis]
                        combi = [word, coordinates, locate]
                        solutions[word] = combi
                        coordinates.clear
                        combi.clear
                    else:
                        y_axis = str(m - 1 - final_lowright.index(diag) + diag.index(word[::-1]) + len(word) - 1)
                        x_axis = str(diag.index(word[::-1]) + len(word) - 1)
                        locate = "left-up"
                        coordinates = [x_axis, y_axis]
                        combi = [word, coordinates, locate]
                        solutions[word] = combi
                        coordinates.clear
                        combi.clear
                
def print_solutions(solutions):
    print("\nSolutions:")
    x = solutions.items()
    for word, sol in x:
        print(word + ": (" +  sol[1][0] + "," + sol[1][1] + ") - " + sol[2], end = "\n")
        
def main():
    n = input("Get n: ")
    words = []
    get_words(n, words)
    sort_words(n, words)
    print_words(n, words)
    m = input("Get m: ")
    board = []
    populate_board(m, board)
    print_board(m, board)
    solutions = {}
    search_words(m, board, n, words, solutions)
    print_solutions(solutions)
    
main()
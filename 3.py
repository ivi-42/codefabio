
#i will start by creating a function that contains board (current state) and the position
#of the gem that i want to swap. they are given as tuples
def legal_m(board, position1, position2):
    #here i will create a function that swaps the gems at position1 and position2 and reverse after seeing 
    #. its 2d grid so i need which row the number is and which column in that row the number is
    def swap(c1, c2):
        board[c1[0]][c1[1]], board[c2[0]][c2[1]] = board[c2[0]][c2[1]], board[c1[0]][c1[1]]
    #here i will create a function that checks if there is a line of 3 or more gems of the same type starting
    #at the given position (row, col). 
    def line_check(position):
        row, col = position
        gem = board[row][col]

    # check horizontally, only if they are 3 columns to the left
        horizontal_check = False
        if col <= 2:  #check 3
            horizontal_check = all(col + i < len(board[row]) for i in range(1, 3)) and gem == board[row][col+1] == board[row][col+2]
        if not horizontal_check and col <= 1:  # check 4
            horizontal_check = all(col + i < len(board[row]) for i in range(1, 4)) and gem == board[row][col+1] == board[row][col+2] == board[row][col+3]


    # check vertically only if they are 3 lines below
        vertical_check = False
        if row <= 2:  #again3
            vertical_check = all(row + i < len(board) for i in range(1, 3)) and gem == board[row+1][col] == board[row+2][col]
        if not vertical_check and row <= 1:  
            vertical_check = all(row + i < len(board) for i in range(1, 4)) and gem == board[row+1][col] == board[row+2][col] == board[row+3][col]


      l = False
      t = False

      # l check 3 of the same with one additional right or left to make l shaped combos. check current position with current limitation
        if row <= 2 and col <= 2:
          l = (gem == board[row+1][col] == board[row+2][col]) and (gem == board[row][col+1] or gem == board[row+2][col+1])

        if row <= 2 and col >= 1:
          l = l or (gem == board[row+1][col] == board[row+2][col]) and (gem == board[row][col-1] or gem == board[row+2][col-1])

        #t checks for 3 and 2 from center to down
        if row <= 1 and col >= 1 and col <= 2:
          t = (gem == board[row][col-1] == board[row][col+1]) and (gem == board[row+1][col] == board[row+2][col])


 

        return horizontal_check or vertical_check or l or t


        



    #here i will check if the move is legal by swapping the gems at position1 and position2, checking if there
    #is a line of 3 or more gems of the same type starting at either position1 or position2, and then swapping
    #the gems back.    return legal
    swap(position1, position2)
    legal = line_check(position1) or line_check(position2)
    swap(position1, position2)  # swap back
    return legal

# ex.
board = [[1, 2, 3, 5], [4, 4, 4, 6], [5, 3, 4, 5]] # 3x3 board. as i dont need to create a random one ill just use this one
move_legal = legal_m(board, (1, 0), (1, 1))  # swap (1,0) with (1,1)
print(move_legal)

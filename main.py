from sudoku_connections import SudokuConnections


class SudokuBoard : 
    def __init__(self) : 

        self.board = self.getBoard()
        
        self.sudokuGraph = SudokuConnections() #makes the graph connections
        self.mappedGrid = self.__getMappedMatrix() # Maps all the ids to the position in the matrix

    def __getMappedMatrix(self) : 
        matrix = [[0 for cols in range(16)] 
        for rows in range(16)]

        count = 1
        for rows in range(16) : 
            for cols in range(16):
                matrix[rows][cols] = count
                count+=1
        return matrix

#Give Your Input here

    def getBoard(self):

        board3 = [  
[0,2,3,4,5,0,7,8,0,10,11,12,13,14,15,16],
[0,10,11,12,1,2,3,4,13,14,15,0,5,6,7,8],
[0,6,7,8,13,14,15,16,1,2,3,4,9,10,11,0],
[13,14,15,0,9,10,11,12,5,6,7,8,1,2,3,4],
[3,1,4,2,7,5,8,6,11,9,14,10,15,12,16,13],
[11,9,0,10,3,1,4,2,15,12,16,13,7,5,8,6],
[7,0,8,6,15,12,16,13,3,1,4,0,11,9,14,10],
[15,12,16,13,11,9,0,10,7,5,8,6,3,1,4,2],
[2,4,1,3,6,8,5,7,10,15,9,11,12,16,13,14],
[10,15,9,11,2,4,1,3,12,0,13,14,6,8,5,7],
[6,8,5,7,12,16,13,14,2,4,1,3,10,15,9,0],
[0,16,13,14,0,15,9,11,6,8,5,7,2,0,1,3],
[4,3,2,1,8,7,6,0,14,11,10,9,16,13,12,15],
[14,11,10,9,4,3,2,1,16,13,12,15,8,7,0,5],
[8,7,6,5,16,13,12,15,4,0,2,1,14,11,10,9],
[0,13,12,15,14,11,10,9,8,7,6,5,4,3,2,0]]
        
        return board3
 
#function to print the board
    def printBoard(self):
        for i in range(len(self.board)):
            if i % 4 == 0:
                print("  - - - - - - - - - - - - - - - - - - - - - - ")
            for j in range(len(self.board[i])):
                if j % 4 == 0:
                    print(" | ", end="")
                if j == 15:
                    value = self.board[i][j]
                    if value == 16:
                        print("G", end="")
                  
                    else:
                        print(f"{value:X}", end="")
                    print(" | ")
                
                else:
                    value = self.board[i][j]
                    if value == 16:
                        print("G", end=" ")
                    else:
                        print(f"{self.board[i][j]:X} ", end="")
            print()
        print("  - - - - - - - - - - - - - - - - - - - - - - ")





    def is_Blank(self) : 
        
        for row in range(len(self.board)) :
            for col in range(len(self.board[row])) : 
                if self.board[row][col] == 0 : 
                    return (row, col)
        return None

    def graphColoringInitializeColor(self):
        """
        fill the already given colors
        """
        color = [0] * (self.sudokuGraph.graph.totalV+1)
        given = [] # list of all the ids whos value is already given. Thus cannot be changed
        for row in range(len(self.board)) : 
            for col in range(len(self.board[row])) : 
                if self.board[row][col] != 0 : 
                    #first get the idx of the position
                    idx = self.mappedGrid[row][col]
                    #update the color
                    color[idx] = self.board[row][col] # this is the main imp part
                    given.append(idx)
        return color, given

    def solveGraphColoring(self, m =16) : 
        
        color, given = self.graphColoringInitializeColor()
        if self.__graphColorUtility(m =m, color=color, v =1, given=given) is None :
            print(":(")
            return False
        count = 1
        for row in range(16) : 
            for col in range(16) :
                self.board[row][col] = color[count]
                count += 1
        return color
    
    def __graphColorUtility(self, m, color, v, given) :
        
        if v == self.sudokuGraph.graph.totalV+1  : 
            return True
        for c in range(1, m+1) : 
            if self.__isSafe2Color(v, color, c, given) == True :
                color[v] = c
                if self.__graphColorUtility(m, color, v+1, given) : 
                    return True
            if v not in given : 
                color[v] = 0

    def __isSafe2Color(self, v, color, c, given) : 
        
        if v in given and color[v] == c: 
            return True
        elif v in given : 
            return False

        for i in range(1, self.sudokuGraph.graph.totalV+1) :
            if color[i] == c and self.sudokuGraph.graph.isNeighbour(v, i) :
                return False
        return True
    def validate_sudoku(self):
        # Validate rows
        for row in self.board:
            if sorted(row) != list(range(1, 17)):
                return False

        # Validate columns
        for col in range(16):
            if sorted([self.board[row][col] for row in range(16)]) != list(range(1, 17)):
                return False

        # Validate sub-grids
        for row_start in range(0, 16, 4):
            for col_start in range(0, 16, 4):
                subgrid = [self.board[row][col_start:col_start+4] for row in range(row_start, row_start+4)]
                flat_subgrid = [val for row in subgrid for val in row]
                if sorted(flat_subgrid) != list(range(1, 17)):
                    return False

        return True



def main() : 
    s = SudokuBoard()
    print("\nBEFORE SOLVING ...")
    print("\n\n")
    s.printBoard()
    print("\nSolving ...")
    print("\n\n\nAFTER SOLVING ...")
    print("\n\n")
    s.solveGraphColoring(m=16)
    check=s.validate_sudoku()
    
    if check==True:
        s.printBoard()
    else:
        print(":(")

if __name__ == "__main__" : 
    main()





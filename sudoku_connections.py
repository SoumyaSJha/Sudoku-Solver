from graph import Graph

class SudokuConnections : 
    def __init__(self) :  # constructor

        self.graph = Graph() # Graph Object

        self.rows = 16
        self.cols = 16
        self.total_blocks = self.rows*self.cols #81

        self.__generateGraph() # Generates all the nodes
        self.connectEdges() # connects all the nodes acc to sudoku constraints

        self.allIds = self.graph.getAllNodesIds() # storing all the ids in a list

        

    def __generateGraph(self) : 
        """
        Generates nodes with id from 1 to 256.
        Both inclusive
        """
        for idx in range(1, self.total_blocks+1) : 
            _ = self.graph.addNode(idx)

    def connectEdges(self) : 
        """
        Connect nodes according to Sudoku Constraints : 

        # ROWS

       from start of each id number connect all the 
       successive numbers till you reach a multiple of 16


        # BLOCKS
        Connect all the elements in the block which do not 
        come in the same column or row.
       

        """
        matrix = self.__getGridMatrix()

        head_connections = dict() # head : connections

        for row in range(16) :
            for col in range(16) : 
                
                head = matrix[row][col] #id of the node
                connections = self.__whatToConnect(matrix, row, col)
                
                head_connections[head] = connections
        # connect all the edges

        self.__connectThose(head_connections=head_connections)
        
    def __connectThose(self, head_connections) : 
        for head in head_connections.keys() : #head is the start idx
            connections = head_connections[head]
            for key in connections :  #get list of all the connections
                for v in connections[key] : 
                    self.graph.addEdge(src=head, dst=v)

 
    def __whatToConnect(self, matrix, rows, cols):
        """
        matrix : stores the id of each node representing each cell
        returns dictionary
        connections - dictionary
        rows : [all the ids in the rows]
        cols : [all the ids in the cols]
        blocks : [all the ids in the block]
        ** to be connected to the head.
        """
        connections = dict()

        row = []
        col = []
        block = []

        # ROWS
        for c in range(cols+1, 16):
            row.append(matrix[rows][c])
        connections["rows"] = row

        # COLS 
        for r in range(rows+1, 16):
            col.append(matrix[r][cols])
        connections["cols"] = col

        # BLOCKS
        if rows % 4 == 0:
            # BLOCKS
            if cols % 4 == 0:
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+1][cols+2])
                block.append(matrix[rows+1][cols+3])
                block.append(matrix[rows+2][cols+1])
                block.append(matrix[rows+2][cols+2])
                block.append(matrix[rows+2][cols+3])
                block.append(matrix[rows+3][cols+1])
                block.append(matrix[rows+3][cols+2])
                block.append(matrix[rows+3][cols+3])
            elif cols % 4 == 1:
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+1][cols+2])
                block.append(matrix[rows+2][cols-1])
                block.append(matrix[rows+2][cols+1])
                block.append(matrix[rows+2][cols+2])
                block.append(matrix[rows+3][cols-1])
                block.append(matrix[rows+3][cols+1])
                block.append(matrix[rows+3][cols+2])
            elif cols % 4 == 2:
                block.append(matrix[rows+1][cols-2])
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+2][cols-2])
                block.append(matrix[rows+2][cols-1])
                block.append(matrix[rows+2][cols+1])
                block.append(matrix[rows+3][cols-2])
                block.append(matrix[rows+3][cols-1])
                block.append(matrix[rows+3][cols+1])
            elif cols % 4 == 3:
                block.append(matrix[rows+1][cols-3])
                block.append(matrix[rows+1][cols-2])
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+2][cols-3])
                block.append(matrix[rows+2][cols-2])
                block.append(matrix[rows+2][cols-1])
                block.append(matrix[rows+3][cols-3])
                block.append(matrix[rows+3][cols-2])
                block.append(matrix[rows+3][cols-1])


        elif rows % 4 == 1:

            if cols % 4 == 0:
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows-1][cols+2])
                block.append(matrix[rows-1][cols+3])
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+1][cols+2])
                block.append(matrix[rows+1][cols+3])
                block.append(matrix[rows+2][cols+1])
                block.append(matrix[rows+2][cols+2])
                block.append(matrix[rows+2][cols+3])
            elif cols % 4 == 1:
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows-1][cols+2])
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+1][cols+2])
                block.append(matrix[rows+2][cols-1])
                block.append(matrix[rows+2][cols+1])
                block.append(matrix[rows+2][cols+2])
                
            elif cols % 4 == 2:
                block.append(matrix[rows-1][cols-2])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows+1][cols-2])
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+2][cols-2])
                block.append(matrix[rows+2][cols-1])
                block.append(matrix[rows+2][cols+1])
            elif cols % 4 == 3:
                block.append(matrix[rows-1][cols-3])
                block.append(matrix[rows-1][cols-2])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows+1][cols-3])
                block.append(matrix[rows+1][cols-2])
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+2][cols-3])
                block.append(matrix[rows+2][cols-2])
                block.append(matrix[rows+2][cols-1])

        
 
        elif rows%4==2:

            if cols % 4 == 0:
                block.append(matrix[rows-2][cols+1])
                block.append(matrix[rows-2][cols+2])
                block.append(matrix[rows-2][cols+3])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows-1][cols+2])
                block.append(matrix[rows-1][cols+3])
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+1][cols+2])
                block.append(matrix[rows+1][cols+3])

            elif cols % 4 == 1:
                block.append(matrix[rows-2][cols-1])
                block.append(matrix[rows-2][cols+1])
                block.append(matrix[rows-2][cols+2])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows-1][cols+2])
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+1][cols+1])
                block.append(matrix[rows+1][cols+2])

            elif cols % 4 == 2:
                block.append(matrix[rows-2][cols-2])
                block.append(matrix[rows-2][cols-1])
                block.append(matrix[rows-2][cols+1])
                block.append(matrix[rows-1][cols-2])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows+1][cols-2])
                block.append(matrix[rows+1][cols-1])
                block.append(matrix[rows+1][cols+1])

            elif cols % 4 == 3:
                block.append(matrix[rows-2][cols-3])
                block.append(matrix[rows-2][cols-2])
                block.append(matrix[rows-2][cols-1])
                block.append(matrix[rows-1][cols-3])
                block.append(matrix[rows-1][cols-2])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows+1][cols-3])
                block.append(matrix[rows+1][cols-2])
                block.append(matrix[rows+1][cols-1])




        elif rows % 4 == 3:
 
            if cols % 4 == 0:
                block.append(matrix[rows-3][cols+1])
                block.append(matrix[rows-3][cols+2])
                block.append(matrix[rows-3][cols+3])
                block.append(matrix[rows-2][cols+1])
                block.append(matrix[rows-2][cols+2])
                block.append(matrix[rows-2][cols+3])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows-1][cols+2])
                block.append(matrix[rows-1][cols+3])


            elif cols % 4 == 1:
                block.append(matrix[rows-3][cols-1])
                block.append(matrix[rows-3][cols+1])
                block.append(matrix[rows-3][cols+2])
                block.append(matrix[rows-2][cols-1])
                block.append(matrix[rows-2][cols+1])
                block.append(matrix[rows-2][cols+2])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows-1][cols+1])
                block.append(matrix[rows-1][cols+2])


            elif cols % 4 == 2:
                block.append(matrix[rows-3][cols-2])
                block.append(matrix[rows-3][cols-1])
                block.append(matrix[rows-3][cols+1])
                block.append(matrix[rows-2][cols-2])
                block.append(matrix[rows-2][cols-1])
                block.append(matrix[rows-2][cols+1])
                block.append(matrix[rows-1][cols-2])
                block.append(matrix[rows-1][cols-1])
                block.append(matrix[rows-1][cols+1])


            elif cols % 4 == 3:
                block.append(matrix[rows-3][cols-3])
                block.append(matrix[rows-3][cols-2])
                block.append(matrix[rows-3][cols-1])
                block.append(matrix[rows-2][cols-3])
                block.append(matrix[rows-2][cols-2])
                block.append(matrix[rows-2][cols-1])
                block.append(matrix[rows-1][cols-3])
                block.append(matrix[rows-1][cols-2])
                block.append(matrix[rows-1][cols-1])

        connections["blocks"] = block
        return connections

    def __getGridMatrix(self) : 
        """
        Generates the 16x16 grid or matrix consisting of node ids.
        
        This matrix will act as amapper of each cell with each node 
        through node ids
        """
        matrix = [[0 for cols in range(self.cols)] 
        for rows in range(self.rows)]

        count = 1
        for rows in range(16) :
            for cols in range(16):
                matrix[rows][cols] = count
                count+=1
        return matrix

"""
TESTING
"""       
def test_connections() : 
    sudoku = SudokuConnections()
    sudoku.connectEdges()
    print("All node Ids : ")
    print(sudoku.graph.getAllNodesIds())
    print()
    for idx in sudoku.graph.getAllNodesIds() : 
        print(idx, "Connected to->", sudoku.graph.allNodes[idx].getConnections())

if __name__ == "__main__" : 
    test_connections()

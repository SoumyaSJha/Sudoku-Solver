from flask import Flask, render_template
from main import SudokuBoard
app = Flask(__name__)

@app.route("/")
def index():
    s = SudokuBoard()
    before = s.getBoard()
    s.solveGraphColoring(m=16)
    check = s.validate_sudoku()
    
    if check:
        after=s.board
       
    else:
        after= ":("
    
    return render_template("index.html", before=before, after=after)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
from rubik_solver import utils

app = Flask(__name__)

@app.route('/solve', methods=['POST'])      #cube state route
def solve_cube():
    data = request.get_json()  #json body with 'cube_state'
    cubestring = data['cube_state']
    
    # Use rubik_solver to solve the cube
    try:
        moves = str(utils.solve(cubestring, 'Kociemba'))
        moves = moves.strip('[]')
        solution = moves.split(", ")
        solution = [move.strip() for move in solution]      #format solution so command function can recognise it
        return jsonify({'solution': solution}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#rubik solver assigns a number to each tile on the cube:
#               ----------------
#               | 0  | 1  | 2  |
#               ----------------
#               | 3  | 4  | 5  |
#               ----------------
#               | 6  | 7  | 8  |
#               ----------------
#-------------------------------------------------------------
#| 9  | 10 | 11 | 18 | 19 | 20 | 27 | 28 | 29 | 36 | 37 | 38 |
#-------------------------------------------------------------
#| 12 | 13 | 14 | 21 | 22 | 23 | 30 | 31 | 32 | 39 | 40 | 41 |
#-------------------------------------------------------------
#| 15 | 16 | 17 | 24 | 25 | 26 | 33 | 34 | 35 | 42 | 43 | 44 |
#-------------------------------------------------------------
#               ----------------
#               | 45 | 46 | 47 |
#               ----------------
#               | 48 | 49 | 50 |
#               ----------------
#               | 51 | 52 | 53 |
#               ----------------
#yellow centre must be at pos. 4, red at pos. 22
#cube must be inserted with "yellow" on top and red facing the scanner's motor
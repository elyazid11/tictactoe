from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

board = [''] * 9
current_player = 'X'
game_over = False

def check_winner(b):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for w in wins:
        if b[w[0]] == b[w[1]] == b[w[2]] != '':
            return b[w[0]]
    if '' not in b:
        return 'Nul'
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    global board, current_player, game_over
    data = request.json
    i = data['index']

    if game_over or board[i] != '':
        return jsonify({'error': 'Coup invalide'})

    board[i] = current_player
    winner = check_winner(board)

    if winner:
        game_over = True
        return jsonify({'board': board, 'winner': winner})

    current_player = 'O' if current_player == 'X' else 'X'
    return jsonify({'board': board, 'current': current_player})

@app.route('/reset', methods=['POST'])
def reset():
    global board, current_player, game_over
    board = [''] * 9
    current_player = 'X'
    game_over = False
    return jsonify({'board': board, 'current': current_player})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def check_winner(board):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for w in wins:
        if board[w[0]] and board[w[0]] == board[w[1]] == board[w[2]]:
            return board[w[0]]
    if all(board):
        return 'nul'
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.json
    board = data['board']
    result = check_winner(board)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

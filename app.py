from flask import Flask, render_template, request, jsonify, g, session
import chess
from minmax import predict_best_move, predict_top_5_moves, print_board_position, model, predict_moves
from chessBoard import generate_html_board
from repetition import check_threefold_repetition
from chess import Board

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    user_text = request.form['user_text']
    session['user_text'] = user_text   #session data
    moves = user_text.split()

    board = chess.Board()
    illegal_moves = []
    moves_before_z = []
    moves_after_z = []
    empty_move_found = False

    for move_number, move in enumerate(moves, start=1):
        if 'z' in move.lower():
            empty_move_found = True
            break

        moves_before_z.append(move)

        try:
            board.push_san(move)
        except ValueError:
            illegal_moves.append({'move': move, 'move_number': move_number})
            break

    if empty_move_found:

        z_chess_board = chess.Board()
        print(z_chess_board)
        for move in moves_before_z:
            z_chess_board.push_san(move)


        print(z_chess_board)
        #predictions = predict_moves(fen_before_z.fen())



        # moves = ' '.join(moves_before_z)
        # move_sequence = 'After:' + moves
        message='empty move found in sequence after ' + str(moves_before_z)

        

        # fen = fen_before_z.fen()
        # board = Board(fen)
        # html_board = generate_html_board(board)
        
        # return render_template('empty.html', message = message , move_sequence = move_sequence , html_board=html_board ,top_5_moves=predictions)
        #return jsonify({'message': 'Empty move found'})
        return render_template('index.html',illegal=message)
    elif illegal_moves:
        message='Illegal move found after ' + str(illegal_moves)
        return render_template('index.html',illegal=message)
    else:
        message='Move sequence is legal'
        text = str(user_text)
        return render_template('legal.html',sequence=text)

# @app.route('/predict_move', methods=['POST'])
# def predict_move():

#     fen_before_z = chess.Board()
#     for move in moves_before_z:
#             fen_before_z.push_san(move)
#     predictions = predict_moves(fen_before_z.fen())

#     return render_template('empty.html',top_5_moves=predictions)



@app.route('/back')
def back():
    return render_template('index.html')

@app.route('/process_repetition', methods=['GET'])
def process_repetition():

    user_text = session.get('user_text', 'No text available')
    repetition_detected = check_threefold_repetition(user_text)
    if repetition_detected:
        message='repetition found'
        return render_template('repetition.html',message=message)
    else:
        message_r='repetition not found in :' + str(user_text)
        return render_template('repetition.html',message_r=message_r)

if __name__ == '__main__':
    app.run(debug=True)

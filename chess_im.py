from cairosvg import svg2png
import chess
import chess.svg
import random
from PIL import Image, ImageOps


def get_concat_h(im1, im2):
    im1 = ImageOps.expand(im1, border=20, fill=0)
    im2 = ImageOps.expand(im2, border=20, fill=0)
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0), )
    dst.paste(im2, (im1.width, 0))
    return dst


def gen_first_board(nb_pieces):
    board_ = chess.Board('8/8/8/8/8/8/8/8 w - - 0 1')
    cases_liste = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "c1",
                   "c2", "c3", "c4", "c5", "c6", "c7", "c8", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "e1", "e2",
                   "e3", "e4", "e5", "e6", "e7", "e8", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "g1", "g2", "g3",
                   "g4", "g5", "g6", "g7", "g8", "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"]
    piece_liste = ["K", "Q", "N", "P", "R", "B", "k", "q", "n", "p", "r", "b"]

    for j in range(nb_pieces):
        c = random.choice(cases_liste)
        p = random.choice(piece_liste)
        board_.set_piece_at(square=chess.SQUARE_NAMES.index(c), piece=chess.Piece.from_symbol(p))
        cases_liste.remove(c)

    board_svg = chess.svg.board(board_, coordinates=False)
    svg2png(bytestring=board_svg,
            write_to=f'positions/chessboard_{i}-0.png')

    im1 = Image.open(f'positions/chessboard_{i}-0.png')
    im1 = ImageOps.expand(im1, border=20, fill=0)
    return board_


def add_diff():
    square = random.choice(chess.SQUARE_NAMES)
    piece = random.choice(chess.PIECE_SYMBOLS[1:])
    board_bis = board_
    if board_.piece_at(square=chess.SQUARE_NAMES.index(square)) is not None:  # if there's a piece on the square
        board_bis.remove_piece_at(square=chess.SQUARE_NAMES.index(square))
    else:
        board_bis.set_piece_at(square=chess.SQUARE_NAMES.index(square),
                               piece=chess.Piece.from_symbol(piece))  # add a piece
    return board_bis


for i in range(76, 101):
    L = []
    list_diff = list(range(0, 7))
    # build and save the initial image
    nb_pieces = random.randint(15, 20)  # J est le nombre de pieces sur l'image initiale de l'échequier
    board_ = gen_first_board(nb_pieces)

    # generate two nb of differences
    L.append(random.choice(list_diff))
    list_diff.remove(L[0])
    L.append(random.choice(list_diff))

    for nb_diff in L:
        if nb_diff == 0:
            im1 = Image.open(f'positions/chessboard_{i}-0.png')
            get_concat_h(im1, im1).save(f'Chess_PNG/img_{i}_{nb_diff}.png')
        else:
            for diff in range(nb_diff):
                new_board = add_diff()
            new_board_svg = chess.svg.board(new_board, coordinates=False)
            svg2png(bytestring=new_board_svg,
                    write_to=f'positions/chessboard_{i}-{diff}.png')
            get_concat_h(new_board_svg, new_board_svg).save()


            #new_board_svg = chess_differences.svg.board(new_board, coordinates=False)
            #svg2png(bytestring=new_board_svg,
                    #write_to=f'positions/chess14avril#{i}-{nb_diff}.png')
            #im1 = Image.open(f'positions/chess14avril#{i}-0.png')
            #im2 = Image.open(f'positions/chess14avril#{i}-{nb_diff}.png')
            #get_concat_h(im1, im2).save(f'Chess_PNG/img_{i}_{nb_diff}.png')
    print(f"### Echiquier numéro {i}")

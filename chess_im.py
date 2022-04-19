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
    board = chess.Board('8/8/8/8/8/8/8/8 w - - 0 1')
    cases_liste = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "c1",
                   "c2", "c3", "c4", "c5", "c6", "c7", "c8", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "e1", "e2",
                   "e3", "e4", "e5", "e6", "e7", "e8", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "g1", "g2", "g3",
                   "g4", "g5", "g6", "g7", "g8", "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"]
    piece_liste = ["K", "Q", "N", "P", "R", "B", "k", "q", "n", "p", "r", "b"]

    for j in range(nb_pieces):
        c = random.choice(cases_liste)
        p = random.choice(piece_liste)
        board.set_piece_at(square=chess.SQUARE_NAMES.index(c), piece=chess.Piece.from_symbol(p))
        cases_liste.remove(c)

    board_svg = chess.svg.board(board, coordinates=False)
    svg2png(bytestring=board_svg,
            write_to=f'positions/chessboard_{i}_0.png')

    im1 = Image.open(f'positions/chessboard_{i}_0.png')
    im1 = ImageOps.expand(im1, border=20, fill=0)
    return board, im1


def add_differences(number_difference, board, numero_img):
    no_remove = []
    for j in range(number_difference):
        square = random.choice(chess.SQUARE_NAMES)
        piece = random.choice(chess.PIECE_SYMBOLS[1:])
        print(square, piece)
        while square in no_remove:
            square = random.choice(chess.SQUARE_NAMES)
        if board.piece_at(square=chess.SQUARE_NAMES.index(square)) is not None:
            board.remove_piece_at(square=chess.SQUARE_NAMES.index(square))
        else:
            board.set_piece_at(square=chess.SQUARE_NAMES.index(square),
                               piece=chess.Piece.from_symbol(piece))
            no_remove.append(square)
        print(no_remove)
    board_svg = chess.svg.board(board, coordinates=False)
    svg2png(bytestring=board_svg,
            write_to=f'positions/chessboard_{numero_img}_{number_difference}.png')
    im2 = Image.open(f'positions/chessboard_{numero_img}_{number_difference}.png')
    im2 = ImageOps.expand(im2, border=20, fill=0)
    get_concat_h(im_orig, im2).save(f'Chess_PNG/img_{numero_img}_{number_difference}.png')


for i in range(30, 40):
    print(f"### Echiquier numéro {i}")
    # build and save the initial image
    nb_pieces = random.randint(15, 20)
    board_1, im_orig = gen_first_board(nb_pieces)
    board_2 = board_1.copy()
    board_3 = board_1.copy()
    board_4 = board_1.copy()
    board_5 = board_1.copy()


    # generate two nb of differences
    list_diff = list(range(0, 7))
    L = random.sample(list_diff, 5)
    print("L = ", L)
    cpt = 1

    for nb_diff in L:
        if nb_diff == 0:
            get_concat_h(im_orig, im_orig).save(f'Chess_PNG/img_{i}_0.png')
        else:
            if cpt == 1:
                add_differences(nb_diff, board_1, i)
            if cpt == 2:
                add_differences(nb_diff, board_2, i)
            if cpt == 3:
                add_differences(nb_diff, board_3, i)
            if cpt == 4:
                add_differences(nb_diff, board_4, i)
            if cpt == 5:
                add_differences(nb_diff, board_5, i)

        cpt += 1


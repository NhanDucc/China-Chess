class Chess_Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def is_valid_move(self, new_position, board):
        pass

    def __str__(self):
        return f"{self.color[0]}{self.__class__.__name__[0]}"  # Ví dụ: "WK" cho Vua trắng

class Chess_Board:
    def __init__(self):
        self.board = []
        for i in range (11):
            row = [None] * 11
            self.board.append(row)
        self.initialize_board()

    def initialize_board(self):
        # Vị trí quân cờ trắng
        self.board[1][5] = King("White", (1, 5))
        self.board[1][4] = Advisor("White", (1, 4))
        self.board[1][6] = Advisor("White", (1, 6))
        self.board[1][3] = Elephant("White", (1, 3))
        self.board[1][7] = Elephant("White", (1, 7))
        self.board[1][2] = Knight("White", (1, 2))
        self.board[1][8] = Knight("White", (1, 8))
        self.board[1][1] = Rook("White", (1, 1))
        self.board[1][9] = Rook("White", (1, 9))
        self.board[3][2] = Cannon("White", (3, 2))
        self.board[3][8] = Cannon("White", (3, 8))
        self.board[4][1] = Pawn("White", (4, 1))
        self.board[4][3] = Pawn("White", (4, 3))
        self.board[4][5] = Pawn("White", (4, 5))
        self.board[4][7] = Pawn("White", (4, 7))
        self.board[4][9] = Pawn("White", (4, 9))

        # Vị trí quân cờ đen
        self.board[10][5] = King("Black", (10, 5))
        self.board[10][4] = Advisor("Black", (10, 4))
        self.board[10][6] = Advisor("Black", (10, 6))
        self.board[10][3] = Elephant("Black", (10, 3))
        self.board[10][7] = Elephant("Black", (10, 7))
        self.board[10][2] = Knight("Black", (10, 2))
        self.board[10][8] = Knight("Black", (10, 8))
        self.board[10][1] = Rook("Black", (10, 1))
        self.board[10][9] = Rook("Black", (10, 9))
        self.board[8][2] = Cannon("Black", (8, 2))
        self.board[8][8] = Cannon("Black", (8, 8))
        self.board[7][1] = Pawn("Black", (7, 1))
        self.board[7][3] = Pawn("Black", (7, 3))
        self.board[7][5] = Pawn("Black", (7, 5))
        self.board[7][7] = Pawn("Black", (7, 7))
        self.board[7][9] = Pawn("Black", (7, 9))


    def print_board(self):
        piece_map = {"White": "W", "Black": "B"}
        
        for row in range(11):
            for col in range(11):
                piece = self.board[row][col]
                if piece is None:
                    print("  .  ", end="")
                else:
                    piece_str = piece.__str__()
                    print(f"{piece_map.get(piece_str[0], piece_str[0])} {piece_str[1:]}", end="")
            print()

    def move_piece(self, piece, new_position):
        if piece.is_valid_move(new_position, self.board):
            self.board[piece.position[0]][piece.position[1]] = None
            self.board[new_position[0]][new_position[1]] = piece
            piece.position = new_position
        else:
            print()

class King(Chess_Piece):
    def is_valid_move(self, new_position, board):
        dx, dy = new_position[0] - self.position[0], new_position[1] - self.position[1]
        # Phạm vi di chuyển của Tướng
        return (abs(dx) == 1 and abs(dy) == 0) or (abs(dy) == 1 and abs(dx) == 0) and self.is_in_palace(new_position)

    def is_in_palace(self, new_position):
        # Kiểm tra xem tướng có nằm trong cung hay không
        x, y = new_position
        if 0 <= x <= 2 and 3 <= y <= 5:  # Cung trắng
            return self.color == "White"
        elif 7 <= x <= 9 and 3 <= y <= 5:  # Cung đen
            return self.color == "Black"
        return False

    def __str__(self):
        return f"{self.color[0]}K"

class Advisor(Chess_Piece):
    def is_valid_move(self, new_position, board):
        dx, dy = new_position[0] - self.position[0], new_position[1] - self.position[1]
        # Phạm vi di chuyển của Sĩ
        return abs(dx) == 1 and abs(dy) == 1 and self.is_in_palace(new_position)

    def is_in_palace(self, new_position):
        # Kiểm tra xem sĩ có nằm trong cung hay không
        x, y = new_position
        if 0 <= x <= 2 and 3 <= y <= 5:  # Cung trắng
            return self.color == "White"
        elif 7 <= x <= 9 and 3 <= y <= 5:  # Cung đen
            return self.color == "Black"
        return False

    def __str__(self):
        return f"{self.color[0]}A"

class Elephant(Chess_Piece):
    def is_valid_move(self, new_position, board):
        dx, dy = new_position[0] - self.position[0], new_position[1] - self.position[1]
        # Phạm vi di chuyển của Tượng
        if abs(dx) == 2 and abs(dy) == 2:
            middle_x, middle_y = (self.position[0] + new_position[0]) // 2, (self.position[1] + new_position[1]) // 2
            return middle_x >= 0 and middle_x <= 9 and middle_y >= 0 and middle_y <= 8 and board[middle_x][middle_y] is None
        return False

    def __str__(self):
        return f"{self.color[0]}E"

class Rook(Chess_Piece):
    def is_valid_move(self, new_position, board):
        dx, dy = new_position[0] - self.position[0], new_position[1] - self.position[1]
        # Phạm vi di chuyển của Xe
        if dx == 0:
            for i in range(1, abs(dy)):
                x, y = self.position[0], min(self.position[1], new_position[1]) + i
                if board[x][y] is not None:
                    return False
            return True
        elif dy == 0:
            for i in range(1, abs(dx)):
                x, y = min(self.position[0], new_position[0]) + i, self.position[1]
                if board[x][y] is not None:
                    return False
            return True
        return False

    def __str__(self):
        return f"{self.color[0]}R"

class Knight(Chess_Piece):
    def is_valid_move(self, new_position, board):
        dx, dy = new_position[0] - self.position[0], new_position[1] - self.position[1]
        # Phạm vi di chuyển của Mã
        if abs(dx) == 2 and abs(dy) == 1:
            middle_x, middle_y = self.position[0] + dx // 2, self.position[1] + dy // 2
            return middle_x >= 0 and middle_x <= 9 and middle_y >= 0 and middle_y <= 8 and board[middle_x][middle_y] is None
        elif abs(dx) == 1 and abs(dy) == 2:
            middle_x, middle_y = self.position[0] + dx // 2, self.position[1] + dy // 2
            return middle_x >= 0 and middle_x <= 9 and middle_y >= 0 and middle_y <= 8 and board[middle_x][middle_y] is None
        return False

    def __str__(self):
        return f"{self.color[0]}N"

class Cannon(Chess_Piece):
    def is_valid_move(self, new_position, board):
        dx, dy = new_position[0] - self.position[0], new_position[1] - self.position[1]
        # Phạm vi di chuyển của Pháo
        if board[new_position[0]][new_position[1]] is None:
            if dx == 0:
                for i in range(1, abs(dy)):
                    x, y = self.position[0], min(self.position[1], new_position[1]) + i
                    if board[x][y] is not None:
                        return False
                return True
            elif dy == 0:
                for i in range(1, abs(dx)):
                    x, y = min(self.position[0], new_position[0]) + i, self.position[1]
                    if board[x][y] is not None:
                        return False
                return True
        else:
            count = 0
            if dx == 0:
                for i in range(1, abs(dy)):
                    x, y = self.position[0], min(self.position[1], new_position[1]) + i
                    if board[x][y] is not None:
                        count += 1
                return count == 1
            elif dy == 0:
                for i in range(1, abs(dx)):
                    x, y = min(self.position[0], new_position[0]) + i, self.position[1]
                    if board[x][y] is not None:
                        count += 1
                return count == 1
        return False

    def __str__(self):
        return f"{self.color[0]}C"

class Pawn(Chess_Piece):
    def is_valid_move(self, new_position, board):
        dx, dy = new_position[0] - self.position[0], new_position[1] - self.position[1]
        # Phạm vi di chuyển của Tốt
        if self.color == "White":
            if self.position[0] >= 5:
                return (dx == -1 and dy == 0)
            else:
                return (dx == -1 and dy == 0) or (dx == 0 and abs(dy) == 1)
        else:
            if self.position[0] <= 4:
                return (dx == 1 and dy == 0)
            else:
                return (dx == 1 and dy == 0) or (dx == 0 and abs(dy) == 1)

    def __str__(self):
        return f"{self.color[0]}P"

def print_valid_moves(piece):
    print(f"The move of chess piece {piece.__class__.__name__}:")
    for row in range(10):
        for col in range(9):
            new_position = (row, col)
            if piece.is_valid_move(new_position, chess_board.board):
                print(f"{new_position} ", end="")
        print()
    

chess_board = Chess_Board()
chess_board.print_board()
while True:
        print("Choose a chess piece to see how to move (Rook, Knight, King,...) or enter 'quit' to exit: ")
        choice = input()
        
        if choice.lower() == 'quit':
            break

        piece = None
        for row in range(10):
            for col in range(9):
                if chess_board.board[row][col] is not None and choice.lower() == chess_board.board[row][col].__class__.__name__.lower():
                    piece = chess_board.board[row][col]
                    break

        if piece:
            print_valid_moves(piece)
        else:
            print("No chess piece found.")

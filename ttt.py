import random

class TicTacToe:
    # Create Board
    def __init__(self):
        self.board_size = 3
        self.board = [[0 for row in range(self.board_size)] for j in range(self.board_size)]
        self.turn = 0
        self.winner = None

    def reset(self):
        self.board = [[0 for row in range(self.board_size)] for j in range(self.board_size)]
        self.turn = 0
        self.winner = None

    # Print Board
    def printBoard(self):
        print("------------------")
        for row in range(self.board_size):
            for col in range(self.board_size):
                if (self.board[row][col] == 0):
                    print((row*3+col),"\t", end="")
                elif (self.board[row][col] == 1):
                    print("X\t", end="")
                elif (self.board[row][col] == 2):
                    print("O\t", end="")
            print()
        print("------------------")

    # Check Winner
    def checkWinner(self,marker):
        # check row
        for row in range(self.board_size):
            if (all(marker == x for x in self.board[row])):
                return True
        # check col
        for col in range(self.board_size):
            if (all(marker == x[col] for x in self.board)):
                return True

        # check diagonial
        topleft_bottomright = []
        topright_bottemleft = []
        for diag in range(self.board_size):
            topleft_bottomright.append(self.board[diag][diag])
            topright_bottemleft.append(self.board[diag][self.board_size - diag - 1])

        if (all(marker == x for x in topleft_bottomright) | all(marker == x for x in topright_bottemleft)):
            return True

        # No Win Codition is Meet
        return False

def ai_turn():
    bestScore = float('-inf')
    x, y = None, None
    depth = 9
    for i in range(game.board_size):
        for j in range(game.board_size):
            if (game.board[i][j] == 0):
                game.board[i][j] = 1
                score = minimax(depth - 1, False)
                game.board[i][j] = 0
                if (score > bestScore):
                    bestScore = score
                    x,y = i,j

    return x,y

def minimax(depth, maximizingPlayer):
    global counter
    if depth == 0:
        return 0
    elif (game.checkWinner(1) == True):
        return depth
    elif (game.checkWinner(2) == True):
        return -depth

    if (maximizingPlayer == True):
        maxScore = float('-inf')
        for i in range(game.board_size):
            for j in range(game.board_size):
                if (game.board[i][j] == 0):
                    counter += 1
                    game.board[i][j] = 1
                    score = minimax(depth - 1, False)
                    game.board[i][j] = 0
                    maxScore = max(maxScore, score)
        return maxScore
    elif (maximizingPlayer == False):
        minScore = float('inf')
        for i in range(game.board_size):
            for j in range(game.board_size):
                if (game.board[i][j] == 0):
                    counter += 1
                    game.board[i][j] = 2
                    score = minimax(depth - 1, True)
                    game.board[i][j] = 0
                    minScore = min(minScore, score)
        return minScore

def human_turn():
    user_input = int(input())
    return user_input // game.board_size, user_input % game.board_size

def random_turn():
    x,y = random.randint(0,2), random.randint(0,2)
    while (game.board[x][y] != 0):
        x,y = random.randint(0,2), random.randint(0,2)
    return x,y

# Driver Code
ai_win = 0
human_win = 0
tie = 0
doPrint = False
counter = 0
game = TicTacToe()
for i in range(1):
    print(i)
    game.reset()
    while (game.winner == None):
        if (doPrint):
            game.printBoard()
        x, y = None, None
        if (game.turn % 2 == 0):
            # ai turn
            if (doPrint):
                print("ai turn")
            x,y = ai_turn()

        elif (game.turn % 2 == 1):
            # human turn
            if (doPrint):
                print("human turn")
            x, y = random_turn()
        
        game.board[x][y] = (game.turn % 2 ) + 1
        result = game.checkWinner((game.turn % 2 ) + 1)
        if (result == True):
            game.winner = (game.turn % 2 ) + 1
            if (game.winner == 1):
                if (doPrint):
                    game.printBoard()
                    print("AI WINS")
                ai_win += 1
            elif (game.winner == 2):
                if (doPrint):
                    game.printBoard()
                    print("HUMAN WINS")
                human_win += 1
            break
        elif (game.turn == 8):
            game.winner = 3
            if (doPrint):
                game.printBoard()
                print("TIE")
            tie += 1
            break

        game.turn += 1
    
print("scores")
print(ai_win)
print(human_win)
print(tie)

print("counter", counter)
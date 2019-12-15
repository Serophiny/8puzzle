from collections import deque
import itertools
import math
import heapq
import time

# Configure
INITIAL_BOARD = [4, 8, 3, 7, 6, 2, 5, 0, 1]
WINNING_BOARD = [1, 2, 3, 4, 5, 6, 7, 8, 0]

MANHATTAN = False
MISPLACED = False
#

assert len(INITIAL_BOARD) == len(WINNING_BOARD)
assert len(INITIAL_BOARD) in (9, 16)

LEN_BOARD = len(WINNING_BOARD)
LEN_X = int(math.sqrt(len(INITIAL_BOARD)))
LEN_Y = LEN_X

LEN = LEN_X * LEN_Y


class Puzzle:
    def __init__(self, board, parent, depth):
        self.board = board
        self.parent = parent
        self.depth = depth + 1

        if MANHATTAN:
            self.value = self.manhattan() + self.depth

        elif MISPLACED:
            self.value = self.misplaced() + self.depth

    def is_win(self):
        return self.board == WINNING_BOARD

    def manhattan(self):
        counter = 0
        for i in range(LEN):
            index = WINNING_BOARD.index(self.board[i])

            counter += abs((i % LEN_X - index % LEN_X)) + abs((i / LEN_X - index / LEN_X))

        return counter

    def misplaced(self):
        counter = 0
        for i in range(LEN):
            if self.board[i] != WINNING_BOARD[i] and self.board[i] != 0:
                counter += 1

        return counter


def get_possible_moves(board):
    index = board.index(0)
    moves = []

    if index % LEN_X > 0:
        moves.append((index, index - 1))

    if index % LEN_X < LEN_X - 1:
        moves.append((index, index + 1))

    if index / LEN_X > 0:
        moves.append((index, index - LEN_X))

    if index / LEN_X < LEN_X - 1:
        moves.append((index, index + LEN_X))

    return moves


def get_board(board, move):
    new_board = board.board[:]

    new_board[move[0]] = new_board[move[1]]
    new_board[move[1]] = 0

    return Puzzle(new_board, board, board.depth)


def list_to_string(ls):
    return "".join(str(ls))


def bfs(node):
    queue = deque([node])
    heap = []
    counter = itertools.count()

    if MANHATTAN or MISPLACED:
        heapq.heappush(heap, (node.value, next(counter), node))

    visited = set()
    k = 0

    while queue:

        if MANHATTAN or MISPLACED:
            pop = heapq.heappop(heap)[2]
        else:
            pop = queue.popleft()

        if k % 10000 == 0:
            if MANHATTAN or MISPLACED:
                print(len(heap))
            else:
                print(len(queue))

        if pop.is_win():
            return pop

        for x in get_possible_moves(pop.board):
            node_ = get_board(pop, x)

            if list_to_string(node_.board) not in visited:
                visited.add(list_to_string(node_.board))
                if MANHATTAN or MISPLACED:
                    heapq.heappush(heap, [node_.value, next(counter), node_])
                else:
                    queue.append(node_)
        k += 1


def board_print(board):
    print("\n")
    for i in range(LEN_Y):
        print(board[i * LEN_X: (i + 1) * LEN_X])


start_time = time.time()

root = Puzzle(INITIAL_BOARD, None, 0)
winner = bfs(root)

a = 0
while winner is not None:
    a += 1
    board_print(winner.board)

    winner = winner.parent


print("--- %s seconds ---" % (time.time() - start_time))
print("{} Moves.".format(a - 1))
print(root.misplaced())

import argparse
import enum

class Found(enum.Enum):
    row = 0
    column = 1
    ldiag = 2
    rdiag = 3
    no = 4

def diagonals(arr):
    if len(arr) == 0:
        return []
    ret = []
    for i in range(len(arr) * 2 - 1):
        diag = []
        for j in range(len(arr)):
            if 0 <= i - j < len(arr):
                diag.append(arr[j][i - j])
        if len(diag) > 0:
            ret.append(diag)
    return ret

def word_exists(board, word):
    word = word.upper();
    for i, row in enumerate(board):
        r = "".join(row)
        if word in r or word[::-1] in r:
            return Found.row, i+1
    for i, col in enumerate(zip(*board[::-1])):
        c = "".join(col)
        if word in c or word[::-1] in c:
            return Found.column, i+1

    # shamelessly copied from some stackoverflow post
    ldiags = diagonals(board)
    ldiags = list(map(lambda x: "".join(x), ldiags))

    rdiags = diagonals([list(reversed(row)) for row in board])
    rdiags = list(map(lambda x: "".join(x), rdiags))

    for i, diag in enumerate(ldiags):
        if word in diag or word[::-1] in diag:
            return Found.ldiag, i+1

    for i, diag in enumerate(rdiags):
        if word in diag or word[::-1] in diag:
            return Found.rdiag, i+1

    return Found.no, None

def main():
    parser = argparse.ArgumentParser(description='Crossword Helper')
    parser.add_argument('filename', type=str, help='the input file for the crossword')
    parser.add_argument('--interactive', action=argparse.BooleanOptionalAction, default=False, help='interactive mode (default: False)')

    args = parser.parse_args()

    with open(args.filename, 'r') as f:
        lines = f.readlines();
        lines = map(lambda x: x.rstrip().upper(), lines)
        lines = map(list, lines)
        lines = list(lines)

    if args.interactive:
        print("Interactive mode started: ")

    while True:
        if args.interactive:
            print("> ", end='')

        try:
            word = input().upper()
        except EOFError:
            break

        found, location = word_exists(lines, word)

        if (found == Found.no and args.interactive):
            print(f"{word} not found")
        elif (found == Found.row):
            print(f"{word} found in row {location}");
        elif (found == Found.column):
            print(f"{word} found in column {location}");
        elif (found == Found.ldiag):
            print(f"{word} found in ldiag {location} from left");
        elif (found == Found.rdiag):
            print(f"{word} found in rdiag {location} from right");

if __name__ == '__main__':
    main()

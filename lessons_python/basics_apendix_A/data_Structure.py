import pprint

allCats = []
allCats.append({'name': 'Yukki', 'age': '2', 'color': 'gray'})
allCats.append({'name': 'Toby', 'age': '0.7', 'color': 'tobby-gray'})
allCats.append({'name': 'Kim', 'age': '8', 'color': 'black'})
allCats.append({'name': 'Maxic', 'age': '15', 'color': 'brown'})
print(allCats)


# Tik Tok Game

theBoard = {'top-L': '', 'top-M': '', 'top-R': '',
            'mid-L': '', 'mid-M': '', 'mid-R': '',
            'low-L': '', 'low-M': '', 'low-R': '', }

theBoard['mid-M'] = 'X'
theBoard['top-L'] = 'O'
theBoard['top-M'] = 'O'
theBoard['top-R'] = 'O'
theBoard['mid-L'] = 'X'
theBoard['low-R'] = 'X'
pprint.pprint(theBoard)

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)

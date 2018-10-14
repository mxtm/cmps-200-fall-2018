# Maxwell Richard Tamer Mahoney ID #: 201804029
# Print fun arrow designs

arrow_pieces = ['* * *', ' * * ', '  *  ']

def down():
    for i in range(0,3):
        print(arrow_pieces[i])

def up():
    for i in range(1,4):
        print(arrow_pieces[3-i])

down()
up()
down()
up()

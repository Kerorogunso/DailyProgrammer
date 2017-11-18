def print_board(moves):                                                        
                                                                               
    starting_board = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'             
                                                                               
    chess_board = starting_board.split('/')                                    
    f = lambda x: '.'*int(x) if x.isdigit() else x                             
    chess_board = [''.join([f(x) for x in row]) for row in chess_board]        
    chess_board = [list(x) for x in chess_board]                               
                                                                               
    moves = [row.split(' ') for row in moves.split('\n')]                      
                                                                               
                                                                               
    def move_piece(instruction):                                               
        # convert letters into coordinates                                     
        origin, destination  =  [ord(instruction[0].upper()) - 65, int(instruction[1])-1], [ord(instruction[-2].upper()) - 65, int(instruction[-1])-1]        
        chess_board[destination[1]][destination[0]] = str(chess_board[origin[1]][origin[0]]) # copy the piece to new square                                   
        chess_board[origin[1]][origin[0]] = '.' # change the old piece to blank
                                                                               
        print(*chess_board, sep='\n')                                          
                                                                               
    for turn in moves:                                                         
        for move in turn:                                                      
            print(move)                                                        
            move_piece(move)                                                   
                                                                               
                                                                               
moves = '''e2-e4 c7-c5                                                         
f1-c4 g8-f6                                                                    
c4xf7 e8xf7                                                                    
e4-e5 d7-d5'''                                                                 
                                                                               
print_board(moves)                                                             
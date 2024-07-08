import random


class Player_ships: 
    
    def __init__(self, ship_name, range_ship: int, letter):
        self.ship_name = ship_name
        self.range_ship = range_ship
        self.letter = letter
        self.direction = ['H', 'V']
 
    def create_player_ship(self, board, name):
        player_positions = []
        columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        rows = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        let_to_num = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7, 'I':8}
        placed_successfully = False  
        
        while not placed_successfully:  
            print(f'Admiral {name}, choose a place for your {self.ship_name} this ship takes {self.range_ship} boxes')
            
            ply_shp_dir = input(f"In which direction do you want your {self.ship_name} to be? For vertical enter 'V', for horizontal enter 'H': ").upper()
            while ply_shp_dir not in self.direction:
                ply_shp_dir = input("Please enter a valid letter. For vertical enter 'V', for horizontal enter 'H': ").upper()
                
            print('Enter the coordinates where you want your ship to start. If you choose "V" it will start from the top, and "H" will start from the right ')
            try:
                ply_shp_r = int(input('Enter the row here (1-9): ')) 
                while ply_shp_r not in rows:
                    ply_shp_r = int(input("You have to choose a number between 1-9 ")) 
            except ValueError:
                ply_shp_r = int(input("You have to choose a number between 1-9 ")) 
                
            ply_shp_c = input('Enter the column here (A-I): ').upper()
            while ply_shp_c not in columns:
                ply_shp_c = input("You have to choose a letter from A-I ").upper()
            
            ply_shp_r -= 1  
            ply_shp_c_idx = let_to_num[ply_shp_c]
            
            try:        
                if ply_shp_dir == 'V':
                    if all(board[ply_shp_r + i][ply_shp_c_idx] == '_' for i in range(self.range_ship)):
                        for i in range(self.range_ship):
                            board[ply_shp_r + i][ply_shp_c_idx] = self.letter
                            player_positions.append((ply_shp_r + i, ply_shp_c_idx))
                        placed_successfully = True  
                        
                    else:
                        print("That spot is already occupied. Try again.")
                        
                elif ply_shp_dir == 'H':
                    if all(board[ply_shp_r][ply_shp_c_idx + i] == '_' for i in range(self.range_ship)):
                        for i in range(self.range_ship):
                            board[ply_shp_r][ply_shp_c_idx + i] = self.letter
                            player_positions.append((ply_shp_r, ply_shp_c_idx + i))
                        placed_successfully = True 
                        
                    else:
                        print("That spot is already occupied. Try again.")
                        
            except IndexError:
                print('Your boat is out of the map')

        return player_positions


class Computer_ships(Player_ships):
    
    def __init__(self, ship_name, range_ship: int, letter, index):
        super().__init__(ship_name, range_ship, letter)
        self.ship_name = ship_name
        self.range_ship = range_ship
        self.letter = letter
        self.index = index
        
    def create_computer_ships(self, board):
        list_position_com = []
        ship_dir = random.choice(self.direction)
        if ship_dir == 'V':
            while True:
                ship_r, ship_cl = random.randint(0, self.index), random.randint(0, 8)
                if all(board[ship_r + i][ship_cl] == '_' for i in range(self.range_ship)):
                    for i in range(self.range_ship):
                        board[ship_r + i][ship_cl] = self.letter
                        list_position_com.append((ship_r + i, ship_cl))
                    break
            
        elif ship_dir == 'H':
            while True:
                ship_r, ship_cl = random.randint(0, 8), random.randint(0, self.index)
                if all(board[ship_r][ship_cl + i] == "_" for i in range(self.range_ship)):
                    for i in range(self.range_ship):
                        board[ship_r][ship_cl + i] = self.letter
                        list_position_com.append((ship_r, ship_cl + i))
                    break
        return list_position_com
            
    

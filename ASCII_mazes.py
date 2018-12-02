def maze_animation():
    maze1 = """
     _________________
    |                 |         
    |                 |         
    |                 |         
    |                 |         
    |                 |         
    |                 |             
    |_________________|
    """
    maze2 = """
     _________________
    |        |        |
    |        |        |
    |        |        |
    |                 |
    |        |        |
    |        |        |
    |________|________|
    """
    maze3 = """
     _________________
    |        |        |
    |_____  _|        |
    |        |        |
    |                 |
    |        |        |
    |        |____  __|
    |________|________|
    """
    maze4 = """
     _________________
    |        |  |     |
    |_____  _|  |     |
    |   |    |  |     |
    |   |       |     |
    |   |    |  |     |
    |        |____  __|
    |___|____|________|
    """

    dots = """
     
    
    
           REPEAT
            ...
    
    
    
    """

    maze5 = """
     _________________
    | |__  _ |  | | | |
    |_____| _|_ |___  |
    | | | |  |_ | __| |
    |__ | |     |__ | |
    | | |___ |_ |   | |
    | |  _   |____| __|
    |___|__|_|________|
    """

    maze_list = []
    for i in [maze1, maze2, maze3, maze4, dots, maze5]:
       maze_list.append(i)
    return maze_list
'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    from_member_follow_length = (len(social_graph[from_member]["following"]))
    to_member_follow_length = (len(social_graph[to_member]["following"]))
    is_following = False
    is_followed = False
    
    def get_follow_list(member, index):
        return str(social_graph[member]["following"][index])
    
    for x in range(from_member_follow_length):
        if (get_follow_list(from_member, x) == to_member):
            is_following = True
    for y in range(to_member_follow_length):
        if (get_follow_list(to_member, y) == from_member):
            is_followed = True
            
    status = "ERROR"
    
    if (is_following == True and is_followed == True):
        status = "friends"
    if (is_following == True and is_followed == False):
        status = "follower"
    if (is_following == False and is_followed == True):
        status = "followed by"
    if (is_following == False and is_followed == False):
        status = "no relationship"
    
    # return (len(social_graph["@joeilagan"]["following"]))
    
    return str(status)

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

# print(relationship_status("@eeebeee", "@jobenilagan", social_graph))

# relationship_status("@joeilagan", "@jobenilagan", social_graph)

def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    rows = len(board)
    cols = len(board[0])
    # return (str(len(board[0])))
    #print(board)
    
    def check_horizontal_win(board, rows, cols):
        for x in range(rows):
            consistent_X = True
            consistent_O = True
            for y in range(cols):
                if (board[x][y] == 'X'):
                    consistent_O = False
                if (board[x][y] == 'O'):
                    consistent_X = False
                if (board[x][y] == ''):
                    consistent_X = False
                    consistent_O = False
            if (consistent_X == True):
                return str("X")
            if (consistent_O == True):
                return str("O")
                
    def check_vertical_win(board, rows, cols):
        for x in range(rows):
            consistent_X = True
            consistent_O = True
            for y in range(cols):
                if (board[y][x] == 'X'):
                    consistent_O = False
                if (board[y][x] == 'O'):
                    consistent_X = False
                if (board[y][x] == ''):
                    consistent_X = False
                    consistent_O = False
            if (consistent_X == True):
                return str("X")
            if (consistent_O == True):
                return str("O")
                
    def check_diagonal_win(board, rows, cols):
        #easiest one yet, LOTS OF ASSUMPTIONS AND SHORTCUTS TAKEN but this stupid thing should work.
        consistent_X = True
        consistent_O = True
        for x in range(rows):
            if (board[x][x] == 'X'):
                consistent_O = False
            if (board[x][x] == 'O'):
                consistent_X = False
            if (board[x][x] == ''):
                consistent_X = False
                consistent_O = False
        if (consistent_X == True):
            return str("X")
        if (consistent_O == True):
            return str("O")
    
    if (check_horizontal_win(board, rows, cols) == 'X' or check_vertical_win(board, rows, cols) == 'X' or check_diagonal_win(board, rows, cols) == 'X'):
        return "X"
    if (check_horizontal_win(board, rows, cols) == 'O' or check_vertical_win(board, rows, cols) == 'O' or check_diagonal_win(board, rows, cols) == 'O'):
        return "O"
    return str("NO WINNER")
    
    #print(check_horizontal_win(board, rows, cols))
    #print(check_vertical_win(board, rows, cols))
    #print(check_diagonal_win(board, rows, cols))
'''
Sample data for Tic Tac Toe below:
'''

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
] #X

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
] #X

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
] #O

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
] #X

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
] #O

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
] #NO WINNER

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
] #NO WINNER

board8 = [
['X','X','O'],
['O','O','X'],
['X','',''],
] #NO WINNER

board9 = [
['X','X','O',''],
['O','X','O','O'],
['X','','O','O'],
['X','X','X','X']
] #X

#print(tic_tac_toe(board8))
#tic_tac_toe(board9)

#print(tic_tac_toe(board1)) #X
#print(tic_tac_toe(board2)) #X
#print(tic_tac_toe(board3)) #O
#print(tic_tac_toe(board4)) #NO WINNER
#print(tic_tac_toe(board5)) #O
#print(tic_tac_toe(board6)) #NO WINNER
#print(tic_tac_toe(board7)) #NO WINNER
#print(tic_tac_toe(board8)) #NO WINNER
#print(tic_tac_toe(board9)) #X


def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    route_map_list = list(route_map.keys())
    route_map_values = list(route_map.values())
    route_map_list_length = len(route_map_list)
    route_map_values_length = len(route_map_values)
    
    #print(first_stop)
    
    route_map_values_ordered = [0] * int(route_map_values_length + 1)
    route_map_list_ordered = ['0'] * route_map_values_length * 2
    for x in range(len(route_map_values)):
        string = str(route_map_values[x])
        string = string.split()
        string = string[1]
        string = string.split("}")
        string = string[0]
        route_map_values_ordered[x + 1] = int(string)
    #print(route_map_values_ordered)
    #print(route_map_list)
    
    for x in range(len(route_map_list)):
        string = str(route_map_list[x])
        string = string.split("', '")
        string_1 = ""
        string_2 = ""
        for y in range(len(string)):
            string_1 = str(string[0])
            string_1 = string_1.split("('")
            string_1 = string_1[1]
            string_2 = str(string[1])
            string_2 = string_2.split("')")
            string_2 = string_2[0]
        route_map_list_ordered[x * 2] = string_1
        route_map_list_ordered[(x * 2) + 1] = string_2

    #print(route_map_list_ordered)
    
    for x in range(len(route_map_values_ordered)):
        route_map_values_ordered[0] += route_map_values_ordered[x]
    
    #print(route_map_values_ordered)
    
    route_map_list_no_duplicates = ['0'] * int(len(route_map_list_ordered) / 2)
    i = 0
    j = 0
    while (i < len(route_map_list_ordered)):
        route_map_list_no_duplicates[j] = route_map_list_ordered[i]
        i += 2
        j += 1
    
    #print(route_map_list_no_duplicates)
    
    route_map_list = route_map_list_no_duplicates
    route_map_values = route_map_values_ordered
    
    route_map_list_mirrored = ['0'] * len(route_map_list)
    route_map_values_mirrored = [0] * len(route_map_values)
    
    i = len(route_map_values) - 1
    j = 0
    while (i >= 0):
        route_map_values_mirrored[i] = route_map_values[j]
        i -= 1
        j += 1
    i = len(route_map_list) - 1
    j = 0
    route_map_values_mirrored[len(route_map_values) - 1] += route_map_values_mirrored[0]
    route_map_values_mirrored[0] = route_map_values_mirrored[len(route_map_values) - 1] - route_map_values_mirrored[0]
    route_map_values_mirrored[0] = route_map_values_mirrored[len(route_map_values) - 1] - route_map_values_mirrored[0]
    route_map_values_mirrored[len(route_map_values) - 1] -= route_map_values_mirrored[0]
    while (i >= 0):
        route_map_list_mirrored[i] = route_map_list[j]
        i -= 1
        j += 1
    
    print(route_map_list)
    print(route_map_values_ordered)
    print(route_map_list_mirrored)
    print(route_map_values_mirrored)
    
    position_first_stop = route_map_list.index(first_stop)
    position_second_stop = route_map_list.index(second_stop)
    
    calculated_steps = position_second_stop - position_first_stop
    calculated_time = 0
    for x in range(calculated_steps):
        calculated_time += route_map_values[position_first_stop + x + 1]
    
    #special case for same start and destination
    if (position_second_stop - position_first_stop == 0):
        calculated_time = route_map_values_ordered[0]
    
    return int(calculated_time)

'''
Sample data for ETA below:

(from_stop, to_stop)
'''

legs = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'c1'): {
        'travel_time_mins': 1
    },
    ('c1', 'c2'): {
        'travel_time_mins': 5
    },
    ('c2', 'd1'): {
        'travel_time_mins': 15
    },
    ('d1', 'd2'): {
        'travel_time_mins': 17
    },
    ('d2', 'e1'): {
        'travel_time_mins': 20
    },
    ('e1', 'e2'): {
        'travel_time_mins': 25
    },
    ('e2', 'a1'): {
        'travel_time_mins': 30
    }
}

legs_2 = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

print(eta('c2', 'a2', legs))
#eta('a1', 'e2', legs)
#print(eta("admu", "admu", legs_2))

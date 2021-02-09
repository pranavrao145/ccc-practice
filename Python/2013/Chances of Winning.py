favourite_team = int(input())
num_games_played = int(input())
scores = [0, 0, 0, 0]
matches_done = list()
matches_to_be_played = [(1, 2, "T"), (1, 3, "T"), (1, 4, "T"), (2, 3, "T"), (2, 4, "T"), (3, 4, "T")]
counter = 0

def fast_play(data):
    global scores, matches_done, matches_to_be_played
    
    for game in data:
        team_1 = game[0]
        team_2 = game[1]
        
        if game[2] > game[3]:
            scores[team_1 - 1] += 3
        elif game[2] < game[3]:
            scores[team_2 - 1] += 3
        else:
            scores[team_1 - 1] += 1
            scores[team_2 - 1] += 1
            
        index_of_tuple = matches_to_be_played.index((team_1, team_2, "T"))
        matches_done.append(matches_to_be_played.pop(index_of_tuple))


def simulate(team_1, team_2, state, index, current_scores):
    global counter
    
    current_scores_temp = current_scores.copy()
    # update the scores
    if state == "T":
        current_scores_temp[team_1 - 1] += 1
        current_scores_temp[team_2 - 1] += 1
    else:
        current_scores_temp[state - 1] += 3
    
    if index == len(matches_to_be_played) - 1:
        if current_scores_temp.index(max(current_scores_temp)) == favourite_team - 1 and current_scores_temp.count(max(current_scores_temp)) == 1:
            counter += 1
        return
    
    next_element = matches_to_be_played[index + 1] # (2, 3, "T")
    
    for item in next_element:
        simulate(next_element[0], next_element[1], item, index + 1, current_scores_temp)
    
    
if __name__ == "__main__":
    data = list()
    
    for i in range(num_games_played):
        data.append(list(map(int, input().strip().split())))
    
    fast_play(data)
    
    first_match = matches_to_be_played[0]
    
    for item in first_match:
        simulate(first_match[0], first_match[1], item, 0, scores.copy())

    print(counter)
# [(1, 4, "T"), (2, 3, "T")]

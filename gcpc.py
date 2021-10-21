num_teams, num_events = [int(x) for x in input().split()]
teams_by_index = [(0,0) for i in range(num_teams)]
better_teams = []
team_1_solved = 0
team_1_penalty = 0

def better(solved_1, penalty_1, solved_2, penalty_2):
    if solved_1 > solved_2:
        return True
    elif solved_1 == solved_2 and penalty_1 < penalty_2:
        return True
    return False

for i in range(num_events):
    team, penalty = [int(x) for x in input().split()]
    team -= 1
    team_points, team_penalty = teams_by_index[team]
    team_points += 1
    team_penalty += penalty

    teams_by_index[team] = (team_points, team_penalty)

    if team != 0:
        if not better(team_points - 1, team_penalty - penalty, team_1_solved, team_1_penalty) and better(team_points, team_penalty, team_1_solved, team_1_penalty):
            better_teams.append(team)
        teams_by_index[team] = (team_points, team_penalty)
    
    else:
        team_1_solved += 1
        team_1_penalty += penalty
        new_better_teams = []
        for i in range(len(better_teams)):
            team = better_teams[i]
            team_points, team_penalty = teams_by_index[team]
            if better(team_points, team_penalty, team_1_solved, team_1_penalty):
                new_better_teams.append(team)
        better_teams = list(new_better_teams)
    print(len(better_teams) + 1)



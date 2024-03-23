import random
import time
pos = [0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4,
       6, 6, "wide", "wide", "No BALL", "OUT", "OUT", "OUT"]
toss_pos = ["HEAD", "TAIL"]
how_out = ["BOLD", "STUMPOUT", "CATCHOUT", "RUNOUT", "LBW"]
toss_decision = ["Bat", "Bowl"]
team1 = ["Omkar(c)", "Virat", "Abhi", "Rohit", "Rohan"]
team2 = ["Saurav(c)", "Rahul", "Shubham", "Avesh", "Pratik"]
team1_score = 0
team2_score = 0
team1_extras = 0
team2_extras = 0
value = 1
print("----------------TEAM 1----------------------------- ")
for value in team1:
    print(value)
print("---------------------------------------------------------------------------------------------------------------------------")
print("---------------TEAM 2------------------------------")
for value in team2:
    print(value)
print("-------------------------------------------------------------------------------------------------------------------------------")


print("WELCOME TO THE GAME")
print("*****************************************************************************************************************")
print("Its Inning Toss Time")
print("Press Enter For Toss")
input()
time.sleep(3)
print("Team1 Choice", random.choice(toss_pos),
      "and the Captain Decided to ", random.choice(toss_decision))
over = 1
ball = 1
wicket = 0
i = 0
j = 0
current_player = team1[i]
print(current_player, ":0")
while over < 6:

    print("Press Enter when Batsman is Ready")
    input()
    a = random.choice(pos)
    if (ball-1)/6 == 1:
        print("The Over is", over, "is Ended")
        print("TEAM 1 SCORE IS", team1_score, "IN LOSS OF ", wicket, "WICKETS")
        print(team1[i], ":", j)
        print("---------------------------------------------------------------------------------------------------------")
        over = over+1
        ball = 1
    if over == 6:
        break
    else:
        print("Over:", over, "Ball no:", ball)
        if a == "OUT":
            print("Its a WICKET................................................")
            print(team1[i], "Score:", j)
            print(team1[i], "is", random.choice(
                how_out), "BY", random.choice(team2))
            ball = ball + 1
            i = i + 1
            j = 0
            wicket = wicket + 1
            if wicket == 6:
                print("TEAM1 IS ALL OUT")
                break
            print("Team1 Score is:", team1_score,
                  "in Loss of", wicket, "Wicket")
            print("THE NEXT BATSMAN IS", team1[i])

        elif a == "wide" or a == "No BALL":
            print("It's a:", a)
            print("Ball Again")
            team1_extras = team1_extras+1
            team1_score = team1_score+1
            continue
        else:
            if a == 4:
                print("Yeahh It's a FOUR...........................")
                team1_score = team1_score + 4
                ball = ball+1
                j = j + a
            if a == 6:
                print(
                    "Yeahh It's So Long SIXER.............................................")
                team1_score = team1_score + 6
                ball = ball+1
                j = j + a

            if a == 1 or a == 2 or a == 3 or a == 0:
                print("Its a", a)
                team1_score = team1_score + a
                j = j + a
                ball = ball + 1
print("TEAM1 SCORE:", team1_score)
print("Team1 Innings is Finished........................................ ")
print("For Winning this match Team2 have to score ", team1_score+1)
print("It's time for Inning Break")
print("****************************************************************************************************************")
time.sleep(5)
print("*********************************WELCOME TO SECOND INNING******************************************************")
print("Team 2 needs", team1_score+1, "Runs in 30 Balls")
over = 1
ball = 1
wicket = 0
i = 0
j = 0
current_player2 = team2[i]
print(current_player2, ":0")
print("enter to start second Inning")
input()
while over < 6:
    if wicket == 6:
        break
    print("Press Enter when Batsman is Ready")
    input()
    a = random.choice(pos)
    if team2_score >= team1_score+1:
        print("******************TEAM 2 HAVE SUCCESSFULLY CHASED THE TARGET **************************************** ")
        break
    if (ball-1)/6 == 1:
        print("The Over is", over, "is Ended")
        print("TEAM 2 SCORE IS", team2_score, "IN LOSS OF ", wicket, "WICKETS")
        print(team2[i], ":", j)
        print("--------------------------------------------------------------------------------------------------------")
        over = over + 1
        ball = 1
    if over == 6:
        break
    else:
        print("Over:", over, "Ball no:", ball)
        if a == "OUT":
            print(team2[i], "Score:", j)
            print(team2[i], "is", random.choice(
                how_out), "BY", random.choice(team1))
            ball = ball + 1
            i = i + 1
            j = 0
            wicket = wicket + 1
            print("Team2 Score is:", team2_score,
                  "in Loss of", wicket, "Wicket")
            print("THE NEXT BATSMAN IS", team2[i])

        elif a == "wide" or a == "No BALL":
            print("It's a:", a)
            print("Ball Again")
            team2_extras = team2_extras+1
            team2_score = team2_score+1
            continue

        else:
            if a == 4:
                print("Yeahh It's a FOUR...........................")
                team2_score = team2_score + 4
                ball = ball+1
                j = j + 4

            if a == 6:
                print(
                    "Yeahh It's So Long SIXER.............................................")
                team2_score = team2_score + 6
                ball = ball+1
                j = j+a
            if a == 1 or a == 2 or a == 3 or a == 0:
                print("Its a", a)
                team2_score = team2_score + a
                ball = ball + 1
                j = j+a

print("TEAM2 SCORE:", team2_score)
if team2_score <= team1_score:
    print("TEAM 2 LOSS BY ", team1_score+1-team2_score, "RUNS")
    print("********************TEAM 1 HAVE SUCCESSFULLY DEFNDED THEIR TARGET********************************************* ")

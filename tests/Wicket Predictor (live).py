import pickle
import requests
import json

filename = 'model.sav'
model = pickle.load(open(filename,'rb'))
print("Please enter the Cricinfo match ID.")
matchID = int(input())
balls = []
rollingSumRuns = 0
test_x = []
length = 0
counter = 0
while True:
    length = 0
    page = requests.get("https://www.espncricinfo.com/matches/engine/match/{}.json".format(matchID))
    page = page.json()
    for i in range(len(page["live"]["recent_overs"])):
        for j in range(len(page["live"]["recent_overs"][i])):
            length += 1
            overNumber = int(page["live"]["recent_overs"][i][j]['over_number'])
            ballNumber = int(page["live"]["recent_overs"][i][j]['ball_number'])
            if page["live"]["recent_overs"][i][j]['ball'] == '&bull;':
                balls.append(0)
                position = len(balls)
            elif page["live"]["recent_overs"][i][j]['ball'] == 'W':
                balls.append(0)
                position = len(balls)
            else:
                balls.append(int(page["live"]["recent_overs"][i][j]['ball']))
                position = len(balls)
            rollingSumRuns = 0
            try:
                if length >= 10:
                    for k in range(position-10,position):
                        rollingSumRuns += balls[k]
            except IndexError:
                pass
            if length >= 10:
                if counter == 1:
                    test_x.append([rollingSumRuns])
                if counter > 1:
                    if overNumber == lastOverNumber and ballNumber > lastBallNumber:
                        test_x.append([rollingSumRuns])
                        add = True
                        predictX = test_x.copy()
                        predictRolling = predictX[len(predictX)-1][0]
                        predictRolling += 0
                        try:
                            predictRolling -= balls[position-10]
                        except IndexError:
                            pass
                        predictX.append([predictRolling])
                    if overNumber > lastOverNumber:
                        test_x.append([rollingSumRuns])
                        add = True
                        predictX = test_x.copy()
                        predictRolling = predictX[len(predictX)-1][0]
                        predictRolling += 0
                        try:
                            predictRolling -= balls[position-10]
                        except IndexError:
                            pass
                        predictX.append([predictRolling])
    lastOverNumber = overNumber
    lastBallNumber = ballNumber
    if len(test_x) > 10:
        try:
            probability = model.predict_proba(predictX)
            if add == True:
                print(probability[len(probability)-1][1])
                add = False
        except NameError:
            pass
    counter += 1


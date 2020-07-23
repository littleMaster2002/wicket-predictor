import yaml
import glob
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from imblearn.over_sampling import RandomOverSampler
import pickle
import numpy as np

data = []

runs = []
wickets = []

runs10balls = []

wicketCounter = 0

for filename in glob.glob('*.yaml'):
    wicketCounter = 0
    with open(filename, 'r') as stream:
        try:
            dictionary = yaml.safe_load(stream)
            dictionary = dictionary["innings"]
            for i in range(len(dictionary[0]["1st innings"]["deliveries"])):
                rollingSumRuns = 0
                key = list(dictionary[0]["1st innings"]["deliveries"][i].keys())[0]
                if "wicket" in dictionary[0]["1st innings"]["deliveries"][i][key]:
                    wicketExists = True
                else:
                    wicketExists = False
                if wicketExists == True:
                    wicketCounter += 1
                runs.append(dictionary[0]["1st innings"]["deliveries"][i][key]["runs"]["total"])
                if len(runs) - 10 >= 0:
                    for k in range(len(runs)-10,len(runs)):
                        rollingSumRuns += runs[k]
                else:
                    for k in range(0,len(runs)):
                        rollingSumRuns += runs[k]
                runs10balls.append(rollingSumRuns)
                if wicketExists == True:
                    wickets.append(1)
                else:
                    wickets.append(0)
            if [1] in dictionary:
                for j in range(len(dictionary[1]["2nd innings"]["deliveries"])):
                    rollingSumRuns = 0
                    key = list(dictionary[1]["2nd innings"]["deliveries"][j].keys())[0]
                    if "wicket" in dictionary[1]["2nd innings"]["deliveries"][j][key]:
                        wicketExists = True
                    else:
                        wicketExists = False
                    if wicketExists == True:
                        wicketCounter += 1
                    runs.append(dictionary[1]["2nd innings"]["deliveries"][j][key]["runs"]["total"])
                    if len(runs) - 10 >= 0:
                        for k in range(len(runs)-10,len(runs)):
                            rollingSumRuns += runs[k]
                    else:
                        for k in range(0,len(runs)):
                            rollingSumRuns += runs[k]
                    runs10balls.append(rollingSumRuns)
                    if wicketExists == True:
                        wickets.append(1)
                    else:
                        wickets.append(0)
            if [2] in dictionary:
                for j in range(len(dictionary[1]["3rd innings"]["deliveries"])):
                    rollingSumRuns = 0
                    key = list(dictionary[1]["3rd innings"]["deliveries"][j].keys())[0]
                    if "wicket" in dictionary[1]["3rd innings"]["deliveries"][j][key]:
                        wicketExists = True
                    else:
                        wicketExists = False
                    if wicketExists == True:
                        wicketCounter += 1
                    runs.append(dictionary[1]["3rd innings"]["deliveries"][j][key]["runs"]["total"])
                    if len(runs) - 10 >= 0:
                        for k in range(len(runs)-10,len(runs)):
                            rollingSumRuns += runs[k]
                    else:
                        for k in range(0,len(runs)):
                            rollingSumRuns += runs[k]
                    runs10balls.append(rollingSumRuns)
                    if wicketExists == True:
                        wickets.append(1)
                    else:
                        wickets.append(0)
            if [3] in dictionary:
                for j in range(len(dictionary[1]["4th innings"]["deliveries"])):
                    rollingSumRuns = 0
                    key = list(dictionary[1]["4th innings"]["deliveries"][j].keys())[0]
                    if "wicket" in dictionary[1]["4th innings"]["deliveries"][j][key]:
                        wicketExists = True
                    else:
                        wicketExists = False
                    if wicketExists == True:
                        wicketCounter += 1
                    runs.append(dictionary[1]["4th innings"]["deliveries"][j][key]["runs"]["total"])
                    if len(runs) - 10 >= 0:
                        for k in range(len(runs)-10,len(runs)):
                            rollingSumRuns += runs[k]
                    else:
                        for k in range(0,len(runs)):
                            rollingSumRuns += runs[k]
                    runs10balls.append(rollingSumRuns)
                    if wicketExists == True:
                        wickets.append(1)
                    else:
                        wickets.append(0)
        except yaml.YAMLError as exc:
            print(exc)


RUNS10BALLS = []
WICKETS = []

for i in range(len(runs10balls)):
    RUNS10BALLS.append([runs10balls[i]])
for i in range(len(wickets)):
    WICKETS.append([wickets[i]]) 

train_x,test_x,train_y,test_y = train_test_split(RUNS10BALLS, WICKETS, random_state = 10)


ros = RandomOverSampler(sampling_strategy=0.8,random_state=0)
xR,yR = ros.fit_resample(train_x,np.ravel(train_y))

dtree_model = DecisionTreeClassifier(max_depth=10).fit(xR,yR)
dtree_predictions = dtree_model.predict(test_x)

accuracyDT = dtree_model.score(test_x,test_y)
print(accuracyDT)

cmDT = confusion_matrix(test_y,dtree_predictions)
print(cmDT)

filename = 'model.sav'
pickle.dump(dtree_model,open(filename,'wb'))


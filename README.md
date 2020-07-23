# wicket-predictor

A machine learning project written in Python which attempts to predict when a wicket might fall during a cricket match.

A model is created (for each format) by using a dataset of hundreds of previous cricket matches and a Decision Tree Classifier.

The dataset was downloaded from https://cricsheet.org.

This model can then be downloaded, and then imported and run on live cricket match data provided by ESPNCricinfo.

To run the program, you just need to run the relevant "Wicket Predictor (live).py" file and enter the ESPNCricinfo match ID (this can be found from the URL of a live match: https://www.espncricinfo.com/series/12345/game/XXXXXXX/...)

If you want to re-train the model on new data, download new data from CRICSHEET, add all the YAML files to the directory where the Python files are stored and re-run the file "Wicket Predictor (new).py".

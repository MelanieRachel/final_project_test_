
_______

Final Bootcamp Project
_______


Project Name:

Music & Mental Health | Trying to predict music effects


Project Description:

* In this project I am trying to discover significant trends in order to predict music effects.

Research question:

* Is there a connection between music and mental health?

Sub-questions:

1) What is the connection between mental health and music use?
2) What is the connection between mental health and music preference?
3) What is the connection between mental health and music genres?
4) What is the connection between mental health and music effects?
5) What is the connection between mental health and age?
6) Can I make helpful recommendations based on these findings?

Prerequisites:

* requirements.txt


Data Sources: 

* mxmh_survey_results.csv

Music & Mental Health Survey Results
Survey results on music taste and self-reported mental health
CATHERINE RASGAITIS
CC0: Public Domain
https://www.kaggle.com/datasets/catherinerasgaitis/mxmh-survey-results/data


Data Cleaning and Preprocessing:

* Data Inspection
* Renamed Column
* Handling Missing Values
* Handling Duplicates
* Outlier Detection and Treatment
* Added categories in new column: 'Age group'
* Aggregate with categorical and numerical columns in order to answer research questions
* Linear Regression
* ANOVA
* Chi2 


Data Analysis:

* Data Visualization
* Histogram
* Heatmap
* Countplot
* Boxplot
* Feature Engineering
* Dealing with Skewed Data
* Applied transformer and scaler
* Data Splitting
* Documentation
* Models: Logistic Regression, Decision Trees, Random Forest, Neural Networks


Results:

There is a connection between music and mental health. After conducting the necessary tests, the following columns appear to be related to each other. 
- 'Music effects' and 'While working'
- 'Music effects' and 'Exploratory'
- 'Music effects’  and ‘Depression’
- 'Music effects and 'Age' 

The trends I have dicovered:

The use of music has an effect on mental health. In this case, listening to music while at work and actively searching for new artists and genres. Those whose mental health deteriorates from listening to music experience high levels of depression. The age category 10's - 30's experiences the most improvement in music health through music.

1) What is the connection between mental health and music use?
	* 'Music effects' and 'While working':
	- A large number of people experience improved mental health by listening to music while working
	* 'Music effects' and 'Exploratory':
	- A large number of people experience improved mental health by actively seeking out new artists and genres
2) What is the connection between mental health and music preference? 
	- No connection based on test
3) What is the connection between mental health and music genres? 
	- No connection based on test
4) What is the connection between mental health and music effects?
	* ‘Music effects’  and ‘Depression’
	- Those whose mental health deteriorates from listening to music experience high levels of depression.
5) What is the connection between mental health and age?
	* ‘Age group’  and ‘Music effects’
	- The age category 10 - 30 experiences the most improvement in music health through music.

I now wonder which specific elements in music can ensure improved mental health. This cannot be determined with the current dataset.

_____

There is a connection between music and mental health. We know from this data that listening to music while working and actively searching for new genres and artists has an effect on mental health especially for young people.

______


Discussion:

6) Can I make helpful recommendations based on these findings?

* When I learn to make a succesful model
* When I add to this research by doing a new survey and explore elements in music, I will gain more information to train the model in order to make better and more helpful recommendations


License:
-

Author:

Melanie Nieuwendam



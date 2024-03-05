Final Capstone project:
Project name: Sentiment_Analysis
 
Dataset Description:
The dataset contains product reviews from Amazon.

Preprocessing Steps:
Text data was preprocessed by removing stopwords and basic cleaning using spaCy

Evaluation of Results:
- Tested the sentiment analysis model on sample product reviews.
- Predicted sentiment (Positive/Negative/Neutral) and calculated polarity score.

Insights into Model's Strengths and Limitations:
- Strengths: The model accurately predicts sentiment based on polarity scores.
- Limitations: Limited by the accuracy of spaCy's sentiment analysis.
## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Credits](#credits)
## Installation
To install and run this project locally, follow these steps:
1. Clone the repository to your local machine:
   git clone https://github.com/Lubna-Intezar/sentiment-analysis.git
2. Navigate to the project directory:
   cd sentiment-analysis
3.Install the required dependencies using pip (macos):
pip3 install spacy
pip3 install Textblob
pip3 install pandas
## Usage
After installing the project, you can follow these steps to use it:
1. Run the main script to perform sentiment analysis on your text data:
   python sentiment_analysis.py --input <input_file.txt>
2.Replace `<input_file.txt>` with the path to your input text file.
2. The sentiment analysis results will be displayed, indicating the sentiment (positive, negative, or neutral) of each text sample.  
## Screenshots
*Screenshot of the sentiment analysis results* 
![Screenshot](https://github.com/Lubna-Intezar/finalCapstone/blob/main/sentiment_analysis.png)
## Credits
- This project was created by [Lubna Intezar](https://github.com/Lubna_Intezar).
- Special thanks to [coGrammer-hyperiandev team](https://skills.cogrammar.com) for their contributions.
  


 
 
 

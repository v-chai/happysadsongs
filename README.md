# Project Background
- Title: happysadsongs
- Description: modeling to predict whether song lyrics are happy or sad/angry
- After testing various models, we deployed a RoBERTa model fine-tuned on our training data to a web app. For that deployment, see [/happysadsongs-frontend-2] (./happysadsongs-frontend-2) 

# Data Sources
- Training Data Source: 
  Compiled labeled happy, sad, and angry texts from several sources: 
    - [Hugging Face Emotion] (https://github.com/huggingface/datasets/blob/master/datasets/emotion/README.md)
    - [Google Go Emotions] (https://github.com/google-research/google-research/tree/master/goemotions)
    - [Crowdflower - Emotion in Text] (https://data.world/crowdflower/sentiment-analysis-in-text)
    - [MELD Emotion Lines] (https://affective-meld.github.io/)
    - 
- Test Data Source:
    - Compiled list of 260 songs based on web research (searching for lists of 50 saddest songs, 20 angriest songs, 100 happiest songs, etc.) 
    - Pulled lyrics from Genius API, MusixMatch API 

# Data Cleaning & Analysis

# Modeling



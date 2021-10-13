## Project Background
- Title: happysadsongs
- Description: modeling to predict whether song lyrics are happy or sad/angry
- After testing various models, we deployed a RoBERTa model fine-tuned on our training data to a web app. For that deployment, see [happysadsongs-frontend-2 repo](../../../happysadsongs-frontend-2) 
- See model in action at https://happysadsongs.herokuapp.com/

## Data Sources
### Training Data Source: 
Compiled labeled happy, sad, and angry texts from several sources: 
- [Hugging Face Emotion](https://github.com/huggingface/datasets/blob/master/datasets/emotion/README.md)
- [Google Go Emotions](https://github.com/google-research/google-research/tree/master/goemotions)
- [Crowdflower - Emotion in Text](https://data.world/crowdflower/sentiment-analysis-in-text)
- [MELD Emotion Lines](https://affective-meld.github.io/)
- [SemEval-2018](https://www.kaggle.com/context/semeval-2018-task-ec?select=2018-E-c-En-train.txt)

From these sources we randomly selected observations to create the following more or less balanced set:
- happy    14529
- sad      14000
- angry    13956
### Test Data Source:
- Compiled list of 260 songs based on web research (searching for lists of 50 saddest songs, 20 angriest songs, 100 happiest songs, etc.) 
- Pulled lyrics from Genius API, MusixMatch API 

## Data Cleaning & Analysis

## Modeling

## Next Steps
There are several areas for further exploration and improvement.

1. We could try to find labeled lyrics as our training data, instead of relying on shorter social media texts. We did not do this at the outset because we could not find a reliable database of labeled lyrics. In particular, we wanted to avoid songs that may have been labeled a particular emotion based more on the music than the lyrics. However, if we could develop a set of labeled lyrics, we might be able to see performance improvements in some of the models tested.
2. Currently, we trained our model only on English language texts. As such, we ignore songs in a user's recent playlist that are deemed to be in another language. Going forward, we could potentially find and add a translation API. Alternatively, we could try to find labeled emotion texts in other languages to expand the language capabilities of the model.
3. The RoBERTa model was fine-tuned to our emotion data using GPUs but, in deployment, we can only run it on CPUs. The model is very taxing and runs very slowly, even on just 10 songs. We might consider continuing to tinker with Logistic Regression or other simpler models to see if we could achieve comparable results with a lighter model. 


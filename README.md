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

## Modeling
After much trial and error of basic machine learning and deep learning models, our final deployed model was a RoBERTa ClassificationModel using the [simpletransformers](https://github.com/ThilinaRajapakse/simpletransformers) library. We fine-tuned the pretrained RoBERTa base model using our training dataset. 

Ultimately, we switched from a 3-class classification to a binary classification of happy or sad/angry (balancing the fine-tuning dataset accordingly). 

### Testing
We tested our model by running it on our 260 song test set. The model runs over overlapping 20-word segments of each song lyric. We then took the mode of the results to classify the entire song lyric as either happy or sad/angry. If a song is bimodal, we default to sad/angry classification because we wanted to be more conservative about happy song classification. 

### Baseline Accuracy Scoring
On a binary classifation (happy vs sad/angry), Zero-Rate baseline was 59%. Random Rate (weighted guess) baseline was 52%.

### Model Performance
On our test set, we achieved the following overall performance metrics:
- Accuracy: 83.1%
- Precision: 83.7%
- Recall: 83.1%
- Weighted f1-score: .826

Of note, the model has a higher precision score for happy and higher recall score for angry/sad. This aligns with our overall goal of not providing false positives for happy songs. (We wouldn't want to tell someone everything is great based on their recent playlist if, in fact, many of the songs were very sad or angry). 

## Application & Deployment
We containerized our model with Docker and uploaded it to Google Cloud Registry. We deploy the model with Google Cloud Run and developed a user-facing web app, see [happysadsongs](https://happysadsongs.herokuapp.com/) and [happysadsongs-frontend-2 repo](../../../happysadsongs-frontend-2). 

## Next Steps
There are several areas for further exploration and improvement.

1. We could try to find labeled lyrics as our training data, instead of relying on shorter social media texts. We did not do this at the outset because we could not find a reliable database of labeled lyrics. In particular, we wanted to avoid songs that may have been labeled a particular emotion based more on the music than the lyrics. However, if we could develop a set of labeled lyrics, we might be able to see performance improvements in some of the models tested.
2. Currently, we trained our model only on English language texts. As such, we ignore songs in a user's recent playlist that are deemed to be in another language. Going forward, we could potentially find and add a translation API. Alternatively, we could try to find labeled emotion texts in other languages to expand the language capabilities of the model.
3. The RoBERTa model was fine-tuned to our emotion data using GPUs but, in deployment, we can only run it on CPUs. The model is very taxing and runs very slowly, even on just 10 songs. We might consider continuing to tinker with Logistic Regression or other simpler models to see if we could achieve comparable results with a lighter model. 


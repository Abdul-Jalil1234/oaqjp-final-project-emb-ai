"""
Emotion detection module.

Sends customer feedback text to the IBM Watson NLP embeddable emotion
detection service and returns a structured dictionary of emotion scores
plus the dominant emotion.
"""

import json
import requests


def emotion_detector(text_to_analyze):
    """
    Calls the Watson NLP Emotion Predict API with the given text and
    returns a dictionary with the anger, disgust, fear, joy, and sadness
    scores, along with the dominant emotion.

    If the input text is blank/invalid (the API responds with a 400
    status code), every value in the returned dictionary is set to
    None. This lets the caller (server.py) detect bad input and show
    an appropriate error message instead of crashing.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header, timeout=10)

    # Task 7: handle blank/invalid input (Watson returns 400 for empty text)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(scores, key=scores.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

"""
Flask web deployment of the Emotion Detection application.

Run with:
    python server.py
Then open the app and submit text through the web interface, or call
the endpoint directly:
    GET /emotionDetector?textToAnalyze=<text>
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emot_detector():
    """Reads the textToAnalyze query parameter, runs emotion detection
    on it, and returns a formatted sentence describing the scores and
    dominant emotion. Blank/invalid input is handled explicitly."""
    text_to_analyze = request.args.get('textToAnalyze')

    # Task 7: handle blank input before even calling the detector
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    # Task 7: handle the case where Watson itself flags the input as invalid
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    label = response['dominant_emotion']
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {label}."
    )


@app.route("/")
def render_index_page():
    """Serves the main HTML page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

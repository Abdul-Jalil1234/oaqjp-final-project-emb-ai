"""
Unit tests for the emotion_detector function.

Run with:
    python -m unittest test_emotion_detection.py
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Verifies emotion_detector returns the expected dominant emotion
    for a range of sample statements, one per emotion category."""

    def test_emotion_detection(self):
        """Checks that each sample statement maps to its expected
        dominant emotion."""
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        result_2 = emotion_detector("I am so angry with you")
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        result_3 = emotion_detector("I am so sad about this")
        self.assertEqual(result_3['dominant_emotion'], 'sadness')

        result_4 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_4['dominant_emotion'], 'fear')

        result_5 = emotion_detector("I am disgusted")
        self.assertEqual(result_5['dominant_emotion'], 'disgust')


if __name__ == '__main__':
    unittest.main()

import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_glad_happened(self):
        text_to_analyze = "I am glad this happened"
        expected_dominant_emotion = 'joy'
        result = emotion_detector(text_to_analyze)
        self.assertIsNotNone(result)
        self.assertEqual(result['dominant_emotion'], expected_dominant_emotion)

    def test_emotion_really_mad(self):
        text_to_analyze = "I am really mad about this"
        expected_dominant_emotion = 'anger'
        result = emotion_detector(text_to_analyze)
        self.assertIsNotNone(result)
        self.assertEqual(result['dominant_emotion'], expected_dominant_emotion)

    def test_emotion_feel_disgusted(self):
        text_to_analyze = "I feel disgusted just hearing about this"
        expected_dominant_emotion = 'disgust'
        result = emotion_detector(text_to_analyze)
        self.assertIsNotNone(result)
        self.assertEqual(result['dominant_emotion'], expected_dominant_emotion)

    def test_emotion_so_sad(self):
        text_to_analyze = "I am so sad about this"
        expected_dominant_emotion = 'sadness'
        result = emotion_detector(text_to_analyze)
        self.assertIsNotNone(result)
        self.assertEqual(result['dominant_emotion'], expected_dominant_emotion)

    def test_emotion_really_afraid(self):
        text_to_analyze = "I am really afraid that this will happen"
        expected_dominant_emotion = 'fear'
        result = emotion_detector(text_to_analyze)
        self.assertIsNotNone(result)
        self.assertEqual(result['dominant_emotion'], expected_dominant_emotion)

if __name__ == '__main__':
    unittest.main()

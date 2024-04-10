import json
import requests

def emotion_detector(text_to_analyze):
    # URL and headers for the Watson NLP Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Input JSON data for the POST request
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        # Send POST request to Watson NLP Emotion Predict endpoint
        response = requests.post(url, json=input_json, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad status codes

        # Convert response text to dictionary
        json_response = json.loads(response.text)

        # Print the parsed JSON response for debugging
        #print("Parsed JSON Response:")
        #print(json_response)

        # Extract emotion predictions
        emotion_predictions = json_response.get('emotionPredictions', [])

        if not emotion_predictions:
            print("No emotion predictions found in response.")
            return None

        # Extract first emotion prediction (assuming single prediction)
        first_prediction = emotion_predictions[0]
        emotion = first_prediction.get('emotion', {})

        # Extract required emotions and scores
        emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        emotion_scores = {emotion_name: emotion.get(emotion_name, 0.0) for emotion_name in emotions}

        # Find the dominant emotion (emotion with the highest score)
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Prepare the output dictionary
        output = {
            'anger': emotion_scores['anger'],
            'disgust': emotion_scores['disgust'],
            'fear': emotion_scores['fear'],
            'joy': emotion_scores['joy'],
            'sadness': emotion_scores['sadness'],
            'dominant_emotion': dominant_emotion
        }

        return output

    except requests.RequestException as e:
        print(f"Error occurred during API request: {e}")
        return None
    except ValueError as ve:
        print(f"Error parsing JSON response: {ve}")
        return None

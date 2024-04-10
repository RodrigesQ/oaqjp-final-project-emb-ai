"""
Flask server for EmotionDetector application.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

def render_index_page():
    """
    Renders the index.html template.

    Returns:
        str: Rendered HTML content.
    """
    return render_template('index.html')

def analyze_emotion():
    """
    Analyzes the emotion from the provided text.

    Retrieves text to analyze from the query parameters.
    Uses the emotion_detector function to analyze the text.
    Formats the output and constructs the response message.

    Returns:
        tuple: A tuple containing the response message and HTTP status code.
    """
    # Get text to analyze from the query parameters
    text_to_analyze = request.args.get('textToAnalyze')

    # Use the emotion_detector function to analyze the text
    result = emotion_detector(text_to_analyze)

    # Format the output as needed
    formatted_output = {
        'anger': result['anger'],
        'disgust': result['disgust'],
        'fear': result['fear'],
        'joy': result['joy'],
        'sadness': result['sadness'],
        'dominant_emotion': result['dominant_emotion']
    }

    if result['dominant_emotion'] is None:
        return "Invalid input! Try again.", 400

    response_message = (
    f"For the given statement, the system response is {formatted_output}. "
    f"The dominant emotion is {result['dominant_emotion']}."
)

    # Return the response in JSON format
    return jsonify({'response': response_message}), 200

# Define routes for the Flask app
app.add_url_rule("/", view_func=render_index_page)
app.add_url_rule("/emotionDetector", view_func=analyze_emotion, methods=['GET'])

if __name__ == '__main__':
    app.run(host='localhost', port=5000)

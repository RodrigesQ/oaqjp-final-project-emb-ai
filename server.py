# server.py
from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def analyze_emotion():
    try:
        # Get text to analyze from the query parameters
        text_to_analyze = request.args.get('textToAnalyze')

        if text_to_analyze:
            # Use the emotion_detector function to analyze the text
            result = emotion_detector(text_to_analyze)

            if result:
                # Format the output as needed
                formatted_output = {
                    'anger': result['anger'],
                    'disgust': result['disgust'],
                    'fear': result['fear'],
                    'joy': result['joy'],
                    'sadness': result['sadness'],
                    'dominant_emotion': result['dominant_emotion']
                }
                response_message = f"For the given statement, the system response is {formatted_output}. The dominant emotion is {result['dominant_emotion']}."

                # Return the response in JSON format
                return jsonify({'response': response_message}), 200
            else:
                return jsonify({'error': 'Emotion detection failed. Please try again.'}), 400

        else:
            return jsonify({'error': 'Text data not provided.'}), 400

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='localhost', port=5000)

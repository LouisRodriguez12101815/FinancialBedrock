from flask import Flask, request, jsonify
import boto3
import os
import json

app = Flask(__name__)

# Configure AWS credentials using environment variables
aws_client = boto3.client(
    'bedrock',
    region_name='region',
    aws_access_key_id=empty,
    aws_secret_access_key=empty
)

AGENT_ARN = 'empty'

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.txt'):
        file_content = file.read().decode('utf-8')
        prompt = f"Generate a business plan based on the following description:\n{file_content}"
        
        try:
            response = aws_client.invoke_model(
                ModelName='10DLCsubmission',
                Input=json.dumps({"prompt": prompt})
            )
            result = json.loads(response['Output'])
            return jsonify(result)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid file type. Only .txt files are allowed.'}), 400

if __name__ == '__main__':
    app.run(ssl_context=('path/to/cert.pem', 'path/to/key.pem'), debug=True)

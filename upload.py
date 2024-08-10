from flask import Flask, render_template, request, redirect, url_for
import os
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/upload')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' in request.files:
        image = request.files['image']
        if image.filename != '':
            image_name='upload.jpeg'
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
            image.save(image_path)

            # Process the image using a Python script
            # Add your image processing code here

            return "Image uploaded and processed successfully."
        
@app.route('/', methods=['POST'])
def run_script():
    # Execute the Python script
    try:
        subprocess.run(['python', 'Handwriting_To_Text_Converter.py'], capture_output=True, text=True, check=True)
        result = "Script executed successfully!"
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.stderr}"
    return result

if __name__ == '__main__':
    app.run()
    

    


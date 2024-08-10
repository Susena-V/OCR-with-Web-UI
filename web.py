from flask import Flask, render_template, request, redirect, url_for
import os
import cv2
import pytesseract
import numpy as np
from transformers import pipeline

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.static_folder = 'static'

@app.route('/upload')
def index():
    return render_template('web.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' in request.files:
        image = request.files['image']
        if image.filename != '':
            image_name='upload.jpeg'
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
            image.save(image_path)
            message="Uploaded Successfully"
            return render_template('web.html',message=message)
        return redirect(url_for("index"))
        
@app.route('/', methods=['POST'])
def run_script():
    try:
        image_path = "uploads/upload.jpeg"
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((5, 5), dtype=int)
        image = cv2.erode(image, kernel, iterations=1)
        image = cv2.dilate(image, kernel, iterations=1)
        image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        image = cv2.bitwise_not(image)
        
        text = pytesseract.image_to_string(image, lang='eng')
        
        return render_template('web.html', output=text)
    except Exception as e:
        return render_template('web.html', output=f"Error: {str(e)}")

@app.route('/summ',methods=["POST"])
def summarize():
    image_path = "uploads/upload.jpeg"
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), dtype=int)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    image = cv2.bitwise_not(image)
    summarizer = pipeline("summarization")
    text = pytesseract.image_to_string(image, lang='eng')
    words=text.split()
    # Summarize the text
    summary = summarizer(text, max_length=len(words)//2)
    summ_print=summary[0]['summary_text']
    return render_template('web.html', summary=summ_print)


if __name__ == '__main__':
    app.run()
    

    


# 🖼️ Handwritten Text Recognition and Summarization Web App

This project is a Flask-based web application that allows users to upload images containing handwritten text, which is then processed to extract the text using Optical Character Recognition (OCR). Additionally, the extracted text can be summarized using a state-of-the-art NLP model. The application leverages the power of OpenCV, PyTesseract, and the Hugging Face Transformers library to provide accurate and efficient text extraction and summarization.

## 📜 Features

- **Image Upload:** Users can upload images directly through the web interface. The uploaded images are saved in a dedicated directory for processing.
- **Handwritten Text Recognition:** Utilizes PyTesseract, an OCR tool, to convert handwritten text in images to digital text. Advanced image preprocessing techniques, such as grayscale conversion, erosion, dilation, and thresholding, are applied to improve recognition accuracy.
- **Text Summarization:** The extracted text can be summarized using the Hugging Face Transformers' summarization pipeline, providing a concise version of the original content.
- **Real-Time Feedback:** The web application provides immediate feedback on the upload status, OCR results, and text summarization.

## 🔧 Technologies Used

- **Flask:** A lightweight WSGI web application framework for Python.
- **OpenCV:** An open-source computer vision library used for image processing.
- **PyTesseract:** A Python wrapper for Google's Tesseract-OCR Engine to perform optical character recognition.
- **Hugging Face Transformers:** A library for state-of-the-art Natural Language Processing (NLP) tasks, including text summarization.
- **HTML/CSS:** For creating a user-friendly web interface.

## 🗂️ Project Structure

- `app.py`: The main Flask application file that handles routes, image processing, and summarization logic.
- `uploads/`: Directory where uploaded images are stored.
- `templates/`: Contains HTML templates for the web interface (`upload.html` and `web.html`).
- `static/`: Folder for storing static files like CSS and JavaScript.

## 🛠️ Future Enhancements

- **Multilingual OCR Support:** Extend OCR capabilities to support multiple languages.
- **Improved Summarization:** Allow users to adjust the summary length dynamically.
- **User Authentication:** Implement user authentication to save and manage uploads for registered users.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

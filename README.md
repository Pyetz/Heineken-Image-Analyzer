# Heineken-Image-Analyzer
HackHCMC AngelHack 290624 Topic 2

## Project Overview
- The Heineken Image Analyzer project processes images related to Heineken, using Optical Character Recognition (OCR) and Large Language Model (LLM) applications to extract and analyze textual and visual information from the images. The project leverages advanced prompt engineering techniques to enhance the accuracy and relevance of the extracted data.
- This project aims to help Heineken automate the process of surveying locations through images.

## Features
- **Image Upload and Management**: Upload multiple image files through a user-friendly drag-and-drop interface.
- **OCR Processing**: Extract text from images using EasyOCR.
- **Image Description**: Use Gemini 1.5 Pro API and technical prompting for important information in the input image.
- **LLM Integration**: Use LLAMA3 to output the results based on the combination of OCR result and image description and in text format according to a specific template.
- **Prompt Engineering**: Customize prompts to improve the quality of data extraction.
- **Dark Mode Support**: Toggle between light and dark themes for better user experience.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/heineken-image-analyzer.git
    cd heineken-image-analyzer
    ```

## Usage
1. **Run the application**:
    ```sh
    python app.py
    ```

2. **Access the application**:
    Open your web browser and navigate to `http://localhost:5000`.

3. **Upload Images**:
    - Drag and drop images into the upload area or click to select files.
    - Choose the relevant categories (e.g., Drinker, Advertisement, Event).

4. **Analyze Images**:
    - Click the "Analyze Image(s)" button.
    - The application will process the images and display the extracted information.
  
## Demo
[![Video demo](https://img.youtube.com/vi/QOyHmc9uJ8w/0.jpg)](https://www.youtube.com/watch?v=QOyHmc9uJ8w)



## Code Structure
- `app.py`: Main application file to run the Flask server.
- `prompts.py`: Contains prompt templates for LLM processing.
- `utils.py`: Utility functions for image processing and data handling.
- `static/css/styles.css`: Styles for the web application.
- `static/js/scripts.js`: JavaScript for handling user interactions and image processing.
- `templates/index.html`: HTML template for the main interface.

## Requirements
Refer to the `requirements.txt` for the complete list of dependencies:
```txt
easyocr
numpy
pillow
groq
ipython
google-generativeai
```

## Acknowledgements
- Team AIO_116 for developing and maintaining the project.
- The creators of EasyOCR, LLMs, and other open-source used in this project.

## Team members
### [@Paietz](https://github.com/Pyetz) - Team Leader
- Responsibilities: Implementing technological solutions and programming for system deployment.
### [@NgocHuyenPhamm](https://github.com/NgocHuyenPhamm) - Advisor
- Responsibilities: Ideation, problem definition, data reporting, and business development for the project.

## Contact
For any questions or suggestions, please open an issue or contact us at vhphatdz@gmail.com.

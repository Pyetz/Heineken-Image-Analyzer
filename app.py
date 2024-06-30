from flask import Flask, request, jsonify, render_template, send_from_directory
from utils import perform_ocr, gen_description, analyze_img, standardize_analysis
from setup import install_requirements
from PIL import Image
import os
import json
# from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_single_image(file, options):
    # Process the image
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    img = Image.open(file_path).convert("RGB")

    ocr_result = perform_ocr(img)
    image_description = gen_description(img, options)
    analysis = analyze_img(ocr_result, image_description, options)
    analysis = standardize_analysis(analysis)

    # Delete the file after processing
    os.remove(file_path)

    result = {
        'filename': file.filename,
        'size': file.content_length,
        'type': file.content_type,
        'info': analysis
    }
    return result

@app.route('/process', methods=['POST'])
def process_images():
    if 'files' not in request.files:
        return jsonify({'error': 'No files provided'}), 400
    
    files = request.files.getlist('files')
    options = request.form.get('options')

    if options:
        options = json.loads(options)
    else:
        options = []
    if not options:
        options = ['Drinker', 'Ad', 'Event', 'Staff', 'Presence', 'Context', 'Logo']

    # print(options)

    results = []
    
    for file in files:
        # Process the image
        # start
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        img = Image.open(file_path).convert("RGB")

        ocr_result = perform_ocr(img)
        from prompts import img_description_prompt, img_analysis_prompt
        image_description = gen_description(img, options)
        # print('len google prompt:', len(img_description_prompt(options)))
        # print('len google descript:', len(image_description))
        analysis = analyze_img(ocr_result, image_description, options)
        # print('len groq prompt:', len(img_analysis_prompt(ocr_result, image_description, options)))
        # print('len groq analysis:', len (analysis))
        analysis = standardize_analysis(analysis)
        # end
        # analysis = "analysis"
        result = {
            'filename': file.filename,
            'size': file.content_length,
            'type': file.content_type,
            'info': analysis
        }
        results.append(result)
        print('done')

        # Delete the file after processing
        os.remove(file_path)

    # with ThreadPoolExecutor() as executor:
    #     futures = [executor.submit(process_single_image, file, options) for file in files]
    #     for future in futures:
    #         results.append(future.result())
    
    return jsonify(results)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    try:
        app.run(debug=True, port=5000)
    except ModuleNotFoundError:
        install_requirements()
        app.run(debug=True, port=5000)
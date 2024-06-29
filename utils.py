import easyocr
import numpy as np
from groq import Groq
import google.generativeai as genai
from prompts import img_description_prompt, img_analysis_prompt

# Initialize the OCR reader
ocr_reader = easyocr.Reader(["en"])
# API Key
GROQ_API_KEY = "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"
GOOGLE_API_KEY = "AIzaSyCzGvH9yi9SchqVDJKV_Ykpd-ipOCjjdlk"
GEMINI_MODEL = "gemini-1.5-flash"

def perform_ocr(img):
    result = ocr_reader.readtext(np.array(img))
    ocr_texts = [line[1] for line in result]
    return ocr_texts

def gen_description(img, options = ['Drinker', 'Ad', 'Event', 'Staff', 'Presence', 'Context', 'Logo']):
    genai.configure(api_key=GOOGLE_API_KEY)
    # img = Image.open('imges/FULL [Heineken Vietnam] Developer Resources/66500927_1705485488446.jpg')

    model = genai.GenerativeModel(model_name=GEMINI_MODEL)
    response = model.generate_content([img_description_prompt(options), img])

    return response.text

def analyze_img(ocr_result, image_description, options = ['Drinker', 'Ad', 'Event', 'Staff', 'Presence', 'Context', 'Logo']):
    prompt = img_analysis_prompt(ocr_result, image_description, options)

    client = Groq(
        api_key=GROQ_API_KEY,
    )

    data = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": prompt}]
    }

    chat_completion = client.chat.completions.create(**data)
    return chat_completion.choices[0].message.content

def standardize_analysis(analysis):
    analysis = analysis.replace("\n", "<br>")

    return analysis
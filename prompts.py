def img_description_prompt(options = ['Drinker', 'Ad', 'Event', 'Staff', 'Presence', 'Context', 'Logo']):
    prompt = f"""
    ### Instruction
Act as a Digital & Technology (D&T) expert of HEINEKEN Vietnam. Your task is to analyze the given image and extract detailed information based on the following questions. Ensure your answers are thorough, specific, and accurate. Note that Bivina and Bia Viet are different but look quite similar, so consider them carefully.

    ### Questions
    """
    if 'Drinker' in options:
        prompt += "How many people are there?\n"
        prompt += "How many of them are drinking Heineken beer?\n"
    if 'Ad' in options:
        prompt += "Are there any promotional materials with the Heineken logo?"
        prompt += "If so, what are they? Specify the types (eg. ice buckets, bottles, cans, refrigerators, signs, billboards, posters, display counters, display tables, posters, standees, umbrellas, shelves, etc.)\n"
    if 'Event' in options:
        prompt += "How many customers are in the image?"
        prompt += "What are they doing?"
        prompt += "What are their emotions when drinking Heineken beer?\n"
    if 'Staff' in options:
        prompt += "How many Heineken staff are there?\n"
    if 'Presence' in options:
        prompt += "How many advertising signs with Heineken logo are in the image?"
        prompt += "How many standees are there in the image?"
        prompt += "How many Heineken beer crates are there?\n"
    if 'Context' in options:
        prompt += "What is the context of the image? (e.g., bar, restaurant, grocery store, supermarket, etc.)"
        prompt += "Are there any restaurant staff members in the image?\n"
    if 'Logo' in options:
        prompt += "Are there any logos of Heineken's competitors in the image?"
        prompt += "If so, what are they? (Heineken competitors include Tiger, Bia Viet, Larue, Bivina, Edelweiss, and Strongbow)\n"

    prompt += "\n   ### Note\n"
    prompt += "Just answer in detail without additional commentary.\n"
    prompt += "No yapping."

    return prompt

def img_analysis_prompt(ocr_result, img_description, options = ['Drinker', 'Ad', 'Event', 'Staff', 'Presence', 'Context', 'Logo']):
    prompt = f"""
    ### Instruction
    Act as a Digital & Technology (D&T) of HEINEKEN Vietnam.
    Here are tasks of D&T:
    1. Brand logos: Detect logos of Heineken, Tiger, Bia Viet, Larue, Bivina, Edelweiss and Strongbow.
    2. Products: Identify beer kegs, beer bottles, and other products.
    3. Customers: Describe the number of customers, their activities, and emotions.
    4. Promotional Materials: Identify any posters, banners, and billboards.
    5. Setup Context: Determine the scene context (e.g., bar, restaurant, grocery store, or supermarket, etc.).

    I will provide you with a description of image and it's ocr result. Your task is to analyze the information provided about an image and fill in the xxx of the template to get a complete answer with suggestions in parentheses.

    ### Image Information
    OCR Results:
    {ocr_result}

    Image Description:
    {img_description}
    

    Answer Template:
"""

    if 'Drinker' in options:
        prompt += """
    About Drinker:
    - Number of people: [xxx]
    - Number of Heineken drinkers: [xxx]
"""
    if 'Ad' in options:
        prompt += """
    About Promotional Materials:
    - List of all promotional materials with Heineken logo: [xxx] ([xxx] xxx can be one or more of ice buckets, bottles, cans, refrigerators, signs, posters, display counters, display tables, standees, umbrellas and shelves, etc.)
"""
    if 'Event' in options:
        prompt += """
    About the success of the event:
    - Number of customers: [xxx]
    - Customer activities: [xxx]
    - Customer emotions: [xxx]
    -> Therefore, the event is [xxx] (e.g., successful, unsuccessful, or neutral)
"""
    if 'Staff' in options:
        prompt += """
    About Staff:
    - Number of Heineken staff: [xxx]
    - There are at least 2 Heineken staff members? [xxx] (True/False)
    -> Therefore, the staff is [xxx] (e.g., sufficient, insufficient, or neutral)
"""
    if 'Presence' in options:
        prompt += """
    About the presence of Heineken:
    - There are at least 1 advertising sign with Heineken logo? [xxx] (True/False)
    - There are at least 1 standee? [xxx] (True/False)
    - There are at least 10 Heineken beer crates? [xxx] (True/False)
    -> Therefore, the presence is [xxx] (e.g., strong, weak, or neutral)
"""
    if 'Context' in options:
        prompt += """
    About the context:
    - The scene context: [xxx] (e.g., bar, restaurant, grocery store, or supermarket, etc.)
    - There are at least 1 restaurant staff member? [xxx] (True/False)
"""
    if 'Logo' in options:
        prompt += """
    About the brand logos:
    - List of all competitor logos: [xxx] (e.g., Tiger, Bia Viet, Larue, Bivina, Edelweiss, and Strongbow)
"""

    prompt += "Fill in the template above accurately. Provide only the filled-in template, nothing else."
    prompt += "No yapping."

    return prompt
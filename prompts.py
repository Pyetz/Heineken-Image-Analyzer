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
        prompt += "What is the context of the image? (e.g., display point, event, bar, restaurant, grocery store, supermarket, etc.)"
        prompt += "Are there any restaurant staff members in the image?\n"
    if 'Logo' in options:
        prompt += "Are there any logos of Heineken's competitors in the image?"
        prompt += "If so, what are they? (Heineken competitors include Tiger, Bia Viet, Larue, Bivina, Edelweiss, and Strongbow)\n"

    prompt += "\n   ### Note\n"
    prompt += "Just answer in detail without additional commentary.\n"
    prompt += "No yapping."

    # print('gemini prompt:', len(prompt))
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
    5. Setup Context: Determine the scene context (e.g., display point, event, bar, restaurant, grocery store, or supermarket, etc.).

    I will provide you with a description of image and it's ocr result. Your task is to analyze the information provided about an image and fill in the xxx of the template to get a complete answer with suggestions in parentheses.

    ### Image Information
    OCR Results:
    {ocr_result}

    Image Description:
    {img_description}
    

    Answer Template:

    The scene context: [xxx] (e.g., display point, event, bar, restaurant, grocery store, or supermarket, etc.)
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
    - There are at least 1 restaurant staff member? [xxx] (True/False)
"""
    if 'Logo' in options:
        prompt += """
    About the brand logos:
    - List of all competitor logos: [xxx] (e.g., Tiger, Bia Viet, Larue, Bivina, Edelweiss, and Strongbow)
"""

    prompt += """
    ### Note
    - A person is considered to be drinking Heineken beer if they are directly holding a Heineken bottle or if there is a Heineken bottle on their table. If their table has multiple types of beer, the ratio of Heineken bottles to other beers represents the ratio of people drinking Heineken. And just consider 'About Drinker' if the context is restaurant, bar or at other social drinking gatherings
    - Not consider 'About the success of the event' if the context is grocery store or supermarket
    - Just consider 'Presence' if the context is grocery store or supermarket
    - Just consider 'There are at least 1 restaurant staff member?' if the context is restaurant
    - The OCR results and image description may be inaccurate due to camera angles or errors during image processing. Therefore, please use the following two rules to identify the logo:
    For OCR results with meaningless characters that match the beginning or end of a beer brand name, it can be concluded that it is a beer brand (e.g., if OCR results in "Bia V" or "Viet" or "iet," it can be concluded as "Bia Viet," or if it results in "tig" and "iger" or "ger," it will be concluded as "Tiger Beer").
    For words that are 80-90% similar to a beer brand name (only 1-2 characters incorrect), it can also be concluded as that beer brand (e.g., "tig3r" is "tiger").
    - Only those wearing Heineken shirts and performing tasks to assist others are considered Heineken employees.
    - You need to distinguish clearly and accurately between advertising signs, standees, beer crates, and other promotional materials, and it is strictly prohibited to fabricate information if you are unsure.
Ice Buckets: Buckets used to keep drinks cold.
Bottles: Containers used to hold beverages.
Cans: Containers, usually made of metal, used to hold beverages.
Refrigerators: Appliances used to store beverages at cool temperatures.
Signs: Small advertising boards typically mounted on walls or doors.
Posters: Printed advertisements with images and product information.
Display Counters: Counters used to display products in stores.
Display Tables: Tables used to showcase products at exhibitions or events.
Standees: Stand-up advertising boards, often shaped like people or products.
Umbrellas: Umbrellas often printed with logos and used outdoors for advertising.
Shelves: Racks used to display products in stores.
"""

    prompt += "Fill in the template above accurately. Provide only the filled-in template, nothing else.\n"
    prompt += "No yapping."

    # print('groq prompt:', len(prompt))
    return prompt
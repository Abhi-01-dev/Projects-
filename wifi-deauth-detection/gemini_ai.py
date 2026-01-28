import google as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

def analyze_attack(details):
    prompt = f"""
You are a cybersecurity expert.

WiFi attack detected with following details:
{details}

Return response in this format:

Attack Type:
<attack name>

Risk Level:
<low / medium / high>

Explanation:
<short explanation>

Prevention:
- step 1
- step 2
- step 3
"""

    response = model.generate_content(prompt)
    return response.text

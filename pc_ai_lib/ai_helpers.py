import google.generativeai as genai

genai.configure(api_key="AIzaSyAUa-pY5sDz7jfUAj8V7Djm2FnzHR15HOQ")

model = genai.GenerativeModel("gemini-2.0-flash")

def get_ai_response(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI Error: {str(e)}"

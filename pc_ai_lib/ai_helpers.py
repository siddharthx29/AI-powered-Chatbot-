import google.generativeai as genai

genai.configure(api_key="AIzaSyAk34ppDyKhqVRKtNSGkJSt_AXBHoXGaF4")

model = genai.GenerativeModel("gemini-2.0-flash")

def get_ai_response(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI Error: {str(e)}"

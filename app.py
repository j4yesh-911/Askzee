# from flask import Flask, render_template, request, jsonify
# import google.generativeai as genai
# import os

# # Configure Gemini
# genai.configure(api_key="")

# model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

# # Set up Flask
# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_input = request.json.get("message")
#     if not user_input:
#         return jsonify({"response": "Please send a valid message."})

#     try:
#         response = model.generate_content(user_input)
#         return jsonify({"response": response.text})
#     except Exception as e:
#         return jsonify({"response": f"Error: {str(e)}"})

# if __name__ == "__main__":
#     app.run(debug=True)




from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

from dotenv import load_dotenv
load_dotenv()


# Configure Gemini using environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

# Set up Flask
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"response": "Please send a valid message."})

    try:
        response = model.generate_content(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's port or default 5000
    app.run(host="0.0.0.0", port=port)














# list_models.py
# import google.generativeai as genai

# genai.configure(api_key="")

# for model in genai.list_models():
#     if "generateContent" in model.supported_generation_methods:
#         print("✅ Available model:", model.name)






# from flask import Flask, render_template, request, jsonify
# import google.generativeai as genai
# import os

# # Configure Gemini
# genai.configure(api_key="")

# model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

# # Set up Flask
# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_input = request.json.get("message")
#     if not user_input:
#         return jsonify({"response": "Please send a valid message."})

#     try:
#         response = model.generate_content(user_input)
#         return jsonify({"response": response.text})
#     except Exception as e:
#         return jsonify({"response": f"Error: {str(e)}"})

# if __name__ == "__main__":
#     app.run(debug=True)




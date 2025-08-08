# from flask import Flask, render_template, request, jsonify
# import google.generativeai as genai
# import os

# # Configure Gemini
# genai.configure(api_key="AIzaSyB9nsn7-umEPTyYeoZR5AEOfHBwuL0NEXk")

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

# Configure Gemini using environment variable
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

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
    app.run(debug=True)













# list_models.py
# import google.generativeai as genai

# genai.configure(api_key="AIzaSyB9nsn7-umEPTyYeoZR5AEOfHBwuL0NEXk")

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




from flask import Flask, render_template, request

app = Flask(__name__)

chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():
    global chat_history

    if request.method == "POST":
        user_input = request.form["user_input"].lower()


        if "ai" in user_input:
            response = "Artificial Intelligence (AI) is the simulation of human intelligence in machines that are programmed to think and learn."

        elif "machine learning" in user_input:
            response = "Machine Learning is a subset of AI that enables systems to learn from data and improve without being explicitly programmed."

        elif "python" in user_input:
            response = "Python is a popular programming language used for web development, AI, machine learning, and data science."

        elif "hello" in user_input:
            response = "Hello! 👋 How can I help you today?"

        elif "hi" in user_input:
            response = "Hi there! 😊 What would you like to know?"

        else:
            response = "I'm still learning 😊 Please ask something related to AI, Machine Learning, or Python."

        
        chat_history.append(("user", user_input))
        chat_history.append(("bot", response))

    return render_template("index.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)

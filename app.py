from flask import Flask,render_template,request,jsonify
from utils.genai_utils import generate_text
from utils.audio_utils import text_to_audio
from utils.image_utils import generate_image
from utils.code_executor import generate_code

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_text",methods=["POST"])
def text():

    topic=request.json["topic"]

    prompt=f"Explain machine learning concept: {topic}"

    result=generate_text(prompt)

    return jsonify({"text":result})

@app.route("/generate_code",methods=["POST"])
def code():

    topic=request.json["topic"]

    code,filename=generate_code(topic)

    return jsonify({"code":code})

@app.route("/generate_audio",methods=["POST"])
def audio():

    topic=request.json["topic"]

    text=generate_text(f"Explain {topic} in simple way")

    file=text_to_audio(text)

    return jsonify({"audio":file})

@app.route("/generate_image",methods=["POST"])
def image():

    topic=request.json["topic"]

    file=generate_image(topic)

    return jsonify({"image":file})

if __name__=="__main__":
    app.run(debug=True)
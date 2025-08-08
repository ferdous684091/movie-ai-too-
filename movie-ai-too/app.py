from flask import Flask, request, jsonify
import wikipedia

app = Flask(__name__)

@app.route("/")
def home():
    return "Movie AI Tool is running."

@app.route("/movie-info", methods=["GET"])
def movie_info():
    query = request.args.get("query")
    try:
        summary = wikipedia.summary(query, sentences=3)
        return jsonify({"status": "success", "summary": summary})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

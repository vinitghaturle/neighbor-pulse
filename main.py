from flask import Flask, render_template, request, jsonify
from google.cloud import firestore
from vertexai.language_models import TextEmbeddingModel
from google.cloud.firestore_v1.vector import Vector
from google.cloud.firestore_v1.base_vector_query import DistanceMeasure
from datetime import datetime

app = Flask(__name__)

# Initialize Firestore and Vertex AI
# Project ID 'neighbor-pulse' confirmed from system logs
db = firestore.Client(project="neighbor-pulse") 
model = TextEmbeddingModel.from_pretrained("text-embedding-004")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_item():
    data = request.json
    description = data.get('description')
    
    if not description:
        return jsonify({"error": "Description is required"}), 400

    # Save to Firestore - This triggers the AI Vector Extension automatically
    doc_ref = db.collection("items").add({
        "description": description,
        "timestamp": datetime.utcnow(),
        "status": "available"
    })
    
    return jsonify({"success": True, "id": doc_ref[1].id})

@app.route('/search', methods=['POST'])
def search():
    user_query = request.json.get('query')
    
    # 1. Turn user text into math (Vector)
    embedding = model.get_embeddings([user_query])[0].values
    
    # 2. Ask Firestore for the top 3 matches
    collection = db.collection("items")
    results = collection.find_nearest(
        vector_field="embedding",
        query_vector=Vector(embedding),
        distance_measure=DistanceMeasure.COSINE,
        limit=3,
        distance_result_field="vector_distance"
    ).get()
    
    # 3. Send results back
    matches = [{"description": d.get("description"), "dist": d.get("vector_distance")} for d in results]
    return jsonify(matches)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
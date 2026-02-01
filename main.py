from flask import Flask, render_template, request, jsonify
from google.cloud import firestore
from vertexai.language_models import TextEmbeddingModel
from google.cloud.firestore_v1.vector import Vector
from google.cloud.firestore_v1.base_vector_query import DistanceMeasure

app = Flask(__name__)
db = firestore.Client(project="neighbor-pulse") # Use your project ID
model = TextEmbeddingModel.from_pretrained("text-embedding-004")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_query = request.json.get('query')
    
    # 1. Turn user text into math (Vector)
    embedding = model.get_embeddings([user_query])[0].values
    
    # 2. Ask Firestore for the top 3 matches using the index you built
    collection = db.collection("items")
    results = collection.find_nearest(
        vector_field="embedding",
        query_vector=Vector(embedding),
        distance_measure=DistanceMeasure.COSINE,
        limit=3,
        distance_result_field="vector_distance"
    ).get()
    
    # 3. Send results back to the neighbor
    matches = [{"description": d.get("description"), "dist": d.get("vector_distance")} for d in results]
    return jsonify(matches)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
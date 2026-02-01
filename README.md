# Neighbor Pulse 📡

**Neighbor Pulse** is a real-time, AI-powered community exchange platform built on Google Cloud. It allows neighbors to share surplus items through a live "Pulse" feed and find exactly what they need using semantic vector search.

## 🚀 The Architectural Evolution (Major Pivot)
This project is an evolution of the "Neighbor Loop" lab. While the original lab used a relational AlloyDB (SQL) backend, **Neighbor Pulse** pivots to a serverless, event-driven NoSQL architecture using **Google Cloud Firestore**.

### Why NoSQL & Firestore?
* **Real-Time Synchronization:** Unlike static SQL databases, Firestore allows for live "Snapshot" listeners. When a neighbor posts an item, it appears on everyone’s feed instantly without a page refresh.
* **Event-Driven AI:** Instead of manual batch processing, this project utilizes the **Firestore Vector Search Extension**. AI embeddings are generated automatically via Cloud Functions the moment a document is written.
* **Serverless Scaling:** The entire stack is serverless, scaling to zero when not in use.

## 🛠️ Tech Stack
* **Frontend:** HTML5, CSS3, JavaScript (Firebase SDK).
* **Backend:** Python (Flask), Google Cloud Firestore.
* **AI/ML:** Vertex AI (`text-embedding-004`), Firestore Vector Search Extension.

## 🔧 Technical Challenges Overcome
* **API Configuration:** Resolved `PERMISSION_DENIED` errors by enabling the Cloud Firestore API.
* **Extension Tuning:** Fixed a configuration error where a leading space in the collection name (`" items"`) stopped the AI worker.
* **Vector Indexing:** Successfully deployed a 768-dimension Vector Index.

## 💻 Setup & Installation
1.  **Clone the Repository:** `git clone https://github.com/vinitghaturle/neighbor-pulse.git`
2.  **Install Dependencies:** `pip install -r requirements.txt`
3.  **Run the App:** `python main.py`

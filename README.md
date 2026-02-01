Neighbor Pulse 📡
Neighbor Pulse is a real-time, AI-powered community exchange platform built on Google Cloud. It allows neighbors to share surplus items through a live "Pulse" feed and find exactly what they need using semantic vector search.

🚀 The Architectural Evolution (Major Pivot)
This project is an evolution of the "Neighbor Loop" lab. While the original lab used a relational AlloyDB (SQL) backend, Neighbor Pulse pivots to a serverless, event-driven NoSQL architecture using Google Cloud Firestore.

Why NoSQL & Firestore?
Real-Time Synchronization: Unlike static SQL databases, Firestore allows for live "Snapshot" listeners. When a neighbor posts an item, it appears on everyone’s feed instantly without a page refresh.

Event-Driven AI: Instead of manual batch processing, this project utilizes the Firestore Vector Search Extension. AI embeddings are generated automatically via Cloud Functions the moment a document is written.

Serverless Scaling: The entire stack is serverless, scaling to zero when not in use to minimize costs and maintenance.

🛠️ Tech Stack
Frontend: HTML5, CSS3 (Modern Responsive UI), JavaScript (Firebase SDK).

Backend: Python (Flask), Google Cloud Firestore.

AI/ML: Vertex AI (text-embedding-004), Firestore Vector Search Extension.

Environment: Project IDX (Nix-based).

🔧 Technical Challenges Overcome
API Configuration: Resolved PERMISSION_DENIED errors by enabling the Cloud Firestore API and configuring proper IAM roles for Vertex AI access.

Extension Tuning: Fixed a critical configuration error where a leading space in the collection name (" items") prevented the AI worker from processing new documents.

Vector Indexing: Successfully deployed a 768-dimension Vector Index with Cosine distance measure to enable semantic similarity searches.

💻 Setup & Installation
Clone the Repository:

Bash
git clone (https://github.com/vinitghaturle/neighbor-pulse.git)
cd neighbor-pulse
Environment Setup (Project IDX/Nix): Ensure your .idx/dev.nix is configured to install Python 3.12 and dependencies.

Install Dependencies:

Bash
pip install -r requirements.txt
Google Cloud Configuration:

Enable Firestore in Native Mode.

Install the Vector Search with Firestore extension.

Deploy a Vector Index on the items collection for the embedding field.

📝 Usage
Post an Item: Add a document to the items collection in Firestore.

Watch the Pulse: The frontend updates in real-time as new items are added.

Search: Use the AI search bar to find items by meaning (e.g., searching for "grass tools" will find a "lawnmower").

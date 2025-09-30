from flask import Flask, render_template, request, jsonify
from OceanQuery.query import fetch_argo_profiles  # assuming OceanQuery has this

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query", "").strip()

    if not query:
        return jsonify({"error": "Empty query"}), 400

    # Example: If query mentions "Argo profiles", call OceanQuery
    if "argo" in query.lower() and "profile" in query.lower():
        # Example: Fetch ±2° latitude, March 2023, salinity vs pressure
        profiles = fetch_argo_profiles(lat_min=-2, lat_max=2, date="2023-03", variable="PSAL_ADJUSTED")

        return jsonify({
            "reply": f"Fetched {len(profiles)} Argo profiles (±2° lat, March 2023).",
            "profiles": profiles  # You can return structured data
        })

    # Default fallback
    return jsonify({"reply": f"You asked: {query}"})


if __name__ == "__main__":
    app.run(debug=True)

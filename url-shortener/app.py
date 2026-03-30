from flask import Flask, request, jsonify, redirect
from database import get_db
from utils import encode_base62

app = Flask(__name__)

#  Home Route
@app.route("/")
def home():
    return "URL Shortener Running 🚀"


# Shorten URL API
@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    long_url = data["url"]

    db = get_db()
    cursor = db.cursor()

    #  Check if URL already exists
    cursor.execute("SELECT short_code FROM urls WHERE long_url=%s", (long_url,))
    existing = cursor.fetchone()

    if existing:
        short_code = existing[0]
        cursor.close()
        db.close()
        return jsonify({
            "short_url": f"{request.host_url}{short_code}"
        })

    # Insert new URL
    cursor.execute("INSERT INTO urls (long_url) VALUES (%s)", (long_url,))
    db.commit()

    url_id = cursor.lastrowid

    # Generate short code
    short_code = encode_base62(url_id)

    # Update DB with short code
    cursor.execute("UPDATE urls SET short_code=%s WHERE id=%s", (short_code, url_id))
    db.commit()

    cursor.close()
    db.close()

    return jsonify({
        "short_url": f"{request.host_url}{short_code}"
    })


# Redirect API
@app.route("/<short_code>")
def redirect_url(short_code):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT long_url FROM urls WHERE short_code=%s", (short_code,))
    result = cursor.fetchone()

    if result:
        long_url = result[0]

        # Track click
        cursor.execute("INSERT INTO clicks (short_code) VALUES (%s)", (short_code,))
        db.commit()

        cursor.close()
        db.close()

        return redirect(long_url)
    else:
        cursor.close()
        db.close()
        return "URL not found", 404


# Analytics API
@app.route("/analytics/<short_code>")
def analytics(short_code):
    db = get_db()
    cursor = db.cursor()

    # Total clicks
    cursor.execute("SELECT COUNT(*) FROM clicks WHERE short_code=%s", (short_code,))
    total_clicks = cursor.fetchone()[0]

    # Last 5 clicks
    cursor.execute(
        "SELECT timestamp FROM clicks WHERE short_code=%s ORDER BY timestamp DESC LIMIT 5",
        (short_code,)
    )
    recent_clicks = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify({
        "short_code": short_code,
        "total_clicks": total_clicks,
        "recent_clicks": [str(x[0]) for x in recent_clicks]
    })


# 🔹 Run App
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "your-secret-key"  # kuch bhi random likh sakta hai


# ---- MEMORIES DATA ----
MEMORIES = {
    "1": {
        "title": "Memories",
        "hint": "Password = YOUR TEETHS 😘",
        "password": "favdi",  # yahi password hai
        "image": None,        # ya "memory1.jpg"
        "text": "valentine day proposal 😁",
        "audio": None,        # ya "voice1.mp3"
        "video_url": "https://www.youtube.com/embed/s1VoZpOAmLo",
    },
     "2": {
        "title": "Diwali",
        "hint": "You are a...",
        "password": "brainrot",
        "image": None,  # abhi image nahi
        "text": "The Diwali moment where I actually got obsessed with you.",
        "audio": None,
        "video_url": "https://www.youtube.com/embed/GhzxznF7bC0",
    },
    "3": {
    "title": "Old Ones 🤭",
    "hint": "Boobie size 😌",
    "password": "small",  # no caps
    "image": None,
    "text": "Miss those days more than the present 😚🤗",
    "audio": None,
    "video_url": "https://www.youtube.com/embed/X7Z4e-4VKms",
},
"4": {
    "title": "Real Brainrot 😈",
    "hint": "Ass size 😳",
    "password": "small",  # keep lowercase
    "image": None,
    "text": "This is where my real brainrot started… 👀🔥",
    "audio": None,
    "video_url": "https://www.youtube.com/embed/_vyjyP5zAzc",
},

}


# ---- ROUTES ----
@app.route("/")
def index():
    return render_template("index.html", memories=MEMORIES)


@app.route("/memory/<mid>", methods=["GET", "POST"])
def memory_lock(mid):
    memory = MEMORIES.get(mid)
    if not memory:
        return "Not found", 404

    if request.method == "POST":
        entered = request.form.get("password", "")
        entered_clean = entered.strip().lower()
        expected_clean = str(memory["password"]).strip().lower()

        print("ENTERED:", repr(entered_clean))
        print("EXPECTED:", repr(expected_clean))

        if entered_clean == expected_clean:
            return render_template("memory_view.html", memory=memory, mid=mid)

        flash("Wrong password 😛")

    return render_template("memory_lock.html", memory=memory, mid=mid)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


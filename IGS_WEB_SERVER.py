
# -*- coding: utf-8 -*-
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <html>
            <head><title>IGS - GLOBAL SYSTEMS</title></head>
            <body style="background-color: #0b0e14; color: #00d4ff; font-family: 'Courier New'; text-align: center;">
                <h1>🏛️ INFINITY GLOBAL SYSTEMS (IGS) 🏛️</h1>
                <p>Status: <span style="color: #00ff00;">LIVE & SECURED</span></p>
                <hr>
                <div style="border: 1px solid #00d4ff; padding: 20px; width: 50%; margin: auto;">
                    <h3>💬 IGS Customer Support (AI-Bot)</h3>
                    <p>Welcome, Ya Abqari. How can IGS protect you today?</p>
                    <input type="text" placeholder="Type your security query..." style="width: 80%;">
                    <button>Send</button>
                </div>
                <footer style="margin-top: 50px;">Property of Infinity-Global-Systems © 2026</footer>
            </body>
        </html>
    ''')

if __name__ == "__main__":
    print("🚀 IGS WEB PORTAL IS STARTING ON http://127.0.0.1:5000")
    app.run(debug=True)


# 📝 AI Text Summarizer

A simple, self-hosted, AI-powered text summarization tool built with **Python (Flask)**, **HTML/CSS/JavaScript**, and a **local or remote LLM**.
Paste in any text, click summarize, and instantly get a concise version of the content.

---

## 🚀 Features

* **Paste & Summarize** – Quickly condense large blocks of text.
* **AI-Powered** – Uses a local or remote LLM for accurate, natural summaries.
* **Loading Animation** – Shows progress while the AI processes your request.
* **Self-Hosted** – Runs locally, no external dependencies required.
* **Optional Remote Access** – Share via Cloudflare Tunnel without port forwarding.

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/summarizer.git
cd summarizer
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App Locally

```bash
python app.py
```

The app will be available at:

```
http://127.0.0.1:5000
```

---

## 🌐 Optional: Remote Access via Cloudflare Tunnel

To make the summarizer accessible over the internet:

```bash
cloudflared tunnel --url http://127.0.0.1:5000
```

Copy the `.trycloudflare.com` link from your terminal and open it in a browser.

---

## 🛠 Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript
* **AI Model:** Local or API-based LLM
* **Optional Networking:** Cloudflare Tunnel

---

## 📜 License

This project is licensed under the **MIT License**.

---


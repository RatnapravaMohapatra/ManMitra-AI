# 🧠 ManMitra AI

### Mental Wellness Companion Powered by Gemma 4

ManMitra AI is an AI-powered mental wellness journaling application that helps users reflect on their emotions, identify stress triggers, and receive supportive wellness insights using Google's Gemma 4 model.

The application encourages self-awareness and emotional well-being while maintaining user privacy. It is designed for students, job seekers, and professionals who want a simple way to track their thoughts and emotions.

---

## 🚀 Problem Statement

Many people experience:

- Stress
- Burnout
- Anxiety
- Career uncertainty
- Emotional overload

However, they often lack a simple tool for daily reflection and emotional awareness.

ManMitra AI addresses this challenge by providing AI-generated emotional insights and wellness recommendations based on daily journal entries.

---

## ✨ Features

### 📝 Daily Journal Entry
Users can write about their thoughts, feelings, and daily experiences.

### 😊 Emotional Summary
Gemma 4 analyzes the journal and provides a concise emotional overview.

### ⚠️ Stress Level Detection
Identifies whether the user's stress level appears Low, Medium, or High.

### 🔍 Main Concern Identification
Highlights possible stress triggers and recurring concerns.

### 🌱 Positive Sign Detection
Recognizes strengths, achievements, and encouraging aspects of the user's entry.

### 💡 Wellness Suggestions
Provides practical wellness recommendations and reflection prompts.

### 🤖 Powered by Gemma 4
Uses Google's Gemma 4 model for intelligent emotional analysis.

---

## 🏗️ Architecture

```text
User Journal Entry
        │
        ▼
   Streamlit UI
        │
        ▼
 Google AI Studio API
        │
        ▼
   Gemma 4 Model
        │
        ▼
 Wellness Insights
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend |
| Streamlit | Frontend UI |
| Google AI Studio | Model Access |
| Gemma 4 | AI Analysis |
| Google GenAI SDK | API Integration |

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/manmitra-ai.git

cd manmitra-ai
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install streamlit google-genai
```

---

## 🔑 Configure API Key

Create a Google AI Studio API key:

https://aistudio.google.com

Replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your generated API key.

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 📸 Example Input

```text
I have been feeling stressed lately because of job searching.
I am worried about my future but I am learning machine learning every day.
Today I completed a project and felt proud of myself.
```

---

## 📸 Example Output

### Emotional Summary
The user appears motivated but experiences moderate stress related to career uncertainty.

### Stress Level
Medium

### Main Concerns
- Job search pressure
- Future uncertainty

### Positive Signs
- Continuous learning
- Project completion
- Self-motivation

### Wellness Suggestions
- Break larger goals into smaller tasks
- Maintain a daily learning routine
- Celebrate small achievements

---

## ⚠️ Disclaimer

ManMitra AI is intended for wellness support and self-reflection purposes only.

It is **not a medical device**, **not a diagnostic tool**, and **does not provide professional mental health advice**.

Users experiencing significant distress should seek support from qualified healthcare professionals.

---

## 🌟 Future Enhancements

- Voice Journaling
- Mood Trend Dashboard
- Multilingual Support
- PDF Wellness Reports
- Daily Reflection Reminders
- Emotional Pattern Tracking
- Personalized Wellness Plans

---

## 🎯 Buildathon Submission

This project was developed using **Gemma 4** and focuses on promoting emotional well-being through AI-assisted journaling and self-reflection.

---

## 👨‍💻 Author

Developed for the Gemma 4 Buildathon.

**Project Name:** ManMitra AI  
**Tagline:** Your AI Wellness Companion

# 🔍 AI-Powered Repository Analyzer

## 🚀 Overview
Understanding and modernizing legacy repositories is a **real-world developer challenge**. Teams spend hours (sometimes days) just to:
- Understand project structure
- Identify outdated practices
- Figure out where to add new features
- Debug existing issues

This tool solves that problem by using **Google Gemini 2.5 Pro** to automatically analyze a GitHub repository and provide structured insights.

## 💡 The Challenge
Developers often struggle when working with unfamiliar or poorly documented repositories.
- Onboarding takes too long
- Modernization efforts are delayed
- Feature integration is risky

## 🧠 The Idea
**AI-Powered Repo Analyzer**: Paste a GitHub URL, ask a question, and get AI-driven insights.

## ✨ Key Features
- **Repository Analysis:** Summarizes structure and purpose.
- **Modernization Suggestions:** Identifies outdated or risky code practices.
- **Feature Integration Guidance:** Suggests where new features can be integrated.
- **Issue Diagnosis:** Provides possible error sources and codes.
- **Architecture & Flow Diagrams:** Auto-generated from repo analysis.

## 📂 Project Structure
```
Hackathon-RepoAnalyzer/
│── app.py                # Streamlit app (main entry)
│── requirements.txt      # Dependencies
│── README.md             # Project overview
│── docs/
│    └── Hackathon_Pitch.pdf   # PDF with challenge, idea, and demo doc
│── .env.example          # Example env file (no keys)
```

## 🛠️ Installation & Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/Hackathon-RepoAnalyzer.git
   cd Hackathon-RepoAnalyzer
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your API key in `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

5. Run the app:
   ```bash
   streamlit run app.py
   ```

## ☁️ Deploy on HuggingFace Spaces
1. Create a HuggingFace account.
2. Create a new Space → select **Streamlit**.
3. Push this repo OR upload manually.
4. Add `GEMINI_API_KEY` in HuggingFace **Secrets**.
5. Your app is live 🚀.

## 📊 Demo Workflow
1. Enter a GitHub repository URL
2. Ask a question: *"Where can I add logging?"*
3. Get:
   - 📌 Repo summary
   - 📂 Suggested files for change
   - ⚡ Error codes / modernization tips
   - 🏗️ Architecture diagram

## 🙌 Why This is Useful
- Reduces onboarding time for new developers
- Boosts productivity for teams
- Provides clear modernization roadmap
- Enhances hackathon speed & innovation

---

# 🎯 Hackathon Pitch Summary
👉 Real-world problem: repo understanding is slow and painful.  
👉 Our solution: AI-powered instant repo analysis with diagrams.  
👉 Benefit: Saves time, boosts collaboration, accelerates delivery.

📄 Detailed description in `docs/Hackathon_Pitch.pdf`


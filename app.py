import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# ----------------------
# Load environment variables
# ----------------------
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ----------------------
# Initialize Gemini model
# ----------------------
model = genai.GenerativeModel("gemini-2.5-pro")

# ----------------------
# Streamlit Page Config
# ----------------------
st.set_page_config(page_title="AI Repo Analyzer", layout="wide")

# ----------------------
# App Title
# ----------------------
st.title("🔍 AI-Powered Repository Analyzer")

st.markdown(
    """
    This tool uses **Gemini 2.5 Pro** to analyze GitHub repositories.  
    - Paste a repo URL  
    - Ask repo/code-related questions (e.g., modernization, finding issues, suggesting feature additions, error codes, diagrams, etc.)  
    """
)

# ----------------------
# Input fields
# ----------------------
repo_url = st.text_input("🔗 Enter GitHub Repository URL:")
user_query = st.text_area(
    "💡 Ask something about this repo:",
    placeholder="e.g., Suggest modernization, detect issues, where to add a new feature, generate architecture diagram..."
)

# ----------------------
# Restrict Non-Code Questions
# ----------------------
def is_repo_related(query: str) -> bool:
    keywords = [
        "repo", "repository", "code", "function", "class", "bug", "issue",
        "modernize", "refactor", "feature", "error", "diagram", "architecture",
        "flow", "logic", "integration", "module", "script"
    ]
    return any(k in query.lower() for k in keywords)

# ----------------------
# Analyze Button
# ----------------------
if st.button("🚀 Analyze Repository"):
    if not repo_url:
        st.warning("⚠️ Please enter a GitHub repo URL before analyzing.")
    elif not user_query.strip():
        st.warning("⚠️ Please enter a question to analyze.")
    elif not is_repo_related(user_query):
        st.error("⚠️ Only repository/code-related questions are allowed. Please rephrase your query.")
    else:
        with st.spinner("⏳ Analyzing repository with Gemini 2.5 Pro..."):
            try:
                # Send to Gemini
                response = model.generate_content(
                    f"""
                    You are analyzing a repository hosted at: {repo_url}.

                    User request: {user_query}.

                    Rules:
                    - Always keep analysis specific to the repository/codebase.
                    - If the user asks for diagrams (architecture/flow), generate an **ASCII diagram** inside markdown code blocks.
                    - Provide structured sections with clear headings (###).
                    - For modernization, suggest languages, frameworks, or practices.
                    - For new features, explain where in the repo they could be integrated.
                    - For errors/issues, include possible error codes and fixes.
                    """
                )
                text = response.text
            except Exception as e:
                st.error(f"❌ Error during analysis: {e}")
                st.stop()

        # ----------------------
        # Display Results
        # ----------------------
        st.success("✅ Analysis Complete!")

        # Split response into sections by "###" headings
        sections = text.split("### ")

        # Display Summary first if available
        for sec in sections:
            if "Summary" in sec or "Concise" in sec:
                st.subheader("📌 Summary")
                st.info(sec.replace("Summary", "").replace("Concise", "").strip())

        # Display remaining sections in Expanders
        for sec in sections:
            if not sec.strip():
                continue
            lines = sec.split("\n", 1)
            header = lines[0].strip()
            content = lines[1] if len(lines) > 1 else ""
            if "Summary" not in header and "Concise" not in header:
                with st.expander(f"📂 {header}"):
                    st.markdown(content, unsafe_allow_html=True)

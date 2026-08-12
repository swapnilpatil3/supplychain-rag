import streamlit as st
import os
from ingest import ingest_pdfs
from rag import query_rag

st.set_page_config(page_title="Supply Chain RAG", page_icon="📦", layout="wide")

# Custom CSS for a premium look
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    /* Headers */
    h1, h2, h3 {
        color: #00d2ff !important;
        font-family: 'Inter', sans-serif;
    }
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #1a1c24;
        border-right: 1px solid #2e303e;
    }
    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 210, 255, 0.3);
    }
    /* Text Input */
    .stTextInput>div>div>input {
        border-radius: 8px;
        border: 1px solid #3a7bd5;
        background-color: #262730;
        color: white;
    }
    /* Source badges */
    .source-badge {
        background-color: #2e303e;
        color: #00d2ff;
        padding: 4px 12px;
        border-radius: 16px;
        font-size: 0.85rem;
        display: inline-block;
        margin-right: 8px;
        margin-bottom: 8px;
        border: 1px solid #00d2ff;
    }
</style>
""", unsafe_allow_html=True)

st.title("📦 Meridian Supply Chain Assistant")
st.markdown("*An intelligent RAG system powered by Meta Llama-3 & FastEmbed*")
st.divider()

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2830/2830305.png", width=80)
    st.header("📄 Knowledge Base")
    st.markdown("Upload your Meridian Supply Chain policy documents here.")
    
    uploaded_files = st.file_uploader("Drag and drop PDFs", type=["pdf"], accept_multiple_files=True)
    
    if st.button("⚡ Index Documents", use_container_width=True):
        if uploaded_files:
            if not os.environ.get("GROQ_API_KEY"):
                st.error("⚠️ GROQ_API_KEY not found in .env file.")
            else:
                os.makedirs("temp_uploads", exist_ok=True)
                file_paths = []
                for file in uploaded_files:
                    file_path = os.path.join("temp_uploads", file.name)
                    with open(file_path, "wb") as f:
                        f.write(file.getvalue())
                    file_paths.append(file_path)
                
                with st.spinner("🧠 Processing and vectorizing documents..."):
                    files_processed, chunks_stored = ingest_pdfs(file_paths)
                st.success(f"✅ Successfully indexed {files_processed} files ({chunks_stored} chunks)!")
                
                for path in file_paths:
                    os.remove(path)
        else:
            st.warning("Please upload at least one PDF first.")

st.header("💬 Ask a Question")
question = st.text_input("What would you like to know about the supply chain policies?", placeholder="e.g., What penalty applies when a supplier delivers late?")

if st.button("🚀 Submit Question"):
    if not os.environ.get("GROQ_API_KEY"):
        st.error("⚠️ Please set the GROQ_API_KEY in the .env file.")
    elif question:
        with st.spinner("🤖 Analyzing policies..."):
            answer, sources = query_rag(question, top_k=5)
            
            st.markdown("### Answer")
            st.info(answer)
            
            st.markdown("### 📚 Sources Referenced")
            source_html = ""
            for source in sources:
                source_html += f'<span class="source-badge">📄 {source["file"]} (Page {source["page"]})</span>'
            st.markdown(source_html, unsafe_allow_html=True)
    else:
        st.warning("Please enter a question to search.")

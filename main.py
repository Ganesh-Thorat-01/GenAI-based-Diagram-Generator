import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import re
import io
from io import BytesIO
import streamlit as st
import json

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

token=os.environ["TOKEN"]
endpoint=os.environ["ENDPOINT"]
model_name=os.environ["MODEL_NAME"]

buffer = BytesIO()

#os.environ["PATH"] += os.pathsep + 'C:\\Users\\hp\\Downloads\\windows_10_cmake_Release_Graphviz-12.2.1-win64\\Graphviz-12.2.1-win64\\bin\\'

def get_response(question):
    prompt=f"""
    You are technical architect. You will be provided user query with project details read it carefully.
    Provide the python code to create diagram using diagrams library (diagrams 0.24.1).
    Diagram name should always be "diagram".
    Strictly Response should be in form of following format ```python\n(code)\n```.
    graph_attr = 
        "dpi": "300",            # High resolution
        "bgcolor": "transparent" # Transparent background
    
    node_attr = 
        "fontname": "Arial",     # Use a clean font
        "fontsize": "12"
    show=False

    Project Details: {question}\n\n
    """
    
    response = llm.invoke(prompt).content
    return(response)

def correct_code(question,code,e):
    
    prompt=f"""
    You will be provided user question, generated code and error message.
    You need to correct the code and provide the correct code.
    Don't change the code structure, just correct the code.
    Diagram name should always be "diagram".
    Strictly response should always be in form of following format ```python\n(code)\n```.

    question: {question}\n
    error: {e}\n\n
    code: {code}\n\n

    Corrected Code in following format: ```python\n(code)\n```
""" 
    
    response = llm.invoke(prompt).content
    code=re.search(r'```python\n(.*)\n```', response, re.DOTALL).group(1)
    return(code)

def execute_code(code,question):
    try:
        exec(code)
    except Exception as e:
        status.update(label="Error in diagram, correcting the diagram...", state="running", expanded=False)
        code=correct_code(question,code,e)
        execute_code(code,question)

    

st.set_page_config(page_title="Diagrams Generator", page_icon=r"logo.png", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.header(":violet[ChatBot] -  :blue[GenAI based] :orange[Diagrams Generator]",divider='rainbow', help = "This bot is designed by Ganesh Thorat to generate diagrams for cloud projects using GenAI")
st.subheader("Hello! There, How can I help you Today- 👩‍💻")
st.caption(":violet[Describe] :orange[your] :violet[cloud] :violet[project] :blue[ᓚᘏᗢ]")

with st.sidebar:
    with open("config.json") as file:
        config = json.load(file)
    
    models=st.selectbox("Select Model",
                        tuple(config["Models"]))
    if "gemini" in models:
        llm = ChatGoogleGenerativeAI(model=models, temperature=0.3)
    elif models=="gpt-4o":
        llm = ChatOpenAI(
            model=models,
            base_url=endpoint,
            api_key=token,
            max_retries=3
        )
    elif models=="gpt-4o-mini":
        llm = ChatOpenAI(
            model=models,
            base_url=endpoint,
            api_key=token,
            max_retries=3
        )
        
    st.markdown("### 📚 **Examples**")
    
    for example in config["Examples"]:
        st.code(example, language="text",wrap_lines=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant" and isinstance(message["content"], io.BytesIO):
            st.image(message["content"], caption="Project Diagram")
        else:
            st.write(message["content"])

question = st.chat_input("Enter the project details")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    
    with st.chat_message("user"):
        st.write(question)
    try:
        with st.status("Generating Diagram...",expanded=False) as status:
            response = get_response(question)    
            code=re.search(r'```python\n(.*)\n```', response, re.DOTALL).group(1)
            execute_code(code,question)
            
            status.update(label="Diagram Generated Successfully!", state="complete", expanded=False)
            diag_path = "diagram.png"  # Generated file path
            with open(diag_path, "rb") as diagram_file:
                buffer.write(diagram_file.read())

            os.remove(diag_path)
            buffer.seek(0)

        with st.chat_message("assistant"):
            st.image(buffer, caption="Project Diagram")

        st.session_state.messages.append({"role": "assistant", "content": buffer})
    
    except Exception as e:
        status.update(label="Some Error Occured!", state="error", expanded=False)
        msg="Internal server error, please try again."
        print(type(e))
        print(e)
        if "RateLimitReached" in str(e) or "Resource has been exhausted" in str(e):
            msg=f"Resource exhausted for model {models}, please try different model."
        st.markdown(msg)
        st.session_state.messages.append({"role": "assistant", "content": msg})
    
# GenAI Diagrams Generator

## Overview
The GenAI Diagrams Generator is a Streamlit-based application that leverages Google Generative AI, OpenAI, and LangChain to generate architecture diagrams for cloud projects. The tool takes user-provided project details, generates Python code using the Diagrams library, and outputs a high-quality architecture diagram.

## Features
- **Interactive Chat Interface**: Users can interact with the chatbot to describe their project requirements.
- **AI-Powered Diagram Generation**: Generates architecture diagrams using generative AI and the `diagrams` Python library.
- **Error Correction**: Automatically corrects errors in the generated code.
- **Multiple AI Models**: Supports different AI models, including Gemini and GPT-based models from OpenAI.
- **Configurable and Extensible**: Easily add or modify models and examples via configuration files.

## Requirements
- Python 3.8+
- Dependencies listed in `requirements.txt`:
  - `streamlit`
  - `google-generativeai`
  - `langchain`
  - `langchain-community`
  - `langchain_google_genai`
  - `langchain-openai`
  - `beautifulsoup4`
  - `python-dotenv`
  - `diagrams`
  - `graphviz`

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables by creating a `.env` file:
   ```
   GOOGLE_API_KEY=<your-google-api-key>
   TOKEN=<your-api-token>
   ENDPOINT=<your-endpoint-url>
   MODEL_NAME=<default-model-name>
   OPENAI_API_KEY=<your-openai-api-key>
   ```
4. Ensure `Graphviz` is installed and available in your PATH. Update the PATH variable in `main.py` if necessary.

## Usage
1. Start the application:
   ```bash
   streamlit run main.py
   ```
2. Open the application in your web browser and interact with the chatbot.
3. Describe your project details and receive the generated diagram as a response.

## Project Workflow
1. **Input Project Details**: Users provide project descriptions through the chatbot.
2. **Generate Code**: The AI generates Python code based on project details using the `diagrams` library.
3. **Error Handling**: Any errors in the generated code are automatically corrected.
4. **Execute Code**: The corrected code is executed to produce the architecture diagram.
5. **Display Diagram**: The generated diagram is displayed in the chat interface.

## Files and Directories
- `main.py`: Main application file containing the Streamlit interface and core logic.
- `config.json`: Configuration file for AI models and example prompts.
- `diagram.png`: Temporary file to store generated diagrams.
- `.env`: Environment variables for API keys and configurations.

## Configuration
The application supports configuration through the `config.json` file:
```json
{
  "Models": ["gemini-1.5-pro", "gemini-1.5-pro-exp-0827", "gemini-1.5-flash", "gemini-1.5-flash-8b", "gpt-4o", "gpt-4o-mini"],
  "Examples": [
    "Deploy a web application using AWS services with high availability, scalability, and fault tolerance.",
    "Design a machine learning pipeline for training and deploying a predictive model on AWS.",
    "Design a machine learning pipeline for training and deploying a predictive model on Azure."
  ]
}
```
- **Models**: List of supported AI models from Google and OpenAI.
- **Examples**: Example prompts displayed in the sidebar.

## Diagram Generation Details
- The application uses the `diagrams` library (version 0.24.1) to create architecture diagrams.
- Diagrams are configured with the following attributes:
  - High resolution (`dpi: 300`)
  - Transparent background
  - Clean font (Arial, size 12)
- The name of the generated diagram is always `diagram.png`.

## Error Correction
If the generated code encounters an error during execution:
1. The error message is analyzed by the AI.
2. The AI provides a corrected version of the code.
3. The corrected code is executed to regenerate the diagram.

## 📷 Screenshot 
Here’s a peek at the app:

![App Screenshot](assets/Screenshot%202024-12-25%20at%2020-41-30%20Diagrams%20Generator.png)

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- Developed by Ganesh Thorat.
- Powered by Google Generative AI, OpenAI, LangChain, and the `diagrams` library.

## Contact
For any queries or issues, please contact:
- **Developer**: Ganesh Thorat
- **Email**: [thorat.ganeshscoe@gmail.com]

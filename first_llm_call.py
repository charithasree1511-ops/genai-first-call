from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("API key is missing. Check your .env file.")

# Create OpenAI client
client = OpenAI(api_key=api_key)

# Send a prompt to the AI model
response = client.responses.create(
    model="gpt-5.5",
    input="Explain Generative AI in simple terms in three bullet points."
)

# Display the generated answer
print(response.output_text)
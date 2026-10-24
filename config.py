import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"
OUTPUTS_DIR = BASE_DIR / "outputs"
OUTPUTS_DIR.mkdir(exist_ok=True)

# Load environment variables
load_dotenv(ENV_FILE)

DEFAULT_OPENAI_KEY = os.getenv("OPENAI_API_KEY", "")
DEFAULT_GEMINI_KEY = os.getenv("GEMINI_API_KEY", "")
DEFAULT_GROQ_KEY = os.getenv("GROQ_API_KEY", "")
DEFAULT_PROVIDER = os.getenv("DEFAULT_PROVIDER", "gemini")

def save_config(openai_key: str = None, gemini_key: str = None, groq_key: str = None, provider: str = None):
    """Save API keys and settings to .env file"""
    current_keys = {}
    
    if ENV_FILE.exists():
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    current_keys[k.strip()] = v.strip()
    
    if openai_key is not None:
        current_keys["OPENAI_API_KEY"] = openai_key
    if gemini_key is not None:
        current_keys["GEMINI_API_KEY"] = gemini_key
    if groq_key is not None:
        current_keys["GROQ_API_KEY"] = groq_key
    if provider is not None:
        current_keys["DEFAULT_PROVIDER"] = provider
        
    with open(ENV_FILE, "w", encoding="utf-8") as f:
        for k, v in current_keys.items():
            f.write(f"{k}={v}\n")
            
    # Reload environment
    load_dotenv(ENV_FILE, override=True)

import uvicorn
import os
import sys

# Add current directory to PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    uvicorn.run("packages.gateway_api.main:app", host="127.0.0.1", port=8000, reload=True)

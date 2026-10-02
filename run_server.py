"""
Server Launcher for Care Chronicle Outpatient Oncology Assistant.
"""

import socket
import uvicorn
import os
import sys

# Ensure project root is on sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

def is_port_in_use(port: int, host: str = "127.0.0.1") -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex((host, port)) == 0

if __name__ == "__main__":
    target_port = 8000
    if is_port_in_use(target_port):
        print(f"[Notice] Port {target_port} is currently in use. Selecting available port 8050.")
        target_port = 8050

    print("=" * 68)
    print("  CARE CHRONICLE • OUTPATIENT ASSISTIVE ONCOLOGY SYSTEM")
    print("  Non-Diagnostic Assistive Tool • 100% Synthetic Records")
    print("  Backend: Python FastAPI & LangGraph / LangChain")
    print(f"  Access Dashboard at: http://127.0.0.1:{target_port}")
    print("=" * 68)

    uvicorn.run("app.main:app", host="127.0.0.1", port=target_port, reload=False, log_level="info")

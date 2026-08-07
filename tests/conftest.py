import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

os.environ.setdefault("LAST_FM_API", "test_api_key")
os.environ.setdefault("LAST_FM_API_SECRET", "test_api_secret")
os.environ.setdefault("LASTFM_SESSION", "test_session")

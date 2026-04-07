import subprocess
import sys

def test_app():
    result = subprocess.run(
        [sys.executable, "app.py"],
        input="Elena\n",
        text=True,
        capture_output=True
    )

    assert "Elena" in result.stdout
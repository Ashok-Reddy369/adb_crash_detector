<<<<<<< HEAD
#  ADB App Crash Detector

**Automated Android app crash detection using pytest + pure-python-adb**

[![pytest](https://github.com/pytest-dev/pytest/workflows/tests/badge.svg)](https://github.com/pytest-dev/pytest)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

##  Features

-  **Monkey stress testing** (1000-10K events)
-  **Real-time crash detection** (FATAL EXCEPTION)
-  **Logcat parsing** + tombstone extraction
-  **pytest markers** (`crash`, `stress`, `device`)
-  **Production logging** + HTML reports
-  **ADB automation** (USB/WiFi devices)

##  Quick Start

```bash
# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Test connection
pytest -m device -v -s

# Run crash tests (phone connected!)
pytest tests/test_crash.py::test_monkey_crash_test -v -s


## 🚀 Quick Start

```bash
# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Test connection
pytest -m device -v -s

# Run crash tests (phone connected!)
pytest tests/test_crash.py::test_monkey_crash_test -v -s

#Test Commands

# Quick test (1000 events)
pytest -m crash -v -s

# Heavy stress (5000 events)  
pytest -m stress -v -s

# Full suite (needs device)
pytest -m device -v -s

#stable test
pytest tests/test_crash.py::TestAppCrashDetection::test_monkey_crash_detection -v -s

#buggy test
pytest tests/test_crash.py::test_monkey_crash_test -s --package=com.android.settings


=======
# adb_crash_detector
Automate the real time Crash detection and generate Reports in both text and HTML format.
>>>>>>> 179e12c053aa4e564c4e08b06199ea8e8314f552

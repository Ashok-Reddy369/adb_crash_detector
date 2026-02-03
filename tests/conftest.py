import pytest
import subprocess
import logging
from src.crash_detector import CrashDetector

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def device_info():
    """
    Ensure at least one Android device is connected.
    """
    try:
        output = subprocess.check_output(
            ["adb", "devices"],
            stderr=subprocess.STDOUT
        ).decode()
    except Exception as e:
        pytest.exit(f"ADB not available: {e}")

    devices = [l for l in output.splitlines() if "\tdevice" in l]
    if not devices:
        pytest.exit(" No Android device connected")

    serial = devices[0].split("\t")[0]
    logger.info(f" Using device: {serial}")

    return {"serial": serial}


@pytest.fixture(scope="session")
def crash_detector(device_info):
    """
    Shared CrashDetector instance.
    """
    return CrashDetector(serial=device_info["serial"])

import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        report.extra = getattr(report, "extra", [])

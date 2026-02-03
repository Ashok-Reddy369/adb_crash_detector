import logging
import subprocess
from datetime import datetime

logger = logging.getLogger(__name__)

class CrashDetector:
    def __init__(self, serial=None):
        self.serial = serial

    def _adb_cmd(self, cmd):
        base = ["adb"]
        if self.serial:
            base += ["-s", self.serial]
        return subprocess.check_output(
            base + cmd,
            stderr=subprocess.STDOUT
        ).decode(errors="ignore")

    def detect(self, package_name):
        """
        Detect crashes for a given package using
        Android crash buffer + activity manager
        """
        logger.info(f"🔍 Checking crash status for {package_name}")

        crash_buffer = self._adb_cmd(["logcat", "-b", "crash", "-d"])
        if package_name in crash_buffer:
            logger.warning("💥 Crash detected in crash buffer")
            return self._build_result(
                package_name, "crash_buffer", crash_buffer
            )

        activity_crashes = self._adb_cmd(
            ["shell", "dumpsys", "activity", "crashes"]
        )
        if package_name in activity_crashes:
            logger.warning("💥 Crash detected in ActivityManager")
            return self._build_result(
                package_name, "activity_manager", activity_crashes
            )

        logger.info("✅ No crash detected")
        return {
            "package": package_name,
            "crash_found": False,
            "source": None,
            "timestamp": datetime.now().isoformat(),
            "details": ""
        }

    def _build_result(self, package, source, details):
        return {
            "package": package,
            "crash_found": True,
            "source": source,
            "timestamp": datetime.now().isoformat(),
            "details": details
        }

import subprocess
import logging
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


class LogCollector:
    """
    Collects Android crash-related logs safely.
    """

    def __init__(self, log_dir="adb_logs", serial=None):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        self.serial = serial

    def _adb_cmd(self, cmd):
        base = ["adb"]
        if self.serial:
            base += ["-s", self.serial]

        try:
            output = subprocess.check_output(
                base + cmd,
                stderr=subprocess.STDOUT,
                timeout=10
            )
            return output.decode(errors="ignore")
        except Exception as e:
            logger.error(f"ADB command failed: {e}")
            return ""

    def collect_crash_buffer(self):
        """
        Collect Android crash buffer (logcat -b crash)
        """
        logger.info("📥 Collecting crash buffer logs")

        output = self._adb_cmd(["logcat", "-b", "crash", "-d"])
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = self.log_dir / f"crash_buffer_{ts}.txt"

        with open(file_path, "w") as f:
            f.write(output)

        return file_path, output

    def collect_activity_crashes(self):
        """
        Collect ActivityManager crash history
        """
        logger.info("📥 Collecting activity crash history")

        output = self._adb_cmd(
            ["shell", "dumpsys", "activity", "crashes"]
        )
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = self.log_dir / f"activity_crashes_{ts}.txt"

        with open(file_path, "w") as f:
            f.write(output)

        return file_path, output

from datetime import datetime
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class CrashReportCollector:
    def __init__(self, report_dir="reports/text_reports"):
        self.report_dir = Path(report_dir)
        self.report_dir.mkdir(parents=True, exist_ok=True)

    def generate(self, package_name, crash_result, device_serial):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = self.report_dir / f"app_crash_report_{ts}.txt"

        with open(report_file, "w") as f:
            f.write("APPLICATION CRASH DETECTION REPORT\n")
            f.write("=" * 45 + "\n")
            f.write(f"Device Serial : {device_serial}\n")
            f.write(f"Package       : {package_name}\n")
            f.write(f"Crash Found   : {crash_result['crash_found']}\n")
            f.write(f"Source        : {crash_result.get('source')}\n")

        return report_file

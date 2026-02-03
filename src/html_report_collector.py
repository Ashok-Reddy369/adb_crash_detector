import pytest
from datetime import datetime


class HTMLReportCollector:
    """
    Attaches crash details to pytest-html report.
    """

    @staticmethod
    def attach_crash_info(package, crash_result):
        if not hasattr(pytest, "html"):
            return

        extras = []

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        summary = (
            f"Package   : {package}\n"
            f"Timestamp : {timestamp}\n"
            f"Crash     : {crash_result['crash_found']}\n"
            f"Source    : {crash_result.get('source')}\n"
        )

        extras.append(pytest.html.extras.text(summary, name="Crash Summary"))

        if crash_result["crash_found"]:
            extras.append(
                pytest.html.extras.text(
                    crash_result.get("details", "No details"),
                    name="Crash Details"
                )
            )

        return extras

import pytest

from src.config import STABLE_PACKAGES, BUGGY_PACKAGES
from src.report_collector import CrashReportCollector
from src.html_report_collector import HTMLReportCollector


@pytest.mark.device
def test_settings_app_stability(crash_detector, request):
    package = STABLE_PACKAGES["settings"]

    result = crash_detector.detect(package)

    # HTML report attachment (HTMLReportCollector ONLY)
    extras = HTMLReportCollector.attach_crash_info(package, result)
    if extras:
        request.node.extra = extras

    assert not result["crash_found"], "Settings app crashed unexpectedly"


@pytest.mark.device
def test_systemui_crash_detection(crash_detector, device_info, request):
    package = BUGGY_PACKAGES["systemui"]

    result = crash_detector.detect(package)

    # TEXT report (CrashReportCollector ONLY)
    text_report = CrashReportCollector(report_dir="reports/text_reports")
    text_report.generate(
        package_name=package,
        crash_result=result,
        device_serial=device_info["serial"]
    )

    # HTML report attachment
    extras = HTMLReportCollector.attach_crash_info(package, result)
    if extras:
        request.node.extra = extras

    assert not result["crash_found"], "SystemUI crash detected"

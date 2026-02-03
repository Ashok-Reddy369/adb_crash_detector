# src/config.py

STABLE_PACKAGES = {
    "settings": "com.android.settings",
}

BUGGY_PACKAGES = {
    "systemui": "com.android.systemui",
}

ALL_PACKAGES = {
    **STABLE_PACKAGES,
    **BUGGY_PACKAGES,
}

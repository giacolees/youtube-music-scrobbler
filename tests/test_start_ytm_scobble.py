import start_ytm_scobble as s
from zoneinfo import ZoneInfo


def test_default_timezone():
    tz = s.get_scrobble_timezone()
    assert tz == ZoneInfo("Asia/Kolkata")


def test_custom_timezone(monkeypatch):
    monkeypatch.setenv("SCROBBLE_TIMEZONE", "America/New_York")
    assert s.get_scrobble_timezone() == ZoneInfo("America/New_York")


def test_invalid_timezone_falls_back(monkeypatch):
    monkeypatch.setenv("SCROBBLE_TIMEZONE", "Not/AZone")
    assert s.get_scrobble_timezone() == ZoneInfo("Asia/Kolkata")


def test_empty_timezone_falls_back(monkeypatch):
    monkeypatch.setenv("SCROBBLE_TIMEZONE", "   ")
    assert s.get_scrobble_timezone() == ZoneInfo("Asia/Kolkata")


def test_get_scrobble_now_is_tz_aware(monkeypatch):
    monkeypatch.setenv("SCROBBLE_TIMEZONE", "Asia/Kolkata")
    now = s.get_scrobble_now()
    assert now.tzinfo is not None
    assert now.utcoffset() == ZoneInfo("Asia/Kolkata").utcoffset(now)


class TestRemovedReportHelpers:
    """Regression tests for the current change: report metric helpers removed."""

    def test_removed_functions_and_constant(self):
        for name in (
            "compute_listening_flow",
            "_bucket_for_hour",
            "compute_most_played_artist",
            "compute_longest_streak",
            "AVG_TRACK_MINUTES",
        ):
            assert not hasattr(s, name), f"{name} should have been removed"

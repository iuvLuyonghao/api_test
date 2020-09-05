
import pytest


class _Tags:
    smoke = pytest.mark.smoke(help="冒烟测试，用于线上监控")
    p1 = pytest.mark.p1


tag = _Tags

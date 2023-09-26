import pytest
from pytest_assume.plugin import assume


class TestAssert:
    def test_assert(self):
        # 第一种
        with assume: assert "tom" in "hahahahah"
        # 第二种 即使断言失败也会继续执行
        pytest.assume(1 + 1 == 3)
        # 第三种
        assert "william" == "william"
        assert "william" != "william-b"
        assert 0 < 1
        assert 2 > 1
        assert 3 <= 7 - 2
        assert 4 >= 1 + 2
        assert "william" in "william UI 自动化测试"
        assert "mike" not in "hshadasdasd"
        assert 1
        assert (9 < 10) is True

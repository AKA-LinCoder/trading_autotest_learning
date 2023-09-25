class TestAssert:
    def test_assert(self):
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

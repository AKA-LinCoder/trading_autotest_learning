import random
import pytest

class TestRerun:
    @pytest.mark.flaky(reruns=5, reruns_delay=1)
    def test_rerun(self):
        num = random.randint(1, 3)
        print("num:", num)
        if num != 1:
            print("not 1")
            raise Exception("wrong")
        else:
            print("right")

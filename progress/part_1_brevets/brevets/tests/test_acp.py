from acp_times

import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def test_closing():
    test_time = arrow.Arrow(2017,1,1)
	assert acp_times.close_time(100, 200, arrow.get(test_time)) == (test_time.shift(hours=6,minutes=40)).isoformat()
    assert acp_times.close_time(100, 300, arrow.get(test_time)) == (test_time.shift(hours=6,minutes=40)).isoformat()
    assert acp_times.close_time(100, 400, arrow.get(test_time)) == (test_time.shift(hours=6,minutes=40)).isoformat()
    assert acp_times.close_time(100, 600, arrow.get(test_time)) != (test_time.shift(hours=0,minutes=0)).isoformat()

def test_opening():
    test_time = arrow.Arrow(2017,1,1)
    assert acp_times.open_time(100, 200, arrow.get(test_time)) == (test_time.shift(hours=2,minutes=56)).isoformat()
    assert acp_times.open_time(100, 300, arrow.get(test_time)) == (test_time.shift(hours=2,minutes=56)).isoformat()
    assert acp_times.open_time(100, 400, arrow.get(test_time)) == (test_time.shift(hours=2,minutes=56)).isoformat()
    assert acp_times.open_time(100, 600, arrow.get(test_time)) != (test_time.shift(hours=0,minutes=0)).isoformat()

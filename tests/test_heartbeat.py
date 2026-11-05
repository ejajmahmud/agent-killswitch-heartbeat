"""Tests for agent-killswitch-heartbeat."""
import unittest
import time
from agent_killswitch_heartbeat.heartbeat import KillswitchHeartbeat


class TestKillswitchHeartbeat(unittest.TestCase):
    def test_heartbeat_trip(self):
        hb = KillswitchHeartbeat(ttl_seconds=0.1)
        self.assertTrue(hb.check_alive())
        time.sleep(0.15)
        self.assertFalse(hb.check_alive())
        self.assertTrue(hb.is_tripped)


if __name__ == "__main__":
    unittest.main()

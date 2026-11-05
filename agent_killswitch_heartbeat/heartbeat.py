"""Dead man's switch and heartbeat monitor for autonomous agents."""
import time
from typing import Dict, Any, Optional, Callable


class KillswitchHeartbeat:
    def __init__(self, ttl_seconds: float = 30.0, on_terminate: Optional[Callable[[], None]] = None):
        self.ttl = ttl_seconds
        self.on_terminate = on_terminate
        self.last_ping = time.time()
        self.is_tripped = False

    def ping(self):
        if not self.is_tripped:
            self.last_ping = time.time()

    def check_alive(self) -> bool:
        if self.is_tripped:
            return False
        if time.time() - self.last_ping > self.ttl:
            self.trip()
            return False
        return True

    def trip(self):
        self.is_tripped = True
        if self.on_terminate:
            try:
                self.on_terminate()
            except Exception:
                pass

    def get_status(self) -> Dict[str, Any]:
        elapsed = time.time() - self.last_ping
        return {
            "is_tripped": self.is_tripped,
            "seconds_since_last_ping": round(elapsed, 2),
            "ttl": self.ttl,
            "seconds_remaining": max(0.0, round(self.ttl - elapsed, 2))
        }

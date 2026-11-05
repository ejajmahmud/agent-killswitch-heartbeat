"""CLI for agent-killswitch-heartbeat."""
import sys
import argparse
from .heartbeat import KillswitchHeartbeat


def main():
    parser = argparse.ArgumentParser(description="Agent Killswitch Heartbeat")
    parser.add_argument("--demo", action="store_true", help="Run heartbeat monitor demonstration")
    args = parser.parse_args()

    heartbeat = KillswitchHeartbeat(ttl_seconds=1.0)
    if args.demo:
        print("Initial status:", heartbeat.get_status())
        print("Checking alive:", heartbeat.check_alive())
        print("Simulating heartbeat expiration...")
        heartbeat.last_ping = time.time() - 2.0
        print("Checking alive after timeout:", heartbeat.check_alive())
        print("Status after timeout:", heartbeat.get_status())
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()

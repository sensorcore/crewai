#!/usr/bin/env python
"""SensorCore Analytics Crew — entry point.

Usage:
    # Run the full analytics crew
    crewai run

    # Or run directly
    python -m sensorcore_crew.main
"""

import sys

from sensorcore_crew.crew import SensorCoreCrew


def run():
    """Run the SensorCore Analytics crew."""
    try:
        result = SensorCoreCrew().crew().kickoff()
        print("\n✅  Analysis complete! Report saved to report.md")
        return result
    except Exception as e:
        print(f"\n❌  Error: {e}", file=sys.stderr)
        raise SystemExit(1) from e


if __name__ == "__main__":
    run()

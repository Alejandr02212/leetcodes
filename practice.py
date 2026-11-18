#!/usr/bin/env python3
"""Run local checks for one attempt, track progress, or audit reference solutions."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import runpy
import sys
import traceback
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
PROGRESS = ROOT / '.progress.json'


def load_progress() -> dict:
    if not PROGRESS.exists():
        return {}
    try:
        value = json.loads(PROGRESS.read_text())
        if not isinstance(value, dict):
            raise ValueError('progress must be an object')
        return value
    except (OSError, ValueError) as error:
        raise SystemExit(f'Could not read {PROGRESS.name}: {error}. Rename it to keep a backup and start fresh.') from error


def check(entry: dict, solution: bool) -> bool:
    path = ROOT / entry['solution' if solution else 'problem']
    label = f"{entry['id']:03d} {entry['title']}"
    try:
        namespace = runpy.run_path(str(path))
        namespace['run_tests']()
    except NotImplementedError:
        print(f'YOUR TURN: {label}\nOpen {path.relative_to(ROOT)} and implement solve.\nThen run: python3 practice.py {entry["id"]}')
        return False
    except Exception:
        print(f'CHECK FAILED: {label}', file=sys.stderr)
        traceback.print_exc()
        return False
    print(f'PASS: {label}' + (' [reference solution]' if solution else ' [your attempt]'))
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, epilog='Examples: python3 practice.py 1 | python3 practice.py 1 --solution | python3 practice.py --next')
    parser.add_argument('number', type=int, nargs='?', help='exercise number, 1–100')
    parser.add_argument('--solution', action='store_true', help='check the explained reference implementation of this number')
    parser.add_argument('--all-solutions', action='store_true', help='check all 100 reference solutions without changing progress')
    parser.add_argument('--list', action='store_true', help='list exercises, patterns, and checked attempts')
    parser.add_argument('--progress', action='store_true', help='show how many of your attempts passed local checks')
    parser.add_argument('--next', action='store_true', help='show the next exercise without a recorded pass')
    args = parser.parse_args()
    if not __debug__:
        parser.error('run Python without -O or -OO; these exercises use assert checks')
    modes = sum([args.number is not None, args.all_solutions, args.list, args.progress, args.next])
    if modes != 1:
        parser.error('choose one exercise number or one of --all-solutions, --list, --progress, --next')
    if args.solution and args.number is None:
        parser.error('--solution needs an exercise number')
    curriculum = json.loads((ROOT / 'curriculum.json').read_text())
    if args.all_solutions:
        passed = sum(check(entry, True) for entry in curriculum)
        print(f'\nReference checks: {passed}/{len(curriculum)} passed.')
        return 0 if passed == len(curriculum) else 1
    progress = load_progress()
    if args.list:
        for entry in curriculum:
            marker = 'x' if str(entry['id']) in progress else ' '
            print(f"[{marker}] {entry['id']:03d} {entry['title']} ({entry['difficulty']}) — {entry['pattern']}")
        return 0
    if args.progress:
        print(f'{sum(str(e["id"]) in progress for e in curriculum)}/100 attempts have passed local checks.')
        print('A pass records a practice milestone. Re-solve later and explain correctness to build mastery.')
        return 0
    if args.next:
        entry = next((e for e in curriculum if str(e['id']) not in progress), None)
        if entry is None:
            print('All 100 attempts have a recorded pass. Pick a pattern to revisit without notes.')
        else:
            print(f"Next: {entry['id']:03d} {entry['title']}\nOpen: {ROOT / entry['problem']}\nCheck: python3 practice.py {entry['id']}")
        return 0
    if not 1 <= args.number <= 100:
        parser.error('exercise number must be between 1 and 100')
    entry = curriculum[args.number - 1]
    passed = check(entry, args.solution)
    if passed and not args.solution:
        progress[str(args.number)] = datetime.now(timezone.utc).isoformat()
        temporary = PROGRESS.with_suffix('.tmp')
        temporary.write_text(json.dumps(progress, indent=2) + '\n')
        temporary.replace(PROGRESS)
        print('Practice milestone saved. Explain the approach, then try it again tomorrow.')
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())

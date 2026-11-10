"""Week 7 record check: Cyber Security lane, Excellent tier."""
from pathlib import Path


def parse_line(raw_line):
    """Clean a source-IP, attempts and result record."""
    data = {}
    for part in raw_line.strip().split(','):
        key, value = part.split('=', 1)
        data[key.strip().lower()] = value.strip().lower()
    data['attempts'] = int(data['attempts'])
    for key in ('src', 'attempts', 'result'):
        if key not in data:
            raise ValueError(f'Missing field: {key}')
    return data


def status_of(record):
    """Flag failed logins with at least five attempts."""
    return 'FLAGGED' if record['result'] == 'failed' and record['attempts'] >= 5 else 'OK'


def main():
    """Read messy records, report statuses, and count flagged events."""
    path = Path(__file__).with_name('cyber_records.txt')
    processed = flagged = invalid = 0
    for raw in path.read_text().splitlines():
        try:
            record = parse_line(raw)
        except (ValueError, KeyError) as error:
            invalid += 1
            print(f'Could not parse: {raw.strip()} ({error})')
            continue
        processed += 1
        status = status_of(record)
        flagged += status == 'FLAGGED'
        print(f"{record['src']:<16} attempts={record['attempts']:<3} result={record['result']:<8} {status}")
    print(f'Summary: {processed} processed, {flagged} flagged, {invalid} invalid')


if __name__ == '__main__':
    main()

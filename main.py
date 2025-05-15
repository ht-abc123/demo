import os
import random
from datetime import datetime, timedelta

def random_dates(start_date, end_date, n):
    """Generate n unique random dates between start_date and end_date"""
    delta = end_date - start_date
    dates = set()
    while len(dates) < n:
        random_days = random.randint(0, delta.days)
        random_date = start_date + timedelta(days=random_days)
        dates.add(random_date)
    return sorted(dates)

def make_random_commits(num_days):
    start_date = datetime(2024, 9, 1)
    end_date = datetime.today()
    dates = random_dates(start_date, end_date, num_days)

    for date in dates:
        # Randomize commits count from 1 to 7 for each day
        commits_count = random.randint(1, 3)
        for i in range(commits_count):
            # Add some seconds offset so each commit has a unique timestamp on the same day
            commit_time = date + timedelta(seconds=i * 10)
            date_str = commit_time.strftime('%Y-%m-%dT%H:%M:%S')
            with open('data.txt', 'a') as file:
                file.write(f"{date_str}\n")
            os.system('git add data.txt')
            os.system(f'git commit --date="{date_str}" -m "Commit for {date_str}"')

make_random_commits(10)  # 10 different days, each with 1-7 commits randomly
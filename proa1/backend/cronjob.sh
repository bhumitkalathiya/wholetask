#!/bin/bash
cd /path/to/backend
source venv/bin/activate
python scraper.py

# for add to crontab     0 0 * * * /bin/bash /path/to/backend/cronjob.sh


# Cron_tab spotify_etl_job

MAILTO=""
0 0 * * * source /path/to/bash_file.sh/ >> /path/to/logfiles/`date +\%Y-\%m-\%d` -spotify_etl.log 2>&1



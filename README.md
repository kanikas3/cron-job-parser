# cron-job-parser
This repo contains the script which helps expand a cron job into its time schedule. For every time based field it mentions the periods in which the command will be executed. For example:

Job: ```*/15 0 1,15 * 1-5 /usr/bin/find```

Gets expanded to the schedule:

```
minute 0 15 30 45
hour 0
day of month 1 15
month 1 2 3 4 5 6 7 8 9 10 11 12
day of week 1 2 3 4 5
command /usr/bin/find
```

Running the script:

- Input parameters: The script takes in the cron job as the only input paramater
- Output: The expanded schedule of the cron job is outputted on the console
- Log: The logs of the script is logged in the file ```output.log```. The file is stored in the same location where the script is run.
- Command to execute script: ```python main.py <cron_job>```

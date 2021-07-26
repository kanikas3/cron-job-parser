"""
Contains business logic related constant definitions only
"""

cron_job_format = {
    0: "minute",
    1:"hour",
    2: "day of month",
    3: "month",
    4: "day of week",
    5: "command"
}

command_index = 5
day_of_month_index = 2

field_column_length = 14

range_floor = {
    "minute": 0,
    "hour": 1,
    "day of week": 1,
    "day of month": 1,
    "month": 1
}

range_ceiling = {
    "minute": 59,
    "hour": 12,
    "day of week": 7,
    "day of month": 30,
    "month": 12
}

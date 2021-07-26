import argparse
import logging
from logger import setup_logger
from definitions import (cron_job_format, range_ceiling, range_floor,
                         field_column_length, command_index, day_of_month_index)

logger = logging.getLogger(__name__)

#TODO: how to enable month end checking 30 or 31
    

def process_cron_job(cron_job):

    parameter_list = get_valid_parameters(cron_job)
    command_to_execute, time_parameters = prune_command_from_list(parameter_list)    

    output = print_time_parameters(time_parameters)
    output += print_command(command_to_execute)

    print(output)


def get_valid_parameters(cron_job):
    if cron_job == "":
        logger.error("Cron job cannot be empty! Invalid argument passed. Please pass the cron job in valid format")
        raise    
    parameter_list = cron_job.split()
    logger.debug("Parameter list: %s", parameter_list)    
    if len(parameter_list) != len(cron_job_format):
        logger.error("Invalid number of parameters passed in cron job! Please pass the cron job in valid format")
        raise
    return parameter_list


def prune_command_from_list(parameter_list):
    command_to_execute = parameter_list[-1]
    time_parameters = parameter_list[:5]
    return command_to_execute, time_parameters


def print_time_parameters(time_parameters):
    output = ""
    for i in range(len(time_parameters)):
        expanded_value = expand_time_parameter(time_parameters[i], i)
        output += print_time_parameter(expanded_value, i)
    return output


def expand_time_parameter(parameter, index):
    expanded_list= []
    if parameter.find(",") != -1:
        expanded_list = parameter.split(",")
    else:
        interval, parameter = get_interval(parameter)
        lower_limit, higher_limit = get_range(parameter, index)
        expanded_list = expand_range(lower_limit, higher_limit, interval)
    logger.debug("expanded_list %s", expanded_list)
    return expanded_list
    

def get_interval(parameter):
    if parameter.find("/") == -1:
        interval = 1
    else:
        interval = parameter[parameter.find("/") + 1 : ]
        parameter = parameter[ : parameter.find("/")]
        logger.debug("modified parameter %s", parameter)
    logger.debug("interval %s", interval)
    return interval, parameter


def get_range(parameter, index):
    if parameter.find("*") != -1:
        lower_limit = range_floor[cron_job_format[index]]
        higher_limit = range_ceiling[cron_job_format[index]]
    elif parameter.find("-") != -1:
        lower_limit = parameter[ : parameter.find("-")]
        higher_limit = parameter[parameter.find("-") + 1 : ]
    else:
        lower_limit = parameter
        higher_limit = parameter
    logger.debug("lower_limit %s higher_limit %s", lower_limit, higher_limit)
    return lower_limit, higher_limit


def expand_range(lower_limit, higher_limit, interval):
    expanded_list = []
    temp = int(lower_limit)
    while(temp <= int(higher_limit)):
        expanded_list.append(temp)
        temp += int(interval)
    return expanded_list


def print_time_parameter(expanded_list, index):
    line = add_field(cron_job_format[index])    
    for element in expanded_list:
        line += str(element)
        line += " "    
    line += "\n"
    return line


def add_field(field_name):
    line = ""
    line += field_name
    whitespace_size = field_column_length - len(field_name)
    for i in range(whitespace_size):
        line += " "
    return line


def print_command(command):
    line = add_field(cron_job_format[command_index])
    line += command    
    return line


def main():

    setup_logger()
    parser = argparse.ArgumentParser(description="Job to parse and expand cron jobs")
    parser.add_argument("cronjob", metavar="cronjob", type=str, nargs="?",
                        default="", help="cron job to execute")
    args = parser.parse_args()
    logging.info("Cron Job passed: %s", args.cronjob)
    process_cron_job(args.cronjob)

if __name__ == "__main__":
    main()
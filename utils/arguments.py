"""Command line argument utilities."""

import random

from argparse   import (
    ArgumentParser,
    Namespace,
    _ArgumentGroup,
    _SubParsersAction
)

# Initialize primary parser
__parser__:     ArgumentParser =    ArgumentParser(
    "legislature",
    description =   "Nested scheduling policy simulator"
)

# Initialize subparsers
__subparsers__: _SubParsersAction = __parser__.add_subparsers(
    dest =          "cmd",
    help =          "Command to be executed"
)

###################################################################################################
# BEGIN ARGUMENTS                                                                                 #
###################################################################################################

# UNIVERSAL ==============================================================

# LOGGING ---------------------------------------
logging:        _ArgumentGroup =    __parser__.add_argument_group("Logging")

logging.add_argument(
    "--logging_path",
    type =          str,
    default =       "logs",
    help =          "Path at which log files will be written. Defaults to \'./logs/\'."
)

logging.add_argument(
    "--logging_level",
    type =          str,
    choices =       ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    default =       "INFO",
    help =          "Minimum logging level (DEBUG < INFO < WARNING < ERROR < CRITICAL). Defaults to \'INFO\'."
)

# OUTPUT ----------------------------------------
output:         _ArgumentGroup =    __parser__.add_argument_group("Output")

output.add_argument(
    "--output_path",
    type =          str,
    default =       "output",
    help =          "Path at which output files will be written. Defaults to \'./output/\'."
)

# MACHINE ---------------------------------------
machine:        _ArgumentGroup =    __parser__.add_argument_group("Machine")

machine.add_argument(
    "--cores",
    type =          int,
    choices =       [1, 2, 4, 8, 16],
    default =       2 ** random.randint(0, 4),
    help =          "Processor quantity with which the machine is equipped"
)

# JOBS ------------------------------------------
jobs:           _ArgumentGroup =    __parser__.add_argument_group("Jobs")

jobs.add_argument(
    "--job_quantity",
    type =          int,
    default =       random.randint(1, 1000),
    help =          "Quantity of jobs to run on machine"
)

# SCHEDULER -------------------------------------
scheduler:      _ArgumentGroup =    __parser__.add_argument_group(
    "Scheduler",
    description =   (
        "FCFS:    First Come First Server, "
        "RR:      Round Robin, "
        "SPN:     Shortest Process Next, "
        "SRT:     Shortest Remining Time, "
        "HRRN:    Highest Response Ratio Next, "
        "FB:      Feedback"
    )
)

scheduler.add_argument(
    "--primary_policy",
    type =          str,
    choices =       ["fcfs", "rr", "spn", "srt", "hrrn", "fb"],
    default =       "fcfs",
    help =          "Primary scheduling policy. Defaults to FCFS."
)

scheduler.add_argument(
    "--secondary_policy",
    type =          str,
    choices =       ["fcfs", "rr", "spn", "srt", "hrrn", "fb"],
    default =       None,
    help =          "Secondary scheduling policy. Defaults to None."
)

scheduler.add_argument(
    "--tertiary_policy",
    type =          str,
    choices =       ["fcfs", "rr", "spn", "srt", "hrrn", "fb"],
    default =       None,
    help =          "Tertiary scheduling policy. Defaults to None."
)

scheduler.add_argument(
    "--queues",
    type =          int,
    default =       1,
    help =          "Number of queues with which scheduler will be equipped. Defaults to 1."
)

scheduler.add_argument(
    "--job_list",
    type =          int,
    choices =       [1, 2, 3, 4],
    default =       1,
    help =          "CSV file (job_list_{int}.csv) holding list of jobs. Defaults to 1."
)

###################################################################################################
# END ARGUMENTS                                                                                   #
###################################################################################################

ARGS:           Namespace =         __parser__.parse_args()
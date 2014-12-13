#!/bin/env python3
import config
import argparse

class Main:
    def parse_arguments(self):
        argument_parser = argparse.ArgumentParser(
            description = "Update a github constitution using specified hook."
        )

        argument_parser.add_argument(
            "-c", "--config",
            dest = "config_file",
            help = "Specify the location of the configuration file"
        )

        argument_parser.add_argument(
            "-p", "--print-config",
            action = "store_true",
            dest = "print_config",
            help = "Print an empty configuration file"
        )

        argument_parser.add_argument(
            "-e", "--event-hook",
            dest = "hook",
            help = "Specify the JSON data from the github hook."
        )

        return argument_parser.parse_args()

    def __init__(self):

        help(config._config)

        arguments = self.parse_arguments()

        if arguments.print_config:
            print(config.print(config.default_config()))
            return

        if not arguments.config_file:
            print("Must specify configuration file via -c. If no configuration"
                  + " file exists, you can generate a blank one with the -p"
                  + " flag")
            return

        try:
            self.config = config.parse(arguments.config_file)
        except config.BadConfiguration:
            print("Your configuration file is invalid. To generate a new,"
                  + " blank configuration, use the -p flag.")

Main()

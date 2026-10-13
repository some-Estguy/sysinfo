import argparse

# import outputs

from cpu import show_cpu
from memory import show_memory
from storage import show_storage
from system import show_system

# arguments

def parse_args():
    parser = argparse.ArgumentParser(
        prog="sysinfo",
        description="A lightweight Python CLI tool for displaying system information on Linux."
    )

    parser.add_argument(
        "-c", "--convert",
        type=str,
        choices=["B", "KiB", "MiB", "GiB", "TiB", "MB", "GB", "TB"],
        default="GiB",
        help="Choose the memory display unit (default: GiB)"
    )

    parser.add_argument(
        "-s", "--section",
        choices=["CPU", "MEM", "DISK", "SYS"],
        default=None,
        help="Choose a section: CPU, MEM, DISK, or SYS"
    )

    parser.add_argument(
        "-A", "--almost-all",
        action="store_true",
        help="Show all statistics for the selected section"
    )

    parser.add_argument(
        "-a", "--all",
        action="store_true",
        help="Show every statistic from every section"
    )

    args = parser.parse_args()

    if args.almost_all and args.section is None:
        parser.error("--almost-all requires --section")

    if args.all and (args.section is not None or args.almost_all):
        parser.error("--all cannot be combined with --section or --almost-all")

    if args.section is None and not args.all:
        args.section = "SYS"

    return args

# main


def main():
    args = parse_args()

    if args.all:
        show_cpu(all_info=True)
        show_memory(args.convert, all_info=True)
        show_storage(all_info=True)
        show_system(all_info=True)

    elif args.section == "CPU":
        show_cpu(all_info=args.almost_all)

    elif args.section == "MEM":
        show_memory(args.convert, all_info=args.almost_all)

    elif args.section == "DISK":
        show_storage(all_info=args.almost_all)

    elif args.section == "SYS":
        show_system()


if __name__ == "__main__":
    main()
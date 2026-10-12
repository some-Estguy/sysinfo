from pathlib import Path
import argparse


# arguments

def parse_args():
    parser = argparse.ArgumentParser(
        prog="sysinfo",
        description="A lightweight Python CLI tool for displaying system information on Linux."
    )

    parser.add_argument(
        "-c", "--convert",
        type=str,
        help="Convert memory values to B, KiB, MiB, GiB, TiB, MB, GB, or TB",
        choices=["B", "KiB", "MiB", "GiB", "TiB", "MB", "GB", "TB"],
        default="GiB"
    )

    return parser.parse_args()


# helpers

def convert_values(value, size):
    unit_sizes = {
        "B": 1,
        "KiB": 1024,
        "MiB": 1024 ** 2,
        "GiB": 1024 ** 3,
        "TiB": 1024 ** 4,
        "MB": 1000 ** 2,
        "GB": 1000 ** 3,
        "TB": 1000 ** 4
    }

    # /proc/meminfo reports memory in KiB
    value_in_bytes = value * 1024

    return value_in_bytes / unit_sizes[size]


# memory

def main():
    args = parse_args()

    mem_path = Path("/proc/meminfo")
    mem_info = mem_path.read_text().splitlines()

    for line in mem_info:
        if line.startswith("MemTotal:"):
            parts = line.split()
            ram_kib = int(parts[1])

            converted = convert_values(ram_kib, args.convert)

            print(f"Total RAM: {converted:.2f} {args.convert}")
            break


if __name__ == "__main__":
    main()

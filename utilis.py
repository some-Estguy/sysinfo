def convert_values(value, size):
    unit_sizes = {
        "B": 1,
        "KiB": 1024,
        "MiB": 1024 ** 2,
        "GiB": 1024 ** 3,
        "TiB": 1024 ** 4,
        "MB": 1000 ** 2,
        "GB": 1000 ** 3,
        "TB": 1000 ** 4,
    }

    # /proc/meminfo reports memory in KiB.
    value_in_bytes = value * 1024

    return value_in_bytes / unit_sizes[size]
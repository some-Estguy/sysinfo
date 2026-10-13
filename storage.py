from pathlib import Path; import shutil
def show_storage(all_info=False):
    print("=== STORAGE ===")

    if not all_info:
        paths = ["/"]
    else:
        paths = []

        for line in Path("/proc/mounts").read_text().splitlines():
            parts = line.split()

            if len(parts) >= 2:
                mount = (
                    parts[1]
                    .replace("\\040", " ")
                    .replace("\\011", "\t")
                    .replace("\\134", "\\")
                )

                if mount not in paths:
                    paths.append(mount)

    for path in paths:
        try:
            total, used, free = shutil.disk_usage(path)
        except (OSError, PermissionError):
            continue

        gib = 1024 ** 3

        print(f"\nMount: {path}")
        print(f"Total: {total / gib:.2f} GiB")
        print(f"Used:  {used / gib:.2f} GiB")
        print(f"Free:  {free / gib:.2f} GiB")

        if total:
            print(f"Usage: {used / total * 100:.1f}%")

    print()

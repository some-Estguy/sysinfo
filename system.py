import platform; from pathlib import Path; import os

def get_system_info():
    info = {
        "Hostname": platform.node(),
        "Operating system": platform.system(),
        "Kernel release": platform.release(),
        "Kernel version": platform.version(),
        "Architecture": platform.machine(),
        "Processor": platform.processor() or "Unknown",
        "Python version": platform.python_version(),
        "Logical CPUs": os.cpu_count() or 1,
    }

    # Linux distribution information
    os_release = Path("/etc/os-release")

    if os_release.exists():
        for line in os_release.read_text().splitlines():
            if "=" not in line:
                continue

            key, value = line.split("=", 1)

            if key in ("PRETTY_NAME", "VERSION_ID", "ID"):
                info[f"Distribution {key}"] = value.strip('"')

    # System uptime
    uptime_path = Path("/proc/uptime")

    if uptime_path.exists():
        uptime_seconds = int(
            float(uptime_path.read_text().split()[0])
        )

        days, remainder = divmod(uptime_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, _ = divmod(remainder, 60)

        info["Uptime"] = (
            f"{days} days, {hours} hours, {minutes} minutes"
        )

    return info


def show_system(all_info=False):
    info = get_system_info()

    print("=== SYSTEM ===")

    for key, value in info.items():
        print(f"{key}: {value}")

    print()
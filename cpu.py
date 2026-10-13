import os; from pathlib import Path; import platform

def get_cpu_info():
    cpu_path = Path("/proc/cpuinfo")
    text = cpu_path.read_text()

    processors = []

    for block in text.strip().split("\n\n"):
        info = {}

        for line in block.splitlines():
            if ":" not in line:
                continue

            key, value = line.split(":", 1)
            info[key.strip()] = value.strip()

        if info:
            processors.append(info)

    return processors


def show_cpu(all_info=False):
    processors = get_cpu_info()

    if not processors:
        print("No CPU information available.")
        return

    print("=== CPU ===")

    if all_info:
        for index, processor in enumerate(processors):
            print(f"\nProcessor {index}:")

            for key, value in processor.items():
                print(f"  {key}: {value}")

    else:
        cpu = processors[0]

        print(f"Model: {cpu.get('model name', cpu.get('Hardware', 'Unknown'))}")
        print(f"Logical CPUs: {os.cpu_count() or 1}")
        print(f"Architecture: {platform.machine() or 'Unknown'}")

    print()

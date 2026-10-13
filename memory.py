from pathlib import Path; from utilis import convert_values

def show_memory(unit, all_info=False):
    mem_path = Path("/proc/meminfo")
    mem_info = mem_path.read_text().splitlines()

    print("=== MEMORY ===")

    for line in mem_info:
        parts = line.split(":", 1)

        if len(parts) != 2:
            continue

        key, raw_value = parts
        values = raw_value.split()

        if not values:
            continue

        if len(values) > 1 and values[1] == "kB":
            kib = int(values[0])

            if all_info:
                converted = convert_values(kib, unit)
                print(f"{key}: {converted:.2f} {unit}")
            elif key == "MemTotal":
                converted = convert_values(kib, unit)
                print(f"Total RAM: {converted:.2f} {unit}")

        elif all_info:
            print(f"{key}: {' '.join(values)}")

    print()
# sysinfo

A lightweight Python CLI tool for displaying system information on Linux.

`sysinfo` reads system information from Linux system files and Python's standard library. It can display CPU, memory, storage, and general system details.

## Features

- **CPU:** processor model, logical CPU count, architecture, and detailed processor information.
- **Memory:** total RAM with configurable units and additional memory statistics.
- **Storage:** total, used, and free disk space, with usage percentages.
- **System:** hostname, operating system, kernel, architecture, Python version, distribution details, and uptime.
- **Flexible output:** display one section, all statistics for a section, or all sections.

## Requirements

- Linux
- Python 3.9 or newer recommended
- No third-party Python packages required

## Usage

Run the program from the project directory:

```bash
python3 sysinfo.py
```

By default, this displays the system section.

### Select a section

```bash
python3 sysinfo.py --section CPU
python3 sysinfo.py --section MEM
python3 sysinfo.py --section DISK
python3 sysinfo.py --section SYS
```

The short option `-s` can be used instead of `--section`.

### Show all statistics for a section

Use `--almost-all` (`-A`) with a selected section:

```bash
python3 sysinfo.py --section CPU --almost-all
python3 sysinfo.py --section MEM --almost-all
python3 sysinfo.py --section DISK --almost-all
python3 sysinfo.py --section SYS --almost-all
```

### Show every section

```bash
python3 sysinfo.py --all
```

The `--all` (`-a`) option cannot be combined with `--section` or `--almost-all`.

### Choose memory units

Use `--convert` (`-c`) to choose the unit used for memory values:

```bash
python3 sysinfo.py --section MEM --convert MiB
python3 sysinfo.py --section MEM --convert GiB
```

Supported units:

- `B` — bytes
- `KiB`, `MiB`, `GiB`, `TiB` — binary units
- `MB`, `GB`, `TB` — decimal units

The default unit is `GiB`.

## Project structure

```text
sysinfo/
├── sysinfo.py
├── cpu.py
├── memory.py
├── storage.py
├── system.py
├── utils.py
└── README.md
```

## Limitations

- The tool is designed for Linux and relies on files such as `/proc/cpuinfo`, `/proc/meminfo`, and `/proc/uptime`.
- Available information may vary by Linux distribution, hardware, and execution environment.
- Detailed storage output may include mount points that are virtual, duplicated, or inaccessible.


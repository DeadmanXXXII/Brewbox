# brewbox - macOS attack suite for smartphones

brewbox is a CLI tool designed to simulate offensive security actions on macOS systems from a smartphone or any terminal. It is a modular framework that replicates some of the core macOS attack vectors, such as ARDAgent RCE, AppleScript droppers, and macOS fingerprinting.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/brewbox.git
   cd brewbox
   ```

2. Install dependencies:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

3. Make `brewbox.py` executable:
   ```bash
   chmod +x brewbox.py
   ln -s $(pwd)/brewbox.py /usr/local/bin/brewbox
   ```

## Usage

### Recon:
```bash
brewbox recon --target <target-ip>
```

### Exploit ARD:
```bash
brewbox exploit-ard --target <target-ip>
```

### Deploy AppleScript payload:
```bash
brewbox applescript-dropper --target <target-ip>
```

### Fingerprint macOS:
```bash
brewbox fingerprint --target <target-ip>
```

### Install dependencies:
```bash
brewbox install
```

## Contributing

Feel free to fork, modify, and submit pull requests. This is a community-driven project.

## Disclaimer

This tool is for educational purposes only. Ensure you have permission before testing on any system.

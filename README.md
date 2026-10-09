# Emergency Alert Packet Integrity Simulator

A defense-grade cybersecurity dashboard designed for college engineering projects. This system simulates emergency alert telemetry packets and provides real-time cryptographic integrity verification using the **CRC-32 (Cyclic Redundancy Check)** checksum algorithm.

---

## 🎯 Project Overview & Objective

In disaster response and public defense operations (e.g., Tsunami Warnings, Earthquake Alerts, Chemical Spills), emergency alert messages transmitted over RF channels, satellite links, or cell broadcast towers are vulnerable to:
1. **Electromagnetic Interference (EMI) & Channel Noise** causing random bit flips.
2. **Adversarial Tampering & Spoofing** where attackers forge sender authorities or modify evacuation coordinates.

This simulator models the transmission of Common Alerting Protocol (CAP) emergency packets, computes standard **CRC-32 checksums**, and demonstrates how cyclical polynomial division guarantees packet data integrity.

---

## 🚀 Quick Start (Running the Dashboard)

### Method 1: 1-Click Launch (Windows)
Double-click `start.bat` in the project directory. This starts the Python local server and opens your browser directly to:
```
http://127.0.0.1:8000/
```

### Method 2: Python Command
Run in PowerShell or Command Prompt:
```powershell
python server.py
```

### Method 3: Direct Browser Launch
You can also open `index.html` directly in any modern web browser (Google Chrome, Microsoft Edge, Firefox, Brave) without any server.

> **Note**: Zero npm or pip installations are required! The dashboard runs out of the box.

---

## 🛡️ Key Features & Dashboard Modules

### 1. Left Sidebar Navigation
- **🛰️ Dashboard**: Telemetry overview, KPI cards, real-time distribution charts, and recent alerts stream.
- **📝 Create Emergency Alert**: Fully interactive form to encode alerts, calculate reference CRC-32 checksums, and frame packets.
- **📦 Packet Construction**: Frame decomposition inspector, Preamble (0xAA55AA55), Metadata Headers, Message Body, Wireshark-compatible Hex Dump, and serialized JSON.
- **🛡️ CRC Integrity Check**: Side-by-side comparison of Reference CRC vs Current CRC with 32-bit bitwise XOR matrix and step-by-step mathematical division trace.
- **📡 Transmission Channel**: Interactive RF channel with tunable channel noise (BER) and latency slider to simulate atmospheric radio interference.
- **⚡ Error Simulation Lab**: Interactive workbench to flip single bits, inject burst noise, spoof sender metadata, tamper coordinates, or edit payloads in real-time.
- **📜 Verification History**: Searchable and filterable chronological audit trail with CSV and JSON data export.
- **📑 Reports (Audit Certificate)**: Formal cryptographic integrity audit report with print-to-PDF formatting and academic examiner sign-off block.
- **⚙️ Settings**: Switch between **CRC-32 IEEE 802.3** and **CRC-32C Castagnoli**, toggle tactical Web Audio synthesis, and reset demo data.

---

## 📊 Dashboard KPI Metrics & Statuses

- **Total Packets**: Total emergency broadcasts framed.
- **Valid Packets**: Packets where `Reference CRC-32 == Current CRC-32`.
- **Corrupted Packets**: Packets where `Reference CRC-32 != Current CRC-32`.
- **Integrity Success Rate**: Real-time percentage with status progress bar.

### Verification Status Banners:
- **`PACKET VALID - INTEGRITY CONFIRMED`**: Displayed in vibrant emerald green when checksums match (0 bit flips).
- **`PACKET CORRUPTED - INTEGRITY FAILURE`**: Displayed in tactical crimson red when checksums diverge, highlighting flipped bits in real-time.

---

## 🔬 Mathematical Principles of CRC-32

### 1. Generator Polynomials
- **CRC-32 (IEEE 802.3 Standard)**:
  $$\text{Polynomial} = x^{32} + x^{26} + x^{23} + x^{22} + x^{16} + x^{12} + x^{11} + x^{10} + x^8 + x^7 + x^5 + x^4 + x^2 + x + 1$$
  - Normal representation: `0x04C11DB7`
  - Reversed (Little-Endian) representation: `0xEDB88320`

- **CRC-32C (Castagnoli)**:
  - Normal representation: `0x1EDC6F41`
  - Reversed representation: `0x82F63B78`

### 2. Error Detection Capabilities
- Detects **100% of single-bit errors**.
- Detects **100% of double-bit errors**.
- Detects **100% of any odd number of bit errors**.
- Detects **100% of burst errors up to 32 bits** in length.
- Detects **99.99999998% of burst errors greater than 32 bits** ($1 - 2^{-32}$).

---

## 🎓 College Viva Voce / Presentation Q&A Guide

**Q1: What is CRC and how is it different from a cryptographic hash like SHA-256?**  
> *Answer*: CRC (Cyclic Redundancy Check) is a linear error-detecting code based on polynomial division designed for fast, hardware-efficient detection of accidental transmission corruptions (noise, bit flips). In contrast, cryptographic hashes (like SHA-256) are non-linear, computationally intensive, and designed for collision resistance against deliberate cryptographic forgery.

**Q2: How does the CRC-32 lookup table optimization work?**  
> *Answer*: Standard bit-by-bit polynomial division requires 8 shift-and-XOR iterations per byte. By pre-calculating the remainder for all 256 possible byte combinations ($2^8$) into a lookup table, we can process an entire byte in a single table lookup and XOR operation.

**Q3: What does the status "PACKET CORRUPTED - INTEGRITY FAILURE" mean?**  
> *Answer*: It indicates that the recalculated CRC over the received payload does not equal the transmitted reference CRC, resulting in a non-zero XOR residual and confirming that one or more bits were corrupted during transit or deliberately tampered with.

---

## 📁 File Structure

```
Emergency alert message error detection/
├── index.html              # Main Cyber Command Dashboard UI (9 views)
├── css/
│   └── style.css           # Cybersecurity tactical theme, radar animation, bit matrix
├── js/
│   ├── crc32.js            # Mathematical CRC-32 engine, tables & bitwise utilities
│   ├── sound.js            # Web Audio API sound synthesizer (beeps, klaxons, chimes)
│   └── app.js              # Application state, charts, error simulator & report generator
├── server.py               # Zero-dependency Python 3 local server
├── start.bat               # 1-click Windows runner
└── README.md               # Complete project documentation & viva guide
```

# 🔐 FunPass - Fun & Secure Password Generator

<p align="center">
  <strong>Generate memorable passwords from poems, quotes, code snippets & more!</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/flask-3.0-green.svg" alt="Flask 3.0">
  <img src="https://img.shields.io/badge/license-MIT-yellow.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
</p>

---

## ✨ Features

### 🎯 **25 Unique Content Sources**
Choose from a diverse library of content to generate your passwords:

| Category | Count | Examples |
|----------|-------|----------|
| 📜 **Poems** | 3 | Classic poetry from Frost, Wordsworth & more |
| 💬 **Quotes** | 3 | Inspiring words from Einstein, Gandhi, Jobs |
| 💻 **Code** | 3 | Programming snippets (JS, Node, Python) |
| 🎵 **Songs** | 3 | Iconic lyrics from Lennon, Beatles & more |
| ✨ **Sayings** | 3 | Timeless proverbs and wisdom |
| 🔤 **Words** | 3 | Creative word combinations |
| 🔬 **Science** | 3 | Fascinating scientific facts |
| 🌿 **Nature** | 3 | Beautiful nature descriptions |
| 🧠 **Philosophy** | 1 | Descartes' famous quote |

### 🔒 **Security Features**
- **Leet Speak Substitution**: Transform letters into symbols (a→@, e→3, i→1, etc.)
- **Customizable Length**: 8-32 characters to fit any requirement
- **Numbers & Symbols**: Toggle to add extra complexity
- **Entropy Calculation**: Real-time password strength measurement
- **Strength Indicator**: Visual feedback (Weak/Medium/Strong)
- **Secure Random**: Uses Python's `secrets` module for cryptographic security

### 🎨 **Beautiful UI**
- Modern, responsive design
- Category filtering system
- Color-coded password characters
- Smooth animations & transitions
- Toast notifications
- Dark theme optimized

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/funpass.git
   cd funpass
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   
   Navigate to: http://localhost:5000

---

## 📖 Usage Guide

### Step 1: Choose Your Source
- Browse the 25 available items across 9 categories
- Use category filters to narrow down your choice
- Click any item to select it (highlighted with blue border)

### Step 2: Customize Options
- **Password Length**: Drag slider from 8 to 32 characters
- **Numbers**: Toggle to include random numbers (100-999)
- **Symbols**: Toggle to add special characters (!@#$%^&*)
- **Leet Speak**: Toggle letter-to-symbol substitutions

### Step 3: Generate
1. Click **🚀 Generate Password**
2. View your unique password with color-coded characters:
   - 🔵 Blue = Letters
   - 🟡 Yellow = Numbers
   - 🔴 Red = Symbols
3. Check the strength meter and entropy score

### Step 4: Copy & Use
- Click **📋 Copy to Clipboard** to copy instantly
- Use **🔄 Regenerate** for a new variation
- Use **🎲 Random Source** to pick a random item

---

## 🛠️ Technical Details

### Password Generation Algorithm

1. **Word Selection**: Randomly selects 4-6 words from the source text
2. **Capitalization**: Capitalizes first letter of each word
3. **Leet Speak**: Applies substitutions with 70% probability per character
4. **Number Insertion**: Adds 3-digit number at random position
5. **Symbol Insertion**: Adds 1-3 symbols at random positions
6. **Length Adjustment**: Pads or truncates to exact specified length
7. **Entropy Calculation**: Measures bits based on character set diversity

### Leet Speak Substitution Table

| Letter | Standard | Advanced |
|--------|----------|----------|
| a/A | @ / 4 | - |
| e/E | 3 | - |
| i/I | 1 / ! | - |
| o/O | 0 | - |
| s/S | $ / 5 | - |
| t/T | 7 / + | - |
| l/L | 1 / \| | - |
| b/B | 8 / \|3 | - |
| c/C | - | ( / { |
| h/H | - | # / ]-[ |
| m/M | - | \|\\/ \| / \|V\| |

### Entropy Strength Thresholds

| Level | Minimum Entropy | Minimum Length | Color |
|-------|----------------|----------------|-------|
| ⚠️ Weak | < 50 bits | < 12 | 🔴 Red |
| 🔐 Medium | ≥ 50 bits | ≥ 12 | 🟡 Orange |
| 🔒 Strong | ≥ 80 bits | ≥ 16 | 🟢 Green |

---

## 📁 Project Structure

```
funpas/
├── app.py                 # Flask backend & password generation
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── .gitignore            # Git ignore rules
├── templates/
│   └── index.html        # Frontend UI
└── static/               # (Optional) Static assets
    └── favicon.ico
```

---

## 🔐 Security Notes

- ✅ All password generation happens **server-side**
- ✅ Uses Python's `secrets` module (cryptographically secure)
- ✅ **No passwords are logged or stored**
- ✅ No external API calls or data transmission
- ✅ Safe for offline use

---

## 🎨 Screenshots

### Main Interface
```
┌─────────────────────────────────────────────────┐
│                   🔐                             │
│                 FunPass                          │
│   Generate secure, memorable passwords...       │
│                                                  │
│  [🎯 All] [📜 Poem] [💬 Quote] [💻 Code]...    │
│                                                  │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  │📜 Poem   │ │📜 Poem   │ │💬 Quote  │        │
│  │Roses are │ │Two roads │ │The only  │        │
│  │red...    │ │diverged..│ │way to do │        │
│  └──────────┘ └──────────┘ └──────────┘        │
│                                                  │
│  📏 Password Length: [████░░░░] 16              │
│  ⚙️ [✓ Numbers] [✓ Symbols] [✓ Leet Speak]     │
│                                                  │
│          🚀 GENERATE PASSWORD                    │
└─────────────────────────────────────────────────┘
```

### Generated Password
```
┌─────────────────────────────────────────────────┐
│  Your Generated Password                         │
│  Source: 📜 Poem: Traditional                    │
│                                                  │
│  R0s3s@r3R3dV10l3t$!92                          │
│                                                  │
│  Security: 🔒 STRONG          Entropy: 95.2 bits│
│  [████████████████████]                          │
│                                                  │
│  [📋 Copy]  [🔄 Regenerate]  [🎲 Random]        │
└─────────────────────────────────────────────────┘
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Ideas for Contributions
- Add more poems, quotes, or songs
- Implement custom leet speak rules
- Add password history (local storage)
- Export passwords to file
- Multi-language support
- Mobile app version

---

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2026 FunPass

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

- Inspired by Diceware password generation methods
- Leet speak (1337) culture and history
- All the poets, musicians, and thinkers whose words we borrow

---

## 📬 Contact & Support

- **Issues**: Open a GitHub issue for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions

---

<p align="center">
  <strong>Made with ❤️ for better password security</strong><br>
  <sub>⭐ Star this repo if you find it useful!</sub>
</p>

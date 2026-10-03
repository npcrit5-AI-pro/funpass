# 🔐 FunPass: Fun & Secure Password Generator

<p align="center">
  <strong>Generate memorable passwords from poems, quotes, code snippets, songs, and more.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/flask-3.x-green.svg" alt="Flask 3.x">
</p>

FunPass is a small web app that runs on your own computer. You pick a piece of text (a poem, a quote, a song lyric, a line of code...), choose a few options, and FunPass turns words from it into a strong password. It shows you how strong the password is and lets you copy it with one click.

**New here?** Follow the step-by-step guide in **[docs/TUTORIAL.md](docs/TUTORIAL.md)**.

---

## ✨ Features

### 🎯 25 content sources in 9 categories

| Category | Count | Examples |
|----------|-------|----------|
| 📜 **Poem** | 3 | Classic poetry from Frost, Wordsworth & more |
| 💬 **Quote** | 3 | Inspiring words from Einstein, Gandhi, Jobs |
| 💻 **Code** | 3 | Programming snippets (JS, Node, Python) |
| 🎵 **Song** | 3 | Iconic lyrics from Lennon, the Beatles & more |
| ✨ **Saying** | 3 | Timeless proverbs |
| 🔤 **Words** | 3 | Creative word combinations |
| 🔬 **Science** | 3 | Scientific facts |
| 🌿 **Nature** | 3 | Nature descriptions |
| 🧠 **Philosophy** | 1 | Descartes' famous quote |

### 🔒 Password options
- **Length:** 8 to 32 characters (slider)
- **Numbers:** adds a random 3-digit number (100-999)
- **Symbols:** adds 1-3 symbols from `!@#$%^&*`
- **Leet speak:** swaps some letters for look-alikes (a→@, e→3, o→0, s→$ ...)
- **Strength meter:** Weak / Medium / Strong, plus an entropy score in bits

### 🎨 Interface
- Dark, responsive design that works on phones and desktops
- Category filter tabs
- Color-coded password characters (letters, numbers, symbols)
- **Copy to Clipboard**, **Regenerate**, and **Random Source** buttons

---

## 🚀 Quick start

You need **Python 3.8 or newer**.

```bash
git clone https://github.com/npcrit5-AI-pro/funpass.git
cd funpass
python -m venv venv            # optional, but keeps things tidy
# Windows: venv\Scripts\activate   macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open **http://localhost:5000** in your browser.

The full walkthrough (with what each button does) is in **[docs/TUTORIAL.md](docs/TUTORIAL.md)**.

---

## ⚙️ Configuration

FunPass has **no environment variables, API keys, or config files**. Everything runs locally.

The few settings that exist are in `app.py`:

| Setting | Where | Default |
|---|---|---|
| Port | `app.run(... port=5000)` at the bottom of `app.py` | `5000` |
| Listen address | `app.run(host='0.0.0.0' ...)` | all network interfaces |
| Debug mode | `app.run(debug=True ...)` | on |
| Content library | `ITEMS` list near the top of `app.py` | 25 items |

---

## 🔌 HTTP endpoints

| Method | Path | What it does |
|---|---|---|
| `GET` | `/` | The web page |
| `POST` | `/generate` | JSON body `{"item_id", "length", "use_numbers", "use_symbols", "use_leet"}` → returns `password`, `strength`, `entropy`, `source` |
| `GET` | `/api/items` | All 25 items and the list of categories |

Example:

```bash
curl -s -X POST http://localhost:5000/generate \
  -H "Content-Type: application/json" \
  -d '{"item_id": 3, "length": 20, "use_numbers": true, "use_symbols": true, "use_leet": true}'
```

---

## 🛠️ How a password is built

1. **Word selection:** picks 4-6 random words from the source text
2. **Capitalization:** capitalizes the first letter of each word
3. **Leet speak (optional):** each letter that has a substitute is swapped about 70% of the time
4. **Number (optional):** inserts a 3-digit number at a random spot
5. **Symbols (optional):** inserts 1-3 symbols at random spots
6. **Length:** cuts or pads (with random characters) to exactly your chosen length
7. **Strength:** entropy = length × log2(character-set size)

### Leet speak substitutions used

| Letter | Becomes | Letter | Becomes |
|---|---|---|---|
| a / A | `@` / `4` | t / T | `7` / `+` |
| e / E | `3` | l / L | `1` / `\|` |
| i / I | `1` / `!` | b / B | `8` / `\|3` |
| o / O | `0` | g / G | `9` / `6` |
| s / S | `$` / `5` | z / Z | `2` / `7_` |

(`app.py` also contains an "advanced" table for letters like c, h, m, but the generator does not currently use it.)

### Strength levels

| Level | Needs |
|---|---|
| ⚠️ Weak | anything below Medium |
| 🔐 Medium | at least 50 bits **and** at least 12 characters |
| 🔒 Strong | at least 80 bits **and** at least 16 characters |

---

## 📁 Project structure

```
funpass/
├── app.py              # Flask server, content library, password generator
├── templates/
│   └── index.html      # The whole web page (HTML, CSS, JavaScript)
├── requirements.txt    # Flask
├── GITHUB-SETUP.md     # Notes from the first upload to GitHub
├── push-to-github.bat  # Windows helper used for the first upload
└── README.md
```

---

## 🔐 Security notes

- Passwords are generated on your machine by the Flask server. Nothing is sent to the internet, logged, or stored.
- Numbers, symbols, and padding characters come from Python's `secrets` module. Word choice, positions, and leet swaps use Python's regular `random` module.
- Because the words come from a short, public text, use the **Numbers** and **Symbols** options and a length of **16 or more** for anything important.
- The server runs with Flask's **debug mode on** and listens on **all network interfaces** (`0.0.0.0`). That is fine on your own computer, but don't expose it to the internet as-is. See the tutorial's troubleshooting section for how to make it local-only.

---

## 🧯 Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'flask'` | Run `pip install -r requirements.txt` (inside your virtual environment if you made one). |
| `python` not found | Try `python3 app.py` (macOS/Linux) or `py app.py` (Windows). |
| `Address already in use` / port 5000 busy | Another app is on port 5000 (on macOS, AirPlay Receiver uses it). Change `port=5000` at the bottom of `app.py` to e.g. `5050`, then open `http://localhost:5050`. |
| Copy button does nothing | Some browsers only allow clipboard access on `localhost` or HTTPS. Open the app at `http://localhost:5000` rather than an IP address, or select the password and copy it by hand. |

More help: [docs/TUTORIAL.md#troubleshooting](docs/TUTORIAL.md#troubleshooting).

---

## 🤝 Contributing

1. Fork the repository
2. Create a branch (`git checkout -b feature/my-idea`)
3. Commit your changes
4. Push and open a Pull Request

Ideas: more poems/quotes/songs, wire up the advanced leet table, password history, more languages.

---

## 🙏 Acknowledgments

- Inspired by Diceware-style password methods
- Leet speak (1337) culture
- The poets, musicians, and thinkers whose words we borrow

<p align="center">
  <strong>Made with ❤️ for better password security</strong>
</p>

# FunPass tutorial

This guide takes you from nothing to your first generated password. No programming experience needed.

- [1. Install Python](#1-install-python)
- [2. Download FunPass](#2-download-funpass)
- [3. Install the one dependency](#3-install-the-one-dependency)
- [4. Start the app](#4-start-the-app)
- [5. Make your first password](#5-make-your-first-password)
- [6. Stop the app](#6-stop-the-app)
- [Tips](#tips)
- [Troubleshooting](#troubleshooting)

---

## 1. Install Python

You need Python **3.8 or newer**.

- **Windows / macOS:** download it from <https://www.python.org/downloads/>. On Windows, tick **"Add python.exe to PATH"** in the installer.
- **Linux:** Python is usually already installed. Check with `python3 --version`.

Check it worked by opening a terminal (Windows: *Command Prompt* or *PowerShell*; macOS: *Terminal*) and running:

```bash
python --version
```

If that says "not found", try `python3 --version` (macOS/Linux) or `py --version` (Windows) and use that word instead of `python` in the steps below.

## 2. Download FunPass

**With git:**

```bash
git clone https://github.com/npcrit5-AI-pro/funpass.git
cd funpass
```

**Without git:** on the GitHub page click **Code → Download ZIP**, unzip it, then open a terminal in the unzipped `funpass` folder.

## 3. Install the one dependency

FunPass only needs [Flask](https://flask.palletsprojects.com/). A *virtual environment* keeps it separate from the rest of your computer (optional, but recommended):

```bash
python -m venv venv
```

Turn it on:

- Windows: `venv\Scripts\activate`
- macOS / Linux: `source venv/bin/activate`

Your prompt now starts with `(venv)`. Install Flask:

```bash
pip install -r requirements.txt
```

## 4. Start the app

```bash
python app.py
```

You should see:

```
🎉 FunPass Password Generator
========================================
🚀 Starting server...
📍 Open http://localhost:5000 in your browser
========================================
```

Open **http://localhost:5000** in your web browser. Leave the terminal window open while you use the app.

## 5. Make your first password

### Step 1: Pick a source

Under **📚 Choose Your Source**, the page shows 25 cards. Each one is a poem, quote, code snippet, song lyric, saying, word list, science fact, nature line, or philosophy quote.

- Use the **category tabs** at the top (🎯 All, 📜 Poem, 💬 Quote, 💻 Code...) to narrow the list.
- **Click a card** to select it. The selected card gets a highlighted border.

### Step 2: Choose options

- **📏 Password Length:** drag the slider between **8** and **32** (it starts at 16). 16 or more is a good choice.

Under **⚙️ Options** there are three checkboxes. All three are on by default.

- **🔢 Numbers:** adds a random 3-digit number.
- **🎭 Symbols:** adds 1-3 symbols like `!`, `#`, or `&`.
- **💀 Leet Speak:** swaps some letters for look-alikes (`a` → `@`, `e` → `3`, `o` → `0`).

### Step 3: Generate

Click **🚀 Generate Password**. You'll see:

- The password, color-coded: letters, numbers, and symbols each get their own color.
- Which source it came from.
- A **strength** label (Weak, Medium, or Strong) and the **entropy** in bits. Higher is better.

### Step 4: Use it

- **📋 Copy to Clipboard** copies the password.
- **🔄 Regenerate** makes a new password from the same source and options.
- **🎲 Random Source** picks a random card for you.

Paste the password into the site or app where you need it, and save it in your password manager.

## 6. Stop the app

Go back to the terminal and press **Ctrl + C**.

Next time, just open a terminal in the `funpass` folder, turn the virtual environment back on (if you made one), and run `python app.py` again.

---

## Tips

- For important accounts, use **Strong** passwords: length 16+, with Numbers and Symbols on.
- Every click on Generate gives a different result, even from the same source.
- Want your own text? Add an entry to the `ITEMS` list near the top of `app.py` (give it the next `id`, a `category`, an `icon`, the `text`, and an `author`) and restart the app.

---

## Troubleshooting

**"No module named 'flask'"**
Flask isn't installed in the Python you're using. Turn on your virtual environment (step 3), then run `pip install -r requirements.txt` again.

**"python is not recognized" / "command not found"**
Use `python3` (macOS/Linux) or `py` (Windows). On Windows you can also re-run the Python installer and tick "Add python.exe to PATH".

**"Address already in use" or the page won't load**
Something else is using port 5000. On macOS this is often *AirPlay Receiver* (turn it off in System Settings → General → AirDrop & Handoff), or change the port: edit the last line of `app.py` from `port=5000` to `port=5050`, restart, and open `http://localhost:5050`.

**The Copy button doesn't copy**
Browsers only allow clipboard access on secure pages. `http://localhost:5000` counts as secure, but `http://192.168.x.x:5000` does not. Use `localhost`, or select the password text and copy it manually.

**Other devices on my network can open the app**
The app listens on all network interfaces and runs in Flask debug mode. To keep it on your computer only, change the last line of `app.py` to:

```python
app.run(debug=False, host='127.0.0.1', port=5000)
```

**I changed `app.py` but nothing happened**
Debug mode normally reloads automatically. If it doesn't, stop the app with Ctrl + C and start it again.

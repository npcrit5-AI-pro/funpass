"""
FunPass - A Fun & Secure Password Generator
Generate memorable passwords from poems, quotes, code snippets, and more!
"""

from flask import Flask, render_template, request, jsonify
import random
import string
import math
import secrets

app = Flask(__name__)

# ============================================================================
# CONTENT LIBRARY - 25 Selectable Items Across 8 Categories
# ============================================================================

ITEMS = [
    # Poems (3)
    {
        "id": 1,
        "category": "Poem",
        "icon": "📜",
        "text": "Roses are red violets are blue sugar is sweet and so are you",
        "author": "Traditional"
    },
    {
        "id": 2,
        "category": "Poem",
        "icon": "📜",
        "text": "Two roads diverged in a yellow wood and sorry I could not travel both",
        "author": "Robert Frost"
    },
    {
        "id": 3,
        "category": "Poem",
        "icon": "📜",
        "text": "I wandered lonely as a cloud that floats on high oer vales and hills",
        "author": "William Wordsworth"
    },
    
    # Quotes (3)
    {
        "id": 4,
        "category": "Quote",
        "icon": "💬",
        "text": "The only way to do great work is to love what you do",
        "author": "Steve Jobs"
    },
    {
        "id": 5,
        "category": "Quote",
        "icon": "💬",
        "text": "In the middle of difficulty lies opportunity",
        "author": "Albert Einstein"
    },
    {
        "id": 6,
        "category": "Quote",
        "icon": "💬",
        "text": "Be the change that you wish to see in the world",
        "author": "Mahatma Gandhi"
    },
    
    # Code (3)
    {
        "id": 7,
        "category": "Code",
        "icon": "💻",
        "text": "function generatePassword length return random bytes secure",
        "author": "JavaScript"
    },
    {
        "id": 8,
        "category": "Code",
        "icon": "💻",
        "text": "import hashlib from crypto create random token sixteen bytes",
        "author": "Node.js"
    },
    {
        "id": 9,
        "category": "Code",
        "icon": "💻",
        "text": "def secure_random return secrets token hex thirty two characters",
        "author": "Python"
    },
    
    # Songs (3)
    {
        "id": 10,
        "category": "Song",
        "icon": "🎵",
        "text": "Imagine all the people living life in peace today",
        "author": "John Lennon"
    },
    {
        "id": 11,
        "category": "Song",
        "icon": "🎵",
        "text": "Here comes the sun and I say its all right my friend",
        "author": "The Beatles"
    },
    {
        "id": 12,
        "category": "Song",
        "icon": "🎵",
        "text": "What a wonderful world I see trees of green and red roses too",
        "author": "Louis Armstrong"
    },
    
    # Sayings (3)
    {
        "id": 13,
        "category": "Saying",
        "icon": "✨",
        "text": "Actions speak louder than words do every single time",
        "author": "Proverb"
    },
    {
        "id": 14,
        "category": "Saying",
        "icon": "✨",
        "text": "Where there is a will there is always a way forward",
        "author": "Proverb"
    },
    {
        "id": 15,
        "category": "Saying",
        "icon": "✨",
        "text": "A journey of a thousand miles begins with one step",
        "author": "Lao Tzu"
    },
    
    # Words (3)
    {
        "id": 16,
        "category": "Words",
        "icon": "🔤",
        "text": "thunder crystal rainbow butterfly symphony dragonfire starlight",
        "author": "Creative"
    },
    {
        "id": 17,
        "category": "Words",
        "icon": "🔤",
        "text": "emerald phoenix midnight velocity quantum whisper cascade",
        "author": "Creative"
    },
    {
        "id": 18,
        "category": "Words",
        "icon": "🔤",
        "text": "aurora nebula titanium eclipse horizon vortex zenith",
        "author": "Creative"
    },
    
    # Science (3)
    {
        "id": 19,
        "category": "Science",
        "icon": "🔬",
        "text": "DNA carries genetic information in a double helix structure",
        "author": "Biology"
    },
    {
        "id": 20,
        "category": "Science",
        "icon": "🔬",
        "text": "Energy equals mass times the speed of light squared",
        "author": "Physics"
    },
    {
        "id": 21,
        "category": "Science",
        "icon": "🔬",
        "text": "Electrons orbit the nucleus in discrete energy levels",
        "author": "Chemistry"
    },
    
    # Nature (3)
    {
        "id": 22,
        "category": "Nature",
        "icon": "🌿",
        "text": "Mountains touch the sky while rivers carve the ancient valleys",
        "author": "Earth"
    },
    {
        "id": 23,
        "category": "Nature",
        "icon": "🌿",
        "text": "Forests whisper secrets of old while wildflowers dance in breeze",
        "author": "Earth"
    },
    {
        "id": 24,
        "category": "Nature",
        "icon": "🌿",
        "text": "Ocean waves crash upon the shore under a canopy of stars",
        "author": "Earth"
    },
    
    # Philosophy (1)
    {
        "id": 25,
        "category": "Philosophy",
        "icon": "🧠",
        "text": "I think therefore I am the mind defines existence itself",
        "author": "Descartes"
    }
]

# ============================================================================
# LEET SPEAK SUBSTITUTION TABLES
# ============================================================================

# Standard substitutions
LEET_STANDARD = {
    'a': '@', 'A': '4',
    'e': '3', 'E': '3',
    'i': '1', 'I': '!',
    'o': '0', 'O': '0',
    's': '$', 'S': '5',
    't': '7', 'T': '+',
    'l': '1', 'L': '|',
    'b': '8', 'B': '|3',
    'g': '9', 'G': '6',
    'z': '2', 'Z': '7_'
}

# Advanced substitutions (more creative)
LEET_ADVANCED = {
    'c': '(', 'C': '{',
    'd': '|)', 'D': '|>',
    'h': '#', 'H': ']-[',
    'k': '|<', 'K': '|{',
    'm': '|\\/|', 'M': '|V|',
    'n': '/\\/', 'N': '|\\|',
    'r': '|2', 'R': '|2',
    'u': '|_|', 'U': '(_)\\',
    'v': '\\/', 'V': '\\/',
    'w': '\\/\\/', 'W': '\\/\\/'
}

# Symbol sets
SYMBOLS_BASIC = '!@#$%^&*'
SYMBOLS_EXTENDED = '!@#$%^&*()_+-=[]{}|;:,.<>?/~`'

# ============================================================================
# PASSWORD GENERATION ENGINE
# ============================================================================

def apply_leet_speak(text, advanced=False):
    """Apply leet speak substitutions to text."""
    substitutions = LEET_STANDARD.copy()
    if advanced:
        substitutions.update(LEET_ADVANCED)
    
    result = []
    for char in text:
        # Randomly apply substitutions for variety (70% chance)
        if char in substitutions and random.random() > 0.3:
            result.append(substitutions[char])
        else:
            result.append(char)
    return ''.join(result)


def calculate_entropy(password):
    """Calculate password entropy in bits."""
    if not password:
        return 0
    
    charset_size = 0
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in SYMBOLS_EXTENDED for c in password)
    
    if has_lower:
        charset_size += 26
    if has_upper:
        charset_size += 26
    if has_digit:
        charset_size += 10
    if has_special:
        charset_size += 32
    
    if charset_size == 0:
        return 0
    
    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 2)


def get_strength_info(entropy, length):
    """Determine password strength based on entropy and length."""
    if entropy >= 80 and length >= 16:
        return {
            "level": "strong",
            "label": "STRONG",
            "percentage": 100,
            "color": "#00ff88",
            "emoji": "🔒"
        }
    elif entropy >= 50 and length >= 12:
        return {
            "level": "medium",
            "label": "MEDIUM",
            "percentage": 66,
            "color": "#ffaa00",
            "emoji": "🔐"
        }
    else:
        return {
            "level": "weak",
            "label": "WEAK",
            "percentage": 33,
            "color": "#ff4444",
            "emoji": "⚠️"
        }


def generate_password_from_item(item, length, use_numbers, use_symbols, use_leet):
    """Generate a password from a selected item."""
    words = item['text'].split()
    
    # Select random words (aim for 4-6 words)
    num_words = min(random.randint(4, 6), len(words))
    selected_words = random.sample(words, num_words)
    
    # Capitalize first letter of each word for readability
    processed_words = [word.capitalize() for word in selected_words]
    
    # Apply leet speak if enabled
    if use_leet:
        processed_words = [apply_leet_speak(word) for word in processed_words]
    
    # Join words
    password_base = ''.join(processed_words)
    
    # Add numbers if enabled
    if use_numbers:
        num_part = str(secrets.randbelow(900) + 100)  # 100-999
        # Insert number at random position
        insert_pos = random.randint(0, len(password_base))
        password_base = password_base[:insert_pos] + num_part + password_base[insert_pos:]
    
    # Add symbols if enabled
    if use_symbols:
        num_symbols = random.randint(1, 3)
        symbols = ''.join(secrets.choice(SYMBOLS_BASIC) for _ in range(num_symbols))
        # Insert symbols at random positions
        for _ in range(num_symbols):
            insert_pos = random.randint(0, len(password_base))
            password_base = password_base[:insert_pos] + secrets.choice(SYMBOLS_BASIC) + password_base[insert_pos:]
    
    # Adjust to desired length
    if len(password_base) > length:
        # Truncate but try to keep it readable
        password_base = password_base[:length]
    elif len(password_base) < length:
        # Pad with random characters
        charset = string.ascii_letters
        if use_numbers:
            charset += string.digits
        if use_symbols:
            charset += SYMBOLS_BASIC
        
        padding_length = length - len(password_base)
        padding = ''.join(secrets.choice(charset) for _ in range(padding_length))
        
        # Insert padding at random positions for better distribution
        password_chars = list(password_base)
        for char in padding:
            insert_pos = random.randint(0, len(password_chars))
            password_chars.insert(insert_pos, char)
        password_base = ''.join(password_chars)
    
    # Ensure minimum length requirement is met
    while len(password_base) < length:
        password_base += secrets.choice(string.ascii_letters + string.digits)
    
    # Final truncation to exact length
    password = password_base[:length]
    
    # Calculate strength
    entropy = calculate_entropy(password)
    strength = get_strength_info(entropy, length)
    
    return {
        "password": password,
        "strength": strength,
        "entropy": entropy,
        "source": f"{item['icon']} {item['category']}: {item['author']}"
    }


# ============================================================================
# FLASK ROUTES
# ============================================================================

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html', items=ITEMS)


@app.route('/generate', methods=['POST'])
def generate():
    """Generate a password based on user preferences."""
    data = request.json or {}
    
    # Parse parameters with validation
    try:
        item_id = int(data.get('item_id', 1))
        length = int(data.get('length', 16))
        use_numbers = bool(data.get('use_numbers', True))
        use_symbols = bool(data.get('use_symbols', True))
        use_leet = bool(data.get('use_leet', True))
    except (ValueError, TypeError):
        item_id, length = 1, 16
        use_numbers = use_symbols = use_leet = True
    
    # Validate ranges
    length = max(8, min(32, length))
    item_id = max(1, min(len(ITEMS), item_id))
    
    # Find selected item
    item = next((i for i in ITEMS if i['id'] == item_id), ITEMS[0])
    
    # Generate password
    result = generate_password_from_item(item, length, use_numbers, use_symbols, use_leet)
    
    return jsonify(result)


@app.route('/api/items')
def get_items():
    """API endpoint to get all items (useful for frontend)."""
    return jsonify({
        "items": ITEMS,
        "categories": list(set(item['category'] for item in ITEMS))
    })


if __name__ == '__main__':
    print("\n🎉 FunPass Password Generator")
    print("=" * 40)
    print("🚀 Starting server...")
    print("📍 Open http://localhost:5000 in your browser")
    print("=" * 40 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)

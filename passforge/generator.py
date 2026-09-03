"""Cryptographically secure generator for passwords, passphrases, and tokens."""

import secrets
import string
import math
from typing import Dict, Any, List

# Curated English Diceware wordlist for memorable passphrases
WORDS = [
    "amber", "anchor", "apple", "arrow", "atlas", "bacon", "badge", "baker", "banana", "beacon",
    "breeze", "bridge", "cabin", "cactus", "camel", "candle", "canyon", "castle", "cedar", "cipher",
    "clover", "comet", "compass", "copper", "coral", "crater", "crystal", "dagger", "dawn", "delta",
    "desert", "diver", "dolphin", "dragon", "drift", "eagle", "echo", "ember", "falcon", "feather",
    "flame", "forest", "fossil", "frost", "galaxy", "garden", "glacier", "glider", "granite", "grove",
    "harbor", "haven", "hawk", "helix", "horizon", "hunter", "island", "jaguar", "jungle", "knight",
    "lagoon", "lantern", "legend", "lemur", "leopard", "lotus", "lumber", "lunar", "magnet", "maple",
    "marble", "meadow", "meteor", "mirage", "monarch", "moss", "nebula", "nest", "ninja", "nova",
    "oasis", "ocean", "olive", "onyx", "orbit", "orchid", "otter", "owl", "palace", "panther",
    "pebble", "phoenix", "pillar", "pixel", "planet", "plasma", "polar", "prism", "quartz", "quiver",
    "radar", "radius", "raven", "reef", "rhino", "ridge", "river", "rocket", "ruby", "saber",
    "safari", "sailor", "sapphire", "saturn", "shadow", "shield", "sierra", "silver", "solar", "spark",
    "spectrum", "sphinx", "spiral", "star", "summit", "tempest", "thunder", "tiger", "timber", "titan",
    "topaz", "torrent", "tower", "tracer", "trail", "tundra", "twilight", "valley", "vapor", "velvet",
    "vortex", "voyager", "walrus", "willow", "winter", "wizard", "wolf", "zenith", "zephyr", "zodiac"
]


def calculate_entropy(password: str) -> float:
    """Calculate bits of cryptographic entropy for a given password."""
    pool_size = 0
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_punct = any(c in string.punctuation for c in password)

    if has_lower:
        pool_size += 26
    if has_upper:
        pool_size += 26
    if has_digit:
        pool_size += 10
    if has_punct:
        pool_size += len(string.punctuation)

    if pool_size == 0 or len(password) == 0:
        return 0.0

    return round(len(password) * math.log2(pool_size), 1)


def generate_password(length: int = 16, no_symbols: bool = False, no_digits: bool = False, no_upper: bool = False) -> Dict[str, Any]:
    """Generate a random cryptographic password."""
    chars = list(string.ascii_lowercase)
    if not no_upper:
        chars.extend(string.ascii_uppercase)
    if not no_digits:
        chars.extend(string.digits)
    if not no_symbols:
        chars.extend("!@#$%^&*()-_=+[]{}<>?~")

    password = "".join(secrets.choice(chars) for _ in range(length))
    entropy = calculate_entropy(password)

    strength = "Weak"
    if entropy >= 80:
        strength = "Very Strong"
    elif entropy >= 60:
        strength = "Strong"
    elif entropy >= 40:
        strength = "Moderate"

    return {
        "password": password,
        "length": length,
        "entropy_bits": entropy,
        "strength": strength
    }


def generate_passphrase(word_count: int = 4, separator: str = "-", capitalize: bool = True, add_number: bool = True) -> Dict[str, Any]:
    """Generate a secure, memorable Diceware passphrase."""
    chosen = [secrets.choice(WORDS) for _ in range(word_count)]
    if capitalize:
        chosen = [w.capitalize() for w in chosen]
    if add_number:
        chosen[-1] = f"{chosen[-1]}{secrets.randbelow(100)}"

    passphrase = separator.join(chosen)
    # Diceware entropy = word_count * log2(len(WORDS))
    entropy = round(word_count * math.log2(len(WORDS)), 1)

    return {
        "passphrase": passphrase,
        "words": word_count,
        "entropy_bits": entropy,
        "strength": "Very Strong" if entropy >= 50 else "Strong"
    }


def generate_token(bytes_len: int = 32, encoding: str = "hex") -> str:
    """Generate random cryptographic token (hex, base64, or urlsafe)."""
    if encoding == "hex":
        return secrets.token_hex(bytes_len)
    elif encoding == "url":
        return secrets.token_urlsafe(bytes_len)
    else:
        return secrets.token_hex(bytes_len)

"""PassForge CLI Main Entrypoint."""

import argparse
import sys
from typing import List

from passforge.generator import generate_password, generate_passphrase, generate_token

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"


def main(args: List[str] = None):
    parser = argparse.ArgumentParser(
        prog="passforge",
        description="🔑 PassForge - High-Entropy Password, Diceware Passphrase & Crypto Token Generator CLI",
        epilog="Examples:\n"
               "  passforge                  # Generate 16-character secure password\n"
               "  passforge -l 24            # Generate 24-character password\n"
               "  passforge --phrase 4       # Generate 4-word Diceware passphrase\n"
               "  passforge --token 32       # Generate 32-byte (64-char) crypto hex token\n",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("-l", "--length", type=int, default=16, help="Password length (default: 16)")
    parser.add_argument("-n", "--count", type=int, default=1, help="Number of passwords/passphrases to generate")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude special characters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude numbers")
    parser.add_argument("--phrase", type=int, metavar="WORDS", help="Generate memorable Diceware passphrase with N words")
    parser.add_argument("--token", type=int, metavar="BYTES", help="Generate random crypto token with N bytes")

    parsed = parser.parse_args(args)

    if parsed.token:
        for _ in range(parsed.count):
            t = generate_token(bytes_len=parsed.token)
            print(f"{GREEN}{BOLD}{t}{RESET}")
        return

    if parsed.phrase:
        for _ in range(parsed.count):
            res = generate_passphrase(word_count=parsed.phrase)
            print(f"\n{CYAN}🔑 Diceware Passphrase:{RESET} {GREEN}{BOLD}{res['passphrase']}{RESET}")
            print(f"   {DIM}Entropy: {res['entropy_bits']} bits | Strength: {res['strength']}{RESET}\n")
        return

    for _ in range(parsed.count):
        res = generate_password(
            length=parsed.length,
            no_symbols=parsed.no_symbols,
            no_digits=parsed.no_digits
        )
        print(f"\n{CYAN}🔑 Generated Password:{RESET} {GREEN}{BOLD}{res['password']}{RESET}")
        print(f"   {DIM}Length: {res['length']} | Entropy: {res['entropy_bits']} bits | Strength: {res['strength']}{RESET}\n")


if __name__ == "__main__":
    main()

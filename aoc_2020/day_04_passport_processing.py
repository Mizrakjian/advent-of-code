"""
AoC2020.4: Passport Processing

Created on Wed Dec 16 17:05:00 2020
"""
import re


def year(value: str, min: int, max: int) -> bool:
    return len(value) == 4 and min <= int(value) <= max


def height(value: str, unit: str) -> bool:
    min, max = (150, 193) if unit == "cm" else (59, 76)
    return unit in ("cm", "in") and min <= int(value) <= max


TESTS = {
    "byr": lambda v: year(v, 1920, 2002),  # Birth Year
    "iyr": lambda v: year(v, 2010, 2020),  # Issue Year
    "eyr": lambda v: year(v, 2020, 2030),  # Expiration Year
    "hgt": lambda v: height(v[:-2], v[-2:]),  # Height
    "hcl": lambda v: re.match(r"^#[0-9a-f]{6}$", v),  # Hair Color
    "ecl": lambda v: v in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},  # Eye Color
    "pid": lambda v: len(v) == 9 and v.isdigit(),  # Passport ID
    # "cid": lambda v: v,  # Country ID (optional)
}


def part_1(passports: list) -> int:
    """Return count of passports with valid fields."""
    valid = [p for p in passports if all(field in p for field in TESTS)]
    return len(valid)


def part_2(passports: list) -> int:
    """Return count of passports with valid fields and data."""
    valid = [
        passport
        for passport in passports
        if all(TESTS[field](passport.get(field, "")) for field in TESTS)
    ]
    return len(valid)


def init() -> list:
    """Return list of dicts made from double-newline separated file data."""
    with open("input/day_04_input.txt") as file:
        return [
            {k: v for k, v in (field.split(":") for field in passport.split())}
            for passport in file.read().split("\n\n")
        ]


def main():
    print(__doc__.splitlines()[1], "\n")

    passports = init()

    print(f"  Passports w/ proper fields: {part_1(passports)}")
    print(f"     Passports w/ valid data: {part_2(passports)}")


if __name__ == "__main__":
    main()

"""
AoC 2020.8: Handheld Halting

Created on Mon Jan 04 02:24 2021
"""


def init() -> list:
    """Return bootrom as a list of operation, value tuples from input file."""
    with open("input/day_08_input.txt") as boot_code:
        return [(op, int(val)) for op, val in (line.split() for line in boot_code)]


def boot_loader(rom: list) -> tuple:
    """Return a tuple of loop flag bool and accumulator int after executing ops in rom."""
    accum = pointer = 0
    executed = set()
    while pointer < len(rom) and pointer not in executed:
        op, val = rom[pointer]
        executed.add(pointer)
        if op == "acc":
            accum += val
        elif op == "jmp":
            pointer += val
            continue
        pointer += 1
    return pointer in executed, accum


def flip_test(rom: list) -> tuple:
    """
    Return tuple of accumulator, instruction pointer, operation and flipped op when
    flipping an op allows the rom to boot normally (no loop).
    """
    flip = {"jmp": "nop", "nop": "jmp"}
    for i, (op, val) in enumerate(rom):
        if op != "acc":
            rom[i] = flip[op], val
            loop, accum = boot_loader(rom)
            rom[i] = op, val
            if not loop:
                return accum, i, op, flip[op]
    return -1, -1, "", ""


def part_1(rom: list) -> int:
    """
    Run your copy of the boot code. Immediately before any instruction is executed
    a second time, what value is in the accumulator?
    """
    _, accum = boot_loader(rom)
    return accum


def part_2(rom: list) -> int:
    """
    Fix the program so that it terminates normally by changing exactly one jmp (to nop)
    or nop (to jmp). What is the value of the accumulator after the program terminates?
    """
    accum, *_ = flip_test(rom)
    return accum


def main():
    print(__doc__.splitlines()[1], "\n")

    rom = init()

    print(f"  Infinite loop: {part_1(rom)}")
    print(f"    Normal boot: {part_2(rom)}")


if __name__ == "__main__":
    main()

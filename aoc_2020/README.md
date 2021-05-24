# Advent of Code 2020 Notes

## Day 1: Report Repair
Today looks like a 2-sum and 3-sum problem. Played with a few different implementations before settling on using itertools.combinations. I wanted both parts to be solved with one scalable function:
```python
def x_sum_prod(array: list, items: int, target: int) -> int:
    """Return the product of array items that sum to target. If not found, return -1."""
    for combo in combinations(array, r=items):
        if sum(combo) == target:
            return prod(combo)
    return -1
```
Not the fastest way to go, but the code is clean and easy to read. But, it didn't take me long to want to improve the performance, so I modified the function to remove one nested loop and also changed the input data from list to set for faster membership testing:
```python
def x_sum_prod(array: set, items: int, target: int) -> int:
    """
    Return the product of items number of array elements that sum to target.
    If not found, return -1.
    """
    for combo in combinations(array, r=items - 1):
        result = target - sum(combo)
        if result in array:
            return result * prod(combo)
    return -1
```

## Day 2: Password Philosophy
Pretty simple filtering. Left some earlier code in comments, and reworked to match my new init(), part_1(), part_2() format.

## Day 3: Toboggan Trajectory
Count trees on a repeating ASCII mountain. Although I was tempted to put the trees into a set to check for count/collisions, it felt better to leave the data as a list of strings instead.

## Day 4: Passport Processing
Another data testing / filtering puzzle. Put all of my tests into a dictionary to encapsulate the tests from the rest of the logic. After a few revisions, I added a regular expression to shorten test code.

## Day 5: Binary Boarding
This was a quick and fun one. After solving it, I realized I'd taken the instructions too literally. My original function decoded the strings like this:
```python
def id_seat(bsp_code: str) -> int:
    """Return int seat ID from boarding pass str binary space partitioning seat code."""
    seat = "".join(str(int(bit in "BR")) for bit in bsp_code.strip())
    row, col = int(seat[:7], 2), int(seat[7:], 2)
    return row * 8 + col
```
It was computing the decimal value of the binary codes for the seat row and column separately, multiplying the row by 8, and finally adding that to the column to get the full seat ID. But then I realized multiplying the row by 8 was the same as shifting it 3 bits over. The same 3 bits the seat column used! Now that I saw the seat code was actually contiguous, I simplified the function to treat the whole input as a single binary number and improved performance and readability.
```python
def id_seat(boarding_pass: str) -> int:
    """Return int seat ID from str boarding pass binary space partitioning seat code."""
    index_bsp = enumerate(reversed(boarding_pass.strip()))
    return sum((bit in "BR") << exp for exp, bit in index_bsp)
```

## Day 6: Custom Customs
Originally solved with list comps, I landed on using sets and set comps here for easier and faster filtering. This resulted in very short and dense, but readable code.

## Day 7: Handy Haversacks
A recursive luggage problem. Stumped on solving one of 2019's advent puzzles, I found code from someone who solved that problem with a queue instead of recursion and have been using a similar method for similar problems since then. I should probably put up a recursive verion for this day as well.

## Day 8: Handheld Halting
Simple virtual machine type problem, but nothing like the recurring int comp puzzles from last year. I might want to tackle this with 3.10's pattern matching at some point.

## Day 9: Encoding Error
Sort of a twist on a 2-sum problem. I don't remember much struggle from this day's puzzle, but when I updated the code to work with my timing/testing script I refined part two to improve performance by removing a few obvious inefficiencies. Originally looking like this:
```python
def find_weakness(xmas: tuple, target: int) -> int:
    """Return the sum of the min and max elements of the slice that sums to target."""
    right = xmas.index(target) - 1
    left = right - 1
    while (current := sum(xmas[left:right])) != target:
        if current > target:
            right -= 1
            left = right
        left -= 1
    return min(xmas[left:right]) + max(xmas[left:right])
```
It was starting its search near the index of the target, because that was better than starting at either end, but starting at the index nearest target / 2 is better. Also, I think I was being too cautious by resetting the length of the search slice to 2 each time the current sum went over the target. Finally, I was summing the entire slice on each loop and that was probably inefficient as well. Making those changes resulted in this:
```python
def find_weakness(xmas: tuple, target: int) -> int:
    """Return the sum of the min and max elements of the slice that sums to target."""

    left = right = next(i for i, x in enumerate(xmas) if x >= target // 2)
    current = xmas[left]

    while current != target:
        if current > target:
            current -= xmas[right]
            right -= 1
        left -= 1
        current += xmas[left]

    return min(xmas[left : right + 1]) + max(xmas[left : right + 1])
```
For my dataset the original function needed 498 iterations of the while loop to find the answer. The updated one only needs 58.

## Day 10: Adapter Array
I remember this one. Part one was easy and took almost no time to answer. Part two had me stumped, and I went down several dead ends before looking for solutions online. Though if I had stuck with it, I think I was on the right track with one of my ideas.

## Day 11: Seating System
This was a fun day to play with and optimize. Basically a play on Conway's Game of Life. When preparing to upload this, I refactored for performance and readability. Originally written within a class, the main neighbor checking loop looked like this:
```python
    def nearby_seats(self, r: int, c: int, adjacent_only: bool) -> int:
        occupied = 0
        for move_row, move_col in product(range(-1, 2), repeat=2):
            if move_row == move_col == 0:
                continue
            row, col = r + move_row, c + move_col
            while 0 <= row < self.height and 0 <= col < self.width:
                if self.seats[row][col] != ".":
                    occupied += self.seats[row][col] == "#"
                    break
                if adjacent_only == True:
                    break
                row += move_row
                col += move_col
        return occupied
```
After killing the class and refactoring into two more streamlined functions:
```python
def nearby(seats: dict, x: int, y: int) -> int:
    """Return count of nearby occupied seats (incluing origin seat if occupied)."""
    occupied = 0

    for x_move, y_move in product((-1, 0, 1), repeat=2):
        nearby = x + x_move, y + y_move
        while seats.get(nearby) == ".":
            nearby = nearby[0] + x_move, nearby[1] + y_move
        occupied += seats.get(nearby) == "#"

    return occupied


def adjacent(seats: dict, x: int, y: int) -> int:
    """Return count of adjacent occupied seats (incluing origin seat if occupied)."""
    adjacent = product(range(x - 1, x + 2), range(y - 1, y + 2))
    return sum(seats.get(spot) == "#" for spot in adjacent)
```
Though I split the original code into two similar functions, there isn't much overt code duplication. Splitting the functions also allowed for the removal of conditionals in these innermost loops which resulted in a fair overall performance boost.

Those changes rippled into the main update loop and help to take it from this:
```python
    def update(self, adjacent_only: bool) -> int:
        for row, col in product(range(self.height), range(self.width)):
            seat = self.seats[row][col]
            if seat == ".":
                continue
            occupied = self.nearby_seats(row, col, adjacent_only)
            if seat == "L" and occupied == 0:
                self.buffer[row][col] = "#"
            elif seat == "#" and occupied > 4 - adjacent_only:
                self.buffer[row][col] = "L"

        self.seats = [[*row] for row in self.buffer]
        return sum(row.count("#") for row in self.seats)
```
To this less busy version:
```python
def update(seats: dict, count_neighbors: Callable) -> dict:
    """Return dict of new seat state after simulating seat occupancy."""
    state = seats.copy()
    floor, empty, taken = ".L#"
    max_occupancy = 5 - (count_neighbors is adjacent)

    for seat, status in seats.items():
        if status == floor:
            continue
        neighbors = count_neighbors(seats, *seat)
        if status == empty and neighbors == 0:
            state[seat] = taken
        elif status == taken and neighbors > max_occupancy:
            state[seat] = empty

    return state
```
## Day 12: Rain Risk
This was another easy one. Most of the fun was in the refactoring. One of the ways I like to deal with coordinate based puzzles is to use complex numbers as 2D vectors. I'm happiest with the way they allowed me to code the waypoint turning in part two:
```python
elif action in "LR":
    if value == 180:
        waypoint *= -1
        continue
    waypoint = complex(-waypoint.imag, waypoint.real)  # rotate 90 deg right
    if (value == 270) ^ (action == "L"):
        waypoint *= -1  # if 270 deg xor left: flip the previous quarter turn
```
## Day 13: Shuttle Search
Some modulo math and alignment of bus schedules today. I do need to think of another way to standardize these scripts other than putting in the same boilerplate part_1 and part_2 functions. I'll do that when I get all my testing up and running. My current implementation will also break on any non-int output so I need to plan for string / ASCII-art output as well.

## Day 14: Docking Data
One of my favorite days yet. Take a bitmask and apply it to some values. Simple enough premise but with a ton of ways to implement it, I had a ton of fun refactoring. I originally solved both parts with string operations and list comprehensions that looked like this:
```python
def part_2(code: dict) -> int:
    mem = {}
    for mask, ops in code.items():
        for addr, value in ops:
            addr = f"{addr:0{36}b}"
            masked = [m if m != "0" else a for a, m in zip(addr, mask)]
            float_bits = [i for i, bit in enumerate(mask) if bit == "X"]
            length = len(float_bits)
            for float_combo in range(1 << length):
                float_binary = f"{float_combo:0{length}b}"
                for i, bit in enumerate(float_bits):
                    masked[bit] = float_binary[i]
                mem[int("".join(masked), 2)] = value
    return sum(mem.values())
```
But realized I wanted to practice using bitwise operations. I figured they would also simplify and speed up the code. One middle step looked something like this:
```python
def part_2(code: dict) -> int:
    mem = {}
    for (mask, show) ops in code.items():
        for addr, value in ops:
            floating = [i for i in range(36) if show & (1 << i)]
            for fill in product((0, 1), repeat=len(floating)):
                decoded = 0
                for i, bit in enumerate(floating):
                    decoded += fill[i] << bit
                mem[addr & ~show | mask | decoded] = value
    return sum(mem.values())
```
This middle step only had a modest improvement in execution time, but I think it was a little more readable. After trying and discarding a bunch of incremental optimizations to the logic calculating all possible floating addresses (using enumerate, zipping bit-lists together, using map and operator.lshift, etc.) my final version (for now) looks like this:
```python
def part_2(prog: Program) -> int:
    mem = {}
    for (mask, show), ops in prog.items():
        floating_bits = [1 << bit for bit in range(36) if show >> bit & 1]
        floating_sets = [
            sum(state)
            for count in range(len(floating_bits) + 1)
            for state in combinations(floating_bits, count)
        ]
        for addr, value in ops:
            partial_addr = addr & ~show | mask
            for floating_mask in floating_sets:
                mem[partial_addr | floating_mask] = value

    return sum(mem.values())
```
This version makes a few nice changes, pulls some calculations out of loops, and improves the code performance and readability. The original part_2 function took ~150 ms to complete and this version takes ~20 ms. One optimization I decided to leave out uses the bit_length() of the show mask instead of hardcoding range(36) to lower the number of iterations in the floating_bits list comprehension. The visual clutter just didn't seem worth the minor time gain.

## Day 15: Rambunctious Recitation
When I saw the description for today's puzzle I remembered watching a [Numberphile video](https://youtu.be/etMJxB-igrc) about Van Eck's sequence. This was pretty easy to code up. After exploring storing the numbers in a dict I ended up using a memory-inefficient list for lookup performance. My pure Python solution took ~4.35 seconds to run, and that felt too slow. While there doesn't seem to be any way to short-circuit iterating results, I dropped in two lines of code to use Numba and cut the total runtime down to ~770ms. I also played with array and numpy, saving memory by specifing data types, but they weren't any faster than stock lists once Numba was introduced.

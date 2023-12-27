def get_number(line_number, start_index):
    global lines
    number = ""
    index = start_index
    n = lines[line_number][index]
    # First search to the left
    while n.isdigit():
        number = f"{n}{number}"
        index -= 1
        n = lines[line_number][index]
    # Then search to the right
    index = start_index + 1
    n = lines[line_number][index]
    while n.isdigit():
        number = f"{number}{n}"
        index += 1
        n = lines[line_number][index]
    return int(number)


def check_number(line_number, char_index):
    global lines
    if lines[line_number][char_index].isdigit():
        return get_number(line_number, char_index)


def get_adjacent(line_number, char_index):
    global lines
    numbers = []
    start_index = max(0, char_index - 1)
    end_index = min(len(lines[0]) - 1, char_index + 1)
    # First check the current line
    if number := check_number(line_number, start_index):
        numbers.append(number)
    if number := check_number(line_number, end_index):
        numbers.append(number)
    # Then check the previous line (if it's not the first line)
    if line_number > 0:
        if number := check_number(line_number - 1, char_index):
            numbers.append(number)
        else:
            if number := check_number(line_number - 1, start_index):
                numbers.append(number)
            if number := check_number(line_number - 1, end_index):
                numbers.append(number)
    # Finally check the next line (if it's not the last line)
    if line_number < len(lines) - 1:
        if number := check_number(line_number + 1, char_index):
            numbers.append(number)
        else:
            if number := check_number(line_number + 1, start_index):
                numbers.append(number)
            if number := check_number(line_number + 1, end_index):
                numbers.append(number)
    return numbers


sum = 0
with open("schematic.txt", newline="") as file:
    lines = list(file)

for i in range(len(lines)):
    num = ""
    for j, char in enumerate(lines[i]):
        if char == "*":
            nums = get_adjacent(i, j)
            if len(nums) == 2:
                ratio = nums[0] * nums[1]
                sum += ratio

print(sum)

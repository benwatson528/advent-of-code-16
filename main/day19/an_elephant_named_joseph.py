def solve_p1(num_elves) -> int:
    elves = seat_elves(num_elves)
    curr_elf = elves.head
    while curr_elf != curr_elf.next:
        next_elf = curr_elf.next
        curr_elf.num_presents += next_elf.num_presents
        curr_elf.next = next_elf.next
        curr_elf = curr_elf.next
    return curr_elf.elf_id


def solve_p2(num_elves) -> int:
    print()
    elves = seat_elves(num_elves)
    curr_elf = elves.head
    current_elf_idx = 0
    num_elves_left = num_elves
    pre_half_way_elf = elves.head
    half_way_idx = num_elves_left // 2
    for _ in range(half_way_idx - 1):
        pre_half_way_elf = pre_half_way_elf.next

    while curr_elf != curr_elf.next:
        curr_elf.num_presents += pre_half_way_elf.next.num_presents
        pre_half_way_elf.next = pre_half_way_elf.next.next
        curr_elf = curr_elf.next
        current_elf_idx += 1
        num_elves_left -= 1
        old_half_way = half_way_idx
        half_way_idx = (num_elves_left // 2) + current_elf_idx
        half_way_moves = half_way_idx - old_half_way
        for _ in range(half_way_moves):
            pre_half_way_elf = pre_half_way_elf.next

    return curr_elf.elf_id


def seat_elves(num_elves):
    elves = LinkedList()
    elves.head = Node(1)
    curr = elves.head
    for e in range(1, num_elves):
        curr.next = Node(e + 1)
        curr = curr.next
    curr.next = elves.head
    return elves


class Node:
    def __init__(self, elf_id):
        self.elf_id = elf_id
        self.num_presents = 1
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

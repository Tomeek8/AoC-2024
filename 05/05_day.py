from collections import defaultdict


def process_data(path):
    with open(path) as f:
        rules, updates = f.read().split("\n\n")
    rules = [list(map(int, rule.split("|"))) for rule in rules.splitlines()]
    updates = [list(map(int, update.split(","))) for update in updates.splitlines()]
    return rules, updates


def is_valid(update, rules_dict):
    for i, num in enumerate(update[:-1]):
        if not set(update[i + 1 :]).issubset(rules_dict[num]):
            return False
    return True


def find_mid_num(update):
    return int(update[len(update) // 2])


def repair_update(update, rules_dict):
    adjusted_rules = {}
    for num in update:
        adjusted_rules[num] = rules_dict[num].intersection(update)
    update_repaired = sorted(update, key=lambda x: len(adjusted_rules[x]), reverse=True)
    return update_repaired


rules, updates = process_data("./05/input.txt")
rules_dict = defaultdict(set)
for left, right in rules:
    rules_dict[left].add(right)

# Part 1
total = 0
invalid_updates = []
for update in updates:
    if is_valid(update, rules_dict):
        total += find_mid_num(update)
    else:
        invalid_updates.append(update)

# Part 2
total2 = 0
for update in invalid_updates:
    total2 += find_mid_num(repair_update(update, rules_dict))


print(f"Part 1 result: {total}")
print(f"Part 2 result: {total2}")

from math import ceil

section1 = input("How many planks do you have in section 1 (Use Fs): ")
section2 = input("How many planks do you have in section 2 (Use Fs): ")
section3 = input("How many planks do you have in section 3 (Use Fs): ")

plank_total = len(section1) + len(section2) + len(section3)
crates = ceil(plank_total / 12)

print(f"You need {plank_total} cans of paint.")
print(f"You will have {12 * crates - plank_total} leftover.")
print(f"The final cost will be ${14.95 * crates}")
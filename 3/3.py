#!/usr/bin/env python3

def compute_gamma_bits(lines, eq_bit=1):
  sums = [0] * len(lines[0])
  for l in lines:
    for i, c in enumerate(l):
      sums[i] += int(c)
  gamma_bits = []
  for s in sums:
    if s > len(lines) // 2:
      gamma_bits.append(1)
    elif s == len(lines) // 2:
      gamma_bits.append(eq_bit)
    else:
      gamma_bits.append(0)
  return gamma_bits

def part_1(lines):
  gamma_bits = compute_gamma_bits(lines)
  gamma_rate, epsilon_rate = 0, 0
  for i, bit in enumerate(reversed(gamma_bits)):
    gamma_rate += bit * (2 ** i)
    epsilon_rate += (1 - bit) * (2 ** i)
  print(f"part 1: {gamma_rate * epsilon_rate}")

def compute_scrubber_rating(lines, flip=False):
  filtered_lines = list(lines)
  for i in range(len(lines[0])):
    next_filtered_lines = []
    total = 0
    for l in filtered_lines:
      total += int(l[i])
    gamma_bit = 0
    if total >= len(filtered_lines) / 2:
      gamma_bit = 1
    if flip: gamma_bit = 1 - gamma_bit
    for l in filtered_lines:
      if int(l[i]) == gamma_bit:
        next_filtered_lines.append(l)
    filtered_lines = next_filtered_lines
    if len(filtered_lines) <= 1: break
  l = filtered_lines[0]
  return sum(int(b) * (2 ** i) for (i, b) in enumerate(reversed(l)))

def part_2(lines):
  o2 = compute_scrubber_rating(lines)
  co2 = compute_scrubber_rating(lines, flip=True)
  print(f"part 2: {o2 * co2}")

lines = [l.rstrip() for l in open("input.txt")]
#lines = [ "00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010" ]
part_1(lines)
part_2(lines)
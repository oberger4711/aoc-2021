#!/usr/bin/env python3

def part_1(instructions):
  x, depth = 0, 0
  for (op, arg) in instructions:
    arg = int(arg)
    if op == "forward":
      x += arg
    elif op == "down":
      depth += arg
    elif op == "up":
      depth -= arg
    else:
      print(f"Invalid op {op}.")
      return
  print(f"Part 1: {x * depth}")

def part_2(instructions):
  x, depth, aim = 0, 0, 0
  for (op, arg) in instructions:
    arg = int(arg)
    if op == "forward":
      x += arg
      depth += aim * arg
    elif op == "down":
      aim += arg
    elif op == "up":
      aim -= arg
    else:
      print(f"Invalid op {op}.")
      return
  print(f"Part 2: {x * depth}")

instructions = [tuple(l.rstrip().split(" ")) for l in open("input.txt")]
part_1(instructions)
part_2(instructions)
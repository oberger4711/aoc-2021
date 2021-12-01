#!/usr/bin/env python3

def part_1(nums):
  prev = nums[0]
  count = 0
  for cur in nums[1:]:
    if cur > prev: count += 1
    prev = cur
  print(count)

def part_2(nums):
  cur_window_sum = sum(nums[:3])
  prev_window_sum = cur_window_sum
  count = 0
  for i in range(3, len(nums)):
    cur_window_sum += nums[i] - nums[i - 3]
    if cur_window_sum > prev_window_sum: count += 1
    prev_window_sum = cur_window_sum
  print(count)

nums = [int(l) for l in open("input.txt")]
#nums = [ 199, 200, 208, 210, 200, 207, 240, 269, 260, 263 ]
part_1(nums)
part_2(nums)
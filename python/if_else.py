#!/usr/bin/env python3

if __name__ == '__main__':
  n = int(input().strip())

  if n % 2 == 1:
    print("Weird")
  elif n >= 2 and n < 6:
    print("Not Weird")
  elif n >= 6 and n < 21:
    print("Weird")
  elif n >= 21:
    print("Not Weird")

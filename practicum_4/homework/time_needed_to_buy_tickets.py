from typing import Any

import yaml
import numpy as np
from queue import Queue


def time_taken(tickets: list[int], k: int) -> int:
    seconds_elapsed = 0
    q = Queue()
    for i in range(len(tickets)):
        q.put((tickets[i], i))

    while not q.empty():
        el, pos = q.get()
        if el - 1 > 0:
            q.put((el - 1, pos))

        seconds_elapsed += 1

        if el - 1 == 0 and pos == k:
            return seconds_elapsed

    return seconds_elapsed


if __name__ == "__main__":
    # Let's solve Time Needed to Buy Tickets problem from leetcode.com:
    # https://leetcode.com/problems/time-needed-to-buy-tickets/
    with open("practicum_4/time_needed_to_buy_tickets_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)
    for c in cases:
        res = time_taken(tickets=c["input"]["tickets"], k=c["input"]["k"])
        print(f"Input: {c['input']}. Output: {res}. Expected output: {c['output']}")

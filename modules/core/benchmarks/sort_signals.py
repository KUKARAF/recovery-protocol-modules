"""Size-scaling input generator for sort_signals, used to estimate empirical
time/space complexity. Not part of the task - don't edit."""

import random


def scale_input(n: int) -> tuple:
    data = list(range(n))
    random.Random(42).shuffle(data)  # fixed seed: reproducible across runs
    return (data,)

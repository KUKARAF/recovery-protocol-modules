"""Size-scaling input generator for chunk_list, used to estimate empirical
time/space complexity. Not part of the task - don't edit."""


def scale_input(n: int) -> tuple:
    return (list(range(n)), 10)

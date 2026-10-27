"""Size-scaling input generator for find_duplicates, used to estimate
empirical time/space complexity. Not part of the task - don't edit."""


def scale_input(n: int) -> tuple:
    half = max(n // 2, 1)
    return ([i % half for i in range(n)],)

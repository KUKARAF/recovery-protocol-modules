"""Size-scaling input generator for decode_status, used to estimate
empirical time/space complexity. Not part of the task - don't edit."""


def scale_input(n: int) -> tuple:
    return ("SOFU" * (n // 4 + 1),)

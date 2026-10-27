"""Size-scaling input generator for normalize_whitespace, used to estimate
empirical time/space complexity. Not part of the task - don't edit."""


def scale_input(n: int) -> tuple:
    return (" ".join(["word"] * n),)

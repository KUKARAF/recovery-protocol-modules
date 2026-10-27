"""Size-scaling input generator for invert_mapping, used to estimate
empirical time/space complexity. Not part of the task - don't edit."""


def scale_input(n: int) -> tuple:
    return ({f"k{i}": f"v{i}" for i in range(n)},)

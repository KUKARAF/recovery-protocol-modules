"""Size-scaling input generator for filter_logs, used to estimate empirical
time/space complexity. Not part of the task - don't edit."""


def scale_input(n: int) -> tuple:
    return ([f"[ERR] e{i}" if i % 2 == 0 else f"[SYS] s{i}" for i in range(n)],)

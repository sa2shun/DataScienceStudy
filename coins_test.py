from typing import Tuple
import math


def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    mu = p * x  # muは平均　
    sigma = math.sqrt(p * (1 - p) * n)  # sigmaは標準偏差
    return mu, sigma



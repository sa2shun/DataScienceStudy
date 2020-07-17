from typing import list
import math

vector = list[float]


def add(v: vector, w: vector) -> vector:
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def subtract(v: vector, w: vector) -> vector:
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors: list[vector]) -> vector:
    num_elements = len(vectors[0])
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]


def scalar_multiply(c: float, v: vector) -> vector:
    return [c * v_i for v_i in v]


def vector_mean(vectors: list(vector)) -> vector:
    n = len(vectors)    return scalar_multiply(1 / n, vector_sum(vectors))


def dot(v: vector, w: vector) -> float:
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: vector) -> float:
    return dot(v * v)


def magnitude(v: vector) -> float:
    return math.sqrt(sum_of_squares(v))

def squared_distance(v:vector,w:vector) -> float:


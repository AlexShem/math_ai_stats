import numpy as np

PROBABILITY_HEAD = 0.54


def flip_coin(p: float | None = PROBABILITY_HEAD) -> int:
    """Random coin flip.

    The function flips a coin (possibly, *unfair*) and returns:

    - 1, if the coin lands on `head`,
    - 0, if the coin lands on `tail`.

    **Example usage:**

    >>> flip = flip_coin(0.5)

    **Output:**

    >>> print(flip)
    >>> 1  # May vary

    :param p: Probability of the coin to land on `head`. Should be in [0, 1].
              If None, the default probability (0.54) will be used.
    :type p: float or None
    :return: (int): ``1`` if `head` and ``0`` if `tail`.
    :rtype: int
    """
    if p is None:
        p = PROBABILITY_HEAD

    if p > 1.0 or p < 0.0:
        raise ValueError(f"Parameter `p` should be in [0, 1]. Got {p} instead.")

    return 1 if np.random.rand() <= p else 0

"""간단한 계산기: 더하기와 빼기 기능을 제공합니다."""


def add(a: float, b: float) -> float:
    """두 수를 더합니다."""
    return a + b


def subtract(a: float, b: float) -> float:
    """첫 번째 수에서 두 번째 수를 뺍니다."""
    return a - b


if __name__ == "__main__":
    print("더하기: 10 + 3 =", add(10, 3))
    print("빼기: 10 - 3 =", subtract(10, 3))

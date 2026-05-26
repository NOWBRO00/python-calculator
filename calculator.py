"""간단한 계산기: 사칙연산(더하기, 빼기, 곱하기, 나누기) 기능을 제공합니다."""


def add(a: float, b: float) -> float:
    """두 수를 더합니다."""
    return a + b


def subtract(a: float, b: float) -> float:
    """첫 번째 수에서 두 번째 수를 뺍니다."""
    return a - b


def multiply(a: float, b: float) -> float:
    """두 수를 곱합니다."""
    return a * b


def divide(a: float, b: float) -> float:
    """첫 번째 수를 두 번째 수로 나눕니다."""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b


if __name__ == "__main__":
    print("더하기: 10 + 3 =", add(10, 3))
    print("빼기: 10 - 3 =", subtract(10, 3))
    print("곱하기: 10 * 3 =", multiply(10, 3))
    print("나누기: 10 / 3 =", divide(10, 3))

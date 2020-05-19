import random
import os

from pyfiglet import Figlet

FONTS = open(os.path.join(os.path.dirname(__file__), "fonts.txt")).read().splitlines()


def generate_term(cnt):
    assert cnt > 0
    if cnt == 1:
        num = random.randint(1, 9)
        return num, str(num), 2

    a = random.randint(1, cnt - 1)
    left = generate_term(a)
    right = generate_term(cnt - a)
    operator = random.choice("+-*" + "/" * (right[0] != 0 and left[0] % right[0] == 0))
    if operator == "+":
        result = left[0] + right[0]
        term = f"{left[1]}+{right[1]}"
    elif operator == "-":
        result = left[0] - right[0]
        term = f"{left[1]}-"
        if right[2]:
            term += f"{right[1]}"
        else:
            term += f"({right[1]})"
    elif operator == "*":
        result = left[0] * right[0]
        if left[2]:
            term = f"{left[1]}"
        else:
            term = f"({left[1]})"
        term += "*"
        if right[2]:
            term += f"{right[1]}"
        else:
            term += f"({right[1]})"
    elif operator == "/":
        result = left[0] // right[0]
        if left[2]:
            term = f"{left[1]}"
        else:
            term = f"({left[1]})"
        term += "/"
        if right[2] == 2:
            term += f"{right[1]}"
        else:
            term += f"({right[1]})"
    else:
        assert False
    return result, term, operator == "*"


def validate_term_generator():
    for cnt in range(2, 200):
        print(f"cnt={cnt}")
        for _ in range(200):
            solution, term, _ = generate_term(cnt)
            actual = eval(term.replace("/", "//"))
            if actual != solution:
                print("WRONG", term, solution, actual)
                return False
    return True


def generate_captcha(difficulty):
    solution, term, _ = generate_term(difficulty)
    font = random.choice(FONTS)
    return solution, Figlet(font=font, width=150).renderText(term), term, font


def main():
    total = correct = 0
    while True:
        solution, challenge, term, font = generate_captcha(4)
        print(challenge)
        answer = input(">> ")
        print(answer == str(solution), solution, term, font)
        total += 1
        if answer != str(solution):
            input()
        else:
            correct += 1
        print(correct, total, correct / total * 100)


if __name__ == "__main__":
    main()

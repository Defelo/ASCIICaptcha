from asciicaptcha import generate_captcha


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

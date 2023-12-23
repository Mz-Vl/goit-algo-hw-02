from collections import deque


def palindrome_check(string):
    processed_string = "".join(string.lower().split())

    d = deque(processed_string)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False

    return True


print(palindrome_check("шалАш шал аш"))
print(palindrome_check("Palindr ome"))

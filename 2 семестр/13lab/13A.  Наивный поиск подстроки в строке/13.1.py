

with open("search1.in", "r", encoding='utf-8') as file:
    with open("search1.out", "w", encoding="utf-8") as output:

        s = list(map(str, file.readline()))

        t = list(map(str, file.readline()))

        s = s[:len(s) - 1]

        n = len(t)

        m = len(s)

        cnt = 0

        for i in range(n - m + 1):

            if t[i: i + (m)] == s:
                cnt = cnt + 1

                output.write(str(i + 1) + " ")

with open("search1.out", "r", encoding='utf-8') as output:
    tmp = output.readlines()


with open("search1.out", "w", encoding='utf-8') as file:

    file.write(str(cnt) + "\n")

    file.writelines(tmp)

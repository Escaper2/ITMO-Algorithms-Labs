

with open("prefix.in", "r", encoding='utf-8') as file:
    with open("prefix.out", "w", encoding="utf-8") as output:

        s = file.readline().strip()

        n = len(s)

        prefix = [0] * (len(s) + 1)

        i = 1
        j = 0

        while i < n:
            if s[i] == s[j]:
                i = i + 1
                j = j + 1
                prefix[i] = j
            else:
                if j > 0:
                    j = prefix[j]

                else:
                    i = i + 1
                    prefix[i] = 0

        [output.write(str(prefix[i]) + " ") for i in range(1,n+1)]

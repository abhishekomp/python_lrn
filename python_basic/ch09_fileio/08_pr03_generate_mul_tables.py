for i in range(2, 11):
    with open(f"mul_tables/MultiplicationTable_{i}.txt", "w") as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i * j}")
            if j != 10:
                f.write("\n")
    # break

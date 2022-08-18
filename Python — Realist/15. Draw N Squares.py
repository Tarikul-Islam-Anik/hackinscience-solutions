def draw_n_squares(n):
    odd_line = "+---" * n + "+"
    even_line = "|   " * n + "|"
    final_line = "+---" * n + "+"
    return (odd_line + "\n" + even_line + "\n") * n + final_line

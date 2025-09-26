from pybricks.tools import hub_menu

selected = hub_menu("A", "B", "C", "D", "E")

if selected == "A":
    import run_a
elif selected == "B":
    import run_b
elif selected == "C":
    import run_c
elif selected == "D":
    import run_d
elif selected == "E":
    import reset
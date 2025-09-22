from pybricks.tools import hub_menu

selected = hub_menu("A", "B", "C", "D", "E")

if selected == "A":
    import run_a
elif selected == "B":
    import run_b
elif selected == "C":
    import mission_salvage_operation
elif selected == "D":
    import mission_paint_brush
elif selected == "E":
    import reset
from pybricks.tools import hub_menu

selected = hub_menu("A", "B", "C", "D")

if selected == "A":
    import mission_silo
elif selected == "B":
    import mission_tip_the_scales
elif selected == "C":
    import mission_salvage_operation
elif selected == "D":
    import mission_paint_brush
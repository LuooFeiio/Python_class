employee_info = {
    "Lee": {"部门": "科技部", "工资": 3000, "级别": 1},
    "Law": {"部门": "市场部", "工资": 5000, "级别": 2},
    "Tom": {"部门": "市场部", "工资": 7000, "级别": 3},
    "Tim": {"部门": "科技部", "工资": 4000, "级别": 1},
    "Flo": {"部门": "市场部", "工资": 6000, "级别": 2}
}
print("Pre: ", employee_info)
for ele in employee_info:
    if employee_info[ele]["级别"] == 1:
        employee_info[ele]["级别"] += 1
        employee_info[ele]["工资"] += 1000
print("Pos: ", employee_info)
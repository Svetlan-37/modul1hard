grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]      # дано
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}                            # дано
students = list(students)                                        # преобразовываем множество в список
students.sort()                                                  # сортируем по алфавиту
sr_ball = [sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])]
result = dict(zip(students, sr_ball))        # zip()-объединили два списка, dict()-преобразовали в словарь
print(result)

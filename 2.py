# Визначення класу Teacher
class Teacher:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        email: str,
        can_teach_subjects: set[str],
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects


def create_schedule(subjects: set[str], teachers: list[Teacher]) -> dict[Teacher, set[str]]:
    schedule = {}
    available_teachers = teachers.copy()
    uncovered_subjects = subjects.copy()

    while uncovered_subjects:
        best_teacher = max(
            available_teachers,
            key=lambda teacher: (
                len(teacher.can_teach_subjects & uncovered_subjects),
                -teacher.age,
            ),
        )

        assigned_subjects = best_teacher.can_teach_subjects & uncovered_subjects
        if not assigned_subjects:
            return None

        schedule[best_teacher] = assigned_subjects
        uncovered_subjects -= best_teacher.can_teach_subjects
        available_teachers.remove(best_teacher)

    return schedule


if __name__ == "__main__":
    # Множина предметів
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}
    # Створення списку викладачів
    teachers = [
        Teacher(
            "Олександр",
            "Іваненко",
            45,
            "o.ivanenko@example.com",
            {"Математика", "Фізика"},
        ),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher(
            "Сергій",
            "Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}
        ),
        Teacher(
            "Дмитро",
            "Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher, assigned_subjects in schedule.items():
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(assigned_subjects)}")
            print()
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")

class Student:
    def __init__(self, name: str, marks: list[float]):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if not self.marks:
            return False
        return (sum(self.marks) / len(self.marks)) > 50

    def __str__(self) -> str:
        avg = sum(self.marks) / len(self.marks) if self.marks else 0
        return f"{self.name} (oceny: {self.marks}, średnia: {avg:.1f})"


student_passed = Student("Dominika Nowak", [60, 75, 80])
student_failed = Student("Jakub Kowalski", [30, 45, 50])

print(f"{student_passed.name} zdał/a: {student_passed.is_passed()}")
print(f"{student_failed.name} zdał/a: {student_failed.is_passed()}\n")

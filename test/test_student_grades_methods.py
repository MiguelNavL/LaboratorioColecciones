import unittest
from custom_functions import student_grades_methods


class TestCollectionMethods(unittest.TestCase):

    def test_calculate_final_grade(self):

        list_grades = [3, 3, 4, 5]
        grade = student_grades_methods.calculate_final_grade(list_grades)

        self.assertEqual(grade, 3.75)

    def test_calculate_best_grade(self):

        list_grades = [3, 3, 4, 4.5, 3.2, 2.4, 3.7]
        best_grade = student_grades_methods.calculate_best_grade(list_grades)

        # The best grade must be 4.5
        self.assertEqual(best_grade, 4.5)

    def test_remove_worst_grade(self):

        list_grades = [3, 4, 1, 4, 2]
        new_list = student_grades_methods.remove_worst_grade(list_grades)

        # The list must not contain 1, that is the worst grade
        self.assertListEqual(new_list, [3, 4, 4, 2])


if __name__ == '__main__':
    unittest.main()

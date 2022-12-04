import json
import os


class data_manager():
    def __init__(self, file_path):
        self.file_path = file_path

    def __del__(self):
        try:
            self._close_file()
        except:
            pass
        finally:
            pass

    def _open_file(self, mode="r"):
        self.file_ob = open(self.file_path, mode)

    def _close_file(self):
        self.file_ob.close()

    def _read_file(self):
        self._open_file()
        json_data = json.load(self.file_ob)
        self._close_file()
        return json_data

    def _write_file(self, data: dict):
        """directly wrights data to the file
        WARNING DATA WILL BE OVERWRITTEN AND MAY CAUSE PERMANENT DATA LOSS"""

        json_data = json.dumps(data, indent=4)

        self._open_file(mode="w")
        self.file_ob.write(json_data)
        self._close_file()

    def calc_gpa(self, classes: list) -> float:
        """
        calculates gpa on a 4.0 scale
        """
        a = 0
        b = 0
        c = 0
        d = 0
        f = 0
        total_num = 0
        for clas in classes:
            if 90 <= clas["grade"] <= 100:
                a += 1
                total_num += 1
            elif 80 <= clas["grade"] <= 89:
                b += 1
                total_num += 1
            elif 70 <= clas["grade"] <= 79:
                c += 1
                total_num += 1
            elif 60 <= clas["grade"] <= 69:
                d += 1
                total_num += 1
            else:
                f += 1
                total_num += 1
        total = (a * 4) + (b * 3) + (c * 2) + d
        gpa = total / total_num
        return gpa

    def write_new_student(self, name: str, classes: list):
        """safely adds a new student"""
        data = self._read_file()
        gpa = self.calc_gpa(classes)
        student_data = {"name": name, "classes": classes, "GPA": gpa}
        students = data["students"]
        students.append(student_data)
        data["students"] = students
        self._write_file(data)

    def remove_student(self, name: str):
        index = self.search_student_index(name)
        data = self._read_file()
        data["students"].pop(index)
        self._write_file(data)

    def search_student_index(self, name: str) -> int:
        """
        Searches for a student and returns the index of their location
        """
        data = self._read_file()
        for i in range(len(data["students"])):
            if data["students"][i]["name"] == name:
                return i

    def student_data(self, name: str):
        index = self.search_student_index(name)

        data = self._read_file()
        student = data["students"][index]
        return student


def test_mod():
    test_classes = [{"class_name": "math", "grade": 100, "teacher": "mrs.bin"},
                    {"class_name": "hist", "grade": 100, "teacher": "mrs.bin"}]

    test = data_manager(os.path.join(".", "group_1", "data", "test_data.json"))
    test.write_new_student("gaer", test_classes)
    student_data = test.student_data("gaer")

    if student_data["name"] != "gaer":
        return False
    elif student_data["GPA"] != 4.0:
        return False

    test.remove_student("gaer")
    return True


if __name__ == "__main__":
    test_mod()

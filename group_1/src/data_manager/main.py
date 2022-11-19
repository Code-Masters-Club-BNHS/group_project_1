import json
import os
class data_manager():
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_ob = open(file_path)

        print("created")

    def __del__(self):
        self._close_file()

        print("destroyed")

    def _open_file(self, mode = "r"):
        self.file_ob = open(self.file_path, mode)

    def _close_file(self):
        self.file_ob.close()

    def _read_file(self):
        json_data = json.load(self.file_ob)
        return json_data

    def _write_file(self, data: dict):
        json_data = json.dumps(data, indent = 4)

        self._close_file()
        self._open_file(mode="w")
        self.file_ob.write(json_data)
        self._close_file()
        self._open_file()

    def write_new_student(self, name: str, classes: list):
        data = self._read_file()
        student_data = {"name": name, "classes": classes}
        students = data["students"]
        students.append(student_data)
        data["students"] = students
        self._write_file(data)

    def remove_student(self, name: str):
        pass
    def search_student(self, name: str):
        pass


if __name__ == "__main__":
    test_classes = {"class_name": "english", "grade": 0, "teacher": "mrs.bitch"}

    test = data_manager(os.path.join(".", "group_1", "data", "schema.json"))
    test.write_new_student("gaer", test_classes)

import unittest
from todo import Task, add_task, format_task


class TestAddTask(unittest.TestCase):

    def test_increases_list_length(self):
        # 빈 리스트에 할 일을 추가하면 길이가 1이 돼야 한다
        tasks = []
        add_task(tasks, "장보기")
        self.assertEqual(len(tasks), 1)

    def test_correct_name(self):
        # 추가된 Task의 이름이 입력값과 같아야 한다
        tasks = []
        add_task(tasks, "운동하기")
        self.assertEqual(tasks[0].name, "운동하기")

    def test_done_defaults_to_false(self):
        # 새로 추가된 Task는 완료되지 않은 상태(False)여야 한다
        tasks = []
        add_task(tasks, "독서하기")
        self.assertFalse(tasks[0].done)

    def test_created_at_is_set(self):
        # created_at이 자동으로 채워져야 한다 (빈 문자열이 아닌지 확인)
        tasks = []
        add_task(tasks, "청소하기")
        self.assertNotEqual(tasks[0].created_at, "")

    def test_returns_same_list(self):
        # 반환값이 원본 리스트와 동일한 객체여야 한다 (복사본을 만들지 않음)
        tasks = []
        result = add_task(tasks, "요리하기")
        self.assertIs(result, tasks)

    def test_add_to_empty_list(self):
        # 빈 리스트에서도 오류 없이 동작해야 한다
        tasks = []
        result = add_task(tasks, "빈 리스트 테스트")
        self.assertEqual(len(result), 1)

    def test_multiple_times(self):
        # 여러 번 추가하면 입력한 순서대로 쌓여야 한다
        tasks = []
        add_task(tasks, "첫 번째")
        add_task(tasks, "두 번째")
        add_task(tasks, "세 번째")
        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[0].name, "첫 번째")
        self.assertEqual(tasks[1].name, "두 번째")
        self.assertEqual(tasks[2].name, "세 번째")


class TestFormatTask(unittest.TestCase):

    def test_not_done_shows_empty_bracket(self):
        # 완료되지 않은 Task는 [ ] (공백) 으로 표시돼야 한다
        task = Task(name="운동하기", done=False, created_at="2026-01-01 09:00:00")
        result = format_task(1, task)
        self.assertIn("[ ]", result)

    def test_done_shows_x_bracket(self):
        # 완료된 Task는 [x] 로 표시돼야 한다
        task = Task(name="운동하기", done=True, created_at="2026-01-01 09:00:00")
        result = format_task(1, task)
        self.assertIn("[x]", result)

    def test_contains_name(self):
        # 출력 문자열에 Task 이름이 포함돼야 한다
        task = Task(name="독서하기", done=False, created_at="2026-01-01 09:00:00")
        result = format_task(1, task)
        self.assertIn("독서하기", result)

    def test_contains_index(self):
        # index=2 (0-based 3번째)를 전달하면 화면에는 3번으로 시작해야 한다
        task = Task(name="장보기", done=False, created_at="2026-01-01 09:00:00")
        result = format_task(2, task)
        self.assertTrue(result.startswith("3."))

    def test_contains_created_at(self):
        # 출력 문자열에 생성 시간이 포함돼야 한다
        task = Task(name="청소하기", done=False, created_at="2026-05-12 10:30:00")
        result = format_task(1, task)
        self.assertIn("2026-05-12 10:30:00", result)

    def test_format_structure(self):
        # index=1 (0-based 2번째)를 전달하면 "2. [ ] 이름  (날짜)" 형식이어야 한다
        task = Task(name="요리하기", done=False, created_at="2026-01-01 00:00:00")
        result = format_task(1, task)
        self.assertEqual(result, "2. [ ] 요리하기  (2026-01-01 00:00:00)")

    def test_index_zero_displays_as_one(self):
        # index=0 (0번째)을 전달하면 화면에는 1번으로 표시돼야 한다
        task = Task(name="테스트", done=False, created_at="2026-01-01 00:00:00")
        result = format_task(0, task)
        self.assertTrue(result.startswith("1."))


if __name__ == "__main__":
    unittest.main()

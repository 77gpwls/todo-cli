import json
from dataclasses import asdict, dataclass, field
from datetime import datetime


@dataclass
class Task:
    name: str
    done: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def add_task(tasks, task_name):
    tasks.append(Task(name=task_name))
    return tasks


def format_task(index, task):
    status = "x" if task.done else " "
    return f"{index + 1}. [{status}] {task.name}  ({task.created_at})"


def delete_task(tasks: list[Task], index: int) -> list[Task]:
    """0-based index에 해당하는 Task를 리스트에서 삭제하고 반환한다."""
    if index < 0 or index >= len(tasks):
        raise IndexError(f"index {index}는 유효한 범위(0~{len(tasks) - 1})가 아닙니다.")
    tasks.pop(index)
    return tasks


def save_tasks(tasks: list[Task], filename: str = 'tasks.json') -> None:
    """할일 목록을 JSON 파일로 저장한다."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump([asdict(task) for task in tasks], f, ensure_ascii=False, indent=2)


def load_tasks(filename: str = 'tasks.json') -> list[Task]:
    """JSON 파일에서 할일 목록을 불러온다. 파일이 없으면 빈 리스트를 반환한다."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return [Task(**item) for item in json.load(f)]
    except FileNotFoundError:
        return []


def main():
    tasks = load_tasks()
    if not tasks:
        for name in ['장보기', '운동하기', '독서하기']:
            tasks = add_task(tasks, name)
        tasks[1].done = True
        save_tasks(tasks)

    for i, task in enumerate(tasks, start=0):
        print(format_task(i, task))


if __name__ == '__main__':
    main()

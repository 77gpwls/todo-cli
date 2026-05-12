# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# 앱 실행
python3 todo.py

# 전체 테스트 실행
python3 -m unittest test_todo.py -v

# 특정 테스트 하나만 실행
python3 -m unittest test_todo.TestFormatTask.test_format_structure -v
```

> `pytest`는 설치되어 있지 않으므로 내장 `unittest`를 사용한다.

## Architecture

`todo.py` 단일 파일로 구성된 CLI 앱이다.

- **`Task` (dataclass)** — 할 일 데이터. `name`, `done(bool)`, `created_at(str)` 필드를 가진다. `created_at`은 생성 시점의 날짜/시간으로 자동 설정된다.
- **`add_task(tasks, task_name)`** — 리스트에 새 Task를 추가하고 같은 리스트 객체를 반환한다 (in-place 수정).
- **`format_task(index, task)`** — 0-based `index`를 받아 `"{index+1}. [x/공백] 이름  (날짜)"` 형식의 문자열을 반환한다.
- **`main()`** — `enumerate(tasks, start=0)`으로 순회하며 `format_task`에 0-based 인덱스를 전달한다.

## Coding conventions

- 모든 함수에 타입 힌트를 작성한다.
  ```python
  def add_task(tasks: list[Task], task_name: str) -> list[Task]:
  ```
- 모든 함수에 docstring을 작성한다.
  ```python
  def add_task(tasks: list[Task], task_name: str) -> list[Task]:
      """tasks 리스트에 새 Task를 추가하고 같은 리스트를 반환한다."""
  ```

## Commit message format

`동사: 내용` 형식을 따른다.

```
add: 할일 완료 기능 추가
fix: index=0일 때 번호 표시 오류 수정
remove: 미사용 함수 삭제
```

## Notes

- `tasks.json`은 사용자 데이터 파일이다. 코드 변경 시 절대 삭제하지 않는다.

## Testing conventions

테스트는 `test_todo.py`에 `unittest.TestCase` 기반으로 작성한다.

- `TestAddTask` — `add_task` 함수 검증
- `TestFormatTask` — `format_task` 함수 검증
- `format_task` 테스트에서 Task를 직접 생성할 때는 `created_at`을 고정값으로 지정해 예측 가능한 출력을 만든다.
  ```python
  task = Task(name="예시", done=False, created_at="2026-01-01 00:00:00")
  ```

import todo_manager as tm


if __name__ == "__main__":
    task1 = tm.Task(
        title="Buy milk",
        description="Buy in store"
    )
    tm.create_task(task1)

    task2 = tm.Task(
        title="But pepsi"
    )
    tm.create_task(task2)

    print(tm.get_tasks(pretty=True))

    tm.update_task(
        task1,
        completed=True
    )

    print(tm.get_tasks(pretty=True))

    tm.delete_task(task2._id)
    print(tm.get_tasks(pretty=True))  # Task 2 deleted

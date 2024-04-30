from enum import Enum  # Импортируем Enum из модуля enum

class TaskStatus(Enum):  # Создаем перечисление TaskStatus
    TODO = "TODO"  # Статус задачи "TODO" - яғни тапсырма әлі басталмаған кезде
    IN_PROGRESS = "IN_PROGRESS"  # Тапсырма күйі "IN_PROGRESS" - яғни тапсырма орындалып жатқанда
    DONE = "DONE"  # Тапсырманың күйі «ДАЙЫН» – яғни тапсырма орындалған кезде

class Task:  # Создаем класс задачи
    def __init__(self, title, status=TaskStatus.TODO):  # Конструктор класса, задаем заголовок и статус по умолчанию "TODO"
        self.title = title  # Устанавливаем заголовок задачи
        self.status = status  # Устанавливаем статус задачи

    def change_status(self, new_status):  # Тапсырма күйін өзгерту әдісі
        return Task(self.title, new_status)  # Возвращаем новый экземпляр задачи с обновленным статусом

class TaskManager:  # Создаем класс менеджера задач
    def __init__(self):  # Конструктор класса
        self.tasks = []  # Инициализируем список задач

    def add_task(self, task):  # Метод добавления задачи
        self.tasks.append(task)  # Тізімге тапсырма қосу

    def get_all_tasks(self):  # Метод получения всех задач
        return self.tasks  # Барлық тапсырмалар тізімін қайтару

    def get_tasks_by_status(self, status):  # Күй бойынша тапсырмаларды алу әдісі
        return [task for task in self.tasks if task.status == status]  # Берілген күйі бар тапсырмалар тізімін қайтару

def change_task_status(task_manager, task_title, new_status):  # Тапсырма күйін өзгерту функциясы
    updated_tasks = [task.change_status(new_status) if task.title == task_title else task for task in task_manager.get_all_tasks()]  # Жаңартылған күйі бар жаңа тапсырмалар тізімін жасаңыз
    task_manager.tasks = updated_tasks  # Менеджердегі тапсырмалар тізімін жаңарту

task_manager = TaskManager()  # Создаем экземпляр менеджера задач
task_manager.add_task(Task("Тазарту"))  # Добавляем задачу "Тазарту"
task_manager.add_task(Task("Қарау"))  # Добавляем задачу "Қарау"

change_task_status(task_manager, "Тазарту", TaskStatus.IN_PROGRESS)  # "Тазарту" тапсырмасының күйін "IN_PROGRESS" күйіне өзгерту

print("Барлық жағдайлар:")  # Барлық тапсырмалар тізімін көрсетіңіз
for task in task_manager.get_all_tasks():  # Барлық тапсырмалар тізіміндегі әрбір тапсырма үшін
    print(f"{task.title}: {task.status.value}")  # Тапсырманың тақырыбы мен күйін көрсетіңіз

print("\nОрындалған жағдайлар:")  # Орындалып жатқан тапсырмалар тізімін көрсету
for task in task_manager.get_tasks_by_status(TaskStatus.IN_PROGRESS):  # Орындалып жатқан тапсырмалар тізіміндегі әрбір тапсырма үшін
    print(f"{task.title}: {task.status.value}")  # Тапсырманың тақырыбы мен күйін көрсетіңіз

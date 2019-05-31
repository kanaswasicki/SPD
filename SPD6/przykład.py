from __future__ import print_function
import collections
from ortools.sat.python import cp_model


def MinimalJobshopSat():
    "Problem job_shop"
    model = cp_model.CpModel()

    jobs_data = [  # task = (machine_id, processing_time).
        [(0, 3), (1, 2), (2, 2)],  # Job0
        [(0, 2), (2, 1), (1, 4)],  # Job1
        [(1, 4), (2, 3)]  # Job2
    ]

    machines_count = 1 + max(task[0] for job in jobs_data for task in job)
    all_machines = range(machines_count)

    #wyliczanie maksymalnej możliwej wartości Cmax poprzez dodawanie wszystkich czasów
    horizon = sum(task[1] for job in jobs_data for task in job)

    # Nazwany tuple do przechowywania wszystkich zadań
    task_type = collections.namedtuple('task_type', 'start end interval')
    # Nazwany tuple żeby manipulować informacjami rozwiązania (wykorzystane do wyświetlania danych)
    assigned_task_type = collections.namedtuple('assigned_task_type',
                                                'start job index duration')

    #Wpisanie poszczególnych task'ów do tuple all_task i dodanie do powiązanej listy maszyn
    all_tasks = {}
    machine_to_intervals = collections.defaultdict(list)

    for job_id, job in enumerate(jobs_data):
        for task_id, task in enumerate(job):
            machine = task[0]
            duration = task[1]
            suffix = '_%i_%i' % (job_id, task_id)
            start_var = model.NewIntVar(0, horizon, 'start' + suffix)
            end_var = model.NewIntVar(0, horizon, 'end' + suffix)
            interval_var = model.NewIntervalVar(start_var, duration, end_var,
                                                'interval' + suffix)
            all_tasks[job_id, task_id] = task_type(
                start=start_var, end=end_var, interval=interval_var)
            machine_to_intervals[machine].append(interval_var)

    # Dodanie constraina odpowiadającego za to żeby nie było możliwości wykonywania się 2 zadań na jednej maszynie w tym samym czasie
    for machine in all_machines:
        model.AddNoOverlap(machine_to_intervals[machine])

    # Dodanie constraina odpowiadajacego za to, żeby nie było możliwości aby zadanie kolejne w ramach jednego job'a zaczęło się szybciej niż poprzednie się skończyło
    for job_id, job in enumerate(jobs_data):
        for task_id in range(len(job) - 1):
            model.Add(all_tasks[job_id, task_id +
                                1].start >= all_tasks[job_id, task_id].end)

    # zdefiniowanie problem obj_var jest wartościa maksymalna z zakonczonych zadan
    obj_var = model.NewIntVar(0, horizon, 'makespan')
    model.AddMaxEquality(obj_var, [
        all_tasks[job_id, len(job) - 1].end
        for job_id, job in enumerate(jobs_data)
    ])
    # ustawienie constraina na obj_var (finalnego) odpowiadajacego za minimalizacje wartosci Cmax problemu job_shop
    model.Minimize(obj_var)

    # wywolanie modelu i rozwiazania
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        # Stworzenie listy zadan przypisanych do danej maszyny
        assigned_jobs = collections.defaultdict(list)
        for job_id, job in enumerate(jobs_data):
            for task_id, task in enumerate(job):
                machine = task[0]
                assigned_jobs[machine].append(
                    assigned_task_type(
                        start=solver.Value(all_tasks[job_id, task_id].start),
                        job=job_id,
                        index=task_id,
                        duration=task[1]))

        # Stworzenie linii tekstu dla poszczegolnej maszyny
        output = ''
        for machine in all_machines:
            # Sortowanie po wartosciach poczatkowych
            assigned_jobs[machine].sort()
            sol_line_tasks = 'Machine ' + str(machine) + ': '
            sol_line = '           '

            for assigned_task in assigned_jobs[machine]:
                name = 'job_%i_%i' % (assigned_task.job, assigned_task.index)
                # dodanie spacji do stringa output zeby wyrownac kolumny
                sol_line_tasks += '%-10s' % name

                start = assigned_task.start
                duration = assigned_task.duration
                sol_tmp = '[%i,%i]' % (start, start + duration)
                # dodanie spacji do stringa output zeby wyrownac kolumny
                sol_line += '%-10s' % sol_tmp

            sol_line += '\n'
            sol_line_tasks += '\n'
            output += sol_line_tasks
            output += sol_line

        # Printowanie wyniku programu solver metoda CP
        print('Optymalna długość uszeregowania: %i' % solver.ObjectiveValue())
        print(output)
MinimalJobshopSat()


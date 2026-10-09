# Sprint_2
Learning Python, solving basic tasks.

## task_1
In this task, you need to create a subclass of a test case.  
There is a `Case` class. It contains a `print_test_case_info()` method that prints the test case id, its name, step description, and expected result to the screen.

What you need to do:
1. Create a subclass `ExtendedCase`. It inherits all attributes from the Case class. In addition, add two new attributes to it through the constructor — precondition and environment. The data type for them is strings.
2. Call the `__init__()` method of the superclass. Use the `super()` function.
3. Override the `print_test_case_info()` method in the `ExtendedCase` class.  
It should print:
- all attributes of the superclass;
- new attributes of the subclass in the format "Предусловие: {precondition}" and "Окружение: {environment}".  
Each attribute must be printed on a new line.

4. Create an object case of the `ExtendedCase` class. Input parameters are: ('1', 'Наличие кнопки Принять', '1. Открыть вкладку приёма документов 2. Проверить наличие кнопки ', 'Кнопка доступна', 'Открыть сервис', 'Яндекс Браузер').
5. Call the `print_test_case_info()` method for the case object.

Starter code:
```
class Case:
    def __init__(self, test_case_id, name, step_description, expected_result):
        self.test_case_id = test_case_id
        self.name = name
        self.step_description = step_description
        self.expected_result = expected_result

    def print_test_case_info(self):
        print(f"ID тест-кейса:  {self.test_case_id}"
              f"\nНазвание: {self.name}"
              f"\nОписание шага: {self.step_description}"
              f"\nОжидаемый результат: {self.expected_result}")

... # write your code here
```

## task_2
1. Create a `Movies` class:  
* initialize an empty `self.movies` list in it through the constructor;  
* add an `add_movie()` method.  
It will take a `movie` parameter and add it to the end of the `self.movies` list.
2. Create two child classes — `Comedy` and `Drama`.  
They inherit the `add_movie()` method.  
The method of these classes should take a `movie` parameter and add it to the end of the `self.movies` list.  
Then return records of the form "Комедии: '[]'" and "Драмы: '[]'" respectively.
3. Call the `add_movie()` method for a `Comedy()` object. Input parameter — 'Большой куш'. Print the result to the screen.
4. Call the `add_movie()` method for a `Drama()` object. Input parameter — 'Оружейный барон'. Print the result to the screen.

## task_3
You need to write three classes for sports competitions — different ways to award athletes points:
1. `PointsForPlace` — the number of points is calculated based on the place the athlete finished.
2. `PointsForMeters` — the number of points is calculated based on the distance the athlete threw the discus. 
3. `TotalPoints` — can work both with the athlete's place and with the distance.

Now in detail:

Write the `PointsForPlace` class. It receives points depending on the place the athlete finished.  
In this class, write a `get_points_for_place()` method that takes a `place` argument — an integer. Specifically: 
- If the place is strictly greater than 100, the message 'Баллы начисляются только первым 100 участникам' should be output.
- If a value less than 1 was passed as an argument, the message 'Спортсмен не может занять нулевое или отрицательное место' should be printed.  

In all other cases, points are awarded according to the formula: 101 - place.  
Initially, the number of points is zero: think about how to reflect this in the code.  
The `get_points_for_place()` method should return `points`.

Write the `PointsForMeters` class. It calculates points depending on the distance the athlete pushed the shot put or threw the discus: distance*0.5. For example, if the distance is 10 meters, the athlete will receive 5 points.  
Write a `get_points_for_meters()` method that takes a `meters` argument — an integer. Specifically:
- If the number of meters is negative, the message 'Количество метров не может быть отрицательным' should be output.

In all other cases, points are awarded according to the formula: "distance multiplied by 0.5".  
The method should return `points`. Initially, the number of points is 0.

Write the `TotalPoints` class for multi-event athletes. It is inherited from both `PointsForPlace` and `PointsForMeters` classes and implements all their methods. It should also contain:
- a `get_total_points()` method that takes `meters` and `place` as arguments;
- a `total` variable that sums the values of the `get_points_for_place()` and `get_points_for_meters()` methods.

The method returns the `total` variable.

## task_4
Write an `EmployeeSalary` class. It calculates the hourly salary of employees for a week.

1. Use the `hourly_payment` variable to set the hourly rate of pay equal to 400.
2. Initialize the attributes `name`, `hours`, `rest_days`, `email` through the constructor.
3. Add a class method `get_hours()`. If the value of `hours` is unknown, the method calculates the hours based on the number of days off — `rest_days`. The formula for this case is: `(7 - rest_days) * 8`.
4. Add a class method `get_email()`. If the value of `email` is unknown, the method generates it like this: `f"{name}@email.com"`.
5. Add a class method `set_hourly_payment()`. It changes the value of the `hourly_payment` variable.
6. Add a salary calculation method `salary()`. The calculation formula is: `hours * hourly_payment`.

## task_5
You need to create a class that calculates the results of competitions — `Results`. And two of its heirs — `Football` and `Hockey`. Subclasses inherit all attributes, and they also have their own methods.

1. Write the `Results` class. Initialize the `victories`, `draws`, `losses` attributes in it through the constructor.
2. Write the `Football` class, which is inherited from the `Results` class.  
Its methods:
* `number_of_wins()`, which should return a record like "Футбольных побед: The number of wins should be taken from the `victories` variable.
* `number_of_draws()`, which should return a record like "Футбольных ничьих: The number of draws should be taken from the `draws` variable.
* `number_of_losses()`, which should return a record like "Футбольных поражений: The number of losses should be taken from the `losses` variable.
* `total_points()`, which should return a record like "Общее количество очков: Calculate the number of points using the formula: `3*количество побед + количество ничьих.`
3. Write the `Hockey` class, which is inherited from the `Results` class.  
Its methods:
* `number_of_wins()`, which should return a record like "Хоккейных побед: The number of wins is taken from the `victories` variable.
* `number_of_draws()`, which should return a record like "Хоккейных ничьих: The number of draws is taken from the `draws` variable.
* `number_of_losses()`, which should return a record like "Хоккейных поражений: The number of losses should be taken from the `losses` variable.
* `total_points()`, which should return a record like "Общее количество очков: The number of points is calculated using the formula: `2*количество побед + количество ничьих`.
4. Create `football_team` and `hockey_team` objects of the `Football` and `Hockey` classes respectively. Pass (2, 2, 2) as parameters.
5. Call all methods for the `football_team` and `hockey_team` objects. Use a for loop. Method names should not be repeated for both objects.

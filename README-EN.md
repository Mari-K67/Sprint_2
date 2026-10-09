# Sprint_1
Learning Python, solving basic tasks.

## task_1
The string contains five time values. They are written separated by commas:
'1h 45m,360s,25m,30m 120s,2h 60s'.  
Write a loop that calculates the total number of minutes. Save the result in a variable and print it on the screen.  
Use the split(), replace() methods and the in operator in your solution.  
Note: a time value can consist of one, two, or three time units.   
Values are decoded as follows:
* hours — any positive integer and the character h;
* minutes — any positive integer and the character m;
* seconds — a positive integer divisible by 60 and the character s.

## task_2
Fix the Tester class so that:
* when calling the work_hard method on the tester_1 class instance, it prints 'tester_1 Можно отдыхать';
* when calling the work_hard method on the tester_2 class instance, it prints 'tester_2 Что ж, ещё часок поработаю!'.

Do not change the function calls.
```
class Tester:
    def __init__(name):
        name = name
        deadline = True

    def work_hard(self, deadline=True):
        if self.deadline:
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester(name='tester_1')
tester_1.work_hard(deadline=False)  # 'tester_1 Можно отдыхать'
tester_2 = Tester(name='tester_2')
tester_2.work_hard(deadline=True)   # 'tester_2 Что ж, ещё часок поработаю!' 
```

## task_3
A dictionary contains information about football championships in the 21st century:
* year. For example, 1988;
* the country that won the FIFA World Cup. For example, England.
 
What needs to be done:  
* Add 2022 to the dictionary. In 2022, Argentina became champion.
* Print all champions on the screen in the format year - country.
* Check if Italy won in the 21st century. There is a variable country with the value Italy. Check if it is contained in the dictionary. If yes, print the message Italy became a world football champion in the 21st century!. And if the country is missing from the dictionary values, print Italy did not win the FIFA World Cup in the 21st century.
```
world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}
```

## task_4
There are two task lists. The new_tasks list contains tasks that are planned to be tested by the end of the month. The completed_tasks list contains tasks already completed this month.  
What needs to be done:  
* The tester just completed task_005. Move it from the new_tasks list to the completed_tasks list. Do this in one action.
* The customer removed task_007 from the plan because requirements need to be refined. Delete it from the new_tasks list.
* The customer raised the priority for the last task in the new_tasks list, so it will need to be taken up next. Print it on the screen.
```
new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']
```

## task_5
Write a TestCase class. It should contain a constructor and methods.  
In the constructor, the following fields are initialized:
* steps — test case steps, takes an empty dictionary as a parameter;
* result — the expected result of the test case execution, takes None as a parameter.
 
Methods:
* set_step method — adds a test case step to the steps dictionary. Takes two parameters: step_number and step_text. The key is step_number (step number), and the value is step_text (text description of the step).
* delete_step method — removes a step from steps by the key step_number, which was passed to the method.
* set_result method — sets the expected result. It places it in the result attribute according to the result parameter passed to the method.
* get_test_case method — prints information about the composition of the test case in the format {'Steps': {<step_number>: '<step_description>'}, 'Expected result': '<expected result output>'}.

Example output of the get_test_case method:
```
{
    'Steps': {
            1: 'Перейти на сайт', 
            2: 'Перейти в раздел Товары', 
            3: 'Нажать кнопку «В корзину» у первого товара'
    }, 
    'Expected result': 'Товар окажется в корзине'
} 
class TestCase:

    def __init__(self):
   ...
   ...

test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case() 
```

## task_1_extra
A types dictionary stores bug types. Its keys are numbers from 1 to 5, and values are from 'Blocking' to 'Trivial' respectively. 
```
types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}
```
A tickets dictionary stores tickets (tasks) for these bugs. Keys are severity values from 1 to 5, and values are lists of tickets corresponding to these severity levels. But some tickets have been added multiple times in different lists.
```
tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}
```
Compile a summary dictionary where keys are severity levels, such as 'Significant', and values are lists with unique tickets.  
To do this, write two functions: 
* one that removes duplicates from the ticket lists,
* the second that links the severity level to the list of unique tickets.
If a ticket is in one list, it cannot be in lists at a lower severity level.   
The second function takes two parameters: types dictionary with bug types and tickets dictionary with bug lists. The function returns a dictionary where the severity level is linked to the list of unique tickets.  
The final dictionary should look like this:
```
tickets_by_type = {
    'Блокирующий': ['API_45', 'API_76', 'E2E_4'],
    'Критический': ['UI_19', 'API_65', 'E2E_45'],
    'Значительный': ['E2E_2'],
    'Незначительный': ['E2E_9'],
    'Тривиальный': ['API_61']
}
```
Calling the function is optional.

## task_2_extra
Write a function that calculates the digital root of a number.  
To get the digital root of a number, you need to:
* Split the original number into digits by place value.
* Add these digits together.

Do the same with the sum: split it into digits and add them.  
And so on — until you get a single digit (from 1 to 9), which will be the digital root of the number.  
For example, the digital root of 4851 is 9.  
4851 → 4+8+5+1 = 18. 
18 → 1+8 = 9. 
The digital root of 97569 is 9:  
97569 → 9+7+5+6+9 = 36. 
36 → 3+6 = 9. 
A more complex example. For the number 889987, the digital root is 4:  
889987 → 8+8+9+9+8+7 = 49. 
49 → 4+9 = 13. 
13 → 4.

The function can be named digit_root(num). It takes one parameter — num (number), and returns the digital root.
Conditions: 
* the input number is a natural number (1, 2, 3, … );
* the number does not exceed 10**7.

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
- new attributes of the subclass in the format "Precondition: {precondition}" and "Environment: {environment}".  
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
Then return records of the form "Comedies: '[]'" and "Dramas: '[]'" respectively.
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
- If the place is strictly greater than 100, the message 'Points are awarded only to the first 100 participants' should be output.
- If a value less than 1 was passed as an argument, the message 'An athlete cannot take a zero or negative place' should be printed.  

In all other cases, points are awarded according to the formula: 101 - place.  
Initially, the number of points is zero: think about how to reflect this in the code.  
The `get_points_for_place()` method should return `points`.

Write the `PointsForMeters` class. It calculates points depending on the distance the athlete pushed the shot put or threw the discus: distance*0.5. For example, if the distance is 10 meters, the athlete will receive 5 points.  
Write a `get_points_for_meters()` method that takes a `meters` argument — an integer. Specifically:
- If the number of meters is negative, the message 'The number of meters cannot be negative' should be output.

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
* `number_of_wins()`, which should return a record like "Football wins: The number of wins should be taken from the `victories` variable.
* `number_of_draws()`, which should return a record like "Football draws: The number of draws should be taken from the `draws` variable.
* `number_of_losses()`, which should return a record like "Football losses: The number of losses should be taken from the `losses` variable.
* `total_points()`, which should return a record like "Total number of points: Calculate the number of points using the formula: `3*number of wins + number of draws.`
3. Write the `Hockey` class, which is inherited from the `Results` class.  
Its methods:
* `number_of_wins()`, which should return a record like "Hockey wins: The number of wins is taken from the `victories` variable.
* `number_of_draws()`, which should return a record like "Hockey draws: The number of draws is taken from the `draws` variable.
* `number_of_losses()`, which should return a record like "Hockey losses: The number of losses should be taken from the `losses` variable.
* `total_points()`, which should return a record like "Total number of points: The number of points is calculated using the formula: `2*number of wins + number of draws`.
4. Create `football_team` and `hockey_team` objects of the `Football` and `Hockey` classes respectively. Pass (2, 2, 2) as parameters.
5. Call all methods for the `football_team` and `hockey_team` objects. Use a for loop. Method names should not be repeated for both objects.

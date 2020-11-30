# Вывод:
# Task A: Compute factorial(2)...
# Task B: Compute factorial(2)...
# Task C: Compute factorial(2)...
# Task A: factorial(2) = 2
# Task B: Compute factorial(3)...
# Task C: Compute factorial(3)...
# Task B: factorial(3) = 6
# Task C: Compute factorial(4)...
# Task C: factorial(4) = 24
#
# Одновременно запускаются 3 задачи: A, B, C. В цикле for выводятся на печать сразу 3 строчки,
# которые говорят нам о параллельном выполнении задач A, B и C соответственно тому порядку, в котором
# они были заданы в основной программе. И так как для цикла for в случае задачи A число 3 является
# правой границей, которая не включается в "подсчёт" при работе цикла for, то происходит вывод итогового
# результата, т.е. вывод факторитала числа 2. В дальнейшем цикл for выведет уже только две строчки, как
# мы можем видеть, для задач B и С (так как задача A уже выполнена). И так как для B будет выполнятся
# то же самое условие, что и для A, которое я описала выше, то выведется результат работы задачи B, а именно
# факториал числа 3. То же самое работает для задачи C. Функция sleep помогает нам сделать так, чтобы все
# задачи выполнялись параллельно. Если бы этой функции не было, то все задачи выпонялись бы последовательно.
#
# Вывод без sleep:
# Task A: Compute factorial(2)...
# Task A: factorial(2) = 2
# Task B: Compute factorial(2)...
# Task B: Compute factorial(3)...
# Task B: factorial(3) = 6
# Task C: Compute factorial(2)...
# Task C: Compute factorial(3)...
# Task C: Compute factorial(4)...
# Task C: factorial(4) = 24
#

import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


async def main():
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

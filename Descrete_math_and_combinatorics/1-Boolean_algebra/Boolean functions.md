# Двоїсті та самодвоїсті функції

Перевірити, чи є функція самодвоїстою використовуючи тотожні перетворення: $f(x,y,z) = (x \vee \overline{y} \vee \overline{z}) (\overline{x} \vee y \vee z) (\overline{x} \vee y \vee \overline{z})$ 

(Звернемо увагу, що початкова функція $f(x,y,z)$ задана у ДКНФ).

Розіб'ємо задачу на кроки:
1. Знайдемо двоїсту $f^{*}$ функцію до поданої $f$ та максимально спростимо
2. Приведемо $f$ та $f^{*}$ до однієї форми - лише такі функції можна порівняти (чи за таблицею істиності)
3. Перевіремо умову самодвоїстості

## 1. Знаходження двоїстої функції та спрощення
Для того, щоб знайти функцію $f^{*}$ двоїсту до висхідної $f$, потрібно знайти функцію: $f^{*}(x,y,z) = f\overline{(\overline{x}, \overline{y}, \overline{z})}$ - іншими словами, $f^{*}$ - це функція-заперечення висхідної функції $f$ над запереченнями аргументів.

Умовою самодвоїстості є рівність поданої функції $f$ до двоїстої $f^{*}$: 
$$f = f^{*} \Longleftrightarrow f(x,y,z) = f^{*}\overline{(\overline{x}, \overline{y},\overline{z})}$$

Будуємо двоїсту функцію до поданої $f(x,y,z)$:
1. За означенням двоїстої функції $f^{*}$:
$f^{*}(x,y,z)=f\overline{(\overline{x}, \overline{y}, \overline{z})} = \overline{ (\overline{x} \vee \overline{\overline{y}} \vee \overline{\overline{z}}) (\overline{\overline{x}} \vee \overline{y} \vee \overline{z}) (\overline{\overline{x}} \vee \overline{y} \vee \overline{\overline{z}}) } = \overline{(\overline{x} \vee y \vee z) (x \vee \overline{y} \vee \overline{z}) (x \vee \overline{y} \vee z)}$ - оскільки функція логічного заперечення інволютивна (обернена сама собі), то можемо позбавитись подвійних заперечень над змінніми у дужках.

2. Для подальшого спрощення функції - замінемо операції між дужками з логічного "ТА" на логічне "АБО" за законами де Моргана:
$$f^{*}(x,y,z)=f\overline{(\overline{x}, \overline{y}, \overline{z})} = \overline{(\overline{x} \vee y \vee z) (x \vee \overline{y} \vee \overline{z}) (x \vee \overline{y} \vee z)} = \overline{(\overline{x} \vee y \vee z)} \vee \overline{(x \vee \overline{y} \vee \overline{z})} \vee \overline{(x \vee \overline{y} \vee z)}$$
3. Знов можемо застосувати правило де Моргана окремо до кожної з дужок, щоб позбавитись заперечень над ними:
$$f^{*}(x,y,z)=f\overline{(\overline{x}, \overline{y}, \overline{z})} = (\overline{\overline{x}}\overline{y}  \overline{z}) \vee (\overline{x} \ \overline{\overline{y}}  \overline{\overline{z}}) \vee (\overline{x} \overline{\overline{y}} \overline{z}) = x \overline{y}  \overline{z} \vee \overline{x} y  z \vee \overline{x} y \overline{z}$$ - остаточно спростили та отримали двоїсту функцію задану у ДДНФ (диз'юнкція кон'юнкцій).
## 2. Приведемо початкову функцію та двоїсту до однієї форми
За умовою самодвоїстості $f^{*} = f$. Щоб відповісти на питання, чи дорівнює функція $f^{*}(x,y,z)$ початковій $f(x,y,z)$, потрібно скористатись оним з двох способів:
- Для порівняння, нам потрібно привести ці функції до однієї форми: чи початкову $f(x,y,z)$ до ДДНФ, чи двоїсту $f^{*}(x,y,z)$ до ДКНФ
- Побудувати таблиці істинності для $f$ та $f^{*}$ - якщо відповідні таблиці істиності функцій рівні, то і функції рівні, інакше подана функція - не самодвоїста

Оскільки за умової задачі потрібно використовувати тотожні перетворення, то скористаємось першим способом.

Приведемо початкову функцію $f(x,y,z)$ задану ДКНФ у ДДНФ, тоді $f(x,y,z)$ та $f^{*}(x,y,z)$ будуть задані в одній формі - в даному випадку у ДДНФ.

Скористаємось алгоритмом знаходження ДДНФ за таблицею істиності.
Будуємо таблицю істіності для $f(x,y,z) = (x \vee \overline{y} \vee \overline{z}) (\overline{x} \vee y \vee z) (\overline{x} \vee y \vee \overline{z})$:

| x               | y               | z               | $x \vee \overline{y} \vee \overline{z}$ | $\overline{x} \vee y \vee z$ | $\overline{x} \vee y \vee \overline{z}$ | $f(x,y,z)$      |
| --------------- | --------------- | --------------- | --------------------------------------- | ---------------------------- | --------------------------------------- | --------------- |
| $\underline{0}$ | $\underline{0}$ | $\underline{0}$ | 1                                       | 1                            | 1                                       | $\underline{1}$ |
| 0               | 0               | 1               | 1                                       | 1                            | 0                                       | 0               |
| $\underline{0}$ | $\underline{1}$ | $\underline{0}$ | 1                                       | 1                            | 1                                       | $\underline{1}$ |
| 0               | 1               | 1               | 0                                       | 1                            | 1                                       | 0               |
| 1               | 0               | 0               | 1                                       | 0                            | 1                                       | 0               |
| 1               | 0               | 1               | 1                                       | 1                            | 0                                       | 0               |
| $\underline{1}$ | $\underline{1}$ | $\underline{0}$ | 1                                       | 1                            | 1                                       | $\underline{1}$ |
| $\underline{1}$ | $\underline{1}$ | $\underline{1}$ | $\underline{1}$                         | $\underline{1}$              | $\underline{1}$                         | $\underline{1}$ |
Для побуови ДДНФ, нам потрібно виписати диз'юнкти за наступним алгоритмом:
* Дивимось на строки таблиці істинності, для яких функція приймає значення "1"
* Якщо аргумент для цієї строки входить, як 0, то записуємо його заперечення, а якщо - 1, то без заперечення

Для нашої таблиці істинності функція приймає значення "1" (ІСТИНА) на інтерпретаціях 0, 2, 6, 7 - відповідно виписуємо диз'юнкти за алгоритмом:

$0: \overline{x}\overline{y}\overline{z}$
$2: \overline{x}y\overline{z}$
$6: xy\overline{z}$
$7: xyz$

І записуємо ДДНФ: $\overline{x}\overline{y}\overline{z} \vee \overline{x}y\overline{z} \vee xy\overline{z} \vee xyz$ 
## 3. Перевірка умови самодвоїстості
Отже маємо: $x \overline{y}  \overline{z} \vee \overline{x} y  z \vee \overline{x} y \overline{z} \neq \overline{x}\overline{y}\overline{z} \vee \overline{x}y\overline{z} \vee xy\overline{z} \vee xyz \Longrightarrow f \neq f^{*}$ - функція не є самодвоїстою
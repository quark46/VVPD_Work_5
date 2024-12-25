# **Проект: Вычисление математических функций с использованием разложений в ряды**

## **Описание проекта**

Этот проект реализует вычисление различных математических функций с использованием разложений в ряды Тейлора:

1. **sinh(x)** — гиперболический синус.
2. **arctan(x)** — арктангенс.
3. **(1 - x)^m** — степенной ряд.

Пользователь может выбрать одну из функций через меню, ввести необходимые параметры и получить результат.

---

## **Функции**

### **sinh_taylor(x, terms=50)**

Вычисляет гиперболический синус числа **x** с использованием ряда Тейлора.

- **Аргументы**:
  - `x` — Входное значение.
  - `terms` — Количество членов ряда (по умолчанию 50).
- **Возвращаемое значение**:  
  Приближённое значение **sinh(x)**.

---

### **arctan_taylor(x, terms=50)**

Вычисляет арктангенс числа **x** с использованием ряда Тейлора.

- **Аргументы**:
  - `x` — Входное значение, \(|x| \leq 1\).
  - `terms` — Количество членов ряда (по умолчанию 50).
- **Возвращаемое значение**:  
  Приближённое значение **arctan(x)**.
- **Исключения**:  
  Генерируется, если \(|x| > 1\).

---

### **power_series(x, m, terms=50)**

Вычисляет \((1 - x)^m\) с использованием разложения в ряд Тейлора.

- **Аргументы**:
  - `x` — Входное значение, \(-1 < x < 1\).
  - `m` — Степень.
  - `terms` — Количество членов ряда (по умолчанию 50).
- **Возвращаемое значение**:  
  Приближённое значение \((1 - x)^m\).
- **Исключения**:  
  Генерируется, если \(x\) не удовлетворяет условиям \(-1 < x < 1\).

---

## **Как использовать**

1. Клонируйте репозиторий:

   ```bash
   git clone <ссылка на репозиторий>
   ```

2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Запустите программу:

   ```bash
   python __main__.py
   ```

4. Следуйте инструкциям в меню:

   - Выберите номер функции.
   - Введите параметры \(x\), \(m\) (если требуется) и количество членов ряда \(n\).

---

## **Пример работы**

```text
Выберите действие:
"1" - Выполнить первую функцию (sinh)
"2" - Выполнить вторую функцию (arctan)
"3" - Выполнить третью функцию (power series)
"4" - Завершить выполнение программы
```
## Фотография 
![](## Фотография 
![](https://ru.pinterest.com/pin/914864111806819277/)

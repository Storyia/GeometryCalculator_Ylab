import math
import tkinter as tk
from tkinter import messagebox, Canvas, ttk
from abc import ABC, abstractmethod

# Базовый класс для всех фигур (абстрактный)
class Shape(ABC):
    instances = 0  # Переменная класса для хранения количества созданных фигур

    def __init__(self):
        Shape.instances += 1  # Увеличиваем счетчик при создании каждой фигуры

    @classmethod
    def total_shapes(cls) -> int:
        return cls.instances  # Метод класса для получения общего числа фигур

    @abstractmethod
    def area(self) -> float:
        """Абстрактный метод для расчета площади"""
        pass

    @abstractmethod
    def visualize(self, canvas: Canvas):
        """Абстрактный метод для отображения фигуры на холсте"""
        pass

# Плоские фигуры
# Класс для круга
class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__()
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2  # Вычисляем площадь круга

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius  # Вычисляем периметр круга

    def visualize(self, canvas: Canvas):
        # Рисуем круг на холсте
        canvas.create_oval(50, 50, 50 + 2 * self.radius, 50 + 2 * self.radius, outline="blue", width=2)

# Класс для квадрата
class Square(Shape):
    def __init__(self, side: float):
        super().__init__()
        self.side = side

    def area(self) -> float:
        return self.side ** 2  # Вычисляем площадь квадрата

    def perimeter(self) -> float:
        return 4 * self.side  # Вычисляем периметр квадрата

    def visualize(self, canvas: Canvas):
        # Рисуем квадрат на холсте
        canvas.create_rectangle(50, 50, 50 + self.side, 50 + self.side, outline="green", width=2)

# Класс для прямоугольника
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__()
        self.width = width  # Ширина
        self.height = height  # Высота

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def visualize(self, canvas):
        canvas.create_rectangle(50, 50, 50 + self.width, 50 + self.height, outline="orange", width=2)

# Добавление треугольника
class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def visualize(self, canvas: Canvas):
        # Примерная визуализация треугольника
        canvas.create_polygon(50, 150, 50 + self.a, 150, 50 + (self.a / 2), 150 - self.b, outline="purple", width=2,
                              fill='')

# Класс для ромба
class Rhombus(Shape):
    def __init__(self, diagonal1, diagonal2):
        super().__init__()
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def area(self) -> float:
        # Площадь ромба через диагонали
        return (self.diagonal1 * self.diagonal2) / 2

    def perimeter(self) -> float:
        # Периметр ромба: находим длину одной стороны ромба через диагонали и умножаем на 4
        side = math.sqrt((self.diagonal1 / 2) ** 2 + (self.diagonal2 / 2) ** 2)
        return 4 * side

    def visualize(self, canvas):
        # Визуализация ромба как четырехугольник
        x, y = 100, 100
        canvas.create_polygon(x, y - self.diagonal2 / 2,
                              x + self.diagonal1 / 2, y,
                              x, y + self.diagonal2 / 2,
                              x - self.diagonal1 / 2, y,
                              outline="purple", width=2, fill="")

# Добавление трапеции
class Trapezoid(Shape):
    def __init__(self, a: float, b: float, h: float, c: float, d: float):
        super().__init__()
        self.a = a  # первое основание
        self.b = b  # второе основание
        self.c = c  # боковая сторона
        self.d = d  # боковая сторона
        self.h = h  # высота

    def area(self) -> float:
        return (self.a + self.b) * self.h / 2

    def perimeter(self) -> float:
        return self.a + self.b + self.c + self.d

    def visualize(self, canvas):
        # Визуализация трапеции на холсте
        canvas.create_polygon(50, 150, 50 + self.a, 150, 50 + self.a - (self.a - self.b) / 2, 150 - self.h,
                              50 + (self.a - self.b) / 2, 150 - self.h, outline="brown", width=2, fill='')

# Объемные фигуры
# Сфера
class Sphere(Shape):
    def __init__(self, radius: float):
        super().__init__()
        self.radius = radius

    def area(self) -> float:
        return 4 * math.pi * self.radius ** 2  # 4πr²

    def volume(self) -> float:
        return (4 / 3) * math.pi * self.radius ** 3  # 4/3πr³

    def visualize(self, canvas):
        canvas.create_oval(50, 50, 50 + 2 * self.radius, 50 + 2 * self.radius, outline="red", width=2)

# Класс для цилиндра
class Cylinder(Shape):
    def __init__(self, radius: float, height: float):
        super().__init__()
        self.radius = radius  # Основание
        self.height = height

    def area(self) -> float:
        # Полная площадь поверхности цилиндра
        return 2 * math.pi * self.radius * (self.radius + self.height)  # 2πr(r + h)

    def volume(self) -> float:
        # Объем цилиндра
        return math.pi * self.radius ** 2 * self.height  # πr²h

    def visualize(self, canvas):
        # Визуализация цилиндра (два овала и прямоугольник)
        canvas.create_oval(50, 50, 50 + 2 * self.radius, 50 + self.radius, outline="blue", width=2)
        canvas.create_oval(50, 50 + self.height, 50 + 2 * self.radius, 50 + self.height + self.radius, outline="blue",
                           width=2)
        canvas.create_rectangle(50, 50 + self.radius / 2, 50 + 2 * self.radius, 50 + self.height + self.radius / 2,
                                outline="blue", width=2)

# Класс для куба
class Cube(Shape):
    def __init__(self, side: float):
        super().__init__()
        self.side = side

    def area(self) -> float:
        # Полная площадь поверхности куба
        return 6 * self.side ** 2

    def volume(self) -> float:
        # Объем куба
        return self.side ** 3

    def visualize(self, canvas):
        # Рисуем куб как квадрат с эффектом 3D
        x, y = 50, 50
        offset = self.side / 2
        canvas.create_rectangle(x, y, x + self.side, y + self.side, outline="purple", width=2)  # Передний квадрат
        canvas.create_rectangle(x + offset, y + offset, x + self.side + offset, y + self.side + offset,
                                outline="purple", width=2)  # Задний квадрат
        canvas.create_line(x, y, x + offset, y + offset, fill="purple", width=2)
        canvas.create_line(x + self.side, y, x + self.side + offset, y + offset, fill="purple", width=2)
        canvas.create_line(x, y + self.side, x + offset, y + self.side + offset, fill="purple", width=2)
        canvas.create_line(x + self.side, y + self.side, x + self.side + offset, y + self.side + offset, fill="purple",
                           width=2)

# Класс для параллелепипеда
class Parallelepiped(Shape):
    def __init__(self, length: float, width: float, height: float):
        super().__init__()
        self.length = length
        self.width = width
        self.height = height

    def area(self) -> float:
        # Полная площадь поверхности параллелепипеда
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

    def volume(self) -> float:
        # Объем параллелепипеда
        return self.length * self.width * self.height

    def visualize(self, canvas):
        # Рисуем параллелепипед как прямоугольник с эффектом 3D
        x, y = 50, 50
        offset = self.width / 2
        canvas.create_rectangle(x, y, x + self.length, y + self.height, outline="green", width=2)
        canvas.create_rectangle(x + offset, y + offset, x + self.length + offset, y + self.height + offset,
                                outline="green", width=2)
        canvas.create_line(x, y, x + offset, y + offset, fill="green", width=2)
        canvas.create_line(x + self.length, y, x + self.length + offset, y + offset, fill="green", width=2)
        canvas.create_line(x, y + self.height, x + offset, y + self.height + offset, fill="green", width=2)
        canvas.create_line(x + self.length, y + self.height, x + self.length + offset, y + self.height + offset,
                           fill="green", width=2)

# Класс для пирамиды
class Pyramid(Shape):
    def __init__(self, base_length: float, base_width: float, height: float):
        super().__init__()
        self.base_length = base_length
        self.base_width = base_width
        self.height = height

    def area(self) -> float:
        # Площадь основания
        base_area = self.base_length * self.base_width
        # Вычисляем площадь боковых сторон
        side_area = (self.base_length * math.sqrt((self.base_width / 2) ** 2 + self.height ** 2) +
                     self.base_width * math.sqrt((self.base_length / 2) ** 2 + self.height ** 2))
        return base_area + side_area  # Общая площадь пирамиды

    def volume(self) -> float:
        # Объем пирамиды
        return (1 / 3) * self.base_length * self.base_width * self.height

    def visualize(self, canvas):
        # Рисуем пирамиду как треугольник с прямоугольным основанием
        x, y = 50, 150

        # Рисуем основание (прямоугольник)
        canvas.create_rectangle(x, y, x + self.base_length, y + 10, outline="orange",
                                width=2)  # Прямоугольное основание

        # Рисуем боковые стороны пирамиды
        canvas.create_line(x, y + 5, x + self.base_length / 2, y - self.height, fill="orange", width=2)  # Левая сторона
        canvas.create_line(x + self.base_length, y + 5, x + self.base_length / 2, y - self.height, fill="orange",
                           width=2)  # Правая сторона

# Класс для конуса
class Cone(Shape):
    def __init__(self, radius: float, height: float):
        super().__init__()
        self.radius = radius
        self.height = height

    def area(self) -> float:
        # Площадь боковой поверхности и полная площадь поверхности конуса
        slant_height = math.sqrt(self.radius ** 2 + self.height ** 2)
        return math.pi * self.radius * (self.radius + slant_height)

    def volume(self) -> float:
        # Объем конуса
        return (1 / 3) * math.pi * self.radius ** 2 * self.height

    def visualize(self, canvas):
        # Рисуем конус как треугольник с овальным основанием
        x, y = 50, 150

        canvas.create_oval(x, y, x + 2 * self.radius, y + 20, outline="blue", width=2)  # Овальное основание

        # Рисуем боковые стороны как треугольник
        canvas.create_line(x, y + 10, x + self.radius, y - self.height, fill="blue", width=2)  # Левая сторона
        canvas.create_line(x + 2 * self.radius, y + 10, x + self.radius, y - self.height, fill="blue",
                           width=2)  # Правая сторона

# Функция для выбора фигуры из выпадающего меню
def selected(event):
    selection = combobox.get()  # Получаем выбранное значение
    for widget in frame_inputs.winfo_children():
        widget.destroy()  # Удаляем все виджеты из фрейма перед добавлением новых

    if selection == "Круг":
        label = tk.Label(frame_inputs, text="Введите радиус круга:")  # Добавляем метку для ввода радиуса круга
        label.pack(side=tk.LEFT)
        global entry  # Добавляем поле для ввода радиуса
        entry = tk.Entry(frame_inputs)
        entry.pack(side=tk.LEFT)
        button = tk.Button(frame_inputs, text="Рассчитать", command=calculate_circle)  # Добавляем кнопку для расчета
        button.pack(side=tk.LEFT)

    elif selection == "Квадрат":
        label = tk.Label(frame_inputs, text="Введите сторону квадрата:")
        label.pack(side=tk.LEFT)
        entry = tk.Entry(frame_inputs)
        entry.pack(side=tk.LEFT)
        button = tk.Button(frame_inputs, text="Рассчитать", command=calculate_square)
        button.pack(side=tk.LEFT)

    elif selection == "Прямоугольник":
        label_width = tk.Label(frame_inputs, text="Введите ширину прямоугольника:")
        label_width.pack(side=tk.LEFT)
        global entry_rectangle_width
        entry_rectangle_width = tk.Entry(frame_inputs)
        entry_rectangle_width.pack(side=tk.LEFT)

        label_height = tk.Label(frame_inputs, text="Введите высоту прямоугольника:")
        label_height.pack(side=tk.LEFT)
        global entry_rectangle_height
        entry_rectangle_height = tk.Entry(frame_inputs)
        entry_rectangle_height.pack(side=tk.LEFT)

        button = tk.Button(frame_inputs, text="Рассчитать", command=calculate_rectangle)
        button.pack(side=tk.LEFT)

    elif selection == "Треугольник":
        label_a = tk.Label(frame_inputs, text="Введите сторону a треугольника:")
        label_a.pack(side=tk.LEFT)
        global entry_triangle_a
        entry_triangle_a = tk.Entry(frame_inputs)
        entry_triangle_a.pack(side=tk.LEFT)

        label_b = tk.Label(frame_inputs, text="Введите сторону b треугольника:")
        label_b.pack(side=tk.LEFT)
        global entry_triangle_b
        entry_triangle_b = tk.Entry(frame_inputs)
        entry_triangle_b.pack(side=tk.LEFT)

        label_c = tk.Label(frame_inputs, text="Введите сторону c треугольника:")
        label_c.pack(side=tk.LEFT)
        global entry_triangle_c
        entry_triangle_c = tk.Entry(frame_inputs)
        entry_triangle_c.pack(side=tk.LEFT)

        button = tk.Button(frame_inputs, text="Рассчитать", command=calculate_triangle)
        button.pack(side=tk.LEFT)

    elif selection == "Ромб":
        label_d1 = tk.Label(frame_inputs, text="Введите первую диагональ ромба:")
        label_d1.pack(side=tk.LEFT)
        global entry_rhombus_d1
        entry_rhombus_d1 = tk.Entry(frame_inputs)
        entry_rhombus_d1.pack(side=tk.LEFT)

        label_d2 = tk.Label(frame_inputs, text="Введите вторую диагональ ромба:")
        label_d2.pack(side=tk.LEFT)
        global entry_rhombus_d2
        entry_rhombus_d2 = tk.Entry(frame_inputs)
        entry_rhombus_d2.pack(side=tk.LEFT)

        button = tk.Button(frame_inputs, text="Рассчитать", command=calculate_rhombus)
        button.pack(side=tk.LEFT)

    elif selection == "Трапеция":
        label_trapezoid_a = tk.Label(frame_inputs, text="Введите основание a трапеции:")
        label_trapezoid_a.pack(side=tk.LEFT)
        global entry_trapezoid_a
        entry_trapezoid_a = tk.Entry(frame_inputs)
        entry_trapezoid_a.pack(side=tk.LEFT)

        label_trapezoid_b = tk.Label(frame_inputs, text="Введите основание b трапеции:")
        label_trapezoid_b.pack(side=tk.LEFT)
        global entry_trapezoid_b
        entry_trapezoid_b = tk.Entry(frame_inputs)
        entry_trapezoid_b.pack(side=tk.LEFT)

        label_trapezoid_c = tk.Label(frame_inputs, text="Введите боковую сторону c трапеции:")
        label_trapezoid_c.pack(side=tk.LEFT)
        global entry_trapezoid_c
        entry_trapezoid_c = tk.Entry(frame_inputs)
        entry_trapezoid_c.pack(side=tk.LEFT)

        label_trapezoid_d = tk.Label(frame_inputs, text="Введите боковую сторону d трапеции:")
        label_trapezoid_d.pack(side=tk.LEFT)
        global entry_trapezoid_d
        entry_trapezoid_d = tk.Entry(frame_inputs)
        entry_trapezoid_d.pack(side=tk.LEFT)

        label_trapezoid_h = tk.Label(frame_inputs, text="Введите высоту трапеции:")
        label_trapezoid_h.pack(side=tk.LEFT)
        global entry_trapezoid_h
        entry_trapezoid_h = tk.Entry(frame_inputs)
        entry_trapezoid_h.pack(side=tk.LEFT)

        button_trapezoid = tk.Button(frame_inputs, text="Рассчитать", command=calculate_trapezoid)
        button_trapezoid.pack(side=tk.LEFT)

    elif selection == "Сфера":
        label_sphere = tk.Label(frame_inputs, text="Введите радиус сферы:")
        label_sphere.pack(side=tk.LEFT)
        global entry_sphere
        entry_sphere = tk.Entry(frame_inputs)
        entry_sphere.pack(side=tk.LEFT)

        button_sphere = tk.Button(frame_inputs, text="Рассчитать", command=calculate_sphere)
        button_sphere.pack(side=tk.LEFT)

    elif selection == "Цилиндр":
        label_cylinder_radius = tk.Label(frame_inputs, text="Введите радиус основания цилиндра:")
        label_cylinder_radius.pack(side=tk.LEFT)
        global entry_cylinder_radius
        entry_cylinder_radius = tk.Entry(frame_inputs)
        entry_cylinder_radius.pack(side=tk.LEFT)

        label_cylinder_height = tk.Label(frame_inputs, text="Введите высоту цилиндра:")
        label_cylinder_height.pack(side=tk.LEFT)
        global entry_cylinder_height
        entry_cylinder_height = tk.Entry(frame_inputs)
        entry_cylinder_height.pack(side=tk.LEFT)

        button_cylinder = tk.Button(frame_inputs, text="Рассчитать", command=calculate_cylinder)
        button_cylinder.pack(side=tk.LEFT)

    elif selection == "Куб":
        label_cube_side = tk.Label(frame_inputs, text="Введите длину ребра куба:")
        label_cube_side.pack(side=tk.LEFT)
        global entry_cube_side
        entry_cube_side = tk.Entry(frame_inputs)
        entry_cube_side.pack(side=tk.LEFT)

        button_cube = tk.Button(frame_inputs, text="Рассчитать", command=calculate_cube)
        button_cube.pack(side=tk.LEFT)

    elif selection == "Параллелепипед":
        label_parallelepiped_length = tk.Label(frame_inputs, text="Введите длину параллелепипеда:")
        label_parallelepiped_length.pack(side=tk.LEFT)
        global entry_parallelepiped_length
        entry_parallelepiped_length = tk.Entry(frame_inputs)
        entry_parallelepiped_length.pack(side=tk.LEFT)

        label_parallelepiped_width = tk.Label(frame_inputs, text="Введите ширину параллелепипеда:")
        label_parallelepiped_width.pack(side=tk.LEFT)
        global entry_parallelepiped_width
        entry_parallelepiped_width = tk.Entry(frame_inputs)
        entry_parallelepiped_width.pack(side=tk.LEFT)

        label_parallelepiped_height = tk.Label(frame_inputs, text="Введите высоту параллелепипеда:")
        label_parallelepiped_height.pack(side=tk.LEFT)
        global entry_parallelepiped_height
        entry_parallelepiped_height = tk.Entry(frame_inputs)
        entry_parallelepiped_height.pack(side=tk.LEFT)

        button_parallelepiped = tk.Button(frame_inputs, text="Рассчитать", command=calculate_parallelepiped)
        button_parallelepiped.pack(side=tk.LEFT)

    if selection == "Пирамида":
        label_pyramid_base_length = tk.Label(frame_inputs, text="Введите длину основания пирамиды:")
        label_pyramid_base_length.pack(side=tk.LEFT)
        global entry_pyramid_base_length
        entry_pyramid_base_length = tk.Entry(frame_inputs)
        entry_pyramid_base_length.pack(side=tk.LEFT)

        label_pyramid_base_width = tk.Label(frame_inputs, text="Введите ширину основания пирамиды:")
        label_pyramid_base_width.pack(side=tk.LEFT)
        global entry_pyramid_base_width
        entry_pyramid_base_width = tk.Entry(frame_inputs)
        entry_pyramid_base_width.pack(side=tk.LEFT)

        label_pyramid_height = tk.Label(frame_inputs, text="Введите высоту пирамиды:")
        label_pyramid_height.pack(side=tk.LEFT)
        global entry_pyramid_height
        entry_pyramid_height = tk.Entry(frame_inputs)
        entry_pyramid_height.pack(side=tk.LEFT)

        button_pyramid = tk.Button(frame_inputs, text="Рассчитать", command=calculate_pyramid)
        button_pyramid.pack(side=tk.LEFT)

    elif selection == "Конус":
        label_cone_radius = tk.Label(frame_inputs, text="Введите радиус основания конуса:")
        label_cone_radius.pack(side=tk.LEFT)
        global entry_cone_radius
        entry_cone_radius = tk.Entry(frame_inputs)
        entry_cone_radius.pack(side=tk.LEFT)

        label_cone_height = tk.Label(frame_inputs, text="Введите высоту конуса:")
        label_cone_height.pack(side=tk.LEFT)
        global entry_cone_height
        entry_cone_height = tk.Entry(frame_inputs)
        entry_cone_height.pack(side=tk.LEFT)

        button_cone = tk.Button(frame_inputs, text="Рассчитать", command=calculate_cone)
        button_cone.pack(side=tk.LEFT)

# Универсальная функция для вывода результатов
def display_results(shape: Shape, property_name: str, property_value: float) -> None:
    messagebox.showinfo("Результат", f"{property_name}: {property_value:.2f}")  # всплывающее окно
    canvas.delete("all")  # Очищаем холст
    shape.visualize(canvas)  # Визуализируем фигуру
    update_shape_count_label()  # Обновляем количество созданных фигур

# Универсальная функция для расчета свойств фигур
def calculate_shape(shape_class, *args) -> None:
    try:
        # Создаем объект фигуры с переданными параметрами
        shape = shape_class(*args)

        # Вызываем метод area (если он есть)
        try:
            area = shape.area()
            display_results(shape, "Площадь", area)
        except AttributeError:
            print(f"Метод area не поддерживается для {shape_class.__name__}")

        # Вызываем метод volume (если он есть)
        try:
            volume = shape.volume()
            display_results(shape, "Объем", volume)
        except AttributeError:
            print(f"Метод volume не поддерживается для {shape_class.__name__}")

        # Вызываем метод perimeter (если он есть)
        try:
            perimeter = shape.perimeter()
            display_results(shape, "Периметр", perimeter)
        except AttributeError:
            print(f"Метод perimeter не поддерживается для {shape_class.__name__}")

    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные данные")

# Функция для круга
def calculate_circle():
    try:
        radius = float(entry.get())  # Получаем радиус от пользователя
        calculate_shape(Circle, radius)
    except ValueError:
        messagebox.showerror("Ошибка",
                             "Введите корректное число")  # Показываем ошибку, если введены некорректные данные

# Функция для квадрата
def calculate_square():
    try:
        side = float(entry.get())
        calculate_shape(Square, side)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные данные")

# Функция для прямоугольника
def calculate_rectangle():
    try:
        width = float(entry_rectangle_width.get())
        height = float(entry_rectangle_height.get())
        calculate_shape(Rectangle, width, height)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

# Функция для трапеции
def calculate_trapezoid():
    try:
        a = float(entry_trapezoid_a.get())
        b = float(entry_trapezoid_b.get())
        c = float(entry_trapezoid_c.get())
        d = float(entry_trapezoid_d.get())
        h = float(entry_trapezoid_h.get())
        calculate_shape(Trapezoid, a, b, c, d, h)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

# Функция для треугольника
def calculate_triangle():
    try:
        a = float(entry_triangle_a.get())
        b = float(entry_triangle_b.get())
        c = float(entry_triangle_c.get())

        # Проверка: существует ли треугольник
        if a + b > c and a + c > b and b + c > a:
            calculate_shape(Triangle, a, b, c)
        else:
            # показываем ошибку, если треугольник не может существовать
            messagebox.showerror("Ошибка", "Сумма двух сторон треугольника должна быть больше третьей стороны.")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")  # Ошибка при некорректных данных

# Функция для расчета площади и периметра ромба
def calculate_rhombus():
    try:
        diagonal1 = float(entry_rhombus_d1.get())
        diagonal2 = float(entry_rhombus_d2.get())
        calculate_shape(Rhombus, diagonal1, diagonal2)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

# Сфера
def calculate_sphere():
    try:
        radius = float(entry_sphere.get())
        calculate_shape(Sphere, radius)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число")

# Функция для расчета площади и объема цилиндра
def calculate_cylinder():
    try:
        radius = float(entry_cylinder_radius.get())
        height = float(entry_cylinder_height.get())
        calculate_shape(Cylinder, radius, height)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

# Функция для расчета площади и объема куба
def calculate_cube():
    try:
        side = float(entry_cube_side.get())
        calculate_shape(Cube, side)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число")

# Функция для расчета площади и объема параллелепипеда
def calculate_parallelepiped():
    try:
        length = float(entry_parallelepiped_length.get())
        width = float(entry_parallelepiped_width.get())
        height = float(entry_parallelepiped_height.get())
        calculate_shape(Parallelepiped, length, width, height)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

# Функция для расчета площади и объема пирамиды
def calculate_pyramid():
    try:
        base_length = float(entry_pyramid_base_length.get())
        base_width = float(entry_pyramid_base_width.get())
        height = float(entry_pyramid_height.get())
        calculate_shape(Pyramid, base_length, base_width, height)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

# Функция для расчета площади и объема конуса
def calculate_cone():
    try:
        radius = float(entry_cone_radius.get())
        height = float(entry_cone_height.get())
        calculate_shape(Cone, radius, height)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

# Обновление метки с количеством созданных фигур
def update_shape_count_label():
    shape_count_label.config(text=f"Количество созданных фигур: {Shape.total_shapes()}")

# Создаем главное окно программы
root = tk.Tk()
root.title("Геометрический калькулятор")  # заголовок окна

# Список фигур
figures = ["Круг", "Квадрат", "Прямоугольник", "Треугольник", "Ромб", "Трапеция", "Сфера", "Цилиндр", "Куб",
           "Параллелепипед", "Пирамида", "Конус"]

# Метка для вывода выбранной фигуры
label = ttk.Label(text="Выберите фигуру")
label.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)

# Combobox для выбора фигуры
combobox = ttk.Combobox(values=figures, state="readonly")
combobox.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)
combobox.bind("<<ComboboxSelected>>", selected)

# Фрейм для ввода параметров выбранной фигуры
frame_inputs = tk.Frame(root)
frame_inputs.pack()

# Холст для визуализации фигур
canvas = Canvas(root, width=400, height=400)
canvas.pack()

# Отображение количества созданных фигур
shape_count_label = tk.Label(root, text=f"Количество созданных фигур: {Shape.total_shapes()}")
shape_count_label.pack()

root.mainloop()  # запускаем главный цикл программы, чтобы окно оставалось открытым

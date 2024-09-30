import math  #Библиотека для мат функций
import tkinter as tk        # библиотека для создания графического интерфейса
from tkinter import messagebox, Canvas    # окно с сообщениями и холст для рисования

# Базовый класс для всех фигур
class Shape:
    instances = 0  # Переменная класса для хранения количества созданных фигур

    def __init__(self):
        Shape.instances += 1  # Увеличиваем счетчик при создании каждой фигуры

    @classmethod
    def total_shapes(cls):
        return cls.instances  # Метод класса для получения общего числа фигур

    def area(self):
        pass  # Заглушка для функции расчета площади

    def visualize(self, canvas):
        pass  # Заглушка для функции отображения фигуры на холсте

# Плоские фигуры

 # Класс для круга
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()           #вызов базового класса для обновления счётчика
        self.radius = radius      # Сохраняем введеные пользователем значение радиуса

    def area(self):
        return math.pi * self.radius ** 2    # Вычисляем площадь круга

    def perimeter(self):
        return 2 * math.pi * self.radius      # Вычисляем периметр круга

    # Рисуем круг на холсте
    def visualize(self, canvas):
        canvas.create_oval(50, 50, 50 + 2*self.radius, 50 + 2*self.radius, outline="blue", width=2)

# Класс для квадрата
class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    def visualize(self, canvas):
        canvas.create_rectangle(50, 50, 50 + self.side, 50 + self.side, outline="green", width=2)

# Класс для прямоугольника
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width  # Ширина
        self.height = height  # Высота

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def visualize(self, canvas):
        canvas.create_rectangle(50, 50, 50 + self.width, 50 + self.height, outline="orange", width=2)

# Добавление треугольника
class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def visualize(self, canvas):
        canvas.create_polygon(50, 150, 50 + self.a, 150, 50 + (self.a / 2), 150 - self.b, outline="purple", width=2, fill='')

# Класс для ромба
class Rhombus(Shape):
    def __init__(self, diagonal1, diagonal2):
        super().__init__()
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def area(self):
        # Площадь ромба через диагонали
        return (self.diagonal1 * self.diagonal2) / 2

    def perimeter(self):
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
    def __init__(self, a, b, c, d, h):
        super().__init__()
        self.a = a  # первое основание
        self.b = b  # второе основание
        self.c = c  # боковая сторона
        self.d = d  # боковая сторона
        self.h = h  # высота

    def area(self):
        return (self.a + self.b) * self.h / 2

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def visualize(self, canvas):
        # Визуализация трапеции на холсте
        canvas.create_polygon(50, 150, 50 + self.a, 150, 50 + self.a - (self.a - self.b) / 2, 150 - self.h, 50 + (self.a - self.b) / 2, 150 - self.h, outline="brown", width=2, fill='')



# Объемные фигуры

# Сфера
class Sphere(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return 4 * math.pi * self.radius ** 2   # 4πr²

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3    #  4/3πr³

    def visualize(self, canvas):
        canvas.create_oval(50, 50, 50 + 2*self.radius, 50 + 2*self.radius, outline="red", width=2)

# Класс для цилиндра
class Cylinder(Shape):
    def __init__(self, radius, height):
        super().__init__()
        self.radius = radius   # Основание
        self.height = height

    def area(self):
        # Полная площадь поверхности цилиндра
        return 2 * math.pi * self.radius * (self.radius + self.height)  # 2πr(r + h)

    def volume(self):
        # Объем цилиндра
        return math.pi * self.radius ** 2 * self.height     # πr²h

    def visualize(self, canvas):
        # Визуализация цилиндра (два овала и прямоугольник)
        canvas.create_oval(50, 50, 50 + 2 * self.radius, 50 + self.radius, outline="blue", width=2)
        canvas.create_oval(50, 50 + self.height, 50 + 2 * self.radius, 50 + self.height + self.radius, outline="blue", width=2)
        canvas.create_rectangle(50, 50 + self.radius / 2, 50 + 2 * self.radius, 50 + self.height + self.radius / 2, outline="blue", width=2)


# Класс для куба
class Cube(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        # Полная площадь поверхности куба
        return 6 * self.side ** 2

    def volume(self):
        # Объем куба
        return self.side ** 3

    def visualize(self, canvas):
        # Рисуем куб как квадрат с эффектом
        x, y = 50, 50
        offset = self.side / 2
        canvas.create_rectangle(x, y, x + self.side, y + self.side, outline="purple", width=2)     # Передний квадрат
        canvas.create_rectangle(x + offset, y + offset, x + self.side + offset, y + self.side + offset, outline="purple", width=2)      # Задний квадрат
        canvas.create_line(x, y, x + offset, y + offset, fill="purple", width=2)
        canvas.create_line(x + self.side, y, x + self.side + offset, y + offset, fill="purple", width=2)
        canvas.create_line(x, y + self.side, x + offset, y + self.side + offset, fill="purple", width=2)
        canvas.create_line(x + self.side, y + self.side, x + self.side + offset, y + self.side + offset, fill="purple", width=2)

# Класс для параллелепипеда
class Parallelepiped(Shape):
    def __init__(self, length, width, height):
        super().__init__()
        self.length = length
        self.width = width
        self.height = height

    def area(self):
        # Полная площадь поверхности параллелепипеда
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

    def volume(self):
        # Объем параллелепипеда
        return self.length * self.width * self.height

    def visualize(self, canvas):
        # Рисуем параллелепипед как прямоугольник с эффектом 3D
        x, y = 50, 50
        offset = self.width / 2
        canvas.create_rectangle(x, y, x + self.length, y + self.height, outline="green", width=2)
        canvas.create_rectangle(x + offset, y + offset, x + self.length + offset, y + self.height + offset, outline="green", width=2)
        canvas.create_line(x, y, x + offset, y + offset, fill="green", width=2)
        canvas.create_line(x + self.length, y, x + self.length + offset, y + offset, fill="green", width=2)
        canvas.create_line(x, y + self.height, x + offset, y + self.height + offset, fill="green", width=2)
        canvas.create_line(x + self.length, y + self.height, x + self.length + offset, y + self.height + offset, fill="green", width=2)

# Класс для пирамиды
class Pyramid(Shape):
    def __init__(self, base_length, base_width, height):
        super().__init__()
        self.base_length = base_length
        self.base_width = base_width
        self.height = height

    def area(self):
        # Площадь основания
        base_area = self.base_length * self.base_width
        # Вычисляем площадь боковых сторон
        side_area = (self.base_length * math.sqrt((self.base_width / 2) ** 2 + self.height ** 2) +
                     self.base_width * math.sqrt((self.base_length / 2) ** 2 + self.height ** 2))
        return base_area + side_area      # Общая площадь пирамиды

    def volume(self):
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
    def __init__(self, radius, height):
        super().__init__()
        self.radius = radius
        self.height = height

    def area(self):
        # Площадь боковой поверхности и полная площадь поверхности конуса
        slant_height = math.sqrt(self.radius ** 2 + self.height ** 2)
        return math.pi * self.radius * (self.radius + slant_height)

    def volume(self):
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


# Функции для вычислений
# Функция для расчета площади круга
def calculate_circle_area():
    try:
        radius = float(entry_circle.get())  # Получаем радиус от пользователя
        circle = Circle(radius)  # создаем объект круга
        result = circle.area()  # Вычисляем площадь
        # Показываем результат пользователю
        messagebox.showinfo("Результат", f"Площадь круга: {result:.2f}")
        canvas.delete("all")  # Очищаем холст
        circle.visualize(canvas)  # Рисуем круг
        update_shape_count_label()  # Обновляем количество созданных фигур
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число")  # Показываем ошибку, если введены некорректные данные

# Функция для квадрата
def calculate_square_area():
    try:
        side = float(entry_square.get())
        square = Square(side)
        result = square.area()
        messagebox.showinfo("Результат", f"Площадь квадрата: {result:.2f}")
        canvas.delete("all")
        square.visualize(canvas)
        update_shape_count_label()  # Обновляем количество созданных фигур
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число")

# Функция для прямоугольника
def calculate_rectangle_area():
    try:
        width = float(entry_rectangle_width.get())
        height = float(entry_rectangle_height.get())
        rectangle = Rectangle(width, height)
        result = rectangle.area()
        messagebox.showinfo("Результат", f"Площадь прямоугольника: {result:.2f}")
        canvas.delete("all")
        rectangle.visualize(canvas)
        update_shape_count_label()  # Обновляем количество созданных фигур
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

# Функция для трапеции
def calculate_trapezoid_area():
    try:
        a = float(entry_trapezoid_a.get())
        b = float(entry_trapezoid_b.get())
        c = float(entry_trapezoid_c.get())
        d = float(entry_trapezoid_d.get())
        h = float(entry_trapezoid_h.get())
        trapezoid = Trapezoid(a, b, c, d, h)
        result = trapezoid.area()
        messagebox.showinfo("Результат", f"Площадь трапеции: {result:.2f}")
        canvas.delete("all")
        trapezoid.visualize(canvas)
        update_shape_count_label()  # Обновляем количество созданных фигур
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")


# Функция для треугольника
def calculate_triangle_area():
    try:
        a = float(entry_triangle_a.get())
        b = float(entry_triangle_b.get())
        c = float(entry_triangle_c.get())

        # Проверка: существует ли треугольник
        if a + b > c and a + c > b and b + c > a:
            triangle = Triangle(a, b, c)  # Создаем объект треугольника
            result = triangle.area()  # вычисляем площадь
            # Показываем результат пользователю
            messagebox.showinfo("Результат", f"Площадь треугольника: {result:.2f}")
            canvas.delete("all")  # Очищаем холст
            triangle.visualize(canvas)  # Рисуем треугольник
            update_shape_count_label()  # Обновляем количество созданных фигур
        else:
            # показываем ошибку, если треугольник не может существовать
            messagebox.showerror("Ошибка", "Сумма двух сторон треугольника должна быть больше третьей стороны.")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")  # Ошибка при некорректных данных

# Функция для расчета площади и периметра ромба
def calculate_rhombus_area_perimeter():
    try:
        diagonal1 = float(entry_rhombus_d1.get())
        diagonal2 = float(entry_rhombus_d2.get())
        rhombus = Rhombus(diagonal1, diagonal2)
        area = rhombus.area()
        perimeter = rhombus.perimeter()
        messagebox.showinfo("Результат", f"Площадь ромба: {area:.2f}\nПериметр ромба: {perimeter:.2f}")
        canvas.delete("all")
        rhombus.visualize(canvas)
        update_shape_count_label()  # Обновляем количество созданных фигур
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")


def calculate_sphere_area_volume():
    try:
        radius = float(entry_sphere.get())
        sphere = Sphere(radius)
        surface_area = sphere.area()
        volume = sphere.volume()
        messagebox.showinfo("Результат", f"Площадь поверхности сферы: {surface_area:.2f}\nОбъем сферы: {volume:.2f}")
        canvas.delete("all")
        sphere.visualize(canvas)
        update_shape_count_label()  # Обновляем количество созданных фигур
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число")

# Функция для расчета площади и объема цилиндра
def calculate_cylinder_area_volume():
    try:
        radius = float(entry_cylinder_radius.get())
        height = float(entry_cylinder_height.get())
        cylinder = Cylinder(radius, height)
        surface_area = cylinder.area()
        volume = cylinder.volume()
        messagebox.showinfo("Результат", f"Площадь поверхности цилиндра: {surface_area:.2f}\nОбъем цилиндра: {volume:.2f}")
        canvas.delete("all")
        cylinder.visualize(canvas)
        update_shape_count_label()  # Обновляем количество созданных фигур
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

# Функция для расчета площади и объема куба
def calculate_cube_area_volume():
    try:
        side = float(entry_cube_side.get())
        cube = Cube(side)
        surface_area = cube.area()
        volume = cube.volume()
        messagebox.showinfo("Результат", f"Площадь поверхности куба: {surface_area:.2f}\nОбъем куба: {volume:.2f}")
        canvas.delete("all")
        cube.visualize(canvas)
        update_shape_count_label()  # Обновляем количество созданных фигур
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число")


# Функция для расчета площади и объема параллелепипеда
def calculate_parallelepiped_area_volume():
    try:
        length = float(entry_parallelepiped_length.get())
        width = float(entry_parallelepiped_width.get())
        height = float(entry_parallelepiped_height.get())
        parallelepiped = Parallelepiped(length, width, height)
        surface_area = parallelepiped.area()
        volume = parallelepiped.volume()
        messagebox.showinfo("Результат", f"Площадь поверхности параллелепипеда: {surface_area:.2f}\nОбъем параллелепипеда: {volume:.2f}")
        canvas.delete("all")
        parallelepiped.visualize(canvas)
        update_shape_count_label()  # Обновляем количество созданных фигур
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

# Функция для расчета площади и объема пирамиды
def calculate_pyramid_area_volume():
    try:
        base_length = float(entry_pyramid_base_length.get())
        base_width = float(entry_pyramid_base_width.get())
        height = float(entry_pyramid_height.get())
        pyramid = Pyramid(base_length, base_width, height)
        surface_area = pyramid.area()
        volume = pyramid.volume()
        messagebox.showinfo("Результат", f"Площадь поверхности пирамиды: {surface_area:.2f}\nОбъем пирамиды: {volume:.2f}")
        canvas.delete("all")
        pyramid.visualize(canvas)
        update_shape_count_label()  # Обновляем количество созданных фигур
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

# Функция для расчета площади и объема конуса
def calculate_cone_area_volume():
    try:
        radius = float(entry_cone_radius.get())
        height = float(entry_cone_height.get())
        cone = Cone(radius, height)
        surface_area = cone.area()
        volume = cone.volume()
        messagebox.showinfo("Результат", f"Площадь поверхности конуса: {surface_area:.2f}\nОбъем конуса: {volume:.2f}")
        canvas.delete("all")
        cone.visualize(canvas)
        update_shape_count_label()  # Обновляем количество созданных фигур
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")


# Обновление метки с количеством созданных фигур
def update_shape_count_label():
    shape_count_label.config(text=f"Количество созданных фигур: {Shape.total_shapes()}")


# Создаем главное окно программы
root = tk.Tk()
root.title("Геометрический калькулятор")  # заголовок окна

# Поля для ввода данных и кнопки для круга
frame_circle = tk.Frame(root)  # контейнер для ввода
frame_circle.pack()  # Показываем контейнер на экране
label_circle = tk.Label(frame_circle, text="Введите радиус круга:")  # Надпись для радиуса
label_circle.pack(side=tk.LEFT)  # Размещаем надпись слева
entry_circle = tk.Entry(frame_circle)  # Поле для ввода радиуса
entry_circle.pack(side=tk.LEFT)  # Размещаем поле слева
button_circle = tk.Button(frame_circle, text="Рассчитать", command=calculate_circle_area)  # Кнопка для расчета
button_circle.pack(side=tk.LEFT)  # Размещаем кнопку слева

#Квадрат
frame_square = tk.Frame(root)
frame_square.pack()
label_square = tk.Label(frame_square, text="Введите сторону квадрата:")
label_square.pack(side=tk.LEFT)
entry_square = tk.Entry(frame_square)
entry_square.pack(side=tk.LEFT)
button_square = tk.Button(frame_square, text="Рассчитать", command=calculate_square_area)
button_square.pack(side=tk.LEFT)

# Прямоугольник
frame_rectangle = tk.Frame(root)
frame_rectangle.pack()
label_rectangle_width = tk.Label(frame_rectangle, text="Введите ширину прямоугольника:")
label_rectangle_width.pack(side=tk.LEFT)
entry_rectangle_width = tk.Entry(frame_rectangle)
entry_rectangle_width.pack(side=tk.LEFT)

label_rectangle_height = tk.Label(frame_rectangle, text="Введите высоту прямоугольника:")
label_rectangle_height.pack(side=tk.LEFT)
entry_rectangle_height = tk.Entry(frame_rectangle)
entry_rectangle_height.pack(side=tk.LEFT)

button_rectangle = tk.Button(frame_rectangle, text="Рассчитать", command=calculate_rectangle_area)
button_rectangle.pack(side=tk.LEFT)

# Трапеция
frame_trapezoid = tk.Frame(root)
frame_trapezoid.pack()
label_trapezoid_a = tk.Label(frame_trapezoid, text="Введите основание a трапеции:")
label_trapezoid_a.pack(side=tk.LEFT)
entry_trapezoid_a = tk.Entry(frame_trapezoid)
entry_trapezoid_a.pack(side=tk.LEFT)

label_trapezoid_b = tk.Label(frame_trapezoid, text="Введите основание b трапеции:")
label_trapezoid_b.pack(side=tk.LEFT)
entry_trapezoid_b = tk.Entry(frame_trapezoid)
entry_trapezoid_b.pack(side=tk.LEFT)

label_trapezoid_c = tk.Label(frame_trapezoid, text="Введите боковую сторону c трапеции:")
label_trapezoid_c.pack(side=tk.LEFT)
entry_trapezoid_c = tk.Entry(frame_trapezoid)
entry_trapezoid_c.pack(side=tk.LEFT)

label_trapezoid_d = tk.Label(frame_trapezoid, text="Введите боковую сторону d трапеции:")
label_trapezoid_d.pack(side=tk.LEFT)
entry_trapezoid_d = tk.Entry(frame_trapezoid)
entry_trapezoid_d.pack(side=tk.LEFT)

label_trapezoid_h = tk.Label(frame_trapezoid, text="Введите высоту трапеции:")
label_trapezoid_h.pack(side=tk.LEFT)
entry_trapezoid_h = tk.Entry(frame_trapezoid)
entry_trapezoid_h.pack(side=tk.LEFT)

button_trapezoid = tk.Button(frame_trapezoid, text="Рассчитать", command=calculate_trapezoid_area)
button_trapezoid.pack(side=tk.LEFT)


# Треугольник
frame_triangle = tk.Frame(root)
frame_triangle.pack()
label_triangle_a = tk.Label(frame_triangle, text="Введите сторону a треугольника:")
label_triangle_a.pack(side=tk.LEFT)
entry_triangle_a = tk.Entry(frame_triangle)
entry_triangle_a.pack(side=tk.LEFT)

label_triangle_b = tk.Label(frame_triangle, text="Введите сторону b треугольника:")
label_triangle_b.pack(side=tk.LEFT)
entry_triangle_b = tk.Entry(frame_triangle)
entry_triangle_b.pack(side=tk.LEFT)

label_triangle_c = tk.Label(frame_triangle, text="Введите сторону c треугольника:")
label_triangle_c.pack(side=tk.LEFT)
entry_triangle_c = tk.Entry(frame_triangle)
entry_triangle_c.pack(side=tk.LEFT)

button_triangle = tk.Button(frame_triangle, text="Рассчитать", command=calculate_triangle_area)
button_triangle.pack(side=tk.LEFT)

# Ромб
frame_rhombus = tk.Frame(root)
frame_rhombus.pack()
label_rhombus_d1 = tk.Label(frame_rhombus, text="Введите первую диагональ ромба:")
label_rhombus_d1.pack(side=tk.LEFT)
entry_rhombus_d1 = tk.Entry(frame_rhombus)
entry_rhombus_d1.pack(side=tk.LEFT)

label_rhombus_d2 = tk.Label(frame_rhombus, text="Введите вторую диагональ ромба:")
label_rhombus_d2.pack(side=tk.LEFT)
entry_rhombus_d2 = tk.Entry(frame_rhombus)
entry_rhombus_d2.pack(side=tk.LEFT)

button_rhombus = tk.Button(frame_rhombus, text="Рассчитать", command=calculate_rhombus_area_perimeter)
button_rhombus.pack(side=tk.LEFT)

# Сфера
frame_sphere = tk.Frame(root)
frame_sphere.pack()
label_sphere = tk.Label(frame_sphere, text="Введите радиус сферы:")
label_sphere.pack(side=tk.LEFT)
entry_sphere = tk.Entry(frame_sphere)
entry_sphere.pack(side=tk.LEFT)
button_sphere = tk.Button(frame_sphere, text="Рассчитать", command=calculate_sphere_area_volume)
button_sphere.pack(side=tk.LEFT)

# Цилиндр
frame_cylinder = tk.Frame(root)
frame_cylinder.pack()
label_cylinder_radius = tk.Label(frame_cylinder, text="Введите радиус основания цилиндра:")
label_cylinder_radius.pack(side=tk.LEFT)
entry_cylinder_radius = tk.Entry(frame_cylinder)
entry_cylinder_radius.pack(side=tk.LEFT)

label_cylinder_height = tk.Label(frame_cylinder, text="Введите высоту цилиндра:")
label_cylinder_height.pack(side=tk.LEFT)
entry_cylinder_height = tk.Entry(frame_cylinder)
entry_cylinder_height.pack(side=tk.LEFT)

button_cylinder = tk.Button(frame_cylinder, text="Рассчитать", command=calculate_cylinder_area_volume)
button_cylinder.pack(side=tk.LEFT)


# Куб
frame_cube = tk.Frame(root)
frame_cube.pack()
label_cube_side = tk.Label(frame_cube, text="Введите длину ребра куба:")
label_cube_side.pack(side=tk.LEFT)
entry_cube_side = tk.Entry(frame_cube)
entry_cube_side.pack(side=tk.LEFT)

button_cube = tk.Button(frame_cube, text="Рассчитать", command=calculate_cube_area_volume)
button_cube.pack(side=tk.LEFT)


# Параллелепипед
frame_parallelepiped = tk.Frame(root)
frame_parallelepiped.pack()
label_parallelepiped_length = tk.Label(frame_parallelepiped, text="Введите длину параллелепипеда:")
label_parallelepiped_length.pack(side=tk.LEFT)
entry_parallelepiped_length = tk.Entry(frame_parallelepiped)
entry_parallelepiped_length.pack(side=tk.LEFT)

label_parallelepiped_width = tk.Label(frame_parallelepiped, text="Введите ширину параллелепипеда:")
label_parallelepiped_width.pack(side=tk.LEFT)
entry_parallelepiped_width = tk.Entry(frame_parallelepiped)
entry_parallelepiped_width.pack(side=tk.LEFT)

label_parallelepiped_height = tk.Label(frame_parallelepiped, text="Введите высоту параллелепипеда:")
label_parallelepiped_height.pack(side=tk.LEFT)
entry_parallelepiped_height = tk.Entry(frame_parallelepiped)
entry_parallelepiped_height.pack(side=tk.LEFT)

button_parallelepiped = tk.Button(frame_parallelepiped, text="Рассчитать", command=calculate_parallelepiped_area_volume)
button_parallelepiped.pack(side=tk.LEFT)


# Пирамида
frame_pyramid = tk.Frame(root)
frame_pyramid.pack()
label_pyramid_base_length = tk.Label(frame_pyramid, text="Введите длину основания пирамиды:")
label_pyramid_base_length.pack(side=tk.LEFT)
entry_pyramid_base_length = tk.Entry(frame_pyramid)
entry_pyramid_base_length.pack(side=tk.LEFT)

label_pyramid_base_width = tk.Label(frame_pyramid, text="Введите ширину основания пирамиды:")
label_pyramid_base_width.pack(side=tk.LEFT)
entry_pyramid_base_width = tk.Entry(frame_pyramid)
entry_pyramid_base_width.pack(side=tk.LEFT)

label_pyramid_height = tk.Label(frame_pyramid, text="Введите высоту пирамиды:")
label_pyramid_height.pack(side=tk.LEFT)
entry_pyramid_height = tk.Entry(frame_pyramid)
entry_pyramid_height.pack(side=tk.LEFT)

button_pyramid = tk.Button(frame_pyramid, text="Рассчитать", command=calculate_pyramid_area_volume)
button_pyramid.pack(side=tk.LEFT)


# Конус
frame_cone = tk.Frame(root)
frame_cone.pack()
label_cone_radius = tk.Label(frame_cone, text="Введите радиус основания конуса:")
label_cone_radius.pack(side=tk.LEFT)
entry_cone_radius = tk.Entry(frame_cone)
entry_cone_radius.pack(side=tk.LEFT)

label_cone_height = tk.Label(frame_cone, text="Введите высоту конуса:")
label_cone_height.pack(side=tk.LEFT)
entry_cone_height = tk.Entry(frame_cone)
entry_cone_height.pack(side=tk.LEFT)

button_cone = tk.Button(frame_cone, text="Рассчитать", command=calculate_cone_area_volume)
button_cone.pack(side=tk.LEFT)


# Холст для визуализации фигур
canvas = Canvas(root, width=400, height=400)
canvas.pack()


# Отображение количества созданных фигур
shape_count_label = tk.Label(root, text=f"Количество созданных фигур: {Shape.total_shapes()}")
shape_count_label.pack()

root.mainloop()           # запускаем главный цикл программы, чтобы окно оставалось открытым

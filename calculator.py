import math
import tkinter as tk
from tkinter import messagebox, Canvas, ttk
from abc import ABC, abstractmethod

# Базовый класс для всех фигур (абстрактный)
class Shape(ABC):
    shapes_count = 0  # Переменная класса для хранения количества созданных фигур

    def __init__(self):
        Shape.shapes_count += 1  # Увеличиваем счетчик при создании каждой фигуры

    @classmethod
    def total_shapes(cls) -> int:
        return cls.shapes_count  # Метод класса для получения общего числа фигур

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

    def visualize(self, canvas: Canvas):
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

    def visualize(self, canvas: Canvas):
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

    def visualize(self, canvas: Canvas):
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

    def visualize(self, canvas: Canvas):
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

    def visualize(self, canvas: Canvas):
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

    def visualize(self, canvas: Canvas):
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

    def visualize(self, canvas: Canvas):
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

    def visualize(self, canvas: Canvas):
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

    def visualize(self, canvas: Canvas):
        # Рисуем конус как треугольник с овальным основанием
        x, y = 50, 150

        canvas.create_oval(x, y, x + 2 * self.radius, y + 20, outline="blue", width=2)  # Овальное основание

        # Рисуем боковые стороны как треугольник
        canvas.create_line(x, y + 10, x + self.radius, y - self.height, fill="blue", width=2)  # Левая сторона
        canvas.create_line(x + 2 * self.radius, y + 10, x + self.radius, y - self.height, fill="blue",
                           width=2)  # Правая сторона


figures = {
    "Круг": Circle,
    "Квадрат": Square,
    "Прямоугольник": Rectangle,
    "Треугольник": Triangle,
    "Ромб": Rhombus,
    "Трапеция": Trapezoid,
    "Сфера": Sphere,
    "Цилиндр": Cylinder,
    "Куб": Cube,
    "Параллелепипед": Parallelepiped,
    "Пирамида": Pyramid,
    "Конус": Cone
}

figure_params = {
    "Круг": ["радиус"],
    "Квадрат": ["сторона"],
    "Прямоугольник": ["ширина", "высота"],
    "Треугольник": ["сторона A", "сторона B", "сторона C"],
    "Ромб": ["первая диагональ", "вторая диагональ"],
    "Трапеция": ["основание a", "основание b", "боковая сторона c", "боковая сторона d", "высота"],
    "Сфера": ["радиус"],
    "Цилиндр": ["радиус основания", "высота"],
    "Куб": ["сторона"],
    "Параллелепипед": ["длина", "ширина", "высота"],
    "Пирамида": ["длина основания", "ширина основания", "высота"],
    "Конус": ["радиус основания", "высота"]
}

property_names = {
    'area': 'Площадь',
    'volume': 'Объем',
    'perimeter': 'Периметр'
}

entries = {}  # Словарь для хранения ввода


# Функция для выбора фигуры из выпадающего меню
def selected(event) -> None:
    selection = combobox.get()  # Получаем выбранное значение
    for widget in frame_inputs.winfo_children():
        widget.destroy()  # Удаляем все виджеты из фрейма перед добавлением новых

    # Проверяем, есть ли выбранная фигура в списке параметров и создаем поле ввода для него
    if selection in figure_params:
        params = figure_params[selection]
        create_input_fields(params)

        button = tk.Button(frame_inputs, text="Рассчитать", command=lambda: calculate_from_input(selection, params))
        button.pack(side=tk.LEFT)

# Функция для ввода параметров от пользователя
def create_input_fields(params: list[str]) -> None:
    label_info = tk.Label(frame_inputs, text="Введите параметры:")
    label_info.pack(side=tk.TOP)

    for param in params:
        label = tk.Label(frame_inputs, text=f"{param}")
        label.pack(side=tk.LEFT)
        entry = tk.Entry(frame_inputs)
        entry.pack(side=tk.LEFT)
        entries[param] = entry

# Функция для передачи введенных данных в расчет
def calculate_from_input(selection: str, params: list[str]) -> None:
    try:
        # Получаем данные, введенные пользователем, которые хранятся в словаре entries (выше)
        args = [float(entries[param].get()) for param in params]

        # Используем словарь figures для получения класса фигуры
        shape_class = figures[selection]

        # Вызываем универсальную функцию для расчета
        calculate_shape(shape_class, *args)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные данные")


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

        # Список свойств, которые можно вычислить для фигуры
        properties = ['area', 'volume', 'perimeter']

        # Проходим по списку свойств и проверяем есть ли они у фигуры
        for prop in properties:
            if hasattr(shape, prop):
                # Если свойство существует, вызываем его с помощью getattr
                value = getattr(shape, prop)()
                name_prop = property_names.get(prop, prop)    # Выводим пользователю свойство на русском языке
                display_results(shape, name_prop, value)

    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные данные")


# Обновление метки с количеством созданных фигур
def update_shape_count_label() -> None:
    shape_count_label.config(text=f"Количество созданных фигур: {Shape.total_shapes()}")


# Создаем главное окно программы
root = tk.Tk()
root.title("Геометрический калькулятор")  # заголовок окна

figure_names = list(figures.keys())   # Получаем список названий фигур из словаря figures

# Метка для вывода выбранной фигуры
label = ttk.Label(text="Выберите фигуру")
label.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)

# Combobox для выбора фигуры
combobox = ttk.Combobox(values=figure_names, state="readonly")
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

if __name__ == "__main__":
    root.mainloop()

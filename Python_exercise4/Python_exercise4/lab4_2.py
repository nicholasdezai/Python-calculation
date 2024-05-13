import collections, sys
from PyQt6.QtCore import Qt
from lab3_4 import *
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
)


class Servant(Lunch):
    def __init__(self) -> None:
        super().__init__()
        self.food_dict = {}

    def order(self, food_name: str, is_add: bool = True):
        self.food_dict.setdefault(food_name, 0)
        if is_add:
            self.food_dict[food_name] += 1
        elif self.food_dict[food_name] > 0:
            self.food_dict[food_name] -= 1

    def result(self):
        food_count = collections.Counter(self._customer._food_list)
        return [(food, count) for food, count in food_count.items()]


class Meal(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__initUI()
        self.__initData()
        self.show()

    def __initUI(self):
        self.setGeometry(100, 100, 600, 100)
        self.setWindowTitle("点餐界面")
        self.lineedit = QLineEdit(
            self,
            placeholderText="请输入要点的菜",
            clearButtonEnabled=True,
        )
        # test_words = "123456"
        self.button_add_food = QPushButton(
            "确定", clicked=lambda: self.__order_food(self.lineedit.text())
        )

        self.button_finish = QPushButton("完成点餐", clicked=self.__show_food_list)

        self.layouts = QVBoxLayout()
        self.setLayout(self.layouts)
        self.layouts.addWidget(self.lineedit)
        self.layouts.addWidget(self.button_add_food)
        self.layouts.addWidget(self.button_finish)

    def __initData(self):
        # self.servant = Servant()
        self.food_dict = {}
        self.label_dict = {}

    def __get_icons(self, food_name: str):
        return (
            QLabel(food_name, self),
            QLabel("数量：1", self),
            QPushButton("+", clicked=lambda: self.__order_food(food_name, True)),
            QPushButton("-", clicked=lambda: self.__order_food(food_name, False)),
        )

    def __order_food(self, food_name: str, is_add: bool = True):
        if not food_name:
            return
        self.food_dict.setdefault(food_name, 0)
        if is_add:
            self.food_dict[food_name] += 1
            if self.food_dict[food_name] == 1:
                food_layout = self.__add_food_layout(self.__get_icons(food_name))
                self.label_dict[food_name] = food_layout
            # else:
        elif self.food_dict[food_name] > 0:
            self.food_dict[food_name] -= 1
            if self.food_dict[food_name] == 0:
                self.__remove_food_layout(food_name)
        # self.label_dict.setdefault(food_name,0)
        self.label_dict[food_name].itemAt(1).widget().setText(
            "数量：" + str(self.food_dict[food_name])
        )
        self.update()

    def __add_food_layout(self, icons):
        # icons = self.__get_icons(food_name)
        food_layout = QHBoxLayout()
        for icon in icons:
            food_layout.addWidget(icon)
        self.layouts.addLayout(food_layout)
        return food_layout

    def __remove_food_layout(self, food_name):
        target_dict = self.label_dict[food_name]
        # if target_dict.count() > 0:
        for i in range(target_dict.count()):
            target_dict.itemAt(i).widget().deleteLater()

        target_dict.deleteLater()

    def __show_food_list(self):
        self.layouts.addWidget(QLabel("订单内容如下:"))
        for food_name, food_count in self.food_dict.items():
            self.__remove_food_layout(food_name)
            self.__add_food_layout((QLabel(food_name), QLabel(f"数量：{food_count}")))
        self.button_add_food.clicked.disconnect()
        self.button_finish.clicked.disconnect()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Meal()
    sys.exit(app.exec())

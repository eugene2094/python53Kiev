from abc import ABC, abstractmethod


# AbstractFactory
class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


# ConcreteFactory
class LightThemeFactory(UIFactory):
    def create_button(self):
        return LightButton()

    def create_checkbox(self):
        return LightCheckbox()


class DarkThemeFactory(UIFactory):
    def create_button(self):
        return DarkButton()

    def create_checkbox(self):
        return DarkCheckbox()


# AbstractProduct
class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass


# ConcreteProduct
class LightButton(Button):
    def click(self):
        print("Light Button clicked!")


class DarkButton(Button):
    def click(self):
        print("Dark Button clicked!")


class LightCheckbox(Checkbox):
    def check(self):
        print("Light Checkbox clicked!")


class DarkCheckbox(Checkbox):
    def check(self):
        print("Dark Checkbox clicked!")


# Client (Клієнт
def client_code(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.click()
    checkbox.check()


light_factory = LightThemeFactory()
client_code(light_factory)

dark_factory = DarkThemeFactory()
client_code(dark_factory)

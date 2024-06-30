"""
Паттерн Adapter (Адаптер) позволяет объектам с несовместимыми интерфейсами работать вместе.
В данном примере HDMItoUSBAdapter адаптирует интерфейс HDMI-устройства (HDMIComputer)
к интерфейсу USB-порта, чтобы они могли быть подключены друг к другу.

Применение:

* Паттерн Adapter полезен, когда вам нужно использовать существующий класс,
но его интерфейс не соответствует вашим потребностям.

* Он позволяет вам взаимодействовать с объектами, имеющими различные интерфейсы,
без изменения исходного кода этих объектов.

* Adapter также может быть полезен при интеграции сторонних библиотек или компонентов в вашу систему,
если их интерфейсы не совпадают с вашими требованиями.
"""


class USBPort:
    def connect_usb_device(self, device):
        """
        Подключает USB-устройство к порту.
        """
        device.connect()


class HDMItoUSBAdapter:
    def __init__(self, hdmi_device):
        self.hdmi_device = hdmi_device

    def connect(self):
        """
        Адаптирует HDMI-устройство к USB-порту.
        """
        self.hdmi_device.connect_hdmi_to_usb()


class HDMIComputer:
    def connect_hdmi_to_usb(self):
        """
        Подключает HDMI-устройство к USB-порту.
        """
        print("HDMI-устройство подключено к USB-порту компьютера")


# Использование паттерна Adapter
usb_port = USBPort()
hdmi_device = HDMIComputer()
adapter = HDMItoUSBAdapter(hdmi_device)
usb_port.connect_usb_device(adapter)

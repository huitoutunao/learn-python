# 类的继承

# 单继承
class Phone:
    IMEI = None
    producer = 'HM'

    def call_by_4g(self):
        print('4g call')

class Phone2024(Phone):
    face_id = '10001'

    def call_by_5g(self):
        print('5g call')

phone = Phone2024()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()

# 多继承
class NFC:
    nfc_type = 'NFC-A'
    producer = 'Huawei'

    def read_card(self):
        print('read card')

class RemoteControl:
    def control(self):
        print('remote control')

class Phone2025(Phone, NFC, RemoteControl):
    pass # 空-即什么也不做

phone2 = Phone2025()
print(phone2.producer)
phone2.call_by_4g()
phone2.read_card()
phone2.control()

# 调用父类同名成员
class Phone2026(Phone, NFC, RemoteControl):
    def call_by_4g(self):
        print('4g call')
        # 调用父类同名成员
        Phone.call_by_4g(self)

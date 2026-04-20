class ChatBot:
    def __init__(self):
        self.salom_sozlari = ["Assalomu alaykum", "Salom", "Merhaba"]
        self.xayr_sozlari = ["Xayr", "Xayrli tong", "Xayrli kech"]
        self.savol_sozlari = ["Nega", "Qayerdan", "Qachon"]

    def salom_ber(self):
        return random.choice(self.salom_sozlari)

    def xayr_ber(self):
        return random.choice(self.xayr_sozlari)

    def savol_ber(self):
        return random.choice(self.savol_sozlari)

    def javob_ber(self, savol):
        if savol.lower() in self.salom_sozlari:
            return self.xayr_ber()
        elif savol.lower() in self.xayr_sozlari:
            return self.salom_ber()
        elif savol.lower() in self.savol_sozlari:
            return "Men sizga yordam beraman"
        else:
            return "Men sizga yordam beraman"

import random

chat_bot = ChatBot()

while True:
    savol = input("Botga savol berishingiz mumkin: ")
    print(chat_bot.javob_ber(savol))
```

Kodda chat botning asosiy funksiyalari quyidagilar:

- `salom_ber`: Bot salom beradi
- `xayr_ber`: Bot xayr beradi
- `savol_ber`: Bot savol beradi
- `javob_ber`: Botga qilingan savolga javob beradi

Chat botga savol berish uchun quyidagilar qiling:

1. Chat bot dasturini ishga tushiring.
2. Chat botga savol berishingiz mumkin.
3. Chat bot sizga javob beradi.

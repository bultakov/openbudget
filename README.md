# OpenBudget

```
pip install OpenBudgetAPI -U
```

OpenBudget.uz tizimining Ovoz berish xizmatini ishlatish uchun yordamchi.

Foydalanishni boshlash uchun OpenBudget classidan obyekt olamiz va ushbu obyektdan kerakli so'rovlarni yuborib
foydalanishimiz mumkin bo'ladi.

Mavjud so'rovlar:

1. Telefon nomerga kod yuborish.
2. Kelgan kodni tasdiqlash.

## Namuna:

```python
from asyncio import get_event_loop

from openbudget import OpenBudget


async def main():
    openbudget = OpenBudget(phone='99899#######', application='######')
    data: dict = await openbudget.send_code()
    if data.get('token'):
        code: str = input('******')
        response: dict = await openbudget.vote(token=data.get('token'), code=code)
        print(response)
    await openbudget.close()


if __name__ == '__main__':
    get_event_loop().run_until_complete(main())
```

**Diqqat eslatma!**

**Siz ushbu yordamchi dasturdan foydalanishda barcha javobgarlikni o'zingizga olasiz, ushbu dastur ishlab chiquvchisi
sizning harakatlaringizga javobgar emas.**

🔗 Manzili: https://openbudget.uz

💻 Dasturchi: https://t.me/IbrohimBultakov

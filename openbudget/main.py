from openbudget.requests import Requests


class OpenBudget(Requests):
    async def send_code(self) -> dict:
        json_data = {
            'phone': self.phone,
            'application': self.application
        }
        return await self._requests(json_data=json_data, url='https://admin.openbudget.uz/api/v1/user/validate_phone/')

    async def vote(self, token: str, code: str) -> dict:
        json_data = {
            'phone': self.phone,
            'otp': code,
            'token': token,
            'application': self.application
        }
        return await self._requests(json_data=json_data, url='https://admin.openbudget.uz/api/v1/user/temp/vote/')

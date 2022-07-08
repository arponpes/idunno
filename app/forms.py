from typing import List
from typing import Optional

from fastapi import Request


class JobCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.a_side: Optional[str] = None
        self.b_side: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.a_side = form.get("a_side")
        self.b_side = form.get("b_side")

    def is_valid(self):
        if not self.a_side:
            self.errors.append("a_side is required")
        if not self.b_side:
            self.errors.append("b_side is required")
        print(self.errors)
        return not self.errors

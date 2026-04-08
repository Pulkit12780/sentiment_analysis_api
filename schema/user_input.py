from pydantic import BaseModel, Field
from typing import Annotated

class UserInput(BaseModel):
    text: Annotated[str,Field(...,title='User input', examples=['hello this is a sample text'])]

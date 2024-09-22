import enum 
from typing import Annotated
from livekit.agents import llm


class Zone(enum.Enum):
    LIVING_ROOM = "living_room"
    BED_ROOM = "bedroom" 
    KITCHEN =   "kitchen"
    BATHROOM = "bathroom"
    OFFICE = "office"

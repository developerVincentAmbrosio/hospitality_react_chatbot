from typing import Annotated, TypedDict, List, Dict, Any
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class ChatbotState(TypedDict):
    """Tracks conversation histroy, variables and busniess logic"""

    # chat history
    messages: Annotated[List[BaseMessage], add_messages]

    # guest and res context (from services/db.py)
    guest_info: Dict[str, Any]

    # progression flags
    greeted: bool
    checked_in: bool
    upsell_ptiched: bool

    # data from user
    checkin_data: Dict[str, Any]

    # offers
    targeted_offers: List[str]

def get_state() -> ChatbotState:
    """helper to intialize clean state"""

    return {
        "messages": [],
        "guest_info": {},
        "greeted": False,
        "checked_in": False,
        "upsell_pitched": False,
        "checkin_data": {},
        "targeted_offers": []
    }
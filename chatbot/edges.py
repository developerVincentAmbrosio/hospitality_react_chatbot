from typing import Literal
from chatbot.state import ChatbotState

def route_after_greeting(state:ChatbotState) -> Literal["checkin", "upsell_pitched", "chat"]:
    """determines where to route the use after greeting"""

    # checks to see if guest has bee greeted
    if state.get("greeted") == False:
        return "greeting"

    # checks to see if guest is checked in yet
    elif state.get("checked_in") == False:
        return "checkin"

    # upsells, if that has not been done yet
    if state.get("upsell_ptiched") == False:
        return "upsell_pitched"

    else:
        return "__end__"

def route_after_checkin(state:ChatbotState) -> Literal["upsell", "chat"]:
    """determines route after checkin"""

    # upsells, if that has not been done yet
    if state.get("upsell_ptiched") == False:
        return "upsell"

    else:
        return "chat"

def route_convo_loop(state:ChatbotState) -> Literal["greeting", "checkin", "upsell", "__end__"]:
    """master router"""

    # checks to see if guest was greeted
    if state.get("greeted") == False:
        return "greeting"

    # checks to see if guest is checked in
    elif state.get("checked_in") == False:
        return "checkin"
    
    # checks to see if guest was upsold with amenities
    elif state.get("upsell_ptiched") == False:
        return "upsell"

    else:
        return "__end__"
    
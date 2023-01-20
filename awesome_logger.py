#!/bin/python3

NUMBER_OF_ERROR_MESSAGES = 5

def get_error_code_message(error_code: int) -> str:
    if error_code == 0:
        return "There is a problem with the flux capacitor"
    elif error_code == 1:
        return "There is a problem with the temporal re-igniter"
    elif error_code == 2:
        return "Shields are down"
    elif error_code == 3:
        return "The auto-pilot is drunk"
    else:
        return ""    
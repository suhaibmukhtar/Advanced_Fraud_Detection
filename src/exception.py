"""
Exception Handling

The exc_info() function is a method from the sys module in Python that  provides information about the
most recent exception caught. "When an error occurs and is handled in an except block",after that
 sys.exc_info() can be called to obtain details about the exception, such as the type of error, the error
 message, and the traceback object, which holds details about the point in the code where the error 
 occurred.

The exc_info() function returns a tuple with three elements:

Type of Exception (exc_type) - the type of the exception 
(e.g., ZeroDivisionError, ValueError).
Exception Value (exc_value) - the actual error message associated with the
 exception.
Traceback Object (exc_tb) - a traceback object that provides information 
about where in the code the error occurred.
The third element, exc_tb, is useful for logging or debugging, as it 
allows you to trace the exact line and code segment that led to the 
exception.


sys->library is useful for handling exceptions and will contain the
information about them

"""
#### Example

# import sys

# def divide(a, b):
#     try:
#         result = a / b
#     except Exception as e:
#         exc_type, exc_value, exc_tb = sys.exc_info()
        
#         print("Exception type:", exc_type)  # Type of exception, e.g., <class 'ZeroDivisionError'>
#         print("Exception message:", exc_value)  # Error message, e.g., division by zero
#         print("Traceback object:", exc_tb)  # Traceback object
#         print("Traceback details:")

#         # Print traceback details
#         while exc_tb:
#             print("File:", exc_tb.tb_frame.f_code.co_filename)
#             print("Line:", exc_tb.tb_lineno)
#             print("Function:", exc_tb.tb_frame.f_code.co_name)
#             exc_tb = exc_tb.tb_next

# divide(10, 0)
import sys
from src.logger import logging

#this is called when exception occurs in our code and to handle that this function is used
#error_detail: Accepts the sys module to use its exc_info() function, which is required to get 
# detailed exception information.
def error_message_details(error_message, error_detail:sys):
    #returns three Exception type, exception message, traceback object where error occured in code
    exc_type,exc_value,exc_tb=error_detail.exc_info()
    exception_type=exc_type
    exception_msg=exc_value
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_number=exc_tb.tb_lineno
    function_name=exc_tb.tb_frame.f_code.co_name
    error_message=f"Excetion Type is: {exception_type},Exception message is: {exception_msg}. Exception has occured in File: {file_name}, in line no: {line_number}, inside function: {function_name}"
    logging.info(error_message)
    return error_message

class CustomException(Exception): #receives custom exception as input
    def __init__(self, error_message, error_details:sys): #error details is sys library
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_details)
    
    def __str__(self):
        return self.error_message #when exception obj called returns the error message detailed


if __name__=="__main__":
    logging.info("Started the Project pipeline")
    try:
        a=1/0
        logging.info("Division By Zero error")
    except Exception as e:
        raise CustomException(e,sys)
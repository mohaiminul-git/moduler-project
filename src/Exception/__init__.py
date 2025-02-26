import sys

class Custom_exception(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        self.error_message = Custom_exception.get_detailed_error_mssg(error_message, error_detail)

    @staticmethod
    def get_detailed_error_mssg(error_message: Exception, error_detail: sys) -> str:
        _, _, exec_tb = error_detail.exc_info()
        
        # Extract error details
        try_block_line_number = exec_tb.tb_lineno  # Line where the error occurred
        exceptional_block_line_number = exec_tb.tb_frame.f_lineno  # Line in the traceback frame
        file_name = exec_tb.tb_frame.f_code.co_filename  # File where the error occurred
        
        # Properly format the error message
        error_message_formatted = f"""
        Error occurred in execution of:
        File: {file_name}
        Try block line number: [{try_block_line_number}]
        Exception block line number: [{exceptional_block_line_number}]
        Error message: [{error_message}]
        """
        return error_message_formatted.strip()

    def __str__(self):
        return self.error_message

    def __repr__(self):
        return f"{Custom_exception.__name__}({self.error_message})"
# ------------------------  Color Variables  ------------------------

green_color = "\033[1;32m"
red_color="\033[0;31m"
no_color = "\033[0m"
yellow_color ="\033[0;33m"
blue_color ="\033[0;34m"
purple_color = "\033[0;35m"
light_yellow = "\033[0;93m"


# ------------------------  Message Variables  ------------------------


ok_message = f"{green_color} [ OK ] {no_color}"
failed_message = f"{red_color} [ FAILED ] {no_color}"
warning_message = f"{yellow_color} [ WARNING ] {no_color}"
info_message = f"{blue_color} [ INFO ] {no_color}"
question_message = f"{purple_color} [ QUESTION ] {no_color}"
process_message = f"{light_yellow} [ IN PROCESS ] {no_color}"


def add_header_and_footer(output):
    reforamted_output = f""" 
    ============================================
    {output}
    ============================================
    """
    return print(reforamted_output)
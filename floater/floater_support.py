import json
import os
import re
from datetime import datetime

class FloatConverter:

    def __init__(self) -> None:
        self.patterns = {
            1: "[0-9]{1,3}(\,[0-9]{3}){1,5}\.[0-9]+",  # 1,234,567.890
            2: "[0-9]{1,3}(\.[0-9]{3}){1,5}\,[0-9]+",  # 1.234.567,890
            3: "[0-9]{1,3}(\,[0-9]{3}){2,5}",  # 1,234,567
            4: "[0-9]+[\,][0-9]+",  # 1,234
            5: "[0-9]+[\.][0-9]+",  # 1.234
            6: "[0-9]+",  # 1
        }

    def convert(self, value: str):
        value = value.replace(' ', '')
        for count, pattern in self.patterns.items():
            match = re.search(pattern, value)
            if match is not None:
                value = match.group(0)
                if count in (2, 4):
                    value = value.replace('.', '').replace(',', '.')
                elif count in (1, 3):
                    value = value.replace(',', '')
                return float(value)
        raise ValueError(f'This value ({value}) can not be converted into float type')


class DateConverter:

    def __init__(self) -> None:

        json_file_path = os.path.join(os.getcwd(), 'data', 'floater_config.json')
        with open(json_file_path) as json_file:
            self.formats = json.load(json_file)

    def convert(self, value: str, output_format: str):
        date_obj = None

        formats = self.formats["time_formats"] if "%H" in output_format else self.formats["date_formats"]
        
        # bring possible separators to dot
        value = re.sub(r"(\\|\/|-|,)", '.', value)
        # clean of letters and signs on the edges 
        value = re.sub(r"(^\D*|\D*$)", '', value)

        for format in formats:
            try:
                date_obj = datetime.strptime(value, format)
                if date_obj.year == 1900:
                    date_obj = date_obj.replace(year=datetime.now().year)
            except ValueError:
                pass

            if date_obj is not None:
                try:
                    value = datetime.strftime(date_obj, output_format)
                except ValueError:
                    raise ValueError(f'Passed format ({output_format}) is wrong')
                return value
        
        raise ValueError(f'This value ({value}) can not be converted into date type')

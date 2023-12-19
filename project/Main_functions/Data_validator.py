class Validator:
    @staticmethod
    def sort_by_parameter(list_of_sortable_objects, specific_attributes=None, second_specific_attributes=None,
                          reverse=False):
        if specific_attributes:
            return sorted(list_of_sortable_objects, reverse=reverse,
                          key=lambda x: (
                              getattr(x, specific_attributes, 0),
                              getattr(x, second_specific_attributes, 0)))
        return sorted(list_of_sortable_objects, key=lambda x: x)

    @staticmethod
    def get_validated_data(data_name, data_type, required_data=[], required_choice=[], data_min_length=None,
                           data_max_length=None):
        while True:
            if data_name in required_data:
                data = input(f"*Please enter your {data_name}: ")
            else:
                data = input(f"You can enter your {data_name} (optional): ")

            if Validator.is_valid_type(data, type_of_data=data_type) and \
                    Validator.is_min_length(data, data_min_length) and \
                    Validator.is_max_length(data, data_max_length) and \
                    Validator.is_in_choises(data, required_choice):
                return data

    @staticmethod
    def is_valid_type(data_, type_of_data):
        if Validator.type(data_) != type_of_data:
            print(f"Error: {data_} is not of type {type_of_data.__name__}")
            return False
        return True

    @staticmethod
    def length(output):
        if isinstance(output, str):
            try:
                int_value = int(output)
                return int_value
            except ValueError:
                return len(output.strip())
        elif isinstance(output, list):
            return len(output)
        elif isinstance(output, int):
            return output
        else:
            raise ValueError("Invalid input type !!!")

    @staticmethod
    def type(data):
        if isinstance(data, str):
            try:
                int_value = int(data)
                return int
            except ValueError:
                return str
        elif isinstance(data, list):
            return list
        elif isinstance(data, int):
            return int
        else:
            print("Invalid data type !!!")

    @staticmethod
    def is_min_length(data_, data_min_length):
        data_to_compare = Validator.length(data_)
        if data_min_length is not None and data_to_compare < data_min_length:
            print(f"Error: Minimum length of {data_min_length} for {data_} is not valid")
            return False
        return True

    @staticmethod
    def is_max_length(data_, data_max_length):
        data_to_compare = Validator.length(data_)
        if data_max_length is not None and data_to_compare > data_max_length:
            print(f"Error: Maximum length of {data_max_length} for {data_} is not valid")
            return False
        return True

    @staticmethod
    def is_in_choices(data, required_choise):
        if required_choise:
            if data not in required_choise:
                print(f"Error: {data} is not in {required_choise}")
                return False
        return True

# Example usage:''
# data1 = Validator.get_validated_data('username', data_type=str, required_data=['username'], )
# print(f"You entered: {data1}")

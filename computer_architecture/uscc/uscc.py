class UltraSuperCalculator:

    # Initializes the calculator with a name, number and history registers, and other control variables.
    def __init__(self, name=None):
        self.name = name
        self.number_registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.history_registers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display('Calculator Activated.')

    # Updates the display with a provided message and prints it.
    def update_display(self, to_update):
        self.user_display = to_update
        print(f'{self.name} {to_update}')

    # Stores a binary value to the next available register in the number registers.
    def store_value_to_register(self, value_to_store):
        if self.numbers_index >= 21:  
            self.numbers_index = 0  

        self.number_registers[self.numbers_index] = int(str(value_to_store), 2)
        print(f"Value: {int(value_to_store,2)} stored in Register: {self.numbers_index}.")

        self.numbers_index += 1

    # Loads a value from a specified register address.
    def load_value_from_register(self, register_address):
        index = int(str(register_address), 2)
        int_value = int(self.number_registers[index])
        return int_value

    # Stores the result of an operation to the history registers.
    def store_to_history_register(self, result_to_store):
        if self.history_index > 9:
            self.history_index = 0

        self.history_registers[self.history_index] = bin(result_to_store)
        self.history_index += 1
        self.temp_history_index = self.history_index

    # Adds values from two specified registers and returns the result.
    def add(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 + num2
        return calculated_value

    # Multiplies values from two specified registers and returns the result.
    def multiply(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 * num2
        return calculated_value

    # Subtracts the value of the second register from the first and returns the result.
    def subtract(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 - num2
        return calculated_value

    # Divides the value of the first register by the second and returns the result. Handles division by zero.
    def divide(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)

        if num2 != 0:
            calculated_value = int(num1 / num2)
        else:
            print(f"Division by 0 error: {num1}/{num2}.")
            calculated_value = 0
        
        return calculated_value

    # Retrieves and displays the last calculation from the history registers.
    def get_last_calculation(self):
        self.temp_history_index -= 1
        last_value = f'The last calculated value was: {int(self.history_registers[self.temp_history_index], 2)}'
        self.update_display(last_value)

    # Parses a binary instruction and executes the corresponding operation.
    def binary_reader(self, instruction):
        if len(instruction) != 32:
            self.update_display('Invalid Instruction Length.')
            return 
        
        opcode = instruction[0:6]
        source_one = instruction[6:11]
        source_two = instruction[11:16]
        store = instruction[16:26]
        function_code = instruction[26:]
        
        if opcode == '000001':
            self.store_value_to_register(store)
            return
        
        elif opcode == '100001':
            self.get_last_calculation()
            return
        
        elif opcode != '000000':
            self.update_display("Invalid OPCODE")
            return

        result = 0

        if function_code == '100000':
            result = self.add(source_one, source_two)
        
        elif function_code == '100010':
            result = self.subtract(source_one, source_two)
        
        elif function_code == '011000':
            result = self.multiply(source_one, source_two)
        
        elif function_code == '011010':
            result = self.divide(source_one, source_two)
        
        else:
            self.update_display("Invalid Function")
            return
        
        self.store_to_history_register(result)
        self.update_display(f"The result is: {result}")

if __name__ == '__main__':
    my_calculator = UltraSuperCalculator()
    my_calculator.binary_reader("00000100000000000000000101000000")

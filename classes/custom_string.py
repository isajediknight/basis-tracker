class Custom_String:

    def __init__(self,my_string=''):
        if(type('') == type(my_string)):
            self.string = my_string
        else:
            self.string = str(my_string)

    def add_commas(self):

        negative_found = False
        if('-' == self.string[0]):
            negative_found = True
            self.string = self.string[1:]

        length = len(self.string)

        counter = 0
        fixed_string = ''
        for char in reversed(self.string):
            fixed_string += char
            counter += 1
            if counter == length:
                pass
            elif counter % 3 == 0:
                fixed_string += ','

        new_string = ''
        for char in reversed(fixed_string):
            new_string += char

        if(negative_found):
            new_string = '-' + new_string

        self.string = new_string

    def prepend_spaces(self,total_number_of_spaces = 0):
        return 0

    def get_string(self):
        return self.string
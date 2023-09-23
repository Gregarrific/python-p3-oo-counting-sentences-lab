#!/usr/bin/env python3
import ipdb
class MyString:
    def __init__(self, value=""):
        self.value = value

    def get_value(self):
        return self._value
    
    def set_value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print ("The value must be a string.")    
    
    value = property(get_value, set_value)

    def is_sentence(self):
        return self.value.endswith(".")      

    def is_question(self):
        return self.value.endswith("?")
    
    def is_exclamation(self):
        return self.value.endswith("!")
    
    def count_sentences(self):
        count = 0
        replaced_value = self.value.replace(". ", "`").replace("? ", "`").replace("! ", "`")
        if replaced_value.endswith("."):
            count += 1
        elif replaced_value.endswith("?"):
            count += 1
        elif replaced_value.endswith("!"):
            count += 1
        letters = (letter for letter in replaced_value)
        for letter in letters:
            if letter == "`":
                count += 1
        print (count)
        return count

# ipdb.set_trace()
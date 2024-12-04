class CustomString:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("CustomString only accepts string inputs.")
        self.value = value

    def find(self, substring, start=0, end=None):
        
        if end is None:
            end = len(self.value)
        n = len(self.value)
        m = len(substring)

        # Limit the search to the specified range
        if start < 0 or end > n or start >= end:
            return -1
        
        for i in range(start, min(end, n - m + 1)):
            if self.value[i:i + m] == substring:
                return i
        return -1

    def replace(self, old, new):
        
        if not old:
            raise ValueError("The old value cannot be an empty string.")
        
        result = []
        i = 0
        n = len(self.value)
        m = len(old)

        while i < n:
            if self.value[i:i + m] == old:
                result.append(new)
                i += m
            else:
                result.append(self.value[i])
                i += 1
        return CustomString("".join(result))

    def split(self, delimiter=None):
        
        result = []
        current = []
        n = len(self.value)
        d_len = len(delimiter) if delimiter else 0

        i = 0
        while i < n:
            if delimiter and self.value[i:i + d_len] == delimiter:
                result.append("".join(current))
                current = []
                i += d_len
            elif delimiter is None and self.value[i].isspace():
                if current:
                    result.append("".join(current))
                    current = []
                i += 1
            else:
                current.append(self.value[i])
                i += 1

        if current:
            result.append("".join(current))
        return result

    def join(self, iterable):
        
        if not all(isinstance(item, str) for item in iterable):
            raise ValueError("All elements of the iterable must be strings.")
        
        result = ""
        for idx, item in enumerate(iterable):
            result += item
            if idx < len(iterable) - 1:
                result += self.value
        return CustomString(result)

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"CustomString({self.value!r})"


# Example usage:
custom_str = CustomString("hello world")
print(custom_str.find("world"))               # Output: 6
print(custom_str.replace("world", "Python"))  # Output: CustomString('hello Python')
print(custom_str.split(" "))                  # Output: ['hello', 'world']
separator = CustomString(", ")
print(separator.join(["apple", "banana", "cherry"]))  # Output: CustomString('apple, banana, cherry')
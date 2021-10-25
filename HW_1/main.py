# 1) Создать переменную типа String
variable_string = "String"

# 2) Создать переменную типа Integer
variable_integer = 20

# 3) Создать переменную типа Float
variable_float = 20.5123

# 4) Создать переменную типа Bytes
variable_bytes = b'bytes string'
variable_bytes_encode = 'Байты'.encode('utf-8')
variable_bytes_from_list = bytes([23, 4, 254, 1])

# 5) Создать переменную типа List
variable_list = ['l', 'i', 's', 't']
variable_list_using_method = list('list')

# 6) Создать переменную типа Tuple
variable_tuple = ('t', 'u', 'p', 'l', 'e')
variable_tuple_using_method = tuple('tuple')

# 7) Создать переменную типа Set
variable_set_using_method = set('set')
variable_set = {'s', 'e', 't'}

# 8. Создать переменную типа Frozen set
variable_frozenset_using_method = frozenset("frozenset")
variable_frozenset = frozenset("frozenset")

# 9) Создать переменную типа Dict
variable_dictionary = dict([(1, 2), (2, 4)])

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(f"Значение variable_string: '{variable_string}'. Тип: {type(variable_string)}")
print()
print(f"Значение variable_integer: {variable_integer}. Тип: {type(variable_integer)}")
print()
print(f"Значение variable_float: {variable_float}. Тип: {type(variable_float)}")
print()
print(f"Значение variable_bytes: {variable_bytes}. Тип: {type(variable_bytes)}")
print(f"Значение variable_bytes_encode: {variable_bytes_encode}. Тип: {type(variable_bytes_encode)}")
print(f"Значение variable_bytes_from_list: {variable_bytes_from_list}. Тип: {type(variable_bytes_from_list)}")
print()
print(f"Значение variable_list: {variable_list}. Тип: {type(variable_list)}")
print(f"Значение variable_list_using_method: {variable_list_using_method}. Тип: {type(variable_list_using_method)}")
print()
print(f"Значение variable_tuple: {variable_tuple}. Тип: {type(variable_tuple)}")
print(f"Значение variable_tuple_using_method: {variable_tuple_using_method}. Тип: {type(variable_tuple_using_method)}")
print()
print(f"Значение variable_set_using_method: {variable_set_using_method}. Тип: {type(variable_set_using_method)}")
print(f"Значение variable_set: {variable_set}. Тип: {type(variable_set)}")
print()
print(f"Значение variable_frozenset_using_method: {variable_frozenset_using_method}. Тип: {type(variable_frozenset_using_method)}")
print(f"Значение variable_frozenset: {variable_frozenset}. Тип: {type(variable_frozenset)}")
print(f"Значение variable_dictionary: {variable_dictionary}. Тип: {type(variable_dictionary)}")
print()
# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
first_string = "First part "
second_string = "Second part"
result_string = first_string + second_string
print(result_string)
print()
# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(variable_string, variable_integer)
print()
# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(variable_string + " " + str(variable_integer))


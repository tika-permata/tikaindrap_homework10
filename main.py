#point 1
import random
def generate_random_number():
    
   return random.randint(0, 100)
random_number = generate_random_number()
print(random_number)

#point 2
import random
import string

def generate_random_string(length):
    
    # Membuat list yang berisi karakter yang mungkin ada dalam string acak
    characters = string.ascii_letters + string.digits + string.punctuation

    # Menghasilkan string acak dengan menggunakan karakter-karakter dari list
    random_string = ''.join(random.choice(characters) for i in range(length))

    return random_string
random_string = generate_random_string(20)
print(random_string)

#point 3
def split_string(input_string, delimiter):
    # Memisahkan string menjadi array menggunakan metode split()
    substring_array = input_string.split(delimiter)

    return substring_array
input_string = "Hello,world,how,are,you"
delimiter = ","
result_array = split_string(input_string, delimiter)
print(result_array)

#point 4
def is_leap_year(year):
   
    # Mengecek apakah tahun dapat dibagi dengan 4
    if year % 4 == 0:
        # Jika tahun dapat dibagi dengan 4, maka mengecek apakah tahun dapat dibagi dengan 100
        if year % 100 == 0:
            # Jika tahun dapat dibagi dengan 100, maka mengecek apakah tahun dapat dibagi dengan 400
            if year % 400 == 0:
                # Jika tahun dapat dibagi dengan 400, maka tahun tersebut merupakan tahun kabisat
                return True
            else:
                # Jika tahun tidak dapat dibagi dengan 400, maka tahun tersebut bukan tahun kabisat
                return False
        else:
            # Jika tahun tidak dapat dibagi dengan 100, maka tahun tersebut merupakan tahun kabisat
            return True
    else:
        # Jika tahun tidak dapat dibagi dengan 4, maka tahun tersebut bukan tahun kabisat
        return False
year = 2023
is_leap = is_leap_year(year)
print(is_leap)

#point 5
def print_data(data):
    for obj in data:
        print("Name:", obj["name"])
        print("Age:", obj["age"])
        print()

data = [
    {"name": "tika", "age": 22},
    {"name": "indra", "age": 17},
    {"name": "permata", "age": 20}
]
print_data(data)

#point 6
def group_people(data, gender=None, age=None, marital_status=None, social_status=None):
    result = []
    for obj in data:
        if (gender is None or obj["sex"] == gender) and \
           (age is None or obj["age"] == age) and \
           (marital_status is None or obj["marital"] == marital_status) and \
           (social_status is None or obj["social"] == social_status):
            result.append(obj)
    return result

# contoh
data = [
    {"name": "bayu", "sex": "male", "age": 10, "marital": "single", "social": "student"},
    {"name": "cori", "sex": "male", "age": 25, "marital": "married", "social": "employee"},
    {"name": "tika", "sex": "female", "age": 10, "marital": "single", "social": "student"},
    {"name": "risma", "sex": "female", "age": 18, "marital": "married", "social": "employee"},
    {"name": "iqbal", "sex": "male", "age": 20, "marital": "single", "social": "employee"},
]

# pemanggilan fungsi
result = group_people(data, gender="female", age=10)
print(result)

#point 7
def count_aha(word, no_of_loop):
    count = 0
    for i in range(no_of_loop):
        count += word.count("aha")
        word = word.replace("aha", "", 1)
    return count

# contoh penggunaan
word = "ahayakunahablahahahablaha"
no_of_loop = 3
result = count_aha(word, no_of_loop)
print(result)



import os

base_path = os.path.dirname(os.path.abspath(__file__))

start = 1
end = 4000
step = 250

for i in range(start, end + 1, step):
    folder_name = f"{i} - {i + step - 1}"
    folder_path = os.path.join(base_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# Yeah I'm that lazy


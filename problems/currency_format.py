number = 123456.7891

integer, decimal = str(number).split(".") if "." in str(number) else (str(number), "")

integer = integer[::-1]

result_list = []

if len(integer) > 3:
    result_list.append(integer[:3])
    integer = integer[3:]

while len(integer) > 0:
    result_list.append(integer[:2])
    integer = integer[2:]

result = ",".join(result_list)[::-1]
if decimal:
    print(f"{result}.{decimal}")
else:
    print(result)
 
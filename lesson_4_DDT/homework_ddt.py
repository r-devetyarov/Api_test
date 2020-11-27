file = open('data.csv')
# for line in file:
#     print(line)
data_list = file.readlines()
data_list.pop(0)
# print(data_list[1])
# split() - разбивает строку в список по пробелам
data_name = []
data_lastname = []
data_middle_name = []
data_city = []
for item in data_list:
    r = item.split()
    data_lastname.append(r[0])
    data_name.append(r[1])
    data_middle_name.append(r[2])
    data_city.append(str(r[3]).replace(',', '').replace('0', '').replace('1', ''))

new_data_list = [[lastname, name, middle_name, city, credit_card, deposit, mortgage]
                 for lastname in data_lastname
                 for name in data_name
                 for middle_name in data_middle_name
                 for city in data_city
                 for credit_card in ['+', '-']
                 for deposit in ['+', '-']
                 for mortgage in ['+', '-']]

# print(new_data_list)


def data_test_create():
    data_file = open('test123.txt', 'r')
    print(data_file)
    # data_file.write('asdasd')
        # for i in range(10):
        #     print(new_data_list[i][0], file=data_file)


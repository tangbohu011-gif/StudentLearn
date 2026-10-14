import csv
def csv_script(filename,column):
    #将csv文件读入并且转换成二维列表
    with open(filename, mode = 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        data = []
        for row in csv_reader:
            data.append(row)
    #跳过列表的表头（一般表头是数据的标签）读出列表的某一列
    column_data = []
    for row in data[1:]:
        column_data.append(row[column])
    #将列表的某一列转换从字符串转换为数值类型
    column_data_float = []
    none_num = 0
    for value in column_data:
        #判断读入的数据是否为空
        if value.strip() != '':
            column_data_float.append(float(value))
        else:
            none_num += 1
    return column_data_float,none_num

if __name__ == '__main__':
    filename = input("请输入csv文件路径：")
    column = int(input("请输入需要进行统计的列索引："))
    column_data,none_num = csv_script(filename,column)
    if len(column_data) == 0:
        print("本列数据全部为空")
    else:
        mean_value = sum(column_data) / len(column_data)
    max_value = max(column_data)
    min_value = min(column_data)
    print(f"csv数据文本报告：均值为：{mean_value},最大值为：{max_value},最小值为：{min_value},缺失值数量为：{none_num}")
import os #operating system

products = []
# 尋找資料夾裡是否有 products.csv
if os.path.isfile('products.csv'):
	print('yes')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			goods, price = line.strip().split(',')
			products.append([goods, price])
	print(products)
else:
	print('No found')

# 輸入字串
while True:
	goods = input('請輸入商品名稱: ')
	if goods == 'q':
		break
	price = input('請輸入商品價格: ')
	# p = []
	# p.append(goods)
	# p.append(price)

	# p = [goods, price]
	# products.append(p)

# 將字串加入到 list
	products.append([goods, price])
# print(products) = [['ramen', '220'], ['pasta', '280']]
# print(products[0]) = ['ramen', '220']
# print(products[0][0]) = ramen

# 印出所有商品和價格
for product in products:
	print('%s 的價格為 %s 元' % (product[0], product[1]))

# 寫入檔案到 products.csv
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

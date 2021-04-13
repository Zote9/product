
products = []
# 讀取products.csv 檔案 簡稱 f
with open('products.csv', 'r', encoding = 'utf-8') as f:
# 將 f 的檔案一行一行列表出來 = ['ramen', '220', 'pasta', '280']
	for line in f:
		# s = line.strip().split(',')
		# goods = s[0]
		# price = s[1]
# 不要印出 '商品,價格'
		if '商品,價格' in line:
			continue
# 將列表裡第 0 項當作 goods  第 1 項當作 price
		goods, price = line.strip().split(',')
# 再做成小列表 = [['ramen', '220'], ['pasta', '280']]
		products.append([goods, price])
print(products)

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

# 印出所有商品的價格
for product in products:
	print('%s 的價格為 %s 元' % (product[0], product[1]))

# 寫入檔案到 products.csv
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

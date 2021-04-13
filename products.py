
products = []
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

	products.append([goods, price])

# print(products)
# print(products[0])
# print(products[0][0])
for product in products:
	print('%s 的價格為 %s 元' % (product[0], product[1]))

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

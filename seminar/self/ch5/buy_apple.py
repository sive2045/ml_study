<<<<<<< HEAD
from layer_naive import MulLayer
=======
from layer_navie import MulLayer
>>>>>>> 62414ad90e92de7de3dc733759a76e3ef498faec

apple = 100
apple_num = 2
tax = 1.1

# layers
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

<<<<<<< HEAD
# forward propagation
=======
# forward
>>>>>>> 62414ad90e92de7de3dc733759a76e3ef498faec
apple_price = mul_apple_layer.forward(apple, apple_num)
price = mul_tax_layer.forward(apple_price, tax)

print(price)

<<<<<<< HEAD
# back propagation
=======
# backward
>>>>>>> 62414ad90e92de7de3dc733759a76e3ef498faec
dprice = 1
dapple_price, dtax = mul_tax_layer.backward(dprice)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)

print(dapple, dapple_num, dtax)

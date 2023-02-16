from django.shortcuts import render
from base.curves.montgomery import find_point, point_addition, point_subtraction, point_multiplication, point_doubling
import gmpy2
# Create your views here.
def home(request):
	context = []
	if request.method == 'POST':
		a_value = request.POST['a-value']
		b_value = request.POST['b-value']
		prime_number = request.POST['prime-value']
		# print(a_value, b_value, prime_number)

		x_coordinates, y_coordinates, total_points = find_point.findPoint(gmpy2.mpz(a_value), gmpy2.mpz(b_value), gmpy2.mpz(prime_number))
		
		print("________________________________________-")
		print(len(x_coordinates))

		print(x_coordinates)
		print(y_coordinates)
		print(total_points)

	return render(request, 'base/home.html')

def addPointView(request):
	if request.method == "POST":
		x1_value = request.POST['x1-value']
		y1_value = request.POST['y1-value']
		x2_value = request.POST['x2-value']
		y2_value = request.POST['y2-value']
		a_value = request.POST['a-value']
		b_value = request.POST['b-value']
		prime_number = request.POST['prime-value']
		print(x1_value, y1_value, x2_value, y2_value, a_value, b_value, prime_number)

		x3, y3 = point_addition.pointAddition(gmpy2.mpz(x1_value), gmpy2.mpz(y1_value), gmpy2.mpz(x2_value), gmpy2.mpz(y2_value), gmpy2.mpz(a_value), gmpy2.mpz(b_value), gmpy2.mpz(prime_number))
		print(x3, y3)
	return render(request, 'base/addPoint.html')

def subtractPointView(request):
	if request.method == "POST":
		x1_value = request.POST['x1-value']
		y1_value = request.POST['y1-value']
		x2_value = request.POST['x2-value']
		y2_value = request.POST['y2-value']
		a_value = request.POST['a-value']
		b_value = request.POST['b-value']
		prime_number = request.POST['prime-value']
		print(x1_value, y1_value, x2_value, y2_value, a_value, b_value, prime_number)
		
		x3, y3 = point_subtraction.pointSubtraction(gmpy2.mpz(x1_value), gmpy2.mpz(y1_value), gmpy2.mpz(x2_value), gmpy2.mpz(y2_value), gmpy2.mpz(a_value), gmpy2.mpz(b_value), gmpy2.mpz(prime_number))

		# x3, y3 = point_subtraction.pointSubtraction(gmpy2.mpz(x1_value), gmpy2.mpz(y1_value), gmpy2.mpz(x2_value), gmpy2.mpz(y2_value), gmpy2.mpz(a_value), gmpy2.mpz(b_value), gmpy2.mpz(prime_number))
		print(x3, y3)
	return render(request, 'base/subtractPoint.html')


def multiplyPointView(request):
	if request.method == "POST":
		x1_value = request.POST['x1-value']
		y1_value = request.POST['y1-value']
		k_value = request.POST['k-value']
		# y2_value = request.POST['y2-value']
		a_value = request.POST['a-value']
		b_value = request.POST['b-value']
		prime_number = request.POST['prime-value']
		print(x1_value, y1_value, k_value, a_value, b_value, prime_number)
		
		x3, y3 = point_multiplication.pointMultiplication(gmpy2.mpz(x1_value), gmpy2.mpz(y1_value), gmpy2.mpz(k_value), gmpy2.mpz(a_value), gmpy2.mpz(b_value), gmpy2.mpz(prime_number))
		print(x3, y3)
	return render(request, 'base/multiplyPoint.html')

def doublePointView(request):
	if request.method == "POST":
		x1_value = request.POST['x1-value']
		y1_value = request.POST['y1-value']
		# x2_value = request.POST['x2-value']
		# y2_value = request.POST['y2-value']
		a_value = request.POST['a-value']
		b_value = request.POST['b-value']
		prime_number = request.POST['prime-value']
		print(x1_value, y1_value, a_value, b_value, prime_number)
		
		x3, y3 = point_subtraction.pointDoubling(gmpy2.mpz(x1_value), gmpy2.mpz(y1_value), gmpy2.mpz(a_value), gmpy2.mpz(b_value), gmpy2.mpz(prime_number))
		print(x3, y3)
	return render(request, 'base/doublePoint.html')
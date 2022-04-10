n = int(input("Podaj ile liczb chcesz wprowadzić?: "))
var=0
numbers = []
while var < n:
	my_no=int(input("Podaj liczbe: "))
	var+=1
	numbers.append(my_no)
print(numbers)
print("Suma elementów na liście: ",sum(numbers))
print("Średnia wartość elentów z listy: ",sum(numbers)/n)
if sum(numbers) > sum(numbers)/n:
	print("Suma jest wieksza do średniej!")
else:
	print("Suma nie jest większa od średniej")
	
# Uwaga: To zadanie sprawiło mi najwięcej problemów, tzn. wymiślenie
# rozwiązania linie 4 - 7, zwłaszcza 7.	

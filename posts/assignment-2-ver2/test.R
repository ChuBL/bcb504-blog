
elements <- list("Ni", "N",  "C",  "H" )
print(class(elements))
for (i in 1:length(elements)){
  print(elements[i])
  print('hello')
}

for (element in elements){
  print(element)
  print('hello')
}
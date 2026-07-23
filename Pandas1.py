import pandas as pd
mydataset = {
  'name': ["ram", "shyam", "sita"],
  'age': [3, 7, 2],
  'city': ['Maha', "Bang", 'Hyd']
}
myvar = pd.DataFrame(mydataset)
print(myvar)

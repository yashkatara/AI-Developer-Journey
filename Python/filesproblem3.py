def genrateTable(num):
  table =  ''
  for i in range(1, 11):
        table += f"{num} x {i} = {num*i}\n"
  with open (f"tables/table_{num}.text", "w") as f:
        f.write(table)
        
        
for i in range(2, 21):
    genrateTable(i)
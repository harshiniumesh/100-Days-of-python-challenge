print("| Pokemon Name | Table |")
print("________________________________")

from prettytable import prettytable
table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squirtle", "Charmander"])
table.add_column("Type", ["Electric","Water", "Fire"])


table.field_names = ["Name", "Age"]
table.align["Name"] = "l"


print(table.align)
print(table)
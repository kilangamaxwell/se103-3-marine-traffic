from load_data import load_data

all_data = load_data()


def run_help():
  """Prints a menu of commands that the application can run in the CLI."""
  print("Available commands:")
  print("help")
  print("show_countries")
  print("top_countries <num_countries>")
  print("ship_by_types")
  print()
  commands()


def show_countries():
  """Prints the country of origin for each ship without duplicates and sorted alphabetically."""
  all_countries = set()
  for ships in all_data['data']:
    all_countries.add(ships['COUNTRY'])
  sorted_countries = sorted(all_countries)
  for country in sorted_countries:
    print(country)
  print()
  commands()


def ships_by_types():
  """Displays the number of ships for each type of ship."""
  all_types = set()
  ships_types_dict = {}
  for ships in all_data['data']:
    all_types.add(ships['TYPE_SUMMARY'])
    for ship_type in all_types:
      if ship_type not in ships_types_dict:
        ships_types_dict[ship_type] = 1
      else:
        ships_types_dict[ship_type] += 1
  for ship_type in ships_types_dict:
    print(f"{ship_type}: {ships_types_dict[ship_type]}")
  commands()


def sorted_countries_and_ships():
  """Returns dictionary of countries and number of
   ships for each country. Also returns a sorted list
    of countries based on the number of ships in
     descending order."""
  countries_ships = []
  for ships in all_data['data']:
    countries_ships.append(ships['COUNTRY'])
  countries_ships_dict = {}
  for country in countries_ships:
    if country not in countries_ships_dict:
      countries_ships_dict[country] = 1
    else:
      countries_ships_dict[country] += 1
  sorted_countries_lst = sorted(countries_ships_dict,
             key = lambda x: countries_ships_dict[x],
            reverse = True)
  return countries_ships_dict, sorted_countries_lst


def show_top_countries(num_countries):
  """Prints top countries with largest number of
   ships in a descending order"""
  country_ships_dict, sorted_countries_lst = sorted_countries_and_ships()
  count = 0
  for country in sorted_countries_lst:
    if count == num_countries:
      break
    print(f"{country}: {country_ships_dict[country]}")
    count += 1
  print()
  commands()


func_dict = {
  "help" : run_help,
  "show_countries" : show_countries,
  "top_countries" : show_top_countries,
  "ship_by_types" : ships_by_types
}


def commands():
  """Runs the command typed by the user in the CLI."""
  user_entry = input()
  if user_entry.__contains__("top_countries"):
    entry = user_entry.split()
    func_dict[entry[0]](int(entry[1]))
  else:
    func_dict[user_entry]()


def main():
  """Prints welcome message and instructions to run program menu"""
  print("Welcome to the Ships CLI! Enter 'help' to view available commands.")
  commands()


if __name__ == "__main__":
  main()
  
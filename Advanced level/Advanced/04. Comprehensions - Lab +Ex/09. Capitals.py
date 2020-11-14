countries = input().split(", ")
capital = input().split(", ")

[print(f"{country} -> {capital}") for (country, capital) in zip(countries,capital)]

#  dictionary = {key: value for(key, value) in zip(contries, capitals)}
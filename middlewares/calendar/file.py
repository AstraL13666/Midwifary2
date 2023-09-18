month_number = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06",
                "july": "07", "august": "08", "september": "09", "october": "10", "november": "11", "december": "12"}

month_name = {"january": "январь", "february": "февраль", "march": "март", "april": "апрель", "may": "май",
              "june": "июнь", "july": "июль", "august": "август", "september": "сентябрь", "october": "октябрь",
              "november": "ноябрь", "december": "декабрь"}


def month_number_collections(name):
    for key, value in month_number.items():
        if key == name:
            return value
    else:
        return None


def month_name_collections(name):
    for key, value in month_name.items():
        if key == name:
            return value
    else:
        return None

def filter_dicts(elements, key, min_value):
    new_elements = []
    for element in elements:
        if element[key] >= min_value:
            new_elements.append(element)
    return new_elements

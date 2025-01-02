txt = 'LMaasleitbtui'
car_names = ['Lasseti', 'Lamborghini', 'Tesla', 'BMW', 'Audi']
def extract_car_names(text, car_names):
    extracted_names = [car for car in car_names if car.lower() in text.lower()]
    return extracted_names

extracted_names = extract_car_names(txt, car_names)
print(extracted_names)

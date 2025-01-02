user_string = input("Matinni kiriting: ")
start_word = input("Matn boshlanuvchi so'zni kiriting: ")
end_word = input("Matn tugovchi so'zni kiriting : ")
starts_with = user_string.startswith(start_word)
ends_with = user_string.endswith(end_word)
if starts_with and ends_with:
    print(f'Matn boshlanadi:" {start_word}" tugaydi: "{end_word}".')
else:
       if not starts_with:
          print(f'Matn boshlanmaydi: "{start_word}".')
       if not ends_with:
        print(f'Matn tugamaydi: "{end_word}".')
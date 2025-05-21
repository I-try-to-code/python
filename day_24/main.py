PLACEHOLDER="[name]"

with open("./dataa/names.txt" ) as name_file:
    names= name_file.readlines()

with open("./dataa/format.txt") as letter_file:
    letter= letter_file.read()

    for i in names:
        stripped_name=i.strip()
        neww= letter.replace(PLACEHOLDER,i)
        with open(f"./ready to send/letter for {stripped_name}.txt","w") as completed_letter:
            completed_letter.write(neww)


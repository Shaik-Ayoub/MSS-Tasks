with open('product_descriptions.txt', 'r') as input_file:
    content = input_file.readlines()

formatted_content = [line.strip().title() for line in content]

with open('formatted_descriptions.txt', 'w') as output_file:
    output_file.write('\n'.join(formatted_content))

print("Formatting completed. Check formatted_descriptions.txt for the results.")

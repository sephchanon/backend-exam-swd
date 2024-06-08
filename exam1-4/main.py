class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0:
            return "number can not be negative"
        
        count = 0
        i = 5
        while number >= i:
            count += number // i
            i *= 5
        
        return count

    def find_max_index(self, numbers: list) -> int | str:
        if not numbers:
            return "list can not be blank"
        
        max_value = numbers[0]
        max_index = 0
        
        for i in range(1, len(numbers)):
            if numbers[i] > max_value:
                max_value = numbers[i]
                max_index = i
        
        return max_index
    
    def number_to_thai_text(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number > 10_000_000:
            return "number can not be greater than 10,000,000"

        thai_numbers = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า", "สิบ"]
        units = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]

        num_text = ""
        num_str = str(number)

        length = len(num_str)
        for i in range(length):
            digit = int(num_str[i])
            position = length - i - 1

            if digit == 0:
                continue
            if position == 0 and digit == 1 and length > 1:
                num_text += "เอ็ด"
            elif position == 1 and digit == 1:
                num_text += "สิบ"
            elif position == 1 and digit == 2:
                num_text += "ยี่สิบ"
            else:
                num_text += thai_numbers[digit] + units[position]

        return num_text

    def number_to_thai(self, number: int) -> str:
        return self.number_to_thai_text(number)

    def number_to_roman(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        
        if number == 0:
            return "number can not be zero"
        
        roman_numerals = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        result = []
        
        for (value, numeral) in roman_numerals:
            while number >= value:
                result.append(numeral)
                number -= value
        
        return ''.join(result)

    def main(self):
        while True:
            print("Choose an operation:")
            print("1: Find trailing zeroes in factorial")
            print("2: Find max index in a list")
            print("3: Convert number to Thai")
            print("4: Convert number to Roman")
            print("5: Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                number = int(input("Enter a number: "))
                result = self.find_tailing_zeroes(number)
                print(f"Result: {result}")

            elif choice == '2':
                numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
                result = self.find_max_index(numbers)
                print(f"Result: {result}")

            elif choice == '3':
                number = int(input("Enter a number: "))
                result = self.number_to_thai(number)
                print(f"Result: {result}")

            elif choice == '4':
                number = int(input("Enter a number: "))
                result = self.number_to_roman(number)
                print(f"Result: {result}")

            elif choice == '5':
                break

            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    solution = Solution()
    solution.main()

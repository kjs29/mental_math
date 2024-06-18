import random
import datetime


class Abacus:
    def __init__(self, log_file="Mental Math.txt"):
        """
        Initializes the Abacus with the given log file name.
        
        :param log_file: Name of the file to log the questions and answers.
        """
        self.log_file = log_file

    def get_number(self, digit=2):
        """
        Generates a random number with the specified number of digits.
        
        :param digit: Number of digits for the generated number.
        :return: A random number with the specified digits.
        """
        return random.randint(10 ** (digit - 1), (10 ** digit) - 1)

    def generate_questions(self, number_of_questions=5, digit=2, operation="both"):
        """
        Generates a series of addition and subtraction questions.
        
        :param number_of_questions: Number of questions to generate.
        :param digit: Number of digits for each generated number.
        :param operation: Type of operation ("plus", "minus", or "both").
        :return: A tuple containing the list of questions and the list of answers.
        """
        initial_number = self.get_number(digit)
        questions = [initial_number]
        answers = []
        current_value = initial_number

        for _ in range(number_of_questions):
            if operation == "both":
                sign = random.choice([1, 0])
            elif operation == "plus":
                sign = 1
            elif operation == "minus":
                sign = 0

            if sign == 1:  # Addition
                next_number = self.get_number(digit)
                questions.append(next_number)
                current_value += next_number
            elif sign == 0:  # Subtraction
                if current_value > 1:
                    next_number = random.randint(1, max(1, current_value // random.randint(2, number_of_questions)))
                    questions.append(-next_number)
                    current_value -= next_number
                else:
                    questions.append(0)

            answers.append(current_value)

        return questions, answers
    
    def write_log_header(self):
        """
        Writes a header to the log file with the current timestamp.
        """
        try:
            with open(self.log_file, "a") as file:
                file.write('\n=====' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '=====\n')
        except IOError as e:
            print(f"Error while writing header to file {self.log_file}: {e}")

    def write_to_file(self, nums, ans):
        """
        Writes the questions and answers to the log file.
        
        :param nums: List of questions.
        :param ans: List of answers.
        """
        try:
            with open(self.log_file, "a") as file:
                for each in nums:
                    file.write(f"\n{each}\n")
                file.write(f"\nThe answer is {ans[-1]}\n")
        except IOError as e:
            print(f"Error while writing to file: {e}")

    def run(self, frequency=1, number_of_questions=5, digit=2, operation="both"):
        """
        Runs the abacus for a specified number of times and logs the results.
        
        :param frequency: Number of times to run the abacus.
        :param number_of_questions: Number of questions per run.
        :param digit: Number of digits for each generated number.
        :param operation: Type of operation ("plus", "minus", or "both").
        """
        try:
            self.write_log_header()

            for i in range(frequency):
                with open(self.log_file, "a") as file:
                    file.write(f"\n{i + 1}.\n")
                questions, answers = self.generate_questions(number_of_questions, digit, operation)
                self.write_to_file(questions, answers)
                print(f"Questions: {questions} / Answer: {answers}")
        except IOError as e:
            print(f"Error while writing to file: {e}")


# Example usage
if __name__ == "__main__":
    abacus = Abacus()
    abacus.run(frequency=5, number_of_questions=5, digit=1, operation="both")

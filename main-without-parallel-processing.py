import time

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to find primes in a range
def find_primes_in_range(start, end):
    primes = []
    for number in range(start, end):
        if is_prime(number):
            primes.append(number)
    return primes

if __name__ == "__main__":
    start_time = time.time()

    # Define range (adjust the range for your laptop performance)
    start = 1
    end = 20000000  # Finding primes between 1 and 20 million

    # Find primes
    primes = find_primes_in_range(start, end)

    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"Number of primes found: {len(primes)}")

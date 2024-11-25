import time
import ray
import os

# Initialize Ray
ray.init(ignore_reinit_error=True)

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Parallelized function to find primes in a range using Ray
@ray.remote
def find_primes_in_range_parallel(start, end):
    primes = []
    for number in range(start, end):
        if is_prime(number):
            primes.append(number)
    return primes

if __name__ == "__main__":
    start_time = time.time()

    # Define range
    start = 1
    end = 20000000 # Finding primes between 1 and 20 million
    num_splits = os.cpu_count()  # Number of splits (parallel tasks)

    # Split the range into smaller chunks for parallel processing
    range_splits = [(i, i + (end - start) // num_splits) for i in range(start, end, (end - start) // num_splits)]

    # Use Ray to find primes in parallel
    results = ray.get([find_primes_in_range_parallel.remote(split_start, split_end) for split_start, split_end in range_splits])

    # Combine the results
    primes = [prime for sublist in results for prime in sublist]

    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"Number of primes found: {len(primes)}")

    # Shutdown Ray
    ray.shutdown()

import utils.leaders_scraper as scraper
import time

# Start time
start = time.perf_counter()

# Run the program
leaders_per_country = scraper.get_first_paragraph()
scraper.save(leaders_per_country)

# End time
end = time.perf_counter()
execution_time = round((end - start), 2)
print(f'Synchronous execution took {execution_time} sec')
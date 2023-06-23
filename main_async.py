import utils.leaders_scraper_async as scraper
import asyncio
import time

# Start time
start = time.perf_counter()

# Run the program
leaders_per_country = scraper.get_leaders()
responses = asyncio.run(scraper.session_loop_request_async(leaders_per_country))
leaders_per_country = scraper.get_first_paragraph(responses)
scraper.save(leaders_per_country)

# End time
end = time.perf_counter()
execution_time = round((end - start), 2)
print(f'Asynchronous execution took {execution_time} sec')
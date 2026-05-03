import time

text = "B" * 8000 + "A"
pattern = "BA"

start = time.time()
"BA" in text
print("Execution Time:", time.time() - start)
# ./samples should first be loaded by running sample_synthesizer.py
from amadeus import amadeus

a = amadeus("./samples", (12, 19), 32, load_from_file=True, epochs=15)
ans = a.test_accuracy_on_image("./samples/e/4.png")
print(f"it's probably a(n) {ans}, idk man")
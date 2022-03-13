# ./samples should first be loaded by running sample_synthesizer.py
from amadeus import amadeus

a = amadeus("./samples", (12, 19), 32)
a.fit(20)
a.test_accuracy_on_image("./samples/e/4.png")

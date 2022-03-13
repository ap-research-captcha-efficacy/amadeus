# ./samples should first be loaded by running sample_synthesizer.py
from amadeus import amadeus

a = amadeus("./samples", (12, 19), 32, load_from_file=True)
#a.plot_model()
#a.fit(15)
a.test_accuracy_on_image("./samples/e/4.png")

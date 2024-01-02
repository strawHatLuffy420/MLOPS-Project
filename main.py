# main.py

from scripts import data_collection, model_evaluation, concept_drift_detection

def main():
    data_collection.collect_data()
    model_evaluation.evaluate_model()
    concept_drift_detection.detect_concept_drift()

if __name__ == "__main__":
    main()

from data import news_data
from pipeline import preprocess_pipeline

if __name__ == "__main__":
    final_output = preprocess_pipeline(news_data)
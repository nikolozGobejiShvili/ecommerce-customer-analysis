from src.data_cleaning import load_and_clean_data
from src.rfm_analysis import calculate_rfm
from src.visualize import plot_rfm_scatter
import os

def main():
    print("🚀 Starting Ecommerce Customer Analysis Pipeline\n")

    os.makedirs('output', exist_ok=True)

    # 1. Load and clean data
    data = load_and_clean_data('data/OnlineRetail.csv')

    # 2. RFM analysis
    rfm = calculate_rfm(data)

    # 3. Visualization
    plot_rfm_scatter(rfm)

    print("\n🎉 Analysis complete! Check the 'output' folder for results.\n")

if __name__ == "__main__":
    main()

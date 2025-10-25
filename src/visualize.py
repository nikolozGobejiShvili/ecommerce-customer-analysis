import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_rfm_scatter(rfm):
    os.makedirs('output', exist_ok=True)
    print("🔹 Generating scatter plot...")

    # ინდექსის აღდგენა — საჭიროა plotting-სთვის
    rfm = rfm.reset_index()

    # დარწმუნდეთ, რომ Recency და Monetary რიცხვებია
    rfm['Recency'] = rfm['Recency'].astype(float)
    rfm['Monetary'] = rfm['Monetary'].astype(float)

    plt.figure(figsize=(10,6))
    sns.scatterplot(
        data=rfm,
        x='Recency',
        y='Monetary',
        hue='RFM_Score',
        palette='viridis',
        alpha=0.8
    )

    plt.title('Customer Segmentation based on RFM Score', fontsize=14)
    plt.xlabel('Recency (days)')
    plt.ylabel('Monetary Value (Total Spend)')
    plt.legend(title='RFM Score', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('output/rfm_scatter.png', dpi=300)
    plt.close()

    print("✅ Plot saved as output/rfm_scatter.png")

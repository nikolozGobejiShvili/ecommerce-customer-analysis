import pandas as pd
import datetime as dt

def calculate_rfm(data):
    print("🔹 Calculating RFM metrics...")

    NOW = pd.to_datetime(data['InvoiceDate']).max() + pd.Timedelta(days=1)
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

    rfm = data.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (NOW - x.max()).days,
        'InvoiceNo': 'count',
        'TotalPrice': 'sum'
    })

    rfm.rename(columns={
        'InvoiceDate': 'Recency',
        'InvoiceNo': 'Frequency',
        'TotalPrice': 'Monetary'
    }, inplace=True)

    rfm['R_quartile'] = pd.qcut(rfm['Recency'], 4, ['4','3','2','1'])
    rfm['F_quartile'] = pd.qcut(rfm['Frequency'].rank(method='first'), 4, ['1','2','3','4'])
    rfm['M_quartile'] = pd.qcut(rfm['Monetary'], 4, ['1','2','3','4'])

    # კონვერტაცია string-ზე
    rfm['RFM_Score'] = (
        rfm['R_quartile'].astype(str) +
        rfm['F_quartile'].astype(str) +
        rfm['M_quartile'].astype(str)
    )

    rfm['Segment'] = rfm['RFM_Score'].apply(
        lambda x: 'VIP' if x == '444' else
                  'Loyal' if x.startswith('44') else
                  'Potential' if x.startswith('34') else
                  'At Risk' if x.startswith('2') else 'Low-Value'
    )

    # შენახვა
    rfm.to_csv('output/rfm_results.csv', index=True)
    print("✅ RFM analysis completed and saved to output/rfm_results.csv")

    # 🔥 ეს ხაზი აუცილებელია
    return rfm

from pipeline import extract,transform,load,analyze,report

def run_pipeline():
    apiData=extract.fetch_crypto_data()
    cleanedData=transform.transform_data(apiData)
    load.save_to_csv(cleanedData,'crypto_data.csv')
    reportData=analyze.analyze_data('crypto_data.csv')
    report.create_report(reportData)

run_pipeline()
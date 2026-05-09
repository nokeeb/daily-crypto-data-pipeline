from pipeline import extract,transform,load,analyze,report

def run_pipeline():
    apiData=extract.fetch_crypto_data()
    if apiData != []:
        cleanedData=transform.transform_data(apiData)
        load.save_to_csv(cleanedData,'crypto_data.csv')
        reportData=analyze.analyze_data('crypto_data.csv')
        report.create_report(reportData)

 
if __name__=='__main__':
    run_pipeline()
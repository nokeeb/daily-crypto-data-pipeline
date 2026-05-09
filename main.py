from pipeline import extract,transform,load,analyze,report

def run_pipeline():
    api_data=extract.fetch_crypto_data()
    if api_data != []:
        cleaned_data=transform.transform_data(api_data)
        load.save_to_csv(cleaned_data,'crypto_data.csv')
        report_data=analyze.analyze_data('crypto_data.csv')
        report.create_report(report_data)

 
if __name__=='__main__':
    run_pipeline()
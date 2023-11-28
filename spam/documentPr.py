from google.cloud import documentai_v1beta3 as documentai

def analyze_document(project_id='199384322A2', input_uri='gs://path/C:/abhi/document.pdf'):
    client = documentai.DocumentUnderstandingServiceClient()

    gcs_source = documentai.types.GcsSource(content_uri=input_uri)
    input_config = documentai.types.InputConfig(
        gcs_source=gcs_source, mime_type='application/pdf'
    )
    
    features = [
        documentai.enums.DocumentUnderstandingService.Feature(
            type_=documentai.enums.DocumentUnderstandingService.Feature.Type.FORM_EXTRACTOR
        ),
        documentai.enums.DocumentUnderstandingService.Feature(
            type_=documentai.enums.DocumentUnderstandingService.Feature.Type.TEXT_CLASSIFICATION
        ),
    ]

    requests = documentai.types.AnalyzeDocumentRequest(
        input_config=input_config, features=features
    )

    response = client.analyze_document(request=requests)

analyze_document()

from azure.core.credentials import AzurekeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from ultils.Config import Config


def analize_credit_card(card_url);
    try:
        credential = AzurekeyCredential(config.key)
        document_client = DocumentintelligenceClient(config.ENDOINT, credential)

        card_info = document_client.begin_analyze_document(
            "prebuilt-crediCard", AnalyzeDocumentRequest(url_source=card-url))
            result = card_info.result()

    for document in result.documents:
        fields= document.get('fields', {})

        return{
            'card_number': fields.get('cardNumber', {}).get('content'),
            'card_name': fields.get('CardHolderName', {}).get('content'),
            'expiration_date': fields.get('expirationDate', {}).get('content'),
            'bankName': fields.get('IssuingBank', {}).get('content'),
            


        }

    except Exception as ex:
        return None
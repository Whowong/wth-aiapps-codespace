import azure.functions as func
from azure.monitor.opentelemetry import configure_azure_monitor

from controllers.app_llm_quota_enforcement_manger import quota_controller
from controllers.application_initializer import app_initializer_controller
from controllers.ask_elizabeth import ask_elizabeth_controller
from controllers.ask_esther import ask_esther_controller
from controllers.ask_miriam import ask_miriam_controller
from controllers.ask_priscilla import ask_priscilla_controller
from controllers.ask_sarah import ask_sarah_controller
from controllers.azure_blob_contoso_documents import azure_blob_controller
from controllers.azure_document_intelligence import azure_document_intelligence_controller
from controllers.azure_service_bus_grapefruit import service_bus_controller_grapefruit
from controllers.azure_service_bus_lemon import service_bus_controller_lemon
from controllers.azure_service_bus_orange import service_bus_controller_orange
from controllers.azure_service_bus_tangerine import service_bus_controller_tangerine
from controllers.contoso_students_rest_service import students_crud_controller
from controllers.contoso_tourists_basic import contoso_tourists_controller
from controllers.contoso_yachts_data_pipeline import cosmos_controller
from controllers.contoso_yachts_rest_service import yachts_crud_controller
from controllers.customers import customers_controller

configure_azure_monitor()

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

app.register_functions(ask_elizabeth_controller)
app.register_functions(ask_esther_controller)
app.register_functions(ask_miriam_controller)
app.register_functions(ask_priscilla_controller)
app.register_functions(ask_sarah_controller)

app.register_functions(yachts_crud_controller)
app.register_functions(students_crud_controller)
app.register_functions(azure_document_intelligence_controller)

app.register_functions(customers_controller)
app.register_functions(azure_blob_controller)

app.register_functions(service_bus_controller_grapefruit)
app.register_functions(service_bus_controller_lemon)
app.register_functions(service_bus_controller_orange)
app.register_functions(service_bus_controller_tangerine)

app.register_functions(cosmos_controller)
app.register_functions(app_initializer_controller)
app.register_functions(quota_controller)

app.register_functions(contoso_tourists_controller)

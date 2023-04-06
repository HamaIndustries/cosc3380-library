from app import register
from web import static_files
from pages import example
from pages import myforms

register("/myforms/page", myforms.item_management_form, "get")
register("/myforms/handle-new-item", myforms.handle_item_management_form, "post")
register("/myforms/handle-edit-item", myforms.handle_item_management_form, "post")
register("/myforms/handle-delete-item", myforms.handle_item_management_form, "post")
register("/myforms/page", myforms.product_management_form, "get")
register("/myforms/handle-add-product", myforms.handle_product_management_form, "post")
register("/myforms/handle-edit-product", myforms.handle_product_management_form, "post")
register("/myforms/handle-delete-product", myforms.handle_product_management_form, "post")
register("/myforms/page", myforms.new_user_form, "get")
register("/myforms/handle-new-user", myforms.handle_new_user_form, "post")
register("/myforms/page", myforms.generating_holds_form, "get")
register("/myforms/generate-hold", myforms.handle_generating_holds_form, "post")
register("/example/page", example.example_get_response, "get")
register("/example/submit", example.example_post_response, "post")
register("/hello", example.hello)
# register(r"\/static\/.*", static_files("static/", "/static/"))
# register("/favicon.ico", static_files("static/favicon.ico"))

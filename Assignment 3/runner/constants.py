DATABASE_NAME = "pos.db"
TEST_DATABASE_NAME = "testing.db"
TEST_DATABASE_NAME_WITH_UNIT = "testing_with_unit.db"
TEST_DATABASE_NAME_WITH_PRODUCT = "testing_with_product.db"

UNITS_TABLE_NAME = "Units"
UNITS_TABLE_COLUMNS = "id TEXT, name TEXT"

PRODUCTS_TABLE_NAME = "Products"
PRODUCTS_TABLE_COLUMNS = "id TEXT, unit_id TEXT, name TEXT, barcode TEXT, price INTEGER"

RECEIPTS_TABLE_NAME = "Receipts"
RECEIPTS_TABLE_COLUMNS = "id TEXT, status TEXT, total INTEGER"

PRODUCTS_IN_REPOSITORY_COLUMNS = (
    "id TEXT, quantity INTEGER, price INTEGER, total INTEGER"
)

TEST_UNIT_ID = "27b4f218-1cc2-4694-b131-ad481dc08901"
TEST_PRODUCT_ID = "7d3184ae-80cd-417f-8b14-e3de42a98031"
TEST_PRODUCT_PRICE = 100
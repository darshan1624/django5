from product.models import Product

PERMISSION_CONFIG = {
    'seller': {
        Product: ['view', 'add', 'change']
    },
    'customer': {
        Product: ['view']
    }
}
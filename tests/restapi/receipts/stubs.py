"""Stubs for the /receipts endpoint"""

integration_tests = [
    (
        {
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [
                {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6.49"
                },{
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
                },{
                "shortDescription": "Knorr Creamy Chicken",
                "price": "1.26"
                },{
                "shortDescription": "Doritos Nacho Cheese",
                "price": "3.35"
                },{
                "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                "price": "12.00"
                }
            ],
            "total": "35.35"
        },
        28
    ),
    (
        {
            "retailer": "M&M Corner Market",
            "purchaseDate": "2022-03-20",
            "purchaseTime": "14:33",
            "items": [
                {
                "shortDescription": "Gatorade",
                "price": "2.25"
                },{
                "shortDescription": "Gatorade",
                "price": "2.25"
                },{
                "shortDescription": "Gatorade",
                "price": "2.25"
                },{
                "shortDescription": "Gatorade",
                "price": "2.25"
                }
            ],
            "total": "9.00"
        },
        109
    ),
] 

bad_syntax = [
    {  # No items
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [],
        "total": "0"
    },
    {  # Bad date
        "retailer": "Target",
        "purchaseDate": "2022-01-01a",
        "purchaseTime": "13:01",
        "items": [
            {
                "shortDescription": "Gatorade",
                "price": "2.25"
            }
        ],
        "total": "2.25"
    },
    {  # Bad time
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01a",
        "items": [
            {
                "shortDescription": "Gatorade",
                "price": "2.25"
            }
        ],
        "total": "2.25"
    },
    {  # Bad retailer
        "retailer": "Tar@#$^%@%&^#get",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {
                "shortDescription": "Gatorade",
                "price": "2.25"
            }
        ],
        "total": "2.25"
    },
    {  # Bad total
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {
                "shortDescription": "Gatorade",
                "price": "2.25"
            }
        ],
        "total": "2.250"
    },
    {  # Bad item
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {
                "shortDescription": "Gatorade",
                "price": "2.250"
            }
        ],
        "total": "2.25"
    },
]
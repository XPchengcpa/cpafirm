{
    "name": "Library Management",
    "version": "1.0",
    "summary": "Manage Library Books",
    "author": "Your Name",
    "category": "Tools",
    "depends": ["base", "mail"],
    "installable": True,
    "application": True,
    "data": [
        "security/ir.model.access.csv",
        "views/library_book_views.xml",
        "views/ibrary_author_views.xml",
        "views/library_book_tags_views.xml",
        "views/menus.xml",
    ],
}

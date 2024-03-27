from wirpl_books.models.base import Model

# CREATE TABLE IF NOT EXISTS `product` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `title` varchar(256) NOT NULL,
#   `author` varchar(256) NOT NULL,
#   `rating` decimal(4,2) NOT NULL,
#   `description` varchar(3000) NOT NULL,
#   `language` varchar(64) NOT NULL,
#   `isbn` varchar(13) NOT NULL,
#   `genres` varchar(256) NOT NULL,
#   `characters` varchar(1082) NOT NULL,
#   `pages` int(11) NOT NULL,
#   `published_at` date NOT NULL,
#   `cover_img` varchar(256) NOT NULL,
#   `price` decimal(8,0) DEFAULT NULL,
#   PRIMARY KEY (`id`),
#   UNIQUE KEY `id` (`id`)
# )


class ProductModel(Model):
    COLUMN_NAMES = [
        "id",
        "title",
        "author",
        "rating",
        "description",
        "language",
        "isbn",
        "genres",
        "characters",
        "pages",
        "published_at",
        "cover_img",
        "price",
    ]

    def get_all(self):
        self.cursor.execute("SELECT * FROM product")
        return self.cursor.fetchall()

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM product WHERE id = %s", (id,))
        return self.cursor.fetchone()
